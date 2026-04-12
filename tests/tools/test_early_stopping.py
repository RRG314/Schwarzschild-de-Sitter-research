from __future__ import annotations

from src.sds.tools.early_stopping.equilibrium import EquilibriumEarlyStopping
from src.sds.tools.monitor.state_space import SDSMonitorPoint



def test_equilibrium_stopper_triggers_after_collapse() -> None:
    stopper = EquilibriumEarlyStopping(mode="relative_to_peak", min_epochs=3, patience=1, peak_ratio=0.85)
    productive = SDSMonitorPoint(0, 0.6, 0.6, 1.0, 0.1, 0.7, 0.5, 0.59, 1.79, 0.39, 0.29, 0.18, 0.12, 0.31, 0.04, 0.03, "productive")
    collapsed = SDSMonitorPoint(4, 0.42, 0.42, 0.2, 0.02, 0.12, 0.12, 0.12, 0.36, 0.33, 0.02, 0.01, 0.05, 0.88, 0.01, 0.0, "equilibrium")
    stopper.update(0, productive, 0.6)
    stopper.update(1, productive, 0.55)
    stopper.update(2, productive, 0.51)
    decision = stopper.update(4, collapsed, 0.51)
    assert decision.should_stop is True
