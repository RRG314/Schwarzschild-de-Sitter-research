#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$REPO_ROOT"

PYTHON_BIN="${PYTHON_BIN:-python3}"
if [ -x "$REPO_ROOT/.venv/bin/python" ]; then
  PYTHON_BIN="$REPO_ROOT/.venv/bin/python"
fi

"$PYTHON_BIN" -m pytest tests/tools tests/integration tests/regression -q
"$PYTHON_BIN" scripts/validate/run_tools_checks.py
node scripts/validate/check-doc-links.mjs
(
  cd app/sds-workbench
  npm run test
  npm run build
)
