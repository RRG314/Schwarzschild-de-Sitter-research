from __future__ import annotations

from dataclasses import dataclass
import numpy as np

Array = np.ndarray


@dataclass(frozen=True)
class DimensionalWitnessRow:
    dimension: int
    curvature_length: float
    mass_parameter: float
    black_hole_radius: float
    cosmological_radius: float
    candidate_sum_r2: float


def horizon_polynomial_coefficients(dimension: int, curvature_length: float, mass_parameter: float) -> list[float]:
    if dimension < 4:
        raise ValueError("dimension must be at least 4")
    degree = dimension - 1
    coeffs = [0.0] * (degree + 1)
    coeffs[0] = 1.0
    coeffs[2] = -(curvature_length ** 2)
    coeffs[-1] = mass_parameter * (curvature_length ** 2)
    return coeffs


def positive_horizon_roots(dimension: int, curvature_length: float, mass_parameter: float) -> tuple[float, float]:
    coeffs = horizon_polynomial_coefficients(dimension, curvature_length, mass_parameter)
    roots = np.roots(coeffs)
    positives = sorted(root.real for root in roots if abs(root.imag) < 1e-8 and root.real > 1e-10)
    if len(positives) != 2:
        raise ValueError(
            f"Expected exactly two positive roots for D={dimension}, l={curvature_length}, mu={mass_parameter}; got {positives}"
        )
    return positives[0], positives[1]


def d5_entropy_closure_residual(curvature_length: float, mass_parameter: float) -> float:
    rb, rc = positive_horizon_roots(5, curvature_length, mass_parameter)
    return rb * rb + rc * rc - curvature_length * curvature_length


def higher_dimensional_nonclosure_witness(
    dimension: int,
    curvature_length: float,
    mass_parameters: tuple[float, ...],
) -> list[DimensionalWitnessRow]:
    if dimension <= 5:
        raise ValueError("Use dimension >= 6 for nonclosure witnesses")
    rows = []
    for mass_parameter in mass_parameters:
        rb, rc = positive_horizon_roots(dimension, curvature_length, mass_parameter)
        rows.append(
            DimensionalWitnessRow(
                dimension=dimension,
                curvature_length=curvature_length,
                mass_parameter=mass_parameter,
                black_hole_radius=rb,
                cosmological_radius=rc,
                candidate_sum_r2=rb * rb + rc * rc,
            )
        )
    return rows
