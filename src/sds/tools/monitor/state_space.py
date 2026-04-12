from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Literal

from ..common import clamp, ema, ratio_to_unit, safe_sqrt

Regime = Literal["productive", "transition", "equilibrium", "unstable"]


@dataclass(frozen=True)
class SDSMonitorPoint:
    epoch: int
    train_loss: float
    val_loss: float
    grad_norm: float
    step_norm: float
    hot_reservoir: float
    cold_reservoir: float
    deficit: float
    total_budget: float
    x: float
    efficiency: float
    useful_imbalance: float
    instability_score: float
    stall_score: float
    loss_volatility: float
    generalization_gap: float
    regime: Regime

    def as_dict(self) -> dict[str, float | str | int]:
        return asdict(self)


def classify_regime(
    useful_imbalance: float,
    instability_score: float,
    deficit: float,
    efficiency: float,
    hot_reservoir: float,
) -> Regime:
    if instability_score > 0.42 and hot_reservoir > 0.55:
        return "unstable"
    if useful_imbalance > 0.12:
        return "productive"
    if efficiency < 0.15 and deficit < 0.22:
        return "equilibrium"
    return "transition"


class SDSStateSpaceMonitor:
    """Map iterative training behavior into an SDS-inspired state space.

    Structural borrowing:
    - hot reservoir: local update pressure
    - cold reservoir: stability reserve
    - deficit: coupled untapped budget = sqrt(hot * cold)
    - x: reduced 1D state inside the total coupled budget
    - efficiency: bounded imbalance measure between the two reservoirs
    """

    def __init__(
        self,
        fast_alpha: float = 0.35,
        slow_alpha: float = 0.08,
    ) -> None:
        self.fast_alpha = fast_alpha
        self.slow_alpha = slow_alpha
        self._prev_train_loss: float | None = None
        self._grad_fast: float | None = None
        self._grad_slow: float | None = None
        self._loss_fast: float | None = None
        self._loss_slow: float | None = None

    def reset(self) -> None:
        self._prev_train_loss = None
        self._grad_fast = None
        self._grad_slow = None
        self._loss_fast = None
        self._loss_slow = None

    def update(
        self,
        epoch: int,
        train_loss: float,
        val_loss: float,
        grad_norm: float,
        step_norm: float,
    ) -> SDSMonitorPoint:
        self._grad_fast = ema(self._grad_fast, grad_norm, self.fast_alpha)
        self._grad_slow = ema(self._grad_slow, grad_norm, self.slow_alpha)
        self._loss_fast = ema(self._loss_fast, train_loss, self.fast_alpha)
        self._loss_slow = ema(self._loss_slow, train_loss, self.slow_alpha)

        if self._prev_train_loss is None:
            rel_improvement = 0.0
        else:
            rel_improvement = max(self._prev_train_loss - train_loss, 0.0) / max(abs(self._prev_train_loss), 1e-12)
        self._prev_train_loss = train_loss

        grad_pressure = ratio_to_unit(self._grad_fast or 0.0, self._grad_slow or 1e-12)
        improvement_signal = ratio_to_unit(rel_improvement, 0.02)
        hot = clamp(0.65 * grad_pressure + 0.35 * improvement_signal, 0.0, 1.0)

        gap = max(val_loss - train_loss, 0.0) / max(abs(val_loss), 1e-12)
        volatility = abs((self._loss_fast or train_loss) - (self._loss_slow or train_loss)) / max(abs(self._loss_slow or train_loss), 1e-12)
        cold = clamp(1.0 / (1.0 + 2.2 * volatility + 1.7 * gap), 0.0, 1.0)

        deficit = safe_sqrt(hot * cold)
        total_budget = hot + cold + deficit
        x = hot / total_budget if total_budget > 1e-12 else 0.0

        hotter = max(hot, cold) + 1e-12
        colder = min(hot, cold)
        efficiency = clamp(1.0 - colder / hotter, 0.0, 1.0)

        useful_imbalance = clamp(deficit * cold * (0.35 + 0.65 * efficiency), 0.0, 1.0)
        instability_score = clamp(max(0.0, hot - cold) * (0.6 + 0.4 * min(1.0, gap + volatility)), 0.0, 1.0)
        stall_score = clamp(0.5 * (1.0 - cold) + 0.5 * (1.0 - deficit), 0.0, 1.0)
        regime = classify_regime(useful_imbalance, instability_score, deficit, efficiency, hot)

        return SDSMonitorPoint(
            epoch=epoch,
            train_loss=float(train_loss),
            val_loss=float(val_loss),
            grad_norm=float(grad_norm),
            step_norm=float(step_norm),
            hot_reservoir=hot,
            cold_reservoir=cold,
            deficit=deficit,
            total_budget=total_budget,
            x=x,
            efficiency=efficiency,
            useful_imbalance=useful_imbalance,
            instability_score=instability_score,
            stall_score=stall_score,
            loss_volatility=volatility,
            generalization_gap=gap,
            regime=regime,
        )
