from __future__ import annotations

from dataclasses import asdict, dataclass

from ...core.exact import structural_budget_from_x
from ..common import clamp


@dataclass(frozen=True)
class OneParameterSetting:
    mode: str
    x: float
    lr_scale: float
    beta1: float
    weight_decay_scale: float
    noise_scale: float
    hot_fraction: float
    cold_fraction: float
    deficit_fraction: float

    def as_dict(self) -> dict[str, float | str]:
        return asdict(self)


class OneParameterControlFamily:
    PRESETS = {
        "conservative": 0.25,
        "balanced": 0.55,
        "aggressive": 0.85,
    }

    def __init__(self, base_beta1: float = 0.9) -> None:
        self.base_beta1 = base_beta1

    def setting(self, x: float, label: str = "custom") -> OneParameterSetting:
        budget = structural_budget_from_x(x)
        lr_scale = clamp(0.45 + 0.50 * budget.deficit_fraction + 0.60 * budget.hot_fraction, 0.35, 0.95)
        beta1 = clamp(0.94 - 0.12 * budget.hot_fraction + 0.03 * budget.cold_fraction, 0.85, 0.98)
        weight_decay_scale = clamp(0.65 + 1.25 * budget.cold_fraction + 0.35 * budget.deficit_fraction, 0.7, 1.8)
        noise_scale = clamp(0.01 + 0.08 * budget.hot_fraction, 0.01, 0.08)
        return OneParameterSetting(
            mode=label,
            x=x,
            lr_scale=lr_scale,
            beta1=beta1,
            weight_decay_scale=weight_decay_scale,
            noise_scale=noise_scale,
            hot_fraction=budget.hot_fraction,
            cold_fraction=budget.cold_fraction,
            deficit_fraction=budget.deficit_fraction,
        )

    def preset(self, name: str) -> OneParameterSetting:
        if name not in self.PRESETS:
            raise ValueError(f"Unknown preset {name!r}")
        return self.setting(self.PRESETS[name], name)

    def curve(self, num: int = 25) -> list[dict[str, float | str]]:
        return [self.setting(0.05 + 0.9 * i / (num - 1)).as_dict() for i in range(num)]
