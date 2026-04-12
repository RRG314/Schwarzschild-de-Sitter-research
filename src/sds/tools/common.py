from __future__ import annotations

import math


def clamp(value: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, value))


def ratio_to_unit(numerator: float, reference: float, eps: float = 1e-12) -> float:
    numerator = max(0.0, float(numerator))
    reference = max(eps, float(reference))
    return numerator / (numerator + reference)


def ema(previous: float | None, value: float, alpha: float) -> float:
    value = float(value)
    if previous is None:
        return value
    return alpha * value + (1.0 - alpha) * previous


def safe_sqrt(value: float) -> float:
    return math.sqrt(max(0.0, float(value)))
