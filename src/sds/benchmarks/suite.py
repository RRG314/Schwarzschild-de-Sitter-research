from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any, Callable

import numpy as np
from scipy.stats import spearmanr

from ..tools.control_family.one_parameter import OneParameterControlFamily
from ..tools.dual_reservoir.controller import DualReservoirController
from ..tools.early_stopping.equilibrium import EquilibriumEarlyStopping
from ..tools.monitor.state_space import SDSMonitorPoint, SDSStateSpaceMonitor
from ..tools.scheduler.deficit_scheduler import DeficitDrivenScheduler
from ..utils.io import write_csv, write_json
from .baselines import (
    ConstantScheduler,
    CosineDecayScheduler,
    FixedEpochStopper,
    LossChangeStopper,
    PatienceEarlyStopping,
    ReduceOnPlateauScheduler,
    StepDecayScheduler,
)
from .datasets import make_noisy_moons, make_stiff_regression
from .model import TinyMLP
from .optimizer import AdamOptimizer


DATASETS: dict[str, Callable[[int], tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]]] = {
    "noisy_moons": make_noisy_moons,
    "stiff_regression": make_stiff_regression,
}


@dataclass
class TraceSummary:
    task: str
    variant: str
    seed: int
    final_train_loss: float
    final_val_loss: float
    best_val_loss: float
    final_accuracy: float | None
    best_accuracy: float | None
    epochs_run: int
    diverged: bool
    stop_reason: str | None

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


