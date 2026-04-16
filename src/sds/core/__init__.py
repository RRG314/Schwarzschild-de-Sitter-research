"""Exact and structure-preserving helpers derived from the SDS program."""

from .dimensional import d5_entropy_closure_residual, higher_dimensional_nonclosure_witness
from .exact import StructuralBudget, structural_budget_from_x
from .thermo import ExactPhaseState, exact_phase_state, phase_curve_polynomial

__all__ = [
    "StructuralBudget",
    "ExactPhaseState",
    "d5_entropy_closure_residual",
    "exact_phase_state",
    "higher_dimensional_nonclosure_witness",
    "phase_curve_polynomial",
    "structural_budget_from_x",
]
