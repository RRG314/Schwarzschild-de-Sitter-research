# One-Parameter Control Family

## What It Is

A compact control surface where one master variable `x` drives several practical knobs together:
- learning-rate scale
- momentum / `beta1`
- weight-decay scale
- noise scale

Presets:
- conservative
- balanced
- aggressive

## Practical Problem

This tool is for users who want fewer knobs and a cleaner control story.

## SDS Borrowing

This is the closest direct borrowing from the SdS one-parameter state idea:
- one governing parameter
- coupled derived quantities
- bounded fractions for hot, cold, and deficit components

## Benchmark Result

Task:
- stiff regression benchmark

Best preset:
- aggressive preset mean best validation loss `0.00496`

Best manual grid point:
- `grid_lr0.05_b0.92_wd0.0005`
- best validation loss `0.00269`

Interpretation:
- the family is usable and readable
- it reduces tuning burden
- it is not yet close enough to the best manual multi-knob baseline to be promoted

Status:
- experimental

## When To Use This

Use it when:
- you want a small, understandable control surface
- you are exploring or teaching the design space
- you want quick conservative / balanced / aggressive presets

## When Not To Use This

Do not use it when:
- absolute benchmark performance matters more than tuning simplicity
- you are willing to run a richer manual search

## Key Files

- `src/sds/tools/control_family/one_parameter.py`
- `experiments/control_family/run_one_parameter_family_benchmarks.py`
- `app/sds-workbench/src/components/tabs/ToolsTab.tsx`

## Exact vs Empirical

- exact: the borrowed budget fractions are constructed exactly in the tool layer
- empirical: benchmark quality relative to the manual grid
- structural borrowing: the meaning of the single control parameter
