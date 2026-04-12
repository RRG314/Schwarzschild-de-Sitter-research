from __future__ import annotations

from src.sds.tools.control_family.one_parameter import OneParameterControlFamily


def test_control_family_presets_are_ordered() -> None:
    family = OneParameterControlFamily()
    conservative = family.preset("conservative")
    balanced = family.preset("balanced")
    aggressive = family.preset("aggressive")
    assert conservative.lr_scale < balanced.lr_scale < aggressive.lr_scale
    assert conservative.beta1 > aggressive.beta1
