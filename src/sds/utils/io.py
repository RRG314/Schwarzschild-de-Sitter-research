from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Iterable, Mapping


def ensure_parent(path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    return target


def write_json(path: str | Path, payload: object) -> None:
    target = ensure_parent(path)
    target.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def write_csv(path: str | Path, rows: Iterable[Mapping[str, object]]) -> None:
    rows = list(rows)
    target = ensure_parent(path)
    if not rows:
        target.write_text("", encoding="utf-8")
        return
    with target.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
