"""SDS exact and SDS-inspired tool suite.

This package keeps the exact Schwarzschild-de Sitter math separate from the
applied tools that borrow its structural ideas.
"""

from .core import (
    ExactPhaseState,
    SmallMuAsymptoticRow,
    StructuralBudget,
    d5_entropy_closure_residual,
    exact_phase_state,
    higher_dimensional_nonclosure_witness,
    higher_dimensional_small_mu_asymptotics,
    higher_dimensional_small_mu_positive_gap,
    phase_curve_polynomial,
    small_mu_leading_exponent,
    small_mu_sum_asymptotic_prediction,
    structural_budget_from_x,
)

__all__ = [
    "ExactPhaseState",
    "SmallMuAsymptoticRow",
    "StructuralBudget",
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
