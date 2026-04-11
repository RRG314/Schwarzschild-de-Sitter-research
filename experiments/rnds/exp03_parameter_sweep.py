"""
Experiment 03: Parameter Sweep — Robustness and Sensitivity
============================================================
Question: Does the qualitative behavior (convergence to boundary vs. interior
fixed point vs. chaos) change robustly, or is it sensitive to small
perturbations in parameters?

We test:
  1. Multiple initial conditions for fixed (lambda, eps) — do all orbits
     converge to the same attractor? (basin of attraction test)
  2. Asymmetric coupling: beta != 1 in T(u,v) = normalize(u^lambda + eps*v^beta,
     v^lambda + eps*u^gamma) — does symmetry-breaking create new fixed points?
  3. Comparison of mean_x across 20 different initial x0 values for
     three representative (lambda, eps) pairs.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import numpy as np
from src.recursion_models import (
    CoupledSymmetricMap, CoupledAsymmetricMap, iterate, find_attractor
)
from src.stability_analysis import max_lyapunov_exponent
from src.state_space import x_to_uv
from src.utils import save_json, print_section, print_result, Timer


OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")


def run():
    print_section("EXP03: Parameter Sweep — Robustness")

    x0_values = np.linspace(0.05, 0.95, 20)

    # Test cases: (lambda, eps)
    test_cases = [
        (1.5, 0.1, "moderate_coupling"),
        (2.0, 0.3, "strong_coupling"),
        (0.7, 0.1, "subdiffusive"),
    ]

    # -----------------------------------------------------------------------
    # Part A: Basin of attraction test
    # -----------------------------------------------------------------------
    print("\n  Part A: Basin of attraction (multiple initial conditions)")
    basin_results = {}

    with Timer("Part A"):
        for lam, eps, label in test_cases:
            f = CoupledSymmetricMap(lam, eps)
            attractor_xs = []
            for x0 in x0_values:
                u0, v0 = x_to_uv(x0)
                attr = find_attractor(f, u0, v0, n_warmup=3000, n_collect=500)
                attractor_xs.append(attr["mean_x"])

            attractor_xs = np.array(attractor_xs)
            spread = float(np.std(attractor_xs))
            single_basin = spread < 0.01  # all initial conditions converge to same place?

            basin_results[label] = {
                "lambda": lam,
                "eps": eps,
                "attractor_x_values": attractor_xs.tolist(),
                "mean_attractor_x": float(np.mean(attractor_xs)),
                "std_attractor_x": spread,
                "single_basin": single_basin,
            }
            print(f"    {label}: mean_x={np.mean(attractor_xs):.4f}  "
                  f"std={spread:.4f}  single_basin={single_basin}")

    # -----------------------------------------------------------------------
    # Part B: Asymmetric coupling sweep
    # -----------------------------------------------------------------------
    print("\n  Part B: Asymmetric coupling sweep (beta, gamma vary)")
    asym_results = []

    lam_asym = 1.5
    eps_asym = 0.2
    beta_values = [0.5, 1.0, 1.5, 2.0]
    gamma_values = [0.5, 1.0, 1.5, 2.0]

    with Timer("Part B"):
        for beta in beta_values:
            for gamma in gamma_values:
                f = CoupledAsymmetricMap(
                    lam=lam_asym, eps=eps_asym, beta=beta,
                    delta=eps_asym, gamma=gamma
                )
                u0, v0 = x_to_uv(0.3)
                attr = find_attractor(f, u0, v0, n_warmup=3000, n_collect=500)

                asym_results.append({
                    "beta": float(beta),
                    "gamma": float(gamma),
                    "attractor_type": attr["attractor_type"],
                    "mean_x": attr["mean_x"],
                    "std_x": attr["std_x"],
                })
                print(f"    β={beta:.1f} γ={gamma:.1f}  → {attr['attractor_type']:14s}  "
                      f"x̄={attr['mean_x']:.4f}")

    # -----------------------------------------------------------------------
    # Part C: Lyapunov exponent scan
    # -----------------------------------------------------------------------
    print("\n  Part C: Max Lyapunov exponent scan")
    lyap_results = []

    lam_scan = np.linspace(0.5, 3.0, 15)
    eps_fixed = 0.2

    with Timer("Part C"):
        for lam in lam_scan:
            f = CoupledSymmetricMap(lam, eps_fixed)
            u0, v0 = x_to_uv(0.3)
            mle = max_lyapunov_exponent(f, u0, v0, n_steps=3000, n_renorm=30)
            lyap_results.append({
                "lambda": float(lam),
                "eps": float(eps_fixed),
                "max_lyapunov": float(mle),
                "chaotic": mle > 0.01,
            })
            print(f"    λ={lam:.2f}  MLE={mle:.4f}  {'CHAOTIC' if mle > 0.01 else 'stable'}")

    summary = {
        "description": "Parameter sweep: robustness and sensitivity",
        "basin_results": basin_results,
        "asymmetric_coupling": asym_results,
        "lyapunov_scan": lyap_results,
    }

    save_json(summary, os.path.join(OUTPUT_DIR, "exp03_parameter_sweep.json"))
    return summary


if __name__ == "__main__":
    run()
