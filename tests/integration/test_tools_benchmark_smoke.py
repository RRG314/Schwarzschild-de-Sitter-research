from __future__ import annotations

from pathlib import Path

from src.sds.benchmarks.suite import BenchmarkTrainer, run_monitor_benchmark
from src.sds.tools.control_family.one_parameter import OneParameterControlFamily
from src.sds.tools.scheduler.deficit_scheduler import DeficitDrivenScheduler
from src.sds.utils.io import write_json


def test_benchmark_smoke_with_tools(tmp_path: Path) -> None:
    trainer = BenchmarkTrainer(task="noisy_moons", seed=0, max_epochs=8, base_lr=0.04)
    summary, trace = trainer.run(
        variant="smoke",
        scheduler=DeficitDrivenScheduler(),
        controller_mode="full",
        control_setting=OneParameterControlFamily().preset("balanced"),
    )
    assert summary.epochs_run >= 1
    assert len(trace) == summary.epochs_run
    monitor_report = run_monitor_benchmark(trace)
    assert "monitor_rho" in monitor_report
    out = tmp_path / "smoke.json"
    write_json(out, {"summary": summary.as_dict(), "monitor": monitor_report})
    assert out.exists()
