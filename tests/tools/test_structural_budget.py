from __future__ import annotations

import pytest

from src.sds.core.exact import structural_budget_from_x


def test_structural_budget_sums_to_one() -> None:
    budget = structural_budget_from_x(0.55)
    assert abs(budget.total - 1.0) < 1e-12


def test_structural_budget_rejects_invalid_x() -> None:
    with pytest.raises(ValueError):
        structural_budget_from_x(0.0)
