from __future__ import annotations

from ..common import clamp, ema
from ..monitor.state_space import SDSMonitorPoint


class DeficitDrivenScheduler:
    """Drop-in scheduler based on useful imbalance rather than loss alone."""

    def __init__(
        self,
        min_scale: float = 0.18,
        max_scale: float = 1.0,
        smooth_alpha: float = 0.35,
    ) -> None:
        self.min_scale = min_scale
        self.max_scale = max_scale
        self.smooth_alpha = smooth_alpha
        self._scale: float | None = None

    def reset(self) -> None:
        self._scale = None

    def scale(self, point: SDSMonitorPoint, epoch: int, total_epochs: int) -> float:
        del total_epochs
        raw = clamp(
            0.25
            + 2.2 * point.useful_imbalance
            + 0.25 * point.cold_reservoir
            - 0.35 * point.instability_score,
            self.min_scale,
            self.max_scale,
        )
        if point.regime == "unstable":
            raw *= 0.75
        elif point.regime == "equilibrium":
            raw *= 0.65
        if epoch < 3:
            raw = max(raw, 0.78)
        self._scale = ema(self._scale, raw, self.smooth_alpha)
        return clamp(self._scale, self.min_scale, self.max_scale)
