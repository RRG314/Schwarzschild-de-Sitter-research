"""SDS exact and SDS-inspired tool suite.

This package keeps the exact Schwarzschild-de Sitter math separate from the
applied tools that borrow its structural ideas.
"""

from .core.exact import StructuralBudget, structural_budget_from_x

__all__ = ["StructuralBudget", "structural_budget_from_x"]
