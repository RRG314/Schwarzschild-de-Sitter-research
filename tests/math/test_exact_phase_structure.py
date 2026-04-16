from __future__ import annotations

import numpy as np

from src.sds.core.dimensional import (
    d5_entropy_closure_residual,
    higher_dimensional_nonclosure_witness,
    higher_dimensional_small_mu_asymptotics,
)
from src.sds.core.thermo import carnot_efficiency_derivative, deficit_fraction_derivative, exact_phase_state, phase_curve_polynomial


def test_deficit_fraction_is_strictly_increasing_on_subnariai_interval() -> None:
    xs = np.linspace(0.05, 0.95, 19)
    assert all(deficit_fraction_derivative(float(x)) > 0.0 for x in xs)


def test_carnot_efficiency_is_strictly_decreasing_on_subnariai_interval() -> None:
    xs = np.linspace(0.05, 0.95, 19)
    assert all(carnot_efficiency_derivative(float(x)) < 0.0 for x in xs)


def test_exact_phase_curve_polynomial_vanishes() -> None:
    xs = np.linspace(0.05, 0.95, 13)
    for x in xs:
        state = exact_phase_state(float(x))
        residual = phase_curve_polynomial(state.deficit_fraction, state.carnot_efficiency)
        assert abs(residual) < 1e-12


def test_d5_entropy_closure_is_exact() -> None:
    for mu in (0.05, 0.12, 0.18, 0.22):
        residual = d5_entropy_closure_residual(curvature_length=1.0, mass_parameter=mu)
        assert abs(residual) < 1e-10


def test_d6_candidate_two_root_sum_is_not_fixed_by_lambda_alone() -> None:
    rows = higher_dimensional_nonclosure_witness(6, 1.0, (0.02, 0.06, 0.1))
    values = [row.candidate_sum_r2 for row in rows]
    assert max(values) - min(values) > 1e-3


def test_higher_dimensional_small_mu_asymptotics_track_nonclosure_deviation() -> None:
    rows = higher_dimensional_small_mu_asymptotics(6, 1.0, (1e-4, 5e-4, 1e-3))
    actual = [row.actual_deviation for row in rows]
    predicted = [row.predicted_deviation for row in rows]
    assert all(value > 0.0 for value in actual)
    assert all(value > 0.0 for value in predicted)
    relative_errors = [abs(row.actual_deviation - row.predicted_deviation) / row.actual_deviation for row in rows]
    assert max(relative_errors) < 0.1
