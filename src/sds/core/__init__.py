"""Exact and structure-preserving helpers derived from the SDS program."""

from .dimensional import (
    SmallMuAsymptoticRow,
    d5_entropy_closure_residual,
    higher_dimensional_nonclosure_witness,
    higher_dimensional_small_mu_asymptotics,
    higher_dimensional_small_mu_positive_gap,
    small_mu_leading_exponent,
    small_mu_sum_asymptotic_prediction,
)
from .exact import StructuralBudget, structural_budget_from_x
from .thermo import ExactPhaseState, exact_phase_state, phase_curve_polynomial

__all__ = [
    "StructuralBudget",
    "ExactPhaseState",
    "SmallMuAsymptoticRow",
    "d5_entropy_closure_residual",
    "exact_phase_state",
    "higher_dimensional_nonclosure_witness",
    "higher_dimensional_small_mu_asymptotics",
    "higher_dimensional_small_mu_positive_gap",
    "phase_curve_polynomial",
    "small_mu_leading_exponent",
    "small_mu_sum_asymptotic_prediction",
    "structural_budget_from_x",
]
