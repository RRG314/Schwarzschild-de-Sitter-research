from __future__ import annotations

from src.sds.tools.monitor.state_space import SDSStateSpaceMonitor


def test_monitor_outputs_bounded_metrics() -> None:
    monitor = SDSStateSpaceMonitor()
    point = monitor.update(epoch=1, train_loss=0.6, val_loss=0.7, grad_norm=1.2, step_norm=0.08)
    assert 0.0 <= point.hot_reservoir <= 1.0
    assert 0.0 <= point.cold_reservoir <= 1.0
    assert 0.0 <= point.efficiency <= 1.0
    assert point.regime in {"productive", "transition", "equilibrium", "unstable"}
