from __future__ import annotations

from src.sds.benchmarks.suite import BenchmarkTrainer
from src.sds.tools.control_family.one_parameter import OneParameterControlFamily


def test_balanced_control_family_does_not_diverge_on_regression() -> None:
    trainer = BenchmarkTrainer(task="stiff_regression", seed=1, max_epochs=12, base_lr=0.05)
    summary, _ = trainer.run(
        variant="balanced_regression",
        control_setting=OneParameterControlFamily().preset("balanced"),
    )
    assert summary.diverged is False
    assert summary.best_val_loss < 1.5
