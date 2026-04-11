"""utils.py — I/O, timing, JSON serialization."""

import json, time, os, csv
import numpy as np
from pathlib import Path


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer,)): return int(obj)
        if isinstance(obj, (np.floating,)): return float(obj)
        if isinstance(obj, (np.bool_,)): return bool(obj)
        if isinstance(obj, np.ndarray): return obj.tolist()
        if isinstance(obj, complex): return {"real": obj.real, "imag": obj.imag}
        return super().default(obj)


def save_json(data, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2, cls=NumpyEncoder)
    print(f"  -> {path}")


def save_csv(data: dict, path: str):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    arrays = {k: np.asarray(v) for k, v in data.items() if np.asarray(v).ndim == 1}
    if not arrays:
        return
    N = len(next(iter(arrays.values())))
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(list(arrays.keys()))
        for i in range(N):
            writer.writerow([float(arrays[k][i]) for k in arrays])
    print(f"  -> {path}")


class Timer:
    def __init__(self, name=""): self.name = name
    def __enter__(self): self.t0 = time.time(); return self
    def __exit__(self, *a): print(f"  [{self.name}] {time.time()-self.t0:.2f}s")


def section(title):
    print(f"\n{'='*60}\n  {title}\n{'='*60}")
