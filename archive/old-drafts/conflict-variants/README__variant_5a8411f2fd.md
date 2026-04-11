# recursive_spacetime_system

Upgrade of `recursive_horizon_project` from a 1D Eisenstein arc toy model into a
genuine (M, Λ) / (M, Q, Λ) spacetime parameter-space system.

## What this is

Tests recursive maps and flows on the thermodynamic parameter spaces of
Schwarzschild-de Sitter (SdS) and Reissner-Nordström-de Sitter (RNdS) black holes.

All flows are labeled:
- `[PHYS]` — derived from exact thermodynamic identities (trustworthy physics)
- `[CONV]` — mathematically convenient but without physical derivation
- `[EXPL]` — exploratory/arbitrary; labeled so the reader knows

## Run instructions

```bash
pip install numpy scipy

# Run all tests first
python tests/test_sds_identities.py
python tests/test_horizon_reconstruction.py
python tests/test_recursive_flows.py
python tests/test_scalar_field_usefulness.py
python tests/test_physical_admissibility.py

# Run all experiments
python experiments/run_all.py

# Or individual experiments
python experiments/exp01_rebuild_sds_baseline.py
python experiments/exp02_recursive_parameter_flow.py
python experiments/exp03_rnds_extension.py
python experiments/exp04_scalar_field_integration.py
python experiments/exp05_full_robustness_scan.py
python experiments/exp06_compare_with_horizon_only_model.py
```

Results are written to `outputs/json/` and `outputs/csv/`.

## Project structure

```
src/
  sds_state.py          — SdS physical state (M, Lambda) → r_b, r_c, T, S, Delta
  rnds_state.py         — RNdS physical state (M, Q, Lambda) → quartic roots
  scalar_field_state.py — RDT scalar field implementation + honest audit
  recursion_flows.py    — All recursive flows, labeled [PHYS]/[CONV]/[EXPL]
  flow_constraints.py   — Admissibility checks, orbit observables
  stability.py          — Jacobians, Lyapunov exponents, fixed-point search
  spectral_checks.py    — Spectral dimension estimation from heat kernel
  utils.py              — JSON/CSV I/O, timing

experiments/
  exp01 — SdS baseline: verify all exact identities
  exp02 — SdS recursive flows in (M, Lambda) space
  exp03 — RNdS extension: 2D and 3D orbits
  exp04 — Scalar field integration audit
  exp05 — Full robustness scan across parameter space
  exp06 — Comparison with old horizon-only model

tests/
  test_sds_identities.py
  test_horizon_reconstruction.py
  test_recursive_flows.py
  test_scalar_field_usefulness.py
  test_physical_admissibility.py
```

## Key results

See `RESULTS.md` for the full honest verdict. Short version:

- SdS exact algebraic identities hold to machine precision (< 1e-12 residuals)
- RNdS extends to a genuine 3-parameter space with no closed-form entropy identity
- [PHYS] SdS gradient flow is physically motivated; converges to a single attractor
- Scalar field (RDT): NOT USEFUL — takes ≤2 distinct values over SdS arc at Λ=1
- Spectral dimension of all [PHYS] flows ≈ 1 (orbits stay on 1D arcs within fixed-Λ slices)
- Only [EXPL] 3D flows show d_s > 1, by construction (arbitrary rotation in parameter space)

## What the previous model proved

See `BASELINE_ASSESSMENT.md` for a full inventory. The key proven results are:
1. Entropy identity S_Λ = S_b + S_c + √(S_b·S_c) is algebraically exact
2. Eisenstein constraint r_b² + r_b·r_c + r_c² = 3/Λ is algebraically exact
3. Coupled Eisenstein maps create stable interior fixed points
4. All physical flows stay on 1D arcs; spectral dimension ≈ 1