class BenchmarkTrainer:
    def __init__(
        self,
        task: str,
        seed: int,
        max_epochs: int = 48,
        batch_size: int = 32,
        base_lr: float = 0.035,
        base_beta1: float = 0.9,
        base_weight_decay: float = 1e-3,
    ) -> None:
        self.task = task
        self.seed = seed
        self.max_epochs = max_epochs
        self.batch_size = batch_size
        self.base_lr = base_lr
        self.base_beta1 = base_beta1
        self.base_weight_decay = base_weight_decay

        x_train, y_train, x_val, y_val = DATASETS[task](seed)
        self.x_train = x_train
        self.y_train = y_train
        self.x_val = x_val
        self.y_val = y_val
        out_dim = 1
        self.model = TinyMLP(in_dim=x_train.shape[1], hidden_dim=16, out_dim=out_dim, task=("classification" if task == "noisy_moons" else "regression"), seed=seed)
        self.optimizer = AdamOptimizer(self.model.params, lr=base_lr, beta1=base_beta1)
        self.monitor = SDSStateSpaceMonitor()

    def _iterate_batches(self, rng: np.random.Generator):
        idx = rng.permutation(len(self.x_train))
        for start in range(0, len(idx), self.batch_size):
            batch_idx = idx[start:start + self.batch_size]
            yield self.x_train[batch_idx], self.y_train[batch_idx]

    def _evaluate(self, weight_decay: float) -> tuple[float, float | None]:
        result = self.model.loss_and_grads(self.x_val, self.y_val, weight_decay=weight_decay)
        return result.loss, result.accuracy

    def run(
        self,
        variant: str,
        scheduler: Any | None = None,
        controller_mode: str | None = None,
        stopper: Any | None = None,
        control_setting: Any | None = None,
    ) -> tuple[TraceSummary, list[dict[str, Any]]]:
        rng = np.random.default_rng(self.seed)
        trace: list[dict[str, Any]] = []
        best_val_loss = float("inf")
        best_acc: float | None = None
        controller = DualReservoirController(base_beta1=self.base_beta1)

        control_lr_scale = getattr(control_setting, "lr_scale", 1.0)
        control_beta1 = getattr(control_setting, "beta1", self.base_beta1)
        control_wd_scale = getattr(control_setting, "weight_decay_scale", 1.0)

        last_val_acc: float | None = None
        stop_reason: str | None = None
        diverged = False
        current_beta1 = control_beta1

        for epoch in range(self.max_epochs):
            scheduler_scale = 1.0
            epoch_grad_norms: list[float] = []
            epoch_step_norms: list[float] = []
            batch_losses: list[float] = []

            for x_batch, y_batch in self._iterate_batches(rng):
                weight_decay = self.base_weight_decay * control_wd_scale
                if controller_mode == "full" and trace:
                    weight_decay *= trace[-1]["weight_decay_multiplier"]
                result = self.model.loss_and_grads(x_batch, y_batch, weight_decay=weight_decay)
                batch_losses.append(result.loss)

                if controller_mode == "full" and trace:
                    lr_multiplier = trace[-1]["lr_multiplier"]
                    current_beta1 = trace[-1]["beta1"]
                elif controller_mode == "efficiency_only" and trace:
                    lr_multiplier = trace[-1]["lr_multiplier"]
                    current_beta1 = control_beta1
                else:
                    lr_multiplier = 1.0
                    current_beta1 = control_beta1

                if scheduler is not None and trace:
                    scheduler_scale = trace[-1]["scheduler_scale"]

                effective_lr = self.base_lr * control_lr_scale * lr_multiplier * scheduler_scale
                step_stats = self.optimizer.step(
                    result.grads,
                    lr=effective_lr,
                    beta1=current_beta1,
                    weight_decay=0.0,
                    clip_norm=5.0,
                )
                epoch_grad_norms.append(step_stats["grad_norm"])
                epoch_step_norms.append(step_stats["step_norm"])

            train_eval = self.model.loss_and_grads(self.x_train, self.y_train, weight_decay=self.base_weight_decay * control_wd_scale)
            val_loss, val_acc = self._evaluate(weight_decay=self.base_weight_decay * control_wd_scale)
            point = self.monitor.update(
                epoch=epoch,
                train_loss=train_eval.loss,
                val_loss=val_loss,
                grad_norm=float(np.mean(epoch_grad_norms)),
                step_norm=float(np.mean(epoch_step_norms)),
            )

            if scheduler is None:
                scheduler_scale = 1.0
            elif isinstance(scheduler, DeficitDrivenScheduler):
                scheduler_scale = scheduler.scale(point, epoch, self.max_epochs)
            else:
                scheduler_scale = scheduler.scale(epoch, self.max_epochs, val_loss)

            if controller_mode == "full":
                action = controller.full_action(point)
            elif controller_mode == "efficiency_only":
                action = controller.efficiency_only(point)
            else:
                action = None

            if val_loss < best_val_loss:
                best_val_loss = val_loss
            if val_acc is not None:
                best_acc = val_acc if best_acc is None else max(best_acc, val_acc)
                last_val_acc = val_acc

            row = point.as_dict()
            row.update(
                {
                    "variant": variant,
                    "task": self.task,
                    "seed": self.seed,
                    "train_accuracy": train_eval.accuracy,
                    "val_accuracy": val_acc,
                    "batch_loss_mean": float(mean(batch_losses)),
                    "scheduler_scale": scheduler_scale,
                    "lr_multiplier": action.lr_multiplier if action else 1.0,
                    "beta1": action.beta1 if action else current_beta1,
                    "weight_decay_multiplier": action.weight_decay_multiplier if action else 1.0,
                    "effective_lr": self.base_lr * control_lr_scale * (action.lr_multiplier if action else 1.0) * scheduler_scale,
                }
            )
            trace.append(row)

            if not np.isfinite(val_loss) or val_loss > 20.0:
                diverged = True
                stop_reason = "diverged"
                break

            if stopper is not None:
                if isinstance(stopper, EquilibriumEarlyStopping):
                    decision = stopper.update(epoch, point, val_loss)
                    should_stop, reason = decision.should_stop, decision.reason
                else:
                    should_stop, reason = stopper.update(epoch, val_loss)
                if should_stop:
                    stop_reason = reason
                    break

        final_row = trace[-1]
        summary = TraceSummary(
            task=self.task,
            variant=variant,
            seed=self.seed,
            final_train_loss=float(final_row["train_loss"]),
            final_val_loss=float(final_row["val_loss"]),
            best_val_loss=float(best_val_loss),
            final_accuracy=last_val_acc,
            best_accuracy=best_acc,
            epochs_run=len(trace),
            diverged=diverged,
            stop_reason=stop_reason,
        )
        return summary, trace


def _summaries_to_rows(summaries: list[TraceSummary]) -> list[dict[str, Any]]:
    return [item.as_dict() for item in summaries]


def run_dual_reservoir_benchmark() -> dict[str, Any]:
    summaries: list[TraceSummary] = []
    traces: list[dict[str, Any]] = []
    for seed in (0, 1, 2):
        # This controller is intended for aggressive or tuning-sensitive
        # regimes, so the benchmark deliberately spans one safe LR and two
        # brittle ones instead of only measuring the easy band.
        for lr in (0.05, 0.30, 0.60):
            for variant, controller_mode in (
                (f"adam@{lr:.2f}", None),
                (f"efficiency_only@{lr:.2f}", "efficiency_only"),
                (f"dual_reservoir@{lr:.2f}", "full"),
            ):
                trainer = BenchmarkTrainer(task="noisy_moons", seed=seed, base_lr=lr)
                summary, trace = trainer.run(variant=variant, controller_mode=controller_mode)
                summaries.append(summary)
                traces.extend(trace)
    return {"summary_rows": _summaries_to_rows(summaries), "trace_rows": traces}


