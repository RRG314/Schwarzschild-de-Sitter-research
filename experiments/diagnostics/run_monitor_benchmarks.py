from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from src.sds.benchmarks.suite import run_dual_reservoir_benchmark, run_monitor_benchmark
from src.sds.utils.io import write_json


if __name__ == '__main__':
    output_dir = ROOT / 'data' / 'benchmark_outputs' / 'tools'
    dual = run_dual_reservoir_benchmark()
    payload = run_monitor_benchmark(dual['trace_rows'])
    write_json(output_dir / 'monitor.json', payload)
    print(json.dumps(payload, indent=2))
