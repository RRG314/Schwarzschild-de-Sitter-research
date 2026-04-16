#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
PYTHON_BIN="/Users/stevenreid/Documents/New project/.venv_research/bin/python"
if [ ! -x "$PYTHON_BIN" ]; then
  PYTHON_BIN="python3"
fi
"$PYTHON_BIN" -m pytest \
  tests/math/horizon_test_state_space.py \
  tests/math/recursive_test_sds_identities.py \
  tests/math/test_exact_phase_structure.py
