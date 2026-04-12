# State-Space Monitor

## What It Is

A low-dimensional monitor that maps training behavior into an SDS-inspired state space.

Coordinates and signals include:
- reduced state `x`
- hot reservoir
- cold reservoir
- deficit
- efficiency
- useful imbalance
- instability score
- stall score
- regime label

## Practical Problem

Loss curves alone often hide whether a run is productive, stalled, or drifting into a brittle region. This monitor tries to make the training story easier to read.

## Current Result

What worked:
- the trace is readable
- the regimes are interpretable
- the workbench visualization is useful as a diagnostic layer

What did not work well enough yet:
- on the current prediction benchmark, the monitor signal was worse than raw loss slope for short-horizon validation improvement forecasting

Benchmark numbers:
- monitor rho: `0.1277`
- raw loss-slope rho: `0.4189`
- advantage: `-0.2911`

Status:
- experimental

## When To Use This

Use it when:
- you want a better story about the run than loss alone gives you
- you want to inspect transitions between productive, transitional, equilibrium-like, and unstable behavior
- you want logging or export of those higher-level states

## When Not To Use This

Do not use it as:
- a promoted predictor of future improvement
- a replacement for simpler validation plots when prediction quality matters most

## Key Files

- `src/sds/tools/monitor/state_space.py`
- `experiments/diagnostics/run_monitor_benchmarks.py`
- `app/sds-workbench/src/components/tabs/ToolsTab.tsx`

## Exact vs Empirical

- exact: none
- empirical: current predictive benchmark result
- structural borrowing: state-space design and terminology
