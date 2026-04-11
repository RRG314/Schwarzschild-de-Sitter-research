"""
Run all experiments in sequence and collect results.
"""
import sys
import os
import json
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def run_experiment(name, module_path):
    import importlib.util
    spec = importlib.util.spec_from_file_location(name, module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.run()

if __name__ == '__main__':
    exp_dir = os.path.dirname(os.path.abspath(__file__))
    experiments = [
        ('exp01_wkb_baseline',      os.path.join(exp_dir, 'exp01_wkb_baseline.py')),
        ('exp02_lambda_scaling',    os.path.join(exp_dir, 'exp02_lambda_scaling.py')),
        ('exp03_eisenstein_spectral', os.path.join(exp_dir, 'exp03_eisenstein_spectral.py')),
        ('exp04_inverse_spectroscopy', os.path.join(exp_dir, 'exp04_inverse_spectroscopy.py')),
        ('exp05_rdt_overtone',      os.path.join(exp_dir, 'exp05_rdt_overtone.py')),
    ]

    summary = {}
    for name, path in experiments:
        print(f"\n{'='*70}")
        print(f"RUNNING: {name}")
        print(f"{'='*70}")
        t0 = time.time()
        try:
            result = run_experiment(name, path)
            summary[name] = {'status': 'PASS', 'time_s': time.time() - t0}
            print(f"[PASS] {name} ({time.time()-t0:.1f}s)")
        except Exception as e:
            import traceback
            summary[name] = {'status': 'FAIL', 'error': str(e),
                             'time_s': time.time() - t0}
            print(f"[FAIL] {name}: {e}")
            traceback.print_exc()

    print(f"\n{'='*70}")
    print("EXPERIMENT SUMMARY")
    print(f"{'='*70}")
    for name, s in summary.items():
        print(f"  {s['status']:4s}  {name:40s}  ({s['time_s']:.1f}s)")

    results_dir = os.path.join(os.path.dirname(exp_dir), 'results')
    os.makedirs(results_dir, exist_ok=True)
    with open(os.path.join(results_dir, 'run_summary.json'), 'w') as f:
        json.dump(summary, f, indent=2)
