from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from src.sds.benchmarks.suite import run_dual_reservoir_benchmark
from src.sds.utils.io import write_csv, write_json


if __name__ == '__main__':
    output_dir = ROOT / 'data' / 'benchmark_outputs' / 'tools'
    payload = run_dual_reservoir_benchmark()
    write_json(output_dir / 'dual_reservoir.json', payload)
    write_csv(output_dir / 'dual_reservoir_summary.csv', payload['summary_rows'])
    print(json.dumps(payload['summary_rows'][:3], indent=2))
