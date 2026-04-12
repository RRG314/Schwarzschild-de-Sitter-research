from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class StructuralBudget:
    """One-parameter SDS-style reduction of a coupled budget.

    This is an exact structural borrowing from the x-parametrized SdS entropy
    fractions:

        f_hot = x^2 / (1 + x + x^2)
        f_cold = 1 / (1 + x + x^2)
        f_deficit = x / (1 + x + x^2)

    The applied tools use these as a transparent control family rather than as
    a literal black-hole model.
    """

    x: float
    hot_fraction: float
    cold_fraction: float
    deficit_fraction: float

    @property
    def total(self) -> float:
        return self.hot_fraction + self.cold_fraction + self.deficit_fraction


def structural_budget_from_x(x: float) -> StructuralBudget:
    if not 0.0 < x < 1.0:
        raise ValueError(f"x must lie in (0, 1); received {x}")
    denom = 1.0 + x + x * x
    return StructuralBudget(
        x=x,
        hot_fraction=(x * x) / denom,
        cold_fraction=1.0 / denom,
        deficit_fraction=x / denom,
    )
