from __future__ import annotations

from src.sds.tools.dual_reservoir.controller import DualReservoirController
from src.sds.tools.monitor.state_space import SDSStateSpaceMonitor
from src.sds.tools.scheduler.deficit_scheduler import DeficitDrivenScheduler



def _make_point(train_loss: float, val_loss: float, grad_norm: float):
    monitor = SDSStateSpaceMonitor()
    monitor.update(epoch=0, train_loss=train_loss + 0.1, val_loss=val_loss + 0.1, grad_norm=grad_norm * 0.8, step_norm=0.04)
    return monitor.update(epoch=1, train_loss=train_loss, val_loss=val_loss, grad_norm=grad_norm, step_norm=0.05)


def test_full_controller_returns_safe_bounds() -> None:
    point = _make_point(0.45, 0.52, 1.6)
    action = DualReservoirController().full_action(point)
    assert 0.15 <= action.lr_multiplier <= 1.35
    assert 0.78 <= action.beta1 <= 0.985
    assert 0.6 <= action.weight_decay_multiplier <= 2.2


def test_scheduler_scale_stays_bounded() -> None:
    point = _make_point(0.45, 0.5, 1.4)
    scheduler = DeficitDrivenScheduler()
    scale = scheduler.scale(point, epoch=4, total_epochs=40)
    assert 0.18 <= scale <= 1.0
