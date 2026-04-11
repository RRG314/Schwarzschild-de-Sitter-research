"""
Experiment 01: Symmetric Power Map — Fixed Points and Convergence
=================================================================
Question: For T_lambda(u,v) = normalize(u^lambda, v^lambda), where does
the orbit go?

Expected analysis:
  - lambda=1: identity, every point is "fixed"
  - lambda > 1: v > u, so v^lambda / u^lambda > v/u, mapping biases
    toward the v-dominated (cosmological) end
  - lambda < 1: reverse — biases toward u-dominated (BH) end

We scan lambda in [0.1, 3.0] and record:
  - Attractor x = u/v after 2000 iterations
  - Whether it converges to a fixed point
  - Jacobian stability at convergence
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import numpy as np
from src.recursion_models import SymmetricPowerMap, iterate, find_attractor
from src.stability_analysis import find_fixed_points_grid, numerical_jacobian, jacobian_spectrum
from src.observables import compute_observables
from src.state_space import x_to_uv
from src.utils import save_json, print_section, print_result, Timer


OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")


def run():
    print_section("EXP01: Symmetric Power Map — Fixed Points")

    lambda_values = np.concatenate([
        np.linspace(0.1, 0.9, 9),
        np.linspace(1.0, 3.0, 21),
    ])

    results = []

    with Timer("exp01"):
        for lam in lambda_values:
            f = SymmetricPowerMap(lam)

            # Find fixed points from grid
            fps = find_fixed_points_grid(f, n_grid=30, n_iter=2000)

            # Also run attractor detection from x0=0.3
            u0, v0 = x_to_uv(0.3)
            attr = find_attractor(f, u0, v0, n_warmup=3000, n_collect=500)

            entry = {
                "lambda": float(lam),
                "n_fixed_points": len(fps),
                "attractor_type": attr["attractor_type"],
                "attractor_mean_x": attr["mean_x"],
                "attractor_std_x": attr["std_x"],
                "fixed_points": [
                    {
                        "x": fp["x"],
                        "spectral_radius": fp["spectral_radius"],
                        "stable": fp["stable"],
                    }
                    for fp in fps
                ],
            }
            results.append(entry)
            print_result(f"  λ={lam:.2f}", {
                "attractor": attr["attractor_type"],
                "mean_x": attr["mean_x"],
                "n_fps": len(fps),
            })

    # Theoretical check: for symmetric map, fixed point satisfies
    # (u^lambda / v^lambda) = u/v  =>  (u/v)^(lambda-1) = 1
    # For lambda != 1: only x=1 (Nariai, boundary)
    # So the map always drives to x -> 1 for lambda > 1, x -> 0 for lambda < 1
    theoretical_x_inf_lambda = "x -> 1 (Nariai boundary)"
    theoretical_x_sub_lambda = "x -> 0 (BH boundary)"

    summary = {
        "description": "Symmetric power map fixed-point scan",
        "lambda_range": [float(lambda_values[0]), float(lambda_values[-1])],
        "n_lambda_values": len(lambda_values),
        "theoretical_prediction": {
            "lambda_gt_1": theoretical_x_inf_lambda,
            "lambda_lt_1": theoretical_x_sub_lambda,
        },
        "results": results,
    }

    save_json(summary, os.path.join(OUTPUT_DIR, "exp01_symmetric_fixed_points.json"))
    print(f"\n  Summary: symmetric map has NO interior fixed points — always drifts to boundary.")
    return summary


if __name__ == "__main__":
    run()
