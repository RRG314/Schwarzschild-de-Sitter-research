# SDS Tools Final Report

## Scope

This report covers the SDS-inspired practical tool suite added to the repository as an applied layer built from the strongest reusable structural ideas in the Schwarzschild-de Sitter program.

It does not change the exact SdS theory claims. It adds a separate engineering and diagnostics layer.

## Tools Built

1. Dual-Reservoir Controller
2. Deficit-Driven Scheduler
3. State-Space Monitor
4. Equilibrium Early Stopping
5. One-Parameter Control Family

## SDS Principles Reused

- two-reservoir coupling
- bounded shared budget
- deficit term
- one-parameter reduction
- efficiency-like imbalance measure
- equilibrium / endpoint interpretation
- constrained state navigation

## Core Code Locations

- `src/sds/core/exact.py`
- `src/sds/tools/dual_reservoir/controller.py`
- `src/sds/tools/scheduler/deficit_scheduler.py`
- `src/sds/tools/monitor/state_space.py`
- `src/sds/tools/early_stopping/equilibrium.py`
- `src/sds/tools/control_family/one_parameter.py`
- `src/sds/benchmarks/suite.py`

## Workbench Integration

The SDS workbench now includes a dedicated Tools tab that:
- separates exact SdS theory from SDS-inspired engineering tools
- shows promotion and demotion decisions
- visualizes a sample controller trace in reduced SDS state space
- shows the one-parameter control curves
- exports tool benchmark snapshots and traces

Main app files:
- `app/sds-workbench/src/components/tabs/ToolsTab.tsx`
- `app/sds-workbench/src/engine/tools.ts`
- `app/sds-workbench/src/data/sdsToolsSnapshot.json`

## Benchmark Outcome

### Recommended / Supported

#### Dual-Reservoir Controller

Why it survived:
- mean best validation loss improved from `0.0804` to `0.0780` across the tested rate range
- in the aggressive band, mean best validation loss improved from `0.0784` to `0.0728`
- final validation loss improved much more strongly in the aggressive band, from `0.1749` to `0.1105`

Current role:
- promoted supported tool

#### Deficit-Driven Scheduler

Why it survived:
- remained competitive with plateau scheduling
- kept a more interpretable control signal than time-only decay

Current role:
- promoted supported tool

### Experimental But Kept

#### State-Space Monitor

Why it was not promoted:
- current predictive benchmark underperformed raw loss slope
- still useful as an interpretive diagnostic view

Current role:
- experimental

#### Equilibrium Early Stopping

Why it was not promoted:
- stopping logic was readable and stable
- compute savings were not strong enough in the current benchmark

Current role:
- experimental

#### One-Parameter Control Family

Why it was not promoted:
- greatly simplifies tuning
- best preset still lagged the best manual grid point substantially

Current role:
- experimental

## Tests And Validation Run

Python tool tests:
- `tests/tools/`
- `tests/integration/test_tools_benchmark_smoke.py`
- `tests/regression/test_tools_regression_guards.py`

App tests:
- `app/sds-workbench/src/engine/__tests__/tools.test.ts`
- existing physics and evolution tests retained

Validation entry point:
- `scripts/validate/run_sds_tools_suite.sh`

Benchmark outputs:
- `data/benchmark_outputs/tools/summary.json`
- `data/benchmark_outputs/tools/dual_reservoir_summary.csv`
- `data/benchmark_outputs/tools/scheduler_summary.csv`
- `data/benchmark_outputs/tools/early_stopping_summary.csv`
- `data/benchmark_outputs/tools/control_family_summary.csv`
- `data/benchmark_outputs/tools/sample_trace.csv`

## How To Use The Supported Tools

### Dual-Reservoir Controller

Use when:
- the run becomes brittle under aggressive learning rates
- you want a stronger stability/progress controller than a fixed optimizer setting

### Deficit-Driven Scheduler

Use when:
- you want a drop-in scheduler driven by a coupled progress/stability signal
- plateau handling matters, but you want a more structural signal than epoch count alone

## What Was Deliberately Not Overclaimed

- no claim that SdS physics literally governs optimization
- no claim that all tools are competitive by default
- no claim that the monitor is already a better predictor than loss-only baselines
- no claim that one-parameter control beats a real tuning sweep

## Recommended Next Steps

1. Re-benchmark the dual-reservoir controller on a larger supervised task where tuning sensitivity is more costly.
2. Test the deficit scheduler on noisier or longer-horizon training tasks.
3. Try the state-space monitor as a logging layer in real training code before deciding whether it deserves a stronger predictive benchmark.
4. Only keep the one-parameter family prominent if later tasks show it reduces tuning effort enough to matter in practice.
5. Expand early-stopping tests only if there is a task where plateau costs are high enough for the equilibrium signal to matter.

## Final Decision Summary

Recommended:
- Dual-Reservoir Controller
- Deficit-Driven Scheduler

Experimental:
- State-Space Monitor
- Equilibrium Early Stopping
- One-Parameter Control Family
