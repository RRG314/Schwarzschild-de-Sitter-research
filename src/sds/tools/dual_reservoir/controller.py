from __future__ import annotations

from dataclasses import dataclass

from ..common import clamp
from ..monitor.state_space import SDSMonitorPoint


@dataclass(frozen=True)
class DualReservoirAction:
    lr_multiplier: float
    beta1: float
    weight_decay_multiplier: float
    reason: str


class DualReservoirController:
    """Adapt optimizer controls using SDS-inspired coupled metrics."""

    def __init__(
        self,
        base_beta1: float = 0.9,
        min_lr_multiplier: float = 0.15,
        max_lr_multiplier: float = 1.35,
    ) -> None:
        self.base_beta1 = base_beta1
        self.min_lr_multiplier = min_lr_multiplier
        self.max_lr_multiplier = max_lr_multiplier

    def efficiency_only(self, point: SDSMonitorPoint) -> DualReservoirAction:
        stable_efficiency = point.efficiency * (0.4 + 0.6 * point.cold_reservoir)
        lr_multiplier = clamp(0.35 + stable_efficiency, 0.2, 1.2)
        return DualReservoirAction(
            lr_multiplier=lr_multiplier,
            beta1=self.base_beta1,
            weight_decay_multiplier=1.0,
            reason="Single SDS metric ablation using efficiency only",
        )

    def full_action(self, point: SDSMonitorPoint) -> DualReservoirAction:
        lr_multiplier = clamp(
            0.55
            + 0.75 * point.cold_reservoir
            + 0.20 * point.deficit
            - 0.55 * point.hot_reservoir,
            self.min_lr_multiplier,
            self.max_lr_multiplier,
        )
        if point.regime == "equilibrium":
            lr_multiplier *= 0.82
        elif point.regime == "unstable":
            lr_multiplier *= 0.70

        beta1 = clamp(
            self.base_beta1 + 0.06 * point.instability_score - 0.03 * point.useful_imbalance,
            0.78,
            0.985,
        )
        weight_decay_multiplier = clamp(
            0.8 + 1.1 * point.deficit + 0.35 * max(0.0, point.hot_reservoir - point.cold_reservoir),
            0.6,
            2.2,
        )
        return DualReservoirAction(
            lr_multiplier=lr_multiplier,
            beta1=beta1,
            weight_decay_multiplier=weight_decay_multiplier,
            reason=f"Dual-reservoir controller in {point.regime} regime",
        )