def run_scheduler_benchmark() -> dict[str, Any]:
    summaries: list[TraceSummary] = []
    traces: list[dict[str, Any]] = []
    scheduler_factories = {
        "constant": ConstantScheduler,
        "cosine": CosineDecayScheduler,
        "step": StepDecayScheduler,
        "plateau": ReduceOnPlateauScheduler,
        "deficit": DeficitDrivenScheduler,
    }
    for seed in (0, 1, 2):
        for name, factory in scheduler_factories.items():
            trainer = BenchmarkTrainer(task="noisy_moons", seed=seed, base_lr=0.05)
            summary, trace = trainer.run(variant=name, scheduler=factory())
            summaries.append(summary)
            traces.extend(trace)
    return {"summary_rows": _summaries_to_rows(summaries), "trace_rows": traces}


def run_monitor_benchmark(reference_traces: list[dict[str, Any]]) -> dict[str, Any]:
    grouped: dict[tuple[str, int], list[dict[str, Any]]] = {}
    for row in reference_traces:
        key = (row["variant"], row["seed"])
        grouped.setdefault(key, []).append(row)

    monitor_scores: list[float] = []
    raw_scores: list[float] = []
    future_improvements: list[float] = []
    for trace in grouped.values():
        trace = sorted(trace, key=lambda row: int(row["epoch"]))
        val_losses = [float(row["val_loss"]) for row in trace]
        train_losses = [float(row["train_loss"]) for row in trace]
        for idx in range(1, max(1, len(trace) - 5)):
            current_val = val_losses[idx]
            future_best = min(val_losses[idx + 1: idx + 6]) if idx + 1 < len(val_losses) else current_val
            future_gain = max(0.0, current_val - future_best) / max(abs(current_val), 1e-12)
            future_improvements.append(future_gain)
            monitor_scores.append(float(trace[idx]["useful_imbalance"]))
            raw_scores.append(abs(train_losses[idx] - train_losses[idx - 1]) / max(abs(train_losses[idx - 1]), 1e-12))

    monitor_rho = float(spearmanr(monitor_scores, future_improvements).statistic)
    raw_rho = float(spearmanr(raw_scores, future_improvements).statistic)
    return {
        "metric": "spearman_correlation_to_5_epoch_future_validation_improvement",
        "monitor_rho": monitor_rho,
        "raw_loss_slope_rho": raw_rho,
        "advantage": monitor_rho - raw_rho,
    }


def run_early_stopping_benchmark() -> dict[str, Any]:
    summaries: list[TraceSummary] = []
    traces: list[dict[str, Any]] = []
    stopper_factories = {
        "fixed_epochs": FixedEpochStopper,
        "patience": PatienceEarlyStopping,
        "loss_change": LossChangeStopper,
        "equilibrium_threshold": lambda: EquilibriumEarlyStopping(mode="threshold"),
        "equilibrium_relative_peak": lambda: EquilibriumEarlyStopping(mode="relative_to_peak"),
        "equilibrium_smoothed": lambda: EquilibriumEarlyStopping(mode="smoothed"),
    }
    for seed in (0, 1, 2):
        for name, factory in stopper_factories.items():
            trainer = BenchmarkTrainer(task="noisy_moons", seed=seed, base_lr=0.045, max_epochs=60)
            summary, trace = trainer.run(variant=name, stopper=factory())
            summaries.append(summary)
            traces.extend(trace)
    return {"summary_rows": _summaries_to_rows(summaries), "trace_rows": traces}


def run_control_family_benchmark() -> dict[str, Any]:
    summaries: list[TraceSummary] = []
    traces: list[dict[str, Any]] = []
    family = OneParameterControlFamily()
    manual_grid = [
        {"name": f"grid_lr{lr:.2f}_b{beta1:.2f}_wd{wd:.4f}", "lr": lr, "beta1": beta1, "wd": wd}
        for lr in (0.025, 0.035, 0.05)
        for beta1 in (0.88, 0.92, 0.96)
        for wd in (5e-4, 1e-3, 2e-3)
    ]

    for seed in (0, 1, 2):
        for preset_name in ("conservative", "balanced", "aggressive"):
            setting = family.preset(preset_name)
            trainer = BenchmarkTrainer(task="stiff_regression", seed=seed, base_lr=0.05, base_weight_decay=1e-3)
            summary, trace = trainer.run(variant=f"control_{preset_name}", control_setting=setting)
            summaries.append(summary)
            traces.extend(trace)
        for config in manual_grid:
            trainer = BenchmarkTrainer(
                task="stiff_regression",
                seed=seed,
                base_lr=config["lr"],
                base_beta1=config["beta1"],
                base_weight_decay=config["wd"],
            )
            summary, trace = trainer.run(variant=config["name"])
            summaries.append(summary)
            traces.extend(trace)
    return {
        "summary_rows": _summaries_to_rows(summaries),
        "trace_rows": traces,
        "control_curve": family.curve(),
    }


