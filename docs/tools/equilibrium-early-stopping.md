# Equilibrium Early Stopping

## What It Is

An early-stopping utility based on the collapse of useful imbalance rather than only on patience or tiny loss changes.

Supported modes:
- threshold
- relative-to-peak
- smoothed

## Practical Problem

Standard early stopping often says only that improvement has slowed. This tool tries to say something more structural: the process has lost the productive separation that justified continuing.

## Benchmark Result

Compared against:
- fixed epochs
- patience-based stopping
- loss-change threshold

Current result on the benchmark task:
- equilibrium modes ended up matching the fixed-epoch run too closely
- compute savings were not strong enough to justify promotion

Mean epochs:
- fixed epochs: `60.0`
- equilibrium relative peak: `60.0`

Status:
- experimental

## When To Use This

Use it when:
- you want a clear, explainable stopping story for a run
- you are experimenting with alternative stopping criteria

## When Not To Use This

Do not use it as the default stopper yet if your main goal is reducing compute.

## Key Files

- `src/sds/tools/early_stopping/equilibrium.py`
- `experiments/early_stopping/run_equilibrium_stopping_benchmarks.py`
- `tests/tools/test_early_stopping.py`

## Exact vs Empirical

- exact: none
- empirical: benchmark result and current demotion to experimental
- structural borrowing: endpoint / equilibrium logic
