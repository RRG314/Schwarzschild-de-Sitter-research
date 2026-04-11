"""
run_all.py
==========
Run all experiments in sequence and produce master summary.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import json
import time
from src.utils import print_section, NumpyEncoder, save_json

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def run_all():
    print_section("RECURSIVE HORIZON RESEARCH WORKSPACE — FULL RUN")
    print("  Falsification-first build.  Results are what they are.")
    print(f"  Output directory: {OUTPUT_DIR}\n")

    from experiments.exp01_symmetric_fixed_points import run as run01
    from experiments.exp02_coupled_orbits import run as run02
    from experiments.exp03_parameter_sweep import run as run03
    from experiments.exp04_spectral_dimension import run as run04
    from experiments.exp05_rdt_weighting import run as run05

    all_results = {}
    t0 = time.time()

    for label, fn in [
        ("exp01", run01),
        ("exp02", run02),
        ("exp03", run03),
        ("exp04", run04),
        ("exp05", run05),
    ]:
        try:
            print(f"\n{'='*60}")
            print(f"  Running {label} ...")
            t_start = time.time()
            result = fn()
            elapsed = time.time() - t_start
            all_results[label] = {"status": "ok", "elapsed_s": elapsed}
            print(f"  {label} done in {elapsed:.1f}s")
        except Exception as e:
            import traceback
            print(f"  {label} FAILED: {e}")
            traceback.print_exc()
            all_results[label] = {"status": "error", "error": str(e)}

    total = time.time() - t0
    print_section(f"ALL EXPERIMENTS COMPLETE ({total:.1f}s total)")

    save_json(all_results, os.path.join(OUTPUT_DIR, "run_summary.json"))
    return all_results


if __name__ == "__main__":
    run_all()
