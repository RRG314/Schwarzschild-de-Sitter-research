"""
run_all.py — Execute all experiments in order and print a final summary.

Usage: python experiments/run_all.py
"""
import sys, os, time, traceback
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.utils import section

EXPERIMENTS = [
    ("exp01", "exp01_rebuild_sds_baseline"),
    ("exp02", "exp02_recursive_parameter_flow"),
    ("exp03", "exp03_rnds_extension"),
    ("exp04", "exp04_scalar_field_integration"),
    ("exp05", "exp05_full_robustness_scan"),
    ("exp06", "exp06_compare_with_horizon_only_model"),
]


def run_all():
    section("RUNNING ALL EXPERIMENTS")
    outcomes = {}

    for tag, modname in EXPERIMENTS:
        print(f"\n{'='*60}")
        print(f"  STARTING: {modname}")
        print(f"{'='*60}")
        t0 = time.time()
        try:
            mod = __import__(modname, fromlist=["run"])
            result = mod.run()
            elapsed = time.time() - t0
            outcomes[tag] = {"status": "PASSED", "elapsed_s": round(elapsed, 2)}
            print(f"\n  [{tag}] PASSED in {elapsed:.1f}s")
        except Exception as e:
            elapsed = time.time() - t0
            outcomes[tag] = {"status": "FAILED", "error": str(e), "elapsed_s": round(elapsed, 2)}
            print(f"\n  [{tag}] FAILED in {elapsed:.1f}s: {e}")
            traceback.print_exc()

    section("ALL EXPERIMENTS COMPLETE — SUMMARY")
    passed = sum(1 for v in outcomes.values() if v["status"] == "PASSED")
    failed = sum(1 for v in outcomes.values() if v["status"] == "FAILED")
    print(f"\n  Passed: {passed}/{len(outcomes)}")
    print(f"  Failed: {failed}/{len(outcomes)}")
    for tag, v in outcomes.items():
        status = v["status"]
        t = v["elapsed_s"]
        err = v.get("error", "")
        print(f"    {tag}: {status} ({t}s){' — ' + err if err else ''}")

    return outcomes


if __name__ == "__main__":
    run_all()
