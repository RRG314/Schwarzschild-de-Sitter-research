"""
utils.py
========
Utility functions: saving results, timing, progress, report generation.
"""

import json
import time
import numpy as np
import os
from pathlib import Path


class NumpyEncoder(json.JSONEncoder):
    """JSON encoder that handles numpy types."""
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, complex):
            return {"real": obj.real, "imag": obj.imag}
        return super().default(obj)


def save_json(data: dict, path: str):
    """Save dict to JSON file."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2, cls=NumpyEncoder)
    print(f"  Saved: {path}")


def save_csv(data: dict, path: str):
    """Save dict of equal-length arrays as CSV."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    keys = list(data.keys())
    arrays = [np.asarray(data[k]) for k in keys]
    # Filter to 1-D arrays of equal length
    length = len(arrays[0])
    valid = [(k, a) for k, a in zip(keys, arrays) if a.ndim == 1 and len(a) == length]
    if not valid:
        return
    header = ",".join(k for k, _ in valid)
    matrix = np.column_stack([a for _, a in valid])
    np.savetxt(path, matrix, delimiter=",", header=header, comments="")
    print(f"  Saved: {path}")


class Timer:
    def __init__(self, name: str = ""):
        self.name = name

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        elapsed = time.time() - self.start
        print(f"  [{self.name}] {elapsed:.2f}s")


def print_section(title: str):
    bar = "=" * 60
    print(f"\n{bar}\n  {title}\n{bar}")


def print_result(key: str, value, indent: int = 4):
    pad = " " * indent
    if isinstance(value, float):
        print(f"{pad}{key}: {value:.6g}")
    elif isinstance(value, dict):
        print(f"{pad}{key}:")
        for k, v in value.items():
            print_result(k, v, indent + 4)
    else:
        print(f"{pad}{key}: {value}")


def flatten_dict(d: dict, parent_key: str = "", sep: str = ".") -> dict:
    """Recursively flatten nested dict."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
