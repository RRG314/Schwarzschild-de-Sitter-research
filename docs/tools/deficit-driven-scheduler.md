# Deficit-Driven Scheduler

## What It Is

A drop-in scheduler that uses an SDS-inspired useful-imbalance signal instead of a pure epoch counter.

## Practical Problem

Standard schedulers often decay learning rate by time alone or by a narrow plateau rule. This scheduler tries to use a richer signal that combines progress with stability.

## SDS Borrowing

Borrowed structure:
- deficit as shared untapped budget
- useful imbalance as a bounded productivity signal
- near-equilibrium decline as a cue that the system is losing useful separation

## Benchmark Result

Compared against:
- constant learning rate
- cosine decay
- step decay
- ReduceLROnPlateau

Mean best validation loss on noisy-moons benchmark:
- constant: `0.0844`
- plateau: `0.0856`
- deficit-driven: `0.0881`
- cosine: `0.0916`
- step: `0.0950`

Interpretation:
- it was not the absolute winner on this task
- it was close enough to plateau scheduling to remain practical
- it stayed inside the promotion tolerance and is easier to read in the SDS signal language

Status:
- recommended

## When To Use This

Use it when:
- you want a scheduler driven by coupled progress/stability information
- you want a drop-in scheduler with a more interpretable control story
- plateau behavior matters, but you want something less ad hoc than a single patience rule

## When Not To Use This

Do not use it when:
- cosine or plateau scheduling is already clearly good enough
- you are optimizing for absolute simplicity over signal readability

## Key Files

- `src/sds/tools/scheduler/deficit_scheduler.py`
- `src/sds/benchmarks/baselines.py`
- `src/sds/benchmarks/suite.py`
- `experiments/scheduler/run_deficit_scheduler_benchmarks.py`

## Reproduce

```bash
./.venv/bin/python experiments/scheduler/run_deficit_scheduler_benchmarks.py
```

## Exact vs Empirical

- exact: none
- empirical: benchmark ranking and promotion decision
- structural borrowing: scheduler signal construction
