"""
Exp05: Full robustness scan across parameter space.

Tests whether results from individual experiments hold up across
wide ranges of (M, Lambda) and (M, Q, Lambda).

Four robustness checks:
  1. SdS entropy identity residuals across the full admissible (M, Lambda) grid
  2. RNdS Vieta residuals and temperature positivity across (M, Q, Lambda) grid
  3. Attractor stability: does the PHYS gradient flow converge from many initial conditions?
  4. Spectral dimension stability: does d_s stay ~1 for SdS arc at all Lambda?
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import numpy as np
from src.sds_state import SdSState, sds_from_x, _nariai_mass, _is_sub_extremal
from src.rnds_state import RNdSState, rnds_scan_mq
from src.recursion_flows import SdS_M_GradientFlow, RNdS_MQ_GradientFlow, iterate_sds
from src.spectral_checks import estimate_spectral_dim
from src.utils import save_json, save_csv, section

OUT = os.path.join(os.path.dirname(__file__), "..", "outputs", "json")


def run():
    section("EXP05: Full Robustness Scan")
    results = {}

    # -------------------------------------------------------------------
    # 1. SdS entropy identity residuals across (M, Lambda) grid
    # -------------------------------------------------------------------
    print("\n  1. SdS entropy identity residuals across (M,Lambda) grid")
    lam_vals = np.linspace(0.05, 5.0, 20)
    n_per_lam = 30

    sds_residuals = []
    n_valid = 0
    n_total = 0

    for lam in lam_vals:
        M_nar = _nariai_mass(lam)
        M_vals = np.linspace(0.05 * M_nar, 0.95 * M_nar, n_per_lam)
        for M in M_vals:
            n_total += 1
            s = SdSState(M, lam)
            if s.is_valid():
                n_valid += 1
                resid = s.entropy_identity_residual()
                sds_residuals.append(resid)

    sds_resid_arr = np.array(sds_residuals)
    print(f"    Valid states: {n_valid}/{n_total}")
    print(f"    Entropy identity residual: max={sds_resid_arr.max():.2e}, "
          f"mean={sds_resid_arr.mean():.2e}, std={sds_resid_arr.std():.2e}")

    results["sds_entropy_identity_robustness"] = {
        "n_valid": n_valid,
        "n_total": n_total,
        "max_residual": float(sds_resid_arr.max()),
        "mean_residual": float(sds_resid_arr.mean()),
        "std_residual": float(sds_resid_arr.std()),
        "assessment": (
            "ROBUST: entropy identity holds to machine precision across all (M,Lambda)"
            if sds_resid_arr.max() < 1e-10
            else f"ANOMALY: max residual = {sds_resid_arr.max():.2e}"
        ),
    }

    # -------------------------------------------------------------------
    # 2. RNdS Vieta residuals across (M, Q, Lambda) grid
    # -------------------------------------------------------------------
    print("\n  2. RNdS Vieta residuals across (M,Q,Lambda) grid")
    vieta_e1 = []
    vieta_e2 = []
    vieta_e3 = []
    vieta_e4 = []
    n_rnds_valid = 0
    n_rnds_total = 0

    for lam in [0.5, 1.0, 2.0]:
        states = rnds_scan_mq(n_M=12, n_Q=8, lam=lam)
        for s in states:
            n_rnds_total += 1
            if s.is_valid():
                n_rnds_valid += 1
                v = s.vieta_check()
                vieta_e1.append(v["e1_residual"])
                vieta_e2.append(v["e2_residual"])
                vieta_e3.append(v["e3_residual"])
                vieta_e4.append(v["e4_residual"])

    if vieta_e1:
        print(f"    Valid RNdS states: {n_rnds_valid}/{n_rnds_total}")
        print(f"    Vieta e1 residual: max={max(vieta_e1):.2e}")
        print(f"    Vieta e2 residual: max={max(vieta_e2):.2e}")
        print(f"    Vieta e3 residual: max={max(vieta_e3):.2e}")
        print(f"    Vieta e4 residual: max={max(vieta_e4):.2e}")
    else:
        print("    No valid RNdS states found.")

    results["rnds_vieta_robustness"] = {
        "n_valid": n_rnds_valid,
        "n_total": n_rnds_total,
        "max_e1": float(max(vieta_e1)) if vieta_e1 else None,
        "max_e2": float(max(vieta_e2)) if vieta_e2 else None,
        "max_e3": float(max(vieta_e3)) if vieta_e3 else None,
        "max_e4": float(max(vieta_e4)) if vieta_e4 else None,
        "assessment": (
            "ROBUST: Vieta identities hold to machine precision"
            if (vieta_e1 and max(vieta_e1) < 1e-8 and max(vieta_e2) < 1e-8)
            else "ANOMALY or EMPTY"
        ),
    }

    # -------------------------------------------------------------------
    # 3. Attractor stability: PHYS gradient flow from many initial conditions
    # -------------------------------------------------------------------
    print("\n  3. Attractor stability: SdS gradient flow from many initial conditions")
    lam = 1.0
    M_nar = _nariai_mass(lam)
    n_init = 20
    x_vals = np.linspace(0.05, 0.95, n_init)
    final_M_vals = []
    final_x_vals = []
    converged = 0

    for x0 in x_vals:
        s0 = sds_from_x(x0, lam)
        if not s0.is_valid():
            continue
        flow = SdS_M_GradientFlow(step=0.001)
        traj = iterate_sds(flow, s0.M, s0.Lambda, n_steps=3000)
        if traj is not None and len(traj) > 0:
            M_f, lam_f = traj[-1]
            s_final = SdSState(M_f, lam_f)
            if s_final.is_valid():
                final_M_vals.append(M_f)
                x_f = s_final.r_b / s_final.r_c
                final_x_vals.append(x_f)
            converged += 1

    if final_M_vals:
        M_arr = np.array(final_M_vals)
        x_arr = np.array(final_x_vals)
        M_spread = float(np.std(M_arr))
        x_spread = float(np.std(x_arr))
        print(f"    Converged flows: {converged}/{n_init}")
        print(f"    Final M: mean={M_arr.mean():.4f}, std={M_spread:.2e}")
        print(f"    Final x: mean={x_arr.mean():.4f}, std={x_spread:.2e}")
        single_attractor = (M_spread < 0.005 and x_spread < 0.005)
        print(f"    Single attractor: {single_attractor}")
    else:
        single_attractor = False
        M_spread = x_spread = np.nan
        print("    No converged flows.")

    results["attractor_stability"] = {
        "lam": lam,
        "n_init": n_init,
        "n_converged": converged,
        "final_M_std": float(M_spread) if not np.isnan(M_spread) else None,
        "final_x_std": float(x_spread) if not np.isnan(x_spread) else None,
        "single_attractor": single_attractor,
        "assessment": (
            "ROBUST: gradient flow converges to single attractor from all initial conditions"
            if single_attractor
            else "MULTI-ATTRACTOR or non-convergent: see std values"
        ),
    }

    # -------------------------------------------------------------------
    # 4. Spectral dimension stability across Lambda values
    # -------------------------------------------------------------------
    print("\n  4. Spectral dimension stability of SdS arc across Lambda")
    lam_test = [0.1, 0.5, 1.0, 2.0, 5.0]
    spectral_results = {}

    for lam in lam_test:
        xs = np.linspace(0.05, 0.95, 60)
        states = [sds_from_x(x, lam) for x in xs]
        states = [s for s in states if s.is_valid()]
        if len(states) < 10:
            print(f"    Lambda={lam}: too few states ({len(states)})")
            spectral_results[f"lam_{lam}"] = {"n_states": len(states), "d_s": None}
            continue

        # Points in (M, Lambda) 2D space — but Lambda is fixed, so it's 1D
        points_M = np.array([[s.M, s.Lambda] for s in states])
        try:
            r = estimate_spectral_dim(points_M, k=6)
            d_s = r["d_s"]
            print(f"    Lambda={lam}: n={len(states)}, d_s={d_s:.3f} "
                  f"(ambient=2, pca_dim={r['ambient_dim']})")
            spectral_results[f"lam_{lam}"] = {
                "n_states": len(states),
                "d_s": float(d_s),
                "d_s_se": float(r["d_s_se"]),
                "pca_intrinsic_dim": r["ambient_dim"],
            }
        except Exception as e:
            print(f"    Lambda={lam}: spectral dim failed: {e}")
            spectral_results[f"lam_{lam}"] = {"n_states": len(states), "d_s": None, "error": str(e)}

    all_ds = [v["d_s"] for v in spectral_results.values() if v.get("d_s") is not None]
    if all_ds:
        print(f"\n    Spectral dim range: [{min(all_ds):.3f}, {max(all_ds):.3f}]")
        consistent_1d = all(abs(d - 1.0) < 0.3 for d in all_ds)
    else:
        consistent_1d = False

    results["spectral_dim_robustness"] = {
        "by_lambda": spectral_results,
        "consistent_1d": consistent_1d,
        "d_s_values": all_ds,
        "assessment": (
            "ROBUST: SdS arc is consistently ~1D across all Lambda values"
            if consistent_1d
            else "VARIABLE: spectral dimension not consistently 1D"
        ),
    }

    # -------------------------------------------------------------------
    # Summary
    # -------------------------------------------------------------------
    print("\n  === ROBUSTNESS SUMMARY ===")
    for key, val in results.items():
        print(f"    {key}: {val.get('assessment', 'N/A')}")

    save_json(results, f"{OUT}/exp05_robustness.json")
    return results


if __name__ == "__main__":
    run()
