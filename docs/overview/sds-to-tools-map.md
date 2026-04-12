# SdS-to-Tools Map

This page explains how the practical tool layer borrows structure from the Schwarzschild-de Sitter program without pretending to turn the physics into a literal optimizer law.

## Boundary Line

Exact SdS theory stays in the theory papers, theory docs, and exact workbench tabs.

The tool suite lives on the applied side of the repository and uses SdS ideas only as structural design patterns.

## Exact Ideas Reused Structurally

| SdS-side idea | Exact status in the research program | Tool translation |
| --- | --- | --- |
| Two coupled horizons / reservoirs | exact inside the stated SdS model | two coupled observables: update pressure and stability reserve |
| Fixed total entropy budget | exact model identity | bounded joint budget used to prevent runaway control signals |
| Deficit term `Delta` | exact in the model | untapped coupled budget represented by a geometric-mean-style deficit |
| One-parameter reduction by `x` | exact parametrization in the model | one master control variable that drives several knobs together |
| Temperature imbalance / Carnot efficiency | exact within model scope | bounded efficiency-like score for deciding whether imbalance is still useful |
| Natural endpoint behavior | exact thermodynamic structure in the model | early-stopping and stall detection based on loss of productive imbalance |

## What Is Literal vs Borrowed

Literal SdS theory:
- `app/sds-workbench/src/engine/physics.ts`
- `src/evolution/sds_state.py`
- `docs/theory/core-sds-results.md`
- `papers/sds-theory/`

Structural borrowing for tools:
- `src/sds/core/exact.py`
- `src/sds/tools/`
- `src/sds/benchmarks/`
- `docs/tools/`
- `docs/benchmarks/sds-tools-benchmark-summary.md`

## Supported Tools

### Dual-Reservoir Controller

Borrowing:
- hot reservoir = local update pressure
- cold reservoir = stability reserve
- deficit = untapped joint control budget
- efficiency = whether the imbalance is still productive

Status:
- recommended

Why:
- in the aggressive learning-rate band, it improved mean best validation loss from `0.0784` to `0.0728`
- final validation loss improved much more strongly, from `0.1749` to `0.1105`

Docs:
- `docs/tools/dual-reservoir-controller.md`

### Deficit-Driven Scheduler

Borrowing:
- scheduling signal comes from useful imbalance rather than epoch count alone

Status:
- recommended

Why:
- competitive with plateau scheduling while being easier to interpret in the SdS-inspired state language
- mean best validation loss `0.0881` versus `0.0856` for plateau, which stayed inside the promotion tolerance used in the benchmark suite

Docs:
- `docs/tools/deficit-driven-scheduler.md`

## Experimental Tools

### State-Space Monitor

Useful for interpretation, but not promoted as a predictor.

Current benchmark:
- monitor rho `0.128`
- raw loss-slope rho `0.419`

Docs:
- `docs/tools/state-space-monitor.md`

### Equilibrium Early Stopping

Clear idea, but not enough compute savings yet.

Current benchmark:
- equilibrium stopping did not materially beat the fixed-epoch baseline on the chosen task

Docs:
- `docs/tools/equilibrium-early-stopping.md`

### One-Parameter Control Family

Readable and compact, but not strong enough yet to replace a three-knob search.

Current benchmark:
- best preset `0.00496`
- best grid point `0.00269`

Docs:
- `docs/tools/one-parameter-control-family.md`

## How To Read The Tool Layer

1. Start with `docs/benchmarks/sds-tools-benchmark-summary.md`.
2. Use the dual-reservoir controller or deficit-driven scheduler first if you want the strongest practical outcomes.
3. Treat the monitor, equilibrium stopping, and one-parameter family as well-documented experiments rather than defaults.
4. Use the workbench Tools tab for a visual summary of what survived and why.

## Plain-English Rule

If a tool only looked elegant in SdS language but did not hold up against a simpler baseline, it was not promoted.
