# SDS System Report

## Main theory code
- `src/sds/core/exact.py`: exact structural budget helpers
- `src/sds/core/thermo.py`: exact phase-family quantities and phase-curve relation
- `src/sds/core/dimensional.py`: D=5 closure check, D>=6 nonclosure witnesses, and D>=6 small-`mu` asymptotic isolation helpers
- `src/sds_state.py`: direct 4D SdS state calculations and exact thermodynamic identities

## Main validation paths
- `tests/math/recursive_test_sds_identities.py`
- `tests/math/horizon_test_state_space.py`
- `tests/math/test_exact_phase_structure.py`
- `scripts/validate/run_sds_tools_suite.sh`
- `scripts/validate/check-doc-links.mjs`

## Current strongest documentation lanes
- `docs/theory/core-sds-results.md`
- `docs/theory/sds-entropy-structure.md`
- `docs/theory/phase-curve-structure.md`
- `docs/theory/dimensional-closure-classification.md`
- `docs/theory/dimensional-isolation-asymptotics.md`
- `docs/research-program/branch-audit.md`
- `docs/research-program/open-problem-program.md`
- `docs/research-program/novelty-assessment.md`
