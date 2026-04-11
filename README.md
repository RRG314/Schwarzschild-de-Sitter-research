# Schwarzschild-de Sitter (SdS) Research Repository

This repository presents a structured research program on Schwarzschild-de Sitter thermodynamics, spectral/QNM analysis, correction-gap formalization, recursive extensions, and an interactive workbench.

The editorial goal is strict claim discipline: exact results, empirical results, approximation-based results, negative findings, and open questions are explicitly separated.

## Interactive Workbench

- Repository landing page: [https://rrg314.github.io/sds-research/](https://rrg314.github.io/sds-research/)
- Direct workbench: [https://rrg314.github.io/sds-research/workbench/](https://rrg314.github.io/sds-research/workbench/)

## Evidence Classes

- `exact`: derivation-level statements within stated assumptions.
- `empirical`: numerical or computational outcomes.
- `approximation-based`: method-dependent results.
- `disproven` / `retracted`: claims no longer supported after audit.
- `open`: unresolved questions.

## Reading Lanes

- General orientation: `docs/overview/start-here.md`
- Project-wide status map: `docs/overview/status.md`
- Formula summary: `docs/theory/core-formula-sheet.md`
- Paper navigation: `papers/README.md`
- Foundational lane: `papers/foundational/README.md`
- Experimental lane: `papers/experimental/README.md`
- Disproven/retracted lane: `papers/disproven-or-retracted/README.md`
- Open-questions lane: `papers/open-questions/README.md`

## Main Research Areas

1. Core SdS theory
- Horizon identities and entropy structure
- Eisenstein-coordinate formulation
- Exact temperature-ratio and Carnot relations within model scope

2. Spectral / QNM program
- Formal framework and statement pipeline
- Numerical scans and reproducible artifacts
- Negative and retracted findings retained with explicit audit history

3. Correction-gap / cross-domain program
- Theorem-schema construction
- Scope limits and no-go framing

4. Recursive spacetime and extensions
- Recursive-horizon baselines
- RNdS and extension diagnostics
- Robustness and scalar-field audits

5. SdS workbench application
- State-space exploration
- Saved states, comparisons, exports
- Evolution trajectories under a simplified semiclassical parameter model

## Repository Map

- `docs/overview/`: orientation, status, timeline, glossary, file index
- `docs/theory/`: foundational summaries and formula sheets
- `docs/spectral/`: spectral framework, derivations, audits, status files
- `docs/correction-gap/`: correction-gap formalization and limits
- `docs/recursive-spacetime/`: recursive and extension analyses
- `papers/`: lane-based navigation and manuscript locations
- `app/sds-workbench/`: React + TypeScript source for the interactive tool
- `workbench/`: static build served from GitHub Pages
- `src/`: Python modules used by experiment suites
- `experiments/`: experiment scripts by program area
- `data/generated/`: generated numerical outputs
- `tests/`: app and math tests
- `archive/`: historical variants and deprecated artifacts

## Reproducibility (Local)

Workbench:

```bash
cd app/sds-workbench
npm install
npm run test
npm run build
```

Selected math test suites:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pytest numpy scipy
pytest tests/math/horizon_test_state_space.py \
       tests/math/recursive_test_horizon_reconstruction.py \
       tests/math/recursive_test_physical_admissibility.py \
       tests/math/recursive_test_recursive_flows.py \
       tests/math/recursive_test_scalar_field_usefulness.py \
       tests/math/recursive_test_sds_identities.py -q
```

## Provenance and Integrity

Migration provenance is recorded in:

- `scripts/migrate/sds_migration_map.source.csv`
- `scripts/migrate/migration-manifest.csv`
- `scripts/migrate/migration-conflicts.json`

Integrity policy:

- exploratory results are not presented as proofs,
- negative outcomes are retained,
- model scope is stated explicitly,
- historical variants are archived rather than deleted.
