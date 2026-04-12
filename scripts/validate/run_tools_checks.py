from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / 'src'
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from sds.benchmarks.suite import run_all_benchmarks  # noqa: E402


def main() -> int:
    output_dir = REPO_ROOT / 'data' / 'benchmark_outputs' / 'tools'
    payload = run_all_benchmarks(output_dir)
    decisions = payload['promotion_decisions']

    promoted = {name: data for name, data in decisions.items() if data['status'] == 'recommended'}
    experimental = {name: data for name, data in decisions.items() if data['status'] == 'experimental'}

    print('SDS-inspired tools benchmark suite')
    print(f'Output directory: {output_dir}')
    print(f'Recommended: {len(promoted)} | Experimental: {len(experimental)}')
    for name, data in decisions.items():
        print(f"- {name}: {data['status']} :: {data['why']}")

    summary_path = output_dir / 'summary.json'
    summary_path.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
