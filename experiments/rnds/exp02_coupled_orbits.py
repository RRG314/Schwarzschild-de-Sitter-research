"""
Experiment 02: Coupled Symmetric Map — Orbit Classification
============================================================
Question: Does coupling eps in T_{lambda,eps}(u,v) = normalize(u^lambda + eps*v,
v^lambda + eps*u) create interior fixed points or non-trivial dynamics?

Physical interpretation: coupling means the black hole horizon "feels" the
cosmological horizon and vice versa during the recursive step.  This is
analogous to thermal contact between two reservoirs at every iteration step.

Scan over (lambda, eps) grid and classify orbits as:
  - fixed: single attractor
  - cycle: small period limit cycle
  - quasi-periodic: bounded but not periodic
  - chaotic: large Lyapunov exponent
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import numpy as np
from src.recursion_models import CoupledSymmetricMap, iterate, find_attractor
from src.stability_analysis import (
    find_fixed_points_grid, numerical_jacobian, jacobian_spectrum,
    max_lyapunov_exponent
)
from src.observables import compute_observables, summary_stats
from src.state_space import x_to_uv
from src.utils import save_json, save_csv, print_section, print_result, Timer


OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")


def run():
    print_section("EXP02: Coupled Symmetric Map — Orbit Classification")

    lam_values = np.array([0.5, 0.8, 1.2, 1.5, 2.0, 2.5])
    eps_values = np.array([0.0, 0.05, 0.1, 0.2, 0.3, 0.5])

    grid_results = []
    x0 = 0.3  # starting point

    with Timer("exp02 grid scan"):
        for lam in lam_values:
            for eps in eps_values:
                f = CoupledSymmetricMap(lam, eps)
                u0, v0 = x_to_uv(x0)

                attr = find_attractor(f, u0, v0, n_warmup=3000, n_collect=500)

                # Jacobian at final point
                u_f, v_f = attr["final_u"], attr["final_v"]
                try:
                    J = numerical_jacobian(f, u_f, v_f)
                    spec = jacobian_spectrum(J)
                    sr = spec["spectral_radius"]
                    stable = spec["stable"]
                except Exception:
                    sr = np.nan
                    stable = None

                entry = {
                    "lambda": float(lam),
                    "eps": float(eps),
                    "attractor_type": attr["attractor_type"],
                    "mean_x": attr["mean_x"],
                    "std_x": attr["std_x"],
                    "period": attr["period"],
                    "spectral_radius_at_attractor": float(sr) if not np.isnan(sr) else None,
                    "jacobian_stable": stable,
                }
                grid_results.append(entry)
                print(f"    λ={lam:.2f} ε={eps:.2f}  → {attr['attractor_type']:14s}  "
                      f"x̄={attr['mean_x']:.4f}  σ_x={attr['std_x']:.2e}")

    # Detailed orbit for one interesting case: lambda=1.5, eps=0.2
    print("\n  Detailed orbit: λ=1.5, ε=0.2")
    f_detail = CoupledSymmetricMap(1.5, 0.2)
    u0, v0 = x_to_uv(0.3)
    orbit_detail = iterate(f_detail, u0, v0, n_steps=3000)
    obs_detail = compute_observables(orbit_detail)
    stats_detail = summary_stats(obs_detail)

    print_result("  x", {"mean": stats_detail["x"]["mean"], "std": stats_detail["x"]["std"]})
    print_result("  Delta", stats_detail.get("Delta", {}))
    print_result("  eta_C", stats_detail.get("eta_C", {}))

    # Fixed point search for this case
    fps = find_fixed_points_grid(f_detail, n_grid=40, n_iter=2000)
    print(f"  Fixed points found: {len(fps)}")
    for fp in fps:
        print_result("    fp", {"x": fp["x"], "sr": fp["spectral_radius"], "stable": fp["stable"]})

    summary = {
        "description": "Coupled symmetric map orbit classification",
        "grid_results": grid_results,
        "detail_case": {
            "lambda": 1.5,
            "eps": 0.2,
            "stats": {k: v for k, v in stats_detail.items()
                      if k in ["x", "Delta", "eta_C", "M", "T_ratio"]},
            "n_fixed_points": len(fps),
            "fixed_points": fps if fps else [],
        },
    }

    save_json(summary, os.path.join(OUTPUT_DIR, "exp02_coupled_orbits.json"))

    # Save orbit CSV for plotting
    save_csv(
        {k: obs_detail[k] for k in ["x", "Delta", "eta_C", "M", "T_ratio"]},
        os.path.join(OUTPUT_DIR, "exp02_detail_orbit.csv")
    )

    return summary


if __name__ == "__main__":
    run()
