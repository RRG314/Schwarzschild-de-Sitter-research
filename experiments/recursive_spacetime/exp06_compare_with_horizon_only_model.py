"""
Exp06: Compare recursive_spacetime_system with old horizon-only model.

Old model (recursive_horizon_project):
  - Worked at fixed Lambda in 1D Eisenstein arc x = r_b/r_c in (0,1)
  - Showed: entropy identity exact, Eisenstein constraint exact
  - Failed: spectral dimension approx 1, no genuine higher-dimensional behavior

New model (recursive_spacetime_system):
  - Works in (M, Lambda) 2D or (M, Q, Lambda) 3D
  - RNdS adds genuine second direction Q
  - SdS (M, Lambda) flows collapse to 1D if Lambda not varied
  - Only [EXPL] 3D flows show d_s > 1
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import numpy as np
from src.sds_state import SdSState, sds_from_x, _nariai_mass
from src.rnds_state import RNdSState, rnds_scan_mq
from src.recursion_flows import (
    SdS_M_GradientFlow,
    SdS_Coupled_MLambda_Flow,
    RNdS_MQ_CircularFlow,
    RNdS_Coupled_3D_Flow,
    iterate_sds,
    iterate_rnds,
)
from src.spectral_checks import estimate_spectral_dim, intrinsic_dimension_pca
from src.utils import save_json, section

OUT = os.path.join(os.path.dirname(__file__), "..", "outputs", "json")


def _spectral_dim_of_points(points, k=6):
    """Estimate spectral dim and PCA intrinsic dim from a point cloud."""
    try:
        if len(points) < 10:
            return None, None
        r = estimate_spectral_dim(points, k=k)
        pca = intrinsic_dimension_pca(points)
        return float(r["d_s"]), int(pca)
    except Exception as e:
        return None, str(e)


def run():
    section("EXP06: Comparison — Spacetime System vs. Horizon-Only Model")
    results = {}

    lam = 1.0
    M_nar = _nariai_mass(lam)

    # -------------------------------------------------------------------
    # 1. Replicate old model behavior: SdS arc at fixed Lambda
    # -------------------------------------------------------------------
    print("\n  1. Old model: SdS arc at fixed Lambda=1 (1D x-arc)")
    xs = np.linspace(0.05, 0.95, 100)
    arc_states = [sds_from_x(x, lam) for x in xs]
    arc_states = [s for s in arc_states if s.is_valid()]

    arc_points = np.array([[s.r_b, s.r_c] for s in arc_states])
    arc_ds, arc_pca = _spectral_dim_of_points(arc_points)

    arc_resids = [s.entropy_identity_residual() for s in arc_states]

    print(f"    Arc states: {len(arc_states)}")
    print(f"    Spectral dim (r_b,r_c space): {arc_ds}")
    print(f"    PCA intrinsic dim: {arc_pca}")
    print(f"    Max entropy identity residual: {max(arc_resids):.2e}")

    results["old_model_arc"] = {
        "n_states": len(arc_states),
        "d_s_rb_rc": arc_ds,
        "pca_intrinsic_dim": arc_pca,
        "max_entropy_residual": float(max(arc_resids)),
        "assessment": "1D arc — consistent with old model spectral_dim ~1 finding",
    }

    # -------------------------------------------------------------------
    # 2. New model, Form A: SdS flows in (M, Lambda) space
    # -------------------------------------------------------------------
    print("\n  2. New model, Form A: SdS flows — do they escape 1D?")

    s0 = sds_from_x(0.3, lam)

    # [PHYS] M-only gradient flow at fixed Lambda — known 1D
    flow_M = SdS_M_GradientFlow(step=0.001)
    traj_M = iterate_sds(flow_M, s0.M, s0.Lambda, n_steps=500)
    pts_M = np.array([[SdSState(r[0], r[1]).M, r[1]] for r in traj_M
                      if SdSState(r[0], r[1]).is_valid()])
    ds_M, pca_M = _spectral_dim_of_points(pts_M) if len(pts_M) > 10 else (None, None)
    print(f"    [PHYS] M-only gradient flow: d_s={ds_M}, pca={pca_M}")
    print(f"      (Lambda fixed={lam}, MUST be 1D)")

    # [EXPL] Coupled (M, Lambda) thermalization flow
    flow_ML = SdS_Coupled_MLambda_Flow(variant="thermalization", eps_M=0.001, eps_Lambda=0.001)
    traj_ML = iterate_sds(flow_ML, s0.M, s0.Lambda, n_steps=500)
    pts_ML = traj_ML  # (n, 2) array of (M, Lambda)
    lam_range_ML = (float(pts_ML[:, 1].min()), float(pts_ML[:, 1].max()))
    lam_varies_ML = (lam_range_ML[1] - lam_range_ML[0]) > 1e-4
    ds_ML, pca_ML = _spectral_dim_of_points(pts_ML)
    print(f"    [EXPL] Coupled (M,Lambda): d_s={ds_ML}, pca={pca_ML}, varies={lam_varies_ML}")
    print(f"      Lambda range: [{lam_range_ML[0]:.4f}, {lam_range_ML[1]:.4f}]")

    results["form_A_comparison"] = {
        "M_only_flow": {"d_s": ds_M, "pca": pca_M, "note": "1D by construction"},
        "coupled_ML_flow": {
            "d_s": ds_ML, "pca": pca_ML,
            "lambda_varies": lam_varies_ML,
            "lambda_range": list(lam_range_ML),
        },
        "genuine_upgrade_over_old": bool(lam_varies_ML and ds_ML is not None and ds_ML > 1.2),
    }

    # -------------------------------------------------------------------
    # 3. New model, Form C: RNdS 2D and 3D orbits
    # -------------------------------------------------------------------
    print("\n  3. New model, Form C: RNdS orbits — key dimensional upgrade")

    rnds_2d = {"error": "not attempted"}
    rnds_3d = {"error": "not attempted"}

    try:
        M0 = 0.3 * M_nar
        Q0 = 0.01
        s_test = RNdSState(M0, Q0, lam)
        if not s_test.is_valid():
            M0 = 0.2 * M_nar
            Q0 = 0.005

        # [EXPL] 2D circular orbit in (M, Q) space
        flow_circ = RNdS_MQ_CircularFlow(theta=0.1, M_0=M0, Q_0=Q0, radius=0.02*M_nar)
        traj_circ = iterate_rnds(flow_circ, M0 + 0.01*M_nar, Q0, lam, n_steps=400)
        # Filter valid
        pts_circ = []
        for row in traj_circ:
            M_i, Q_i, L_i = row
            s_i = RNdSState(M_i, Q_i, L_i)
            if s_i.is_valid():
                pts_circ.append([M_i, Q_i])
        pts_circ = np.array(pts_circ) if pts_circ else np.zeros((0, 2))
        ds_circ, pca_circ = _spectral_dim_of_points(pts_circ)
        print(f"    [EXPL] RNdS 2D circular: {len(pts_circ)} valid pts, d_s={ds_circ}, pca={pca_circ}")
        rnds_2d = {"n_valid": len(pts_circ), "d_s": ds_circ, "pca": pca_circ}
    except Exception as e:
        print(f"    [EXPL] RNdS 2D circular: FAILED — {e}")
        rnds_2d = {"error": str(e)}

    try:
        M0 = 0.3 * M_nar
        Q0 = 0.01
        flow_3d = RNdS_Coupled_3D_Flow(step=0.005)
        traj_3d = iterate_rnds(flow_3d, M0, Q0, lam, n_steps=500)
        pts_3d = []
        for row in traj_3d:
            M_i, Q_i, L_i = row
            if L_i > 0 and M_i > 0 and Q_i >= 0:
                s_i = RNdSState(M_i, Q_i, L_i)
                if s_i.is_valid():
                    pts_3d.append([M_i, Q_i, L_i])
        pts_3d = np.array(pts_3d) if pts_3d else np.zeros((0, 3))
        ds_3d, pca_3d = _spectral_dim_of_points(pts_3d)
        print(f"    [EXPL] RNdS 3D coupled: {len(pts_3d)} valid pts, d_s={ds_3d}, pca={pca_3d}")
        rnds_3d = {"n_valid": len(pts_3d), "d_s": ds_3d, "pca": pca_3d}
    except Exception as e:
        print(f"    [EXPL] RNdS 3D: FAILED — {e}")
        rnds_3d = {"error": str(e)}

    results["form_C_rnds_orbits"] = {
        "rnds_2d_circular": rnds_2d,
        "rnds_3d_coupled": rnds_3d,
    }

    # -------------------------------------------------------------------
    # 4. Dimension summary
    # -------------------------------------------------------------------
    print("\n  4. Dimension summary")
    print(f"    Old model (SdS 1D arc):           d_s = {arc_ds}")
    print(f"    New SdS M-only flow (1D):          d_s = {ds_M}")
    print(f"    New SdS (M,Lam) coupled:           d_s = {ds_ML}, Lambda varies={lam_varies_ML}")
    print(f"    New RNdS 2D circular:              d_s = {rnds_2d.get('d_s')}")
    print(f"    New RNdS 3D coupled:               d_s = {rnds_3d.get('d_s')}")

    def _classify(d_s):
        if d_s is None: return "UNKNOWN"
        if d_s < 1.2: return "1D — no upgrade"
        elif d_s < 1.8: return "~1.5D — marginal upgrade"
        elif d_s < 2.5: return "~2D — genuine upgrade"
        else: return f"~{d_s:.1f}D"

    upgrade_verdict = {}
    for label, d_s in [
        ("old_arc", arc_ds), ("sds_M_only", ds_M),
        ("sds_ML_coupled", ds_ML), ("rnds_2d", rnds_2d.get("d_s")),
        ("rnds_3d", rnds_3d.get("d_s")),
    ]:
        upgrade_verdict[label] = {"d_s": d_s, "classification": _classify(d_s)}

    results["dimension_comparison"] = upgrade_verdict

    # -------------------------------------------------------------------
    # 5. What new model adds
    # -------------------------------------------------------------------
    additions = {
        "RNdS_quartic_solver": "NEW — handles 3-parameter (M,Q,Lambda) spacetime",
        "Vieta_checks_all_4": "NEW — full algebraic verification of quartic roots",
        "electric_potential_Phi": "NEW — Phi = Q/r at each horizon",
        "3_horizon_temperatures": "NEW — T_inner, T_outer, T_cosmo all computed",
        "entropy_deficit_2horizon": "NEW — Delta = S_Lambda - (S_outer + S_cosmo) for RNdS",
        "entropy_identity_SdS": "INHERITED — exact, machine precision",
        "flow_labels_PHYS_CONV_EXPL": "NEW — explicit epistemic tagging",
        "scalar_field_audit": "NEW — honest audit, verdict: NOT USEFUL",
        "spectral_dim_upgrade": "PARTIAL — only [EXPL] arbitrary 3D flow gets d_s > 1",
    }
    results["additions_vs_old"] = additions

    save_json(results, f"{OUT}/exp06_comparison.json")
    return results


if __name__ == "__main__":
    run()
