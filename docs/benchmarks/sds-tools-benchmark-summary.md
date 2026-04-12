# SDS-Inspired Tools Benchmark Summary

This page records the current benchmark outcomes for the practical SdS-inspired tool suite.

## Promotion Summary

Recommended:
- Dual-Reservoir Controller
- Deficit-Driven Scheduler

Experimental:
- State-Space Monitor
- Equilibrium Early Stopping
- One-Parameter Control Family

## Benchmark Scope

Current benchmark tasks:
- noisy-moons classification for controller, scheduler, monitor, and early stopping
- stiff regression for one-parameter control family

Current benchmark philosophy:
- promote only tools that survive a direct baseline comparison
- do not claim asymptotic or universal merit from a small benchmark grid
- keep useful but non-promoted tools visible as experiments

## Controller Result

All-rate mean best validation loss:

| Variant | Mean best validation loss | Mean final validation loss |
| --- | ---: | ---: |
| Adam baseline | 0.0804 | 0.1457 |
| Efficiency-only ablation | 0.0800 | 0.1414 |
| Full dual-reservoir controller | 0.0780 | 0.1048 |

Aggressive learning-rate band (`0.30-0.60`):

| Variant | Mean best validation loss | Mean final validation loss |
| --- | ---: | ---: |
| Adam baseline | 0.0784 | 0.1749 |
| Efficiency-only ablation | 0.0730 | 0.1633 |
| Full dual-reservoir controller | 0.0728 | 0.1105 |

Decision:
- recommended

Reason:
- this tool earns its keep in the brittle band, which is exactly where a control layer has to justify itself

## Scheduler Result

| Scheduler | Mean best validation loss |
| --- | ---: |
| Constant | 0.0844 |
| Plateau | 0.0856 |
| Deficit-driven | 0.0881 |
| Cosine | 0.0916 |
| Step | 0.0950 |

Decision:
- recommended

Reason:
- it stayed close to the best baseline family and remained more interpretable than a pure epoch-based schedule

## Monitor Result

Metric:
- Spearman correlation to 5-epoch future validation improvement

| Signal | Correlation |
| --- | ---: |
| SDS monitor useful imbalance | 0.1277 |
| Raw loss slope | 0.4189 |

Decision:
- experimental

Reason:
- the monitor helps interpretation, but it is not yet the stronger predictive signal

## Early Stopping Result

| Method | Mean epochs | Mean best validation loss |
| --- | ---: | ---: |
| Fixed epochs | 60.0 | 0.0823 |
| Patience | 48.7 | 0.0876 |
| Loss-change | 60.0 | 0.0823 |
| Equilibrium threshold | 60.0 | 0.0823 |
| Equilibrium relative peak | 60.0 | 0.0823 |
| Equilibrium smoothed | 60.0 | 0.0823 |

Decision:
- experimental

Reason:
- clear concept, but it did not yet save enough compute to become the default

## One-Parameter Family Result

| Variant | Mean best validation loss |
| --- | ---: |
| Conservative preset | 0.00617 |
| Balanced preset | 0.00551 |
| Aggressive preset | 0.00496 |
| Best manual grid point | 0.00269 |

Decision:
- experimental

Reason:
- it is easier to use, but not close enough yet to the best manual grid on the current benchmark

## What Survived The Honest Pass

What clearly survived:
- SDS-style coupled control for brittle optimization regimes
- SDS-style deficit scheduling as a practical drop-in alternative

What survived only as a documented experiment:
- state-space monitoring
- equilibrium-style early stopping
- one-parameter compressed control families

## Reproduce

```bash
./scripts/validate/run_sds_tools_suite.sh
```
