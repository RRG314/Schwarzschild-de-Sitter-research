"""
Experiment 04: Spectral Dimension of Recursive Orbits
=====================================================
THE KEY EXPERIMENT.

Question: Does the recursive horizon system produce an orbit with
emergent spectral dimension d_s != 1?

Expected baseline: d_s = 1 (orbit lives on a 1-D arc → simple diffusion)
Interesting result: d_s != 1 (orbit has multi-scale or fractal structure)

Non-integer d_s would indicate the recursive dynamics creates an effective
geometry that is not simply a 1-D curve.  This would be the strongest
result of the project.

We test:
  1. Reference arc (no iteration): d_s should be ~1
  2. Symmetric map orbits (boundary-drifting): d_s should be ~1 (boring)
  3. Coupled map orbits: does d_s deviate from 1?
  4. Multi-scale spectral dimension: does d_s vary with scale?

Honest reporting: if d_s ~ 1 for all cases, we report that the system
is dynamically trivial at the graph-spectral level.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import numpy as np
from src.recursion_models import SymmetricPowerMap, CoupledSymmetricMap, iterate
from src.graph_spectral import (
    estimate_spectral_dimension, multiscale_spectral_dim, build_proximity_graph
)
from src.state_space import sample_arc, x_to_uv
from src.utils import save_json, print_section, print_result, Timer


OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")


def run():
    print_section("EXP04: Spectral Dimension of Recursive Orbits")

    results = []

    # -----------------------------------------------------------------------
    # Case 0: Reference — uniformly sampled arc (expected d_s ~ 1)
    # -----------------------------------------------------------------------
    print("\n  Case 0: Reference arc (no map, uniform sampling)")
    with Timer("Case 0"):
        arc = sample_arc(n=300)
        ref_spec = estimate_spectral_dimension(arc, k_neighbors=6, t_min=0.05, t_max=3.0)
    print_result("    d_s", ref_spec["d_s"])
    print_result("    d_s_std", ref_spec["d_s_std"])
    results.append({"case": "reference_arc", **{k: ref_spec[k] for k in ["d_s", "d_s_std", "n_zero_modes"]}})

    # -----------------------------------------------------------------------
    # Case 1: Symmetric map lambda=2 (expected: drifts to boundary, d_s ~1)
    # -----------------------------------------------------------------------
    print("\n  Case 1: Symmetric map λ=2")
    with Timer("Case 1"):
        f1 = SymmetricPowerMap(2.0)
        u0, v0 = x_to_uv(0.4)
        orbit1 = iterate(f1, u0, v0, n_steps=500, clip_boundary=5e-4)
        spec1 = estimate_spectral_dimension(orbit1, k_neighbors=6, t_min=0.05, t_max=3.0)
    print_result("    d_s", spec1["d_s"])
    results.append({"case": "symmetric_lam2", **{k: spec1[k] for k in ["d_s", "d_s_std", "n_zero_modes"]}})

    # -----------------------------------------------------------------------
    # Case 2: Coupled symmetric lambda=1.5, eps=0.1
    # -----------------------------------------------------------------------
    print("\n  Case 2: Coupled symmetric λ=1.5, ε=0.1")
    with Timer("Case 2"):
        f2 = CoupledSymmetricMap(1.5, 0.1)
        u0, v0 = x_to_uv(0.4)
        orbit2 = iterate(f2, u0, v0, n_steps=1000)
        spec2 = estimate_spectral_dimension(orbit2, k_neighbors=6, t_min=0.05, t_max=3.0)
    print_result("    d_s", spec2["d_s"])
    results.append({"case": "coupled_lam15_eps01", **{k: spec2[k] for k in ["d_s", "d_s_std", "n_zero_modes"]}})

    # -----------------------------------------------------------------------
    # Case 3: Coupled symmetric lambda=2.0, eps=0.3
    # -----------------------------------------------------------------------
    print("\n  Case 3: Coupled symmetric λ=2.0, ε=0.3")
    with Timer("Case 3"):
        f3 = CoupledSymmetricMap(2.0, 0.3)
        u0, v0 = x_to_uv(0.4)
        orbit3 = iterate(f3, u0, v0, n_steps=1000)
        spec3 = estimate_spectral_dimension(orbit3, k_neighbors=6, t_min=0.05, t_max=3.0)
    print_result("    d_s", spec3["d_s"])
    results.append({"case": "coupled_lam20_eps03", **{k: spec3[k] for k in ["d_s", "d_s_std", "n_zero_modes"]}})

    # -----------------------------------------------------------------------
    # Case 4: Coupled symmetric lambda=0.7, eps=0.2 (subdiffusive)
    # -----------------------------------------------------------------------
    print("\n  Case 4: Coupled symmetric λ=0.7, ε=0.2 (sub-unity lambda)")
    with Timer("Case 4"):
        f4 = CoupledSymmetricMap(0.7, 0.2)
        u0, v0 = x_to_uv(0.6)
        orbit4 = iterate(f4, u0, v0, n_steps=1000)
        spec4 = estimate_spectral_dimension(orbit4, k_neighbors=6, t_min=0.05, t_max=3.0)
    print_result("    d_s", spec4["d_s"])
    results.append({"case": "coupled_lam07_eps02", **{k: spec4[k] for k in ["d_s", "d_s_std", "n_zero_modes"]}})

    # -----------------------------------------------------------------------
    # Multi-scale analysis: Case 3 (most interesting)
    # -----------------------------------------------------------------------
    print("\n  Multi-scale spectral dimension for Case 3")
    t_ranges = [(0.05, 0.3), (0.3, 1.0), (1.0, 5.0), (5.0, 20.0)]
    with Timer("Multiscale"):
        ms_results = multiscale_spectral_dim(orbit3, t_ranges=t_ranges, k_neighbors=6)

    for r in ms_results:
        print(f"    t=[{r['t_min']:.2f}, {r['t_max']:.2f}]  d_s={r['d_s']:.4f}")

    # Assess verdict
    print("\n  VERDICT:")
    for r in results:
        ds = r.get("d_s", float("nan"))
        deviation = abs(ds - 1.0)
        significant = deviation > 0.15
        print(f"    {r['case']:35s}  d_s={ds:.4f}  "
              f"{'SIGNIFICANT deviation from 1' if significant else 'consistent with 1'}")

    summary = {
        "description": "Spectral dimension of recursive horizon orbits",
        "reference_d_s_expected": 1.0,
        "results": results,
        "multiscale_case3": ms_results,
        "verdict": {
            "any_significant_deviation": any(
                abs(r.get("d_s", 1.0) - 1.0) > 0.15 for r in results
            ),
            "interpretation": (
                "If no significant deviation from d_s=1: the recursive dynamics "
                "does not generate non-trivial spectral geometry. The orbit is "
                "always effectively 1-dimensional, as expected for points on a curve."
            ),
        },
    }

    save_json(summary, os.path.join(OUTPUT_DIR, "exp04_spectral_dimension.json"))
    return summary


if __name__ == "__main__":
    run()
