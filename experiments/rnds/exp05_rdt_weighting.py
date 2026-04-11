"""
Experiment 05: RDT Weighting — Effective Entropy and Thermodynamic Observables
==============================================================================
Question: Does applying RDT (base-e geometric depth weighting) to the orbit
produce an "effective" entropy or temperature that has different properties
than the time-average?

RDT gives higher weight to recent (shallow) steps and exponential decay to
older (deeper) steps.  If the orbit has memory or convergence structure,
RDT and uniform averages will differ.

We test:
  1. RDT vs. uniform average of x, Delta, eta_C for coupled orbits
  2. Depth-stratified variance: is variance decreasing over time? (convergence)
  3. RDT-weighted effective Carnot efficiency vs. terminal value
  4. Test the exact S_Lambda conservation along recursion (key diagnostic)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import numpy as np
from src.recursion_models import CoupledSymmetricMap, iterate
from src.observables import compute_observables, check_carnot_relation
from src.depth_weights import (
    rdt_weighted_mean, depth_stratified_variance, effective_rdt_entropy
)
from src.state_space import x_to_uv
from src.utils import save_json, print_section, print_result, Timer


OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")


def run():
    print_section("EXP05: RDT Weighting and Entropy Conservation")

    results = {}

    # -----------------------------------------------------------------------
    # Test cases
    # -----------------------------------------------------------------------
    cases = [
        (1.5, 0.1, 0.3, "coupled_mild"),
        (2.0, 0.3, 0.3, "coupled_strong"),
        (0.7, 0.2, 0.6, "coupled_sub"),
    ]

    with Timer("RDT analysis"):
        for lam, eps, x0, label in cases:
            f = CoupledSymmetricMap(lam, eps)
            u0, v0 = x_to_uv(x0)
            orbit = iterate(f, u0, v0, n_steps=3000)
            obs = compute_observables(orbit)

            # Uniform vs RDT averages
            x_arr = obs["x"]
            Delta_arr = obs["Delta"]
            eta_arr = obs["eta_C"]

            x_uniform = float(np.mean(x_arr))
            x_rdt = rdt_weighted_mean(x_arr)
            Delta_uniform = float(np.mean(Delta_arr))
            Delta_rdt = rdt_weighted_mean(Delta_arr)
            eta_uniform = float(np.mean(eta_arr))
            eta_rdt = rdt_weighted_mean(eta_arr)

            # Depth-stratified variance
            x_variance = depth_stratified_variance(x_arr, n_strata=5)
            Delta_variance = depth_stratified_variance(Delta_arr, n_strata=5)

            # RDT effective entropy
            rdt_ent = effective_rdt_entropy(obs["S_b"], obs["S_c"])

            # S_Lambda conservation check (THE key test)
            carnot_check = check_carnot_relation(obs)

            # Terminal values
            x_terminal = float(x_arr[-1])
            Delta_terminal = float(Delta_arr[-1])

            print(f"\n  Case: {label} (λ={lam}, ε={eps})")
            print(f"    x:     uniform={x_uniform:.4f}  rdt={x_rdt:.4f}  terminal={x_terminal:.4f}")
            print(f"    Delta: uniform={Delta_uniform:.4f}  rdt={Delta_rdt:.4f}  terminal={Delta_terminal:.4f}")
            print(f"    eta_C: uniform={eta_uniform:.4f}  rdt={eta_rdt:.4f}")
            print(f"    S_Lambda conservation: passed={carnot_check['passed']}  "
                  f"rel_std={carnot_check.get('S_Lambda_rel_std', 'N/A')}")
            print(f"    x variance converging: {x_variance['converging']}  "
                  f"ratio={x_variance['variance_ratio']:.4f}")

            results[label] = {
                "lambda": lam,
                "eps": eps,
                "x0": x0,
                "x_uniform": x_uniform,
                "x_rdt": x_rdt,
                "x_terminal": x_terminal,
                "Delta_uniform": Delta_uniform,
                "Delta_rdt": Delta_rdt,
                "eta_uniform": eta_uniform,
                "eta_rdt": eta_rdt,
                "rdt_entropy": rdt_ent,
                "S_Lambda_conservation": carnot_check,
                "x_variance_converging": x_variance["converging"],
                "x_variance_ratio": x_variance["variance_ratio"],
                "x_stratum_variances": x_variance["stratum_variances"],
            }

    # -----------------------------------------------------------------------
    # Conservation law stress test:
    # S_Lambda = S_b + S_c + Delta = 3*pi (for Lambda=1)
    # This must hold exactly because we normalize to Eisenstein ellipse.
    # Any deviation is a numerical error / bug.
    # -----------------------------------------------------------------------
    print("\n  S_Lambda conservation stress test (3*pi = 9.4248...)")
    S_Lambda_exact = 3.0 * np.pi
    print(f"    Expected S_Lambda = {S_Lambda_exact:.6f}")

    f_test = CoupledSymmetricMap(1.5, 0.3)
    u0, v0 = x_to_uv(0.3)
    orbit_test = iterate(f_test, u0, v0, n_steps=5000)
    obs_test = compute_observables(orbit_test)
    S_Lambda_orbit = obs_test["S_b"] + obs_test["S_c"] + obs_test["Delta"]
    max_dev = float(np.max(np.abs(S_Lambda_orbit - S_Lambda_exact)))
    rel_dev = max_dev / S_Lambda_exact

    print(f"    Max absolute deviation: {max_dev:.2e}")
    print(f"    Max relative deviation: {rel_dev:.2e}")
    conservation_exact = rel_dev < 1e-10
    print(f"    Conservation exact to 1e-10: {conservation_exact}")

    results["conservation_stress_test"] = {
        "S_Lambda_exact": S_Lambda_exact,
        "max_abs_deviation": max_dev,
        "max_rel_deviation": rel_dev,
        "conservation_holds": bool(conservation_exact),
    }

    summary = {
        "description": "RDT weighting and entropy conservation diagnostics",
        "S_Lambda_exact": S_Lambda_exact,
        "results": results,
    }

    save_json(summary, os.path.join(OUTPUT_DIR, "exp05_rdt_weighting.json"))
    return summary


if __name__ == "__main__":
    run()
