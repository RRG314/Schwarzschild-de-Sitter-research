from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from src.sds.benchmarks.suite import run_all_benchmarks


if __name__ == '__main__':
    output_dir = ROOT / 'data' / 'benchmark_outputs' / 'tools'
    payload = run_all_benchmarks(output_dir)
    print(json.dumps(payload['promotion_decisions'], indent=2))
