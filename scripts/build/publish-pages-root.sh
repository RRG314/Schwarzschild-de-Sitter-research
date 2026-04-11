#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
APP_DIR="$ROOT_DIR/app/sds-workbench"
OUT_DIR="$ROOT_DIR/workbench"

if [ ! -f "$APP_DIR/package.json" ]; then
  echo "Error: app package not found at $APP_DIR" >&2
  exit 1
fi

echo "Building SdS workbench for root-level GitHub Pages deployment..."
(
  cd "$APP_DIR"
  BASE_PATH=./ npm run build
)

rm -rf "$OUT_DIR"
mkdir -p "$OUT_DIR"
cp -R "$APP_DIR/dist/." "$OUT_DIR/"

echo "Done. Published static app to: $OUT_DIR"
echo "Next: commit and push, then set GitHub Pages source to main/(root)."
