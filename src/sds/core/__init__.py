"""Exact and structure-preserving helpers derived from the SDS program."""

from .dimensional import (
    SmallMuAsymptoticRow,
    d5_entropy_closure_residual,
    higher_dimensional_nonclosure_witness,
    higher_dimensional_small_mu_asymptotics,
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
    "phase_curve_polynomial",
    "small_mu_sum_asymptotic_prediction",
    "structural_budget_from_x",
]
