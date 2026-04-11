"""
Exp03: RNdS extension — the main dimensional upgrade.

RNdS state space: (M, Q, Lambda).
At fixed Lambda: 2D (M, Q) parameter space.
With Lambda varying: 3D.

This is the key test: does working in a genuinely higher-dimensional
parameter space produce orbits with d_s > 1?

We test:
  A. RNdS baseline: verify Vieta relations and admissibility
  B. [PHYS] Gradient flow in (M, Q) — physically derived from first laws
  C. [EXPL] Circular orbit in (M, Q) — genuinely 2D by construction
  D. [EXPL] 3D flow in (M, Q, Lambda)
  E. Spectral dimension comparison: old 1D SdS vs new 2D RNdS orbits

This is the most important experiment in the project.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import numpy as np
from src.rnds_state import RNdSState, rnds_scan_mq, rnds_extremal_charge, _rnds_admissible
from src.recursion_flows import (
    RNdS_MQ_GradientFlow, RNdS_MQ_CircularFlow,
    RNdS_Coupled_3D_Flow, iterate_rnds
)
from src.flow_constraints import check_rnds_orbit, rnds_orbit_observables
from src.spectral_checks import (
    estimate_spectral_dim, multiscale_spectral_dim, intrinsic_dimension_pca
)
from src.stability import max_lyapunov_3d
from src.utils import save_json, save_csv, section, Timer

OUT_J = os.path.join(os.path.dirname(__file__), "..", "outputs", "json")
OUT_C = os.path.join(os.path.dirname(__file__), "..", "outputs", "csv")


def run():
    section("EXP03: RNdS Extension")
    results = {}
    lam = 1.0

    # -----------------------------------------------------------------------
    # A. RNdS baseline
    # -----------------------------------------------------------------------
    print("\n  A. RNdS baseline: Vieta checks and phase diagram")
    states = rnds_scan_mq(n_M=8, n_Q=8, lam=lam)
    print(f"  Admissible states: {len(states)} over (M,Q) grid")

    if not states:
        print("  ERROR: No admissible RNdS states found. Check parameter range.")
        results["baseline"] = {"error": "no admissible states"}
        save_json(results, f"{OUT_J}/exp03_rnds.json")
        return results

    # Vieta residuals
    vieta_residuals = []
    for s in states:
        v = s.vieta_check()
        if v.get("admissible", True):
            vieta_residuals.append(max(v.get(k,0) for k in
                ["e1_residual","e2_residual","e3_residual","e4_residual"]))

    max_vieta = max(vieta_residuals) if vieta_residuals else np.nan
    print(f"  Vieta max residual: {max_vieta:.2e}")
    T_outer_pos = all(s.T_outer > 0 for s in states)
    T_cosmo_pos = all(s.T_cosmo > 0 for s in states)
    print(f"  T_outer>0: {T_outer_pos}, T_cosmo>0: {T_cosmo_pos}")
    print(f"  Delta_total range: [{min(s.Delta_total for s in states):.3f}, "
          f"{max(s.Delta_total for s in states):.3f}]")

    results["A_baseline"] = {
        "n_admissible": len(states),
        "vieta_max_residual": float(max_vieta),
        "T_outer_positive": T_outer_pos,
        "T_cosmo_positive": T_cosmo_pos,
        "Delta_total_range": [
            float(min(s.Delta_total for s in states)),
            float(max(s.Delta_total for s in states)),
        ],
        "note": "No exact entropy identity exists for RNdS. Delta_total = S_Lambda - S_outer - S_cosmo is defined numerically.",
    }

    # Choose reference point
    s_ref = states[len(states)//3]
    M0, Q0 = s_ref.M, s_ref.Q
    print(f"\n  Reference point: M={M0:.4f}, Q={Q0:.4f}, Lambda={lam}")

    # -----------------------------------------------------------------------
    # B. [PHYS] Gradient flow in (M, Q)
    # -----------------------------------------------------------------------
    print("\n  B. [PHYS] (M,Q) gradient flow, Lambda fixed")
    flow_B = RNdS_MQ_GradientFlow(step_M=0.003, step_Q=0.003, direction='descent')
    def f_B(M,Q,L): return flow_B(M, Q, L)

    traj_B = iterate_rnds(f_B, M0, Q0, lam, n_steps=800)
    check_B = check_rnds_orbit(traj_B)
    obs_B = rnds_orbit_observables(traj_B)

    valid_mask_B = np.isfinite(obs_B["S_outer"]) & np.isfinite(obs_B["S_cosmo"])
    pts_B_2d = traj_B[valid_mask_B, :2]  # just (M, Q) for 2D spectral dim
    pts_B_3d = traj_B[valid_mask_B]

    spec_B_2d = estimate_spectral_dim(pts_B_2d) if len(pts_B_2d) > 20 else {"d_s": np.nan}
    pca_B = intrinsic_dimension_pca(pts_B_3d)
    ms_B = multiscale_spectral_dim(pts_B_2d) if len(pts_B_2d) > 30 else []

    Q_range = (float(traj_B[valid_mask_B, 1].min()), float(traj_B[valid_mask_B, 1].max()))
    Q_varies = (Q_range[1] - Q_range[0]) > 1e-5

    print(f"    Admissible: {check_B['admissibility_rate']:.3f}")
    print(f"    Q range: {Q_range}, varies: {Q_varies}")
    print(f"    d_s (2D orbit): {spec_B_2d['d_s']:.4f} (expected ~1-2)")
    print(f"    PCA intrinsic dim: {pca_B}")

    for r in ms_B:
        print(f"    Multiscale [{r['scale_label']}]: d_s={r['d_s']:.4f}")

    results["B_phys_gradient"] = {
        "label": "PHYS",
        "admissibility_rate": check_B['admissibility_rate'],
        "Q_range": Q_range,
        "Q_varies_meaningfully": Q_varies,
        "spectral_dim_2d": spec_B_2d,
        "pca_intrinsic_dim": pca_B,
        "multiscale": ms_B,
    }

    # -----------------------------------------------------------------------
    # C. [EXPL] Circular orbit in (M, Q) — genuinely 2D by construction
    # -----------------------------------------------------------------------
    print("\n  C. [EXPL] Circular (M,Q) orbit")
    radius = min(M0 * 0.3, Q0 * 0.3 if Q0 > 0.01 else M0 * 0.1)
    flow_C = RNdS_MQ_CircularFlow(theta=0.15, M_0=M0, Q_0=Q0, radius=radius)
    def f_C(M,Q,L): return flow_C(M, Q, L)

    traj_C = iterate_rnds(f_C, M0 + radius, Q0, lam, n_steps=1000)
    check_C = check_rnds_orbit(traj_C)
    obs_C = rnds_orbit_observables(traj_C)

    valid_mask_C = np.isfinite(obs_C["S_outer"])
    pts_C_2d = traj_C[valid_mask_C, :2]
    pts_C_3d = traj_C[valid_mask_C]

    spec_C_2d = estimate_spectral_dim(pts_C_2d) if len(pts_C_2d) > 20 else {"d_s": np.nan}
    pca_C = intrinsic_dimension_pca(pts_C_3d)
    ms_C = multiscale_spectral_dim(pts_C_2d) if len(pts_C_2d) > 30 else []

    print(f"    Admissible: {check_C['admissibility_rate']:.3f}")
    print(f"    d_s (2D orbit): {spec_C_2d['d_s']:.4f}")
    print(f"    PCA intrinsic dim: {pca_C}")
    for r in ms_C:
        print(f"    Multiscale [{r['scale_label']}]: d_s={r['d_s']:.4f}")

    results["C_expl_circular"] = {
        "label": "EXPL",
        "admissibility_rate": check_C['admissibility_rate'],
        "spectral_dim_2d": spec_C_2d,
        "pca_intrinsic_dim": pca_C,
        "multiscale": ms_C,
        "note": "Circular orbit is genuinely 2D by design. If d_s~2, confirms 2D geometry.",
    }

    save_csv(
        {k: obs_C[k] for k in ["M","Q","T_outer","T_cosmo","S_outer","S_cosmo","Delta_total"]},
        f"{OUT_C}/exp03_circular_orbit.csv"
    )

    # -----------------------------------------------------------------------
    # D. [EXPL] 3D flow in (M, Q, Lambda)
    # -----------------------------------------------------------------------
    print("\n  D. [EXPL] 3D (M,Q,Lambda) flow")
    flow_D = RNdS_Coupled_3D_Flow(step=0.01)
    def f_D(M,Q,L): return flow_D(M, Q, L)

    traj_D = iterate_rnds(f_D, M0, Q0, lam, n_steps=500)
    check_D = check_rnds_orbit(traj_D)
    valid_mask_D = np.all(np.isfinite(traj_D), axis=1)
    pts_D = traj_D[valid_mask_D]

    spec_D = estimate_spectral_dim(pts_D) if len(pts_D) > 20 else {"d_s": np.nan}
    pca_D = intrinsic_dimension_pca(pts_D)

    print(f"    Admissible: {check_D['admissibility_rate']:.3f}")
    print(f"    d_s (3D orbit): {spec_D['d_s']:.4f} (ambient=3)")
    print(f"    PCA intrinsic dim: {pca_D}")

    results["D_expl_3d"] = {
        "label": "EXPL",
        "admissibility_rate": check_D['admissibility_rate'],
        "spectral_dim_3d": spec_D,
        "pca_intrinsic_dim": pca_D,
    }

    # -----------------------------------------------------------------------
    # E. Comparative summary
    # -----------------------------------------------------------------------
    print("\n  E. Comparative summary (old 1D SdS arc vs new RNdS orbits)")
    # Reference: 1D arc
    from src.sds_state import sds_scan_x
    sds_states = sds_scan_x(200, lam)
    pts_1d = np.array([[s.M, lam] for s in sds_states if s.is_valid()])
    spec_1d = estimate_spectral_dim(pts_1d) if len(pts_1d) > 20 else {"d_s": np.nan}
    pca_1d = intrinsic_dimension_pca(pts_1d)

    print(f"    Old SdS 1D arc:      d_s={spec_1d['d_s']:.4f}, PCA dim={pca_1d}")
    print(f"    RNdS gradient flow:  d_s={spec_B_2d['d_s']:.4f}, PCA dim={pca_B}")
    print(f"    RNdS circular:       d_s={spec_C_2d['d_s']:.4f}, PCA dim={pca_C}")
    print(f"    RNdS 3D flow:        d_s={spec_D['d_s']:.4f}, PCA dim={pca_D}")

    results["E_comparison"] = {
        "sds_1d_arc": {"d_s": spec_1d['d_s'], "pca_dim": pca_1d},
        "rnds_gradient": {"d_s": spec_B_2d['d_s'], "pca_dim": pca_B},
        "rnds_circular": {"d_s": spec_C_2d['d_s'], "pca_dim": pca_C},
        "rnds_3d": {"d_s": spec_D['d_s'], "pca_dim": pca_D},
    }

    save_json(results, f"{OUT_J}/exp03_rnds.json")
    return results


if __name__ == "__main__":
    run()
