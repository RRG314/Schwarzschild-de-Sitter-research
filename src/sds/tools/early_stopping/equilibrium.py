from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..common import ema
from ..monitor.state_space import SDSMonitorPoint

StoppingMode = Literal["threshold", "relative_to_peak", "smoothed"]


@dataclass(frozen=True)
class StopDecision:
    should_stop: bool
    reason: str | None


class EquilibriumEarlyStopping:
    """Stop when useful imbalance has collapsed into equilibrium."""

    def __init__(
        self,
        mode: StoppingMode = "relative_to_peak",
        min_epochs: int = 10,
        patience: int = 6,
        threshold: float = 0.05,
        peak_ratio: float = 0.35,
        smooth_alpha: float = 0.25,
        min_delta: float = 1e-4,
    ) -> None:
        self.mode = mode
        self.min_epochs = min_epochs
        self.patience = patience
        self.threshold = threshold
        self.peak_ratio = peak_ratio
        self.smooth_alpha = smooth_alpha
        self.min_delta = min_delta
        self.best_val_loss = float("inf")
        self.last_improved_epoch = 0
        self.signal_peak = 0.0
        self.smoothed_signal: float | None = None

    def update(self, epoch: int, point: SDSMonitorPoint, val_loss: float) -> StopDecision:
        improved = val_loss < self.best_val_loss - self.min_delta
        if improved:
            self.best_val_loss = val_loss
            self.last_improved_epoch = epoch
        self.smoothed_signal = ema(self.smoothed_signal, point.useful_imbalance, self.smooth_alpha)
        self.signal_peak = max(self.signal_peak, self.smoothed_signal)
        plateau = (epoch - self.last_improved_epoch) >= self.patience

        if epoch < self.min_epochs:
            return StopDecision(False, None)

        if self.mode == "threshold":
            if plateau and self.smoothed_signal <= self.threshold:
                return StopDecision(True, "useful imbalance fell below threshold")
        elif self.mode == "relative_to_peak":
            if plateau and self.smoothed_signal <= self.signal_peak * self.peak_ratio:
                return StopDecision(True, "useful imbalance collapsed relative to peak")
        elif self.mode == "smoothed":
            if self.smoothed_signal <= self.threshold and point.regime == "equilibrium":
                return StopDecision(True, "smoothed equilibrium signal collapsed")
        return StopDecision(False, None)
