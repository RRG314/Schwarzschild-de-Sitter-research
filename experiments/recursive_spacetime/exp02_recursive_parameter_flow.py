"""
Exp02: Recursive parameter flows on the SdS (M, Lambda) space.

THE KEY UPGRADE from the old model:
  Old model: orbits on 1D Eisenstein arc at fixed Lambda.
  New model: orbits in 2D (M, Lambda) parameter space.

We test three flow families (labeled by motivation):
  A. [PHYS]  M-gradient flow, fixed Lambda: dM ∝ -(1/T_c - 1/T_b)
  B. [CONV]  Nariai interpolation: M → M_Nariai
  C. [EXPL]  Coupled (M, Lambda) flows: 3 sub-variants

For each flow, we track:
  - Admissibility of orbit
  - Fixed points
  - Convergence behavior
  - Whether the orbit genuinely explores 2D or collapses to 1D
  - Spectral dimension of the orbit in (M, Lambda) space
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import numpy as np
from src.sds_state import SdSState, _nariai_mass, _is_sub_extremal
from src.recursion_flows import (
    SdS_M_GradientFlow, SdS_Nariai_LinearMap,
    SdS_Coupled_MLambda_Flow, SdS_ConstantX_Flow,
    iterate_sds
)
from src.flow_constraints import check_sds_orbit, sds_orbit_observables
from src.spectral_checks import estimate_spectral_dim, multiscale_spectral_dim, intrinsic_dimension_pca
from src.stability import max_lyapunov_2d, find_fixed_points_2d
from src.utils import save_json, save_csv, section, Timer

OUT_J = os.path.join(os.path.dirname(__file__), "..", "outputs", "json")
OUT_C = os.path.join(os.path.dirname(__file__), "..", "outputs", "csv")


def run():
    section("EXP02: Recursive Parameter Flows on SdS (M, Lambda)")
    results = {}

    lam0 = 1.0
    M0 = 0.15 * _nariai_mass(lam0)

    # -----------------------------------------------------------------------
    # A. [PHYS] M-gradient flow
    # -----------------------------------------------------------------------
    print("\n  A. [PHYS] M-gradient flow (fixed Lambda)")
    flow_A = SdS_M_GradientFlow(step=0.01, direction='descent', lam=lam0)
    # Wrap for 2D iterate
    def f_A(M, lam): return flow_A(M, lam)

    traj_A = iterate_sds(f_A, M0, lam0, n_steps=500)
    check_A = check_sds_orbit(traj_A)
    obs_A = sds_orbit_observables(traj_A)

    # Spectral dim of orbit in (M, Lambda) space
    pts_A = traj_A[~np.any(np.isnan(traj_A), axis=1)]
    spec_A = estimate_spectral_dim(pts_A) if len(pts_A) > 20 else {"d_s": np.nan}
    pca_dim_A = intrinsic_dimension_pca(pts_A)

    # Terminal state
    M_final, lam_final = traj_A[-1]
    s_final = SdSState(M_final, lam_final)

    print(f"    Admissibility: {check_A['admissibility_rate']:.3f}")
    print(f"    M_initial={M0:.4f} -> M_final={M_final:.6f}")
    print(f"    Spectral dim d_s={spec_A['d_s']:.4f} (ambient=2)")
    print(f"    PCA intrinsic dim: {pca_dim_A}")
    print(f"    MLE (Lyapunov): ", end="")
    mle_A = max_lyapunov_2d(f_A, M0, lam0, n_steps=500)
    print(f"{mle_A:.4f}")

    results["A_phys_gradient"] = {
        "label": "PHYS",
        "flow": "M-gradient descent, fixed Lambda",
        "M_initial": M0, "M_final": float(M_final),
        "Lambda_fixed": lam0,
        "admissibility_rate": check_A['admissibility_rate'],
        "spectral_dim": spec_A,
        "pca_intrinsic_dim": pca_dim_A,
        "max_lyapunov": float(mle_A),
        "convergence": "M -> 0 (pure dS) as expected",
        "note": "This flow is physically derived but 1D (Lambda constant). Same topology as old model.",
    }

    # -----------------------------------------------------------------------
    # B. [CONV] Nariai linear map
    # -----------------------------------------------------------------------
    print("\n  B. [CONV] Nariai linear map (Lambda fixed)")
    flow_B = SdS_Nariai_LinearMap(alpha=0.05)
    def f_B(M, lam): return flow_B(M, lam)

    traj_B = iterate_sds(f_B, M0, lam0, n_steps=300)
    check_B = check_sds_orbit(traj_B)
    pts_B = traj_B
    spec_B = estimate_spectral_dim(pts_B) if len(pts_B) > 20 else {"d_s": np.nan}
    pca_dim_B = intrinsic_dimension_pca(pts_B)
    M_final_B = traj_B[-1, 0]
    mle_B = max_lyapunov_2d(f_B, M0, lam0)

    print(f"    M_final={M_final_B:.6f} (M_Nariai={_nariai_mass(lam0):.4f})")
    print(f"    d_s={spec_B['d_s']:.4f}, PCA dim={pca_dim_B}")

    results["B_conv_nariai"] = {
        "label": "CONV",
        "flow": "Linear interpolation toward Nariai, Lambda fixed",
        "M_final": float(M_final_B),
        "M_Nariai": float(_nariai_mass(lam0)),
        "admissibility_rate": check_B['admissibility_rate'],
        "spectral_dim": spec_B,
        "pca_intrinsic_dim": pca_dim_B,
        "max_lyapunov": float(mle_B),
        "note": "Converges to Nariai boundary (degenerate). Also 1D.",
    }

    # -----------------------------------------------------------------------
    # C. [EXPL] Coupled (M, Lambda) flows
    # -----------------------------------------------------------------------
    print("\n  C. [EXPL] Coupled (M, Lambda) flows")
    variants = ['gradient_both', 'thermalization', 'free']
    results["C_expl_coupled"] = {}

    for variant in variants:
        eps_M = 0.005
        eps_L = 0.002
        flow_C = SdS_Coupled_MLambda_Flow(eps_M=eps_M, eps_Lambda=eps_L,
                                           variant=variant, theta=0.7)
        def make_f(fl): return lambda M, lam: fl(M, lam)
        f_C = make_f(flow_C)

        traj_C = iterate_sds(f_C, M0, lam0, n_steps=800)
        check_C = check_sds_orbit(traj_C)

        # Drop inadmissible points for spectral analysis
        obs_C = sds_orbit_observables(traj_C)
        valid_mask = ~np.isnan(obs_C["M"])
        pts_C = traj_C[valid_mask]

        spec_C = estimate_spectral_dim(pts_C) if len(pts_C) > 20 else {"d_s": np.nan}
        pca_C = intrinsic_dimension_pca(pts_C)
        mle_C = max_lyapunov_2d(f_C, M0, lam0, n_steps=500)

        # Range of Lambda explored
        lam_vals = traj_C[valid_mask, 1]
        lam_range = (float(lam_vals.min()), float(lam_vals.max())) if len(lam_vals) > 0 else (np.nan, np.nan)
        lam_varies = (lam_range[1] - lam_range[0]) > 1e-4

        print(f"    variant={variant}: d_s={spec_C['d_s']:.4f}, PCA={pca_C}, "
              f"Lambda varies={lam_varies} ({lam_range[0]:.3f},{lam_range[1]:.3f}), "
              f"admissible={check_C['admissibility_rate']:.2f}, MLE={mle_C:.4f}")

        results["C_expl_coupled"][variant] = {
            "label": "EXPL",
            "admissibility_rate": check_C['admissibility_rate'],
            "lambda_range": lam_range,
            "lambda_varies_meaningfully": lam_varies,
            "spectral_dim": spec_C,
            "pca_intrinsic_dim": pca_C,
            "max_lyapunov": float(mle_C),
        }

        # Save orbit CSV for best-behaved variant
        if variant == 'gradient_both':
            obs_C_full = sds_orbit_observables(traj_C)
            save_csv({k: obs_C_full[k] for k in ["M","Lambda","x","Delta","eta_C","T_b","T_c"]},
                     f"{OUT_C}/exp02_gradient_both_orbit.csv")

    # D. Constant-x flow (for comparison)
    print("\n  D. [CONV] Constant-x scaling flow")
    flow_D = SdS_ConstantX_Flow(scale=1.03)
    def f_D(M, lam): return flow_D(M, lam)
    traj_D = iterate_sds(f_D, M0, lam0, n_steps=200)
    pts_D = traj_D[np.all(np.isfinite(traj_D), axis=1)]
    spec_D = estimate_spectral_dim(pts_D) if len(pts_D) > 20 else {"d_s": np.nan}
    pca_D = intrinsic_dimension_pca(pts_D)
    lam_D = pts_D[:, 1] if len(pts_D) > 0 else np.array([lam0])
    print(f"    d_s={spec_D['d_s']:.4f}, PCA={pca_D}, Lambda range=({lam_D.min():.3f},{lam_D.max():.3f})")
    results["D_conv_constantx"] = {
        "label": "CONV",
        "spectral_dim": spec_D,
        "pca_intrinsic_dim": pca_D,
        "lambda_range": (float(lam_D.min()), float(lam_D.max())),
        "note": "Scales both M,Lambda to preserve x. Orbit traces a 1D curve in 2D space.",
    }

    save_json(results, f"{OUT_J}/exp02_parameter_flows.json")
    return results


if __name__ == "__main__":
    run()
