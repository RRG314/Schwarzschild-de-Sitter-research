from __future__ import annotations

import math


class ConstantScheduler:
    def scale(self, epoch: int, total_epochs: int, val_loss: float) -> float:
        del epoch, total_epochs, val_loss
        return 1.0


class CosineDecayScheduler:
    def __init__(self, min_scale: float = 0.15) -> None:
        self.min_scale = min_scale

    def scale(self, epoch: int, total_epochs: int, val_loss: float) -> float:
        del val_loss
        progress = epoch / max(total_epochs - 1, 1)
        return self.min_scale + 0.5 * (1.0 - self.min_scale) * (1.0 + math.cos(math.pi * progress))


class StepDecayScheduler:
    def __init__(self, drop_every: int = 12, gamma: float = 0.5) -> None:
        self.drop_every = drop_every
        self.gamma = gamma

    def scale(self, epoch: int, total_epochs: int, val_loss: float) -> float:
        del total_epochs, val_loss
        return self.gamma ** (epoch // self.drop_every)


class ReduceOnPlateauScheduler:
    def __init__(self, factor: float = 0.6, patience: int = 5, min_scale: float = 0.18) -> None:
        self.factor = factor
        self.patience = patience
        self.min_scale = min_scale
        self.best = float("inf")
        self.bad_epochs = 0
        self.current_scale = 1.0

    def scale(self, epoch: int, total_epochs: int, val_loss: float) -> float:
        del epoch, total_epochs
        if val_loss < self.best - 1e-4:
            self.best = val_loss
            self.bad_epochs = 0
        else:
            self.bad_epochs += 1
        if self.bad_epochs >= self.patience:
            self.current_scale = max(self.min_scale, self.current_scale * self.factor)
            self.bad_epochs = 0
        return self.current_scale


class FixedEpochStopper:
    def update(self, epoch: int, val_loss: float) -> tuple[bool, str | None]:
        del epoch, val_loss
        return False, None


class PatienceEarlyStopping:
    def __init__(self, patience: int = 8, min_delta: float = 1e-4) -> None:
        self.patience = patience
        self.min_delta = min_delta
        self.best = float("inf")
        self.bad_epochs = 0

    def update(self, epoch: int, val_loss: float) -> tuple[bool, str | None]:
        del epoch
        if val_loss < self.best - self.min_delta:
            self.best = val_loss
            self.bad_epochs = 0
        else:
            self.bad_epochs += 1
        if self.bad_epochs >= self.patience:
            return True, "patience exhausted"
        return False, None


class LossChangeStopper:
    def __init__(self, threshold: float = 2e-3, patience: int = 5) -> None:
        self.threshold = threshold
        self.patience = patience
        self.prev_loss: float | None = None
        self.small_changes = 0

    def update(self, epoch: int, val_loss: float) -> tuple[bool, str | None]:
        del epoch
        if self.prev_loss is None:
            self.prev_loss = val_loss
            return False, None
        rel = abs(self.prev_loss - val_loss) / max(abs(self.prev_loss), 1e-12)
        self.prev_loss = val_loss
        if rel < self.threshold:
            self.small_changes += 1
        else:
            self.small_changes = 0
        if self.small_changes >= self.patience:
            return True, "loss-change threshold reached"
        return False, None
