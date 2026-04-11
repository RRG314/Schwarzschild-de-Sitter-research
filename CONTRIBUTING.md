# Contributing

## Scope

This repository mixes exact theory, numerical experiments, exploratory notes, and historical artifacts. Contributions should preserve that distinction and avoid inflating confidence levels.

## Required labeling

When adding or revising content, mark it clearly as one of:

- `exact`
- `empirical`
- `approximation-based`
- `exploratory`
- `artifact` / `retracted`
- `open`

If a document changes status (for example from exploratory to retracted), update `docs/overview/status.md`.

## Research integrity rules

- Do not present exploratory claims as proved.
- Keep negative results and retractions visible.
- Preserve provenance for migrated and superseded files.
- Prefer adding canonical updates while archiving superseded variants in `archive/`.

## Code contribution rules

- Keep app changes modular and tested.
- Reuse exact core formulas from the existing engine instead of duplicating equations.
- Add/update tests when changing physics/evolution logic.

## Local checks

### App
```bash
cd app/sds-workbench
npm install
npm run test
npm run build
```

### Python tests (selected)
```bash
source .venv/bin/activate
pytest tests/math/horizon_test_state_space.py \
       tests/math/recursive_test_horizon_reconstruction.py \
       tests/math/recursive_test_physical_admissibility.py \
       tests/math/recursive_test_recursive_flows.py \
       tests/math/recursive_test_scalar_field_usefulness.py \
       tests/math/recursive_test_sds_identities.py -q
```

## Pull requests

PR descriptions should include:

1. What changed
2. Status classification impact (`exact`, `empirical`, etc.)
3. Validation run (tests/build)
4. Any migrated/archived files and rationale
