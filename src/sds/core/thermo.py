from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ExactPhaseState:
    x: float
    hot_fraction: float
    cold_fraction: float
    deficit_fraction: float
    temperature_ratio: float
    carnot_efficiency: float


def _check_x(x: float) -> None:
    if not 0.0 < x < 1.0:
        raise ValueError(f"x must lie in (0, 1); received {x}")


def hot_fraction(x: float) -> float:
    _check_x(x)
    return (x * x) / (1.0 + x + x * x)


def cold_fraction(x: float) -> float:
    _check_x(x)
    return 1.0 / (1.0 + x + x * x)


def deficit_fraction(x: float) -> float:
    _check_x(x)
    return x / (1.0 + x + x * x)


def temperature_ratio(x: float) -> float:
    _check_x(x)
    return x * (x + 2.0) / (1.0 + 2.0 * x)


def carnot_efficiency(x: float) -> float:
    return 1.0 - temperature_ratio(x)


def deficit_fraction_derivative(x: float) -> float:
    _check_x(x)
    return (1.0 - x * x) / ((1.0 + x + x * x) ** 2)


def carnot_efficiency_derivative(x: float) -> float:
    _check_x(x)
    return -2.0 * (x * x + x + 1.0) / ((1.0 + 2.0 * x) ** 2)


def exact_phase_state(x: float) -> ExactPhaseState:
    return ExactPhaseState(
        x=x,
        hot_fraction=hot_fraction(x),
        cold_fraction=cold_fraction(x),
        deficit_fraction=deficit_fraction(x),
        temperature_ratio=temperature_ratio(x),
        carnot_efficiency=carnot_efficiency(x),
    )


def phase_curve_polynomial(deficit: float, efficiency: float) -> float:
    d = deficit
    e = efficiency
    return 3.0 * d * d * e * e - 3.0 * d * d * e + 3.0 * d * d + 2.0 * d * e * e - 2.0 * d * e + 2.0 * d + e - 1.0