def classify_tools(dual: dict[str, Any], scheduler: dict[str, Any], monitor: dict[str, Any], early: dict[str, Any], control: dict[str, Any]) -> dict[str, Any]:
    def _mean_where(rows: list[dict[str, Any]], prefix: str, key: str) -> float:
        values = [float(row[key]) for row in rows if str(row["variant"]).startswith(prefix) and row[key] is not None]
        return float(mean(values)) if values else float("nan")

    dual_rows = dual["summary_rows"]
    dual_controller_val = _mean_where(dual_rows, "dual_reservoir", "best_val_loss")
    dual_baseline_val = _mean_where(dual_rows, "adam", "best_val_loss")
    dual_controller_div = _mean_where(dual_rows, "dual_reservoir", "diverged")
    dual_baseline_div = _mean_where(dual_rows, "adam", "diverged")

    scheduler_rows = scheduler["summary_rows"]
    deficit_val = _mean_where(scheduler_rows, "deficit", "best_val_loss")
    plateau_val = _mean_where(scheduler_rows, "plateau", "best_val_loss")

    early_rows = early["summary_rows"]
    fixed_epochs = _mean_where(early_rows, "fixed_epochs", "epochs_run")
    eq_epochs = _mean_where(early_rows, "equilibrium_relative_peak", "epochs_run")
    fixed_acc = _mean_where(early_rows, "fixed_epochs", "best_accuracy")
    eq_acc = _mean_where(early_rows, "equilibrium_relative_peak", "best_accuracy")

    control_rows = control["summary_rows"]
    preset_best = min(float(row["best_val_loss"]) for row in control_rows if str(row["variant"]).startswith("control_"))
    grid_best = min(float(row["best_val_loss"]) for row in control_rows if str(row["variant"]).startswith("grid_"))

    decisions = {
        "dual_reservoir_controller": {
            "status": "recommended" if dual_controller_div <= dual_baseline_div and dual_controller_val <= dual_baseline_val * 1.02 else "experimental",
            "why": "Improves or matches validation loss while reducing divergence under aggressive learning rates." if dual_controller_div <= dual_baseline_div and dual_controller_val <= dual_baseline_val * 1.02 else "Stable but not clearly stronger than a simpler baseline across the tested range.",
        },
        "deficit_driven_scheduler": {
            "status": "recommended" if deficit_val <= plateau_val * 1.03 else "experimental",
            "why": "Competitive with plateau scheduling while using an SDS-inspired useful-imbalance signal." if deficit_val <= plateau_val * 1.03 else "Usable, but not clearly stronger than standard plateau scheduling in the current benchmark.",
        },
        "state_space_monitor": {
            "status": "recommended" if monitor["advantage"] > 0.05 else "experimental",
            "why": "Predicts short-horizon validation improvement better than raw loss slope." if monitor["advantage"] > 0.05 else "Interpretable, but only marginally better than raw loss slope in the current traces.",
        },
        "equilibrium_early_stopping": {
            "status": "recommended" if eq_epochs <= fixed_epochs * 0.8 and eq_acc >= fixed_acc - 0.01 else "experimental",
            "why": "Saves compute with only a small accuracy tradeoff relative to fixed-length training." if eq_epochs <= fixed_epochs * 0.8 and eq_acc >= fixed_acc - 0.01 else "Works, but compute savings are not yet strong enough to make it the default stopper.",
        },
        "one_parameter_control_family": {
            "status": "recommended" if preset_best <= grid_best * 1.08 else "experimental",
            "why": "Gets close to the best three-knob grid while using a single SDS-style control parameter." if preset_best <= grid_best * 1.08 else "Convenient, but not close enough to the best manual grid to make it a default control path.",
        },
    }
    return decisions


def run_all_benchmarks(output_dir: str | Path) -> dict[str, Any]:
    output_dir = Path(output_dir)
    dual = run_dual_reservoir_benchmark()
    scheduler = run_scheduler_benchmark()
    monitor = run_monitor_benchmark(dual["trace_rows"])
    early = run_early_stopping_benchmark()
    control = run_control_family_benchmark()
    decisions = classify_tools(dual, scheduler, monitor, early, control)

    payload = {
        "dual_reservoir": dual,
        "scheduler": scheduler,
        "monitor": monitor,
        "early_stopping": early,
        "control_family": control,
        "promotion_decisions": decisions,
    }
    write_json(output_dir / "summary.json", payload)
    write_csv(output_dir / "dual_reservoir_summary.csv", dual["summary_rows"])
    write_csv(output_dir / "scheduler_summary.csv", scheduler["summary_rows"])
    write_csv(output_dir / "early_stopping_summary.csv", early["summary_rows"])
    write_csv(output_dir / "control_family_summary.csv", control["summary_rows"])
    write_csv(output_dir / "sample_trace.csv", dual["trace_rows"][:120])
    return payload
