from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from src.sds.benchmarks.suite import run_early_stopping_benchmark
from src.sds.utils.io import write_csv, write_json


if __name__ == '__main__':
    output_dir = ROOT / 'data' / 'benchmark_outputs' / 'tools'
    payload = run_early_stopping_benchmark()
    write_json(output_dir / 'early_stopping.json', payload)
    write_csv(output_dir / 'early_stopping_summary.csv', payload['summary_rows'])
    print(json.dumps(payload['summary_rows'][:3], indent=2))
