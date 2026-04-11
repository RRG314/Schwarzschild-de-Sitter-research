# Schwarzschild-de Sitter (SdS) Research Repository

This repository consolidates active and historical research materials on 4D Schwarzschild-de Sitter thermodynamics, spectral/QNM analysis, correction-gap formalization, recursive spacetime extensions, and an interactive SdS workbench application.

The goal is clear technical provenance: preserve exact results, empirical findings, negative outcomes, and exploratory artifacts without overstating claims.

## Research Threads

1. Core SdS theory
- Exact horizon/entropy structure in 4D SdS
- Eisenstein coordinate formulation
- Exact temperature ratio and Carnot-efficiency formulas
- Dimensional closure classification work (D=4, D=5, D>=6)

2. Spectral/QNM program
- Framework and derivation pipeline
- WKB experiments and audits
- Confirmed scaling results
- Retracted/artifact findings documented explicitly
- Open path toward exact (Leaver-type) methods

3. Correction-gap and cross-domain work
- Formal theorem-schema development
- No-go result for universal scalar gap
- Category-specific obstruction theorems/propositions

4. Recursive spacetime extensions
- Recursive-horizon baseline project
- Extended (M, Lambda) and (M, Q, Lambda) system studies
- RNdS and scalar-field audits

5. SdS Workbench app
- Interactive state-space exploration and validation
- Saved states, compare, exports, share URLs
- Evolution mode with simplified semiclassical parameter flow

## Evidence Labels

Every major area is classified with these labels:

- `exact`: closed-form/algebraic results with derivations
- `empirical`: numerical/experimental results
- `approximation-based`: controlled approximations (for example WKB)
- `exploratory`: ideas under development
- `artifact` / `retracted`: known failures or superseded claims
- `open`: unresolved questions and planned work

See [status](docs/overview/status.md) for the current project-wide map.

## Quick Start

### 1. Browse research documentation
- Start with [research map](docs/overview/research-map.md)
- Then review [status](docs/overview/status.md)

### 2. Run the SdS Workbench locally
```bash
cd app/sds-workbench
npm install
npm run dev
```

### 3. Run app tests
```bash
cd app/sds-workbench
npm run test
npm run build
```

### 4. Run migrated Python math tests (optional)
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

## GitHub Pages

The workbench is deployable as a static Vite build from `app/sds-workbench`.

- Deployment workflow: `.github/workflows/deploy-pages.yml`
- Base path is auto-resolved for Pages via `BASE_PATH`/GitHub environment in `vite.config.ts`

## Repository Map

- `docs/overview/`: orientation, status, timeline, file index
- `docs/theory/`: core theory landing and supporting structure notes
- `docs/spectral/`: spectral/QNM framework, derivations, results, audits
- `docs/correction-gap/`: formalization and cross-domain analysis
- `docs/recursive-spacetime/`: recursive-horizon and extended-system assessments
- `papers/`: paper drafts, stronger canonical manuscripts, preprint-ready assets
- `app/sds-workbench/`: React + TypeScript interactive lab
- `src/`: Python source modules (spectral, recursive horizon, recursive spacetime)
- `experiments/`: Python experiment scripts grouped by program
- `data/generated/`: generated experiment outputs
- `tests/`: migrated math tests and app tests
- `archive/`: superseded drafts, deprecated app variants, raw imports
- `scripts/migrate/`: migration provenance and conflict records

## Provenance

Migration provenance is preserved in:
- `scripts/migrate/sds_migration_map.source.csv`
- `scripts/migrate/migration-manifest.csv`
- `scripts/migrate/migration-conflicts.json`

## Current Status

- Core 4D SdS thermodynamic identities: strong and exact
- Spectral/QNM program: mixed (solid derivations + empirical negative findings + open exact-method stage)
- Correction-gap program: theorem schema and no-go framing, not a single universal theorem
- Recursive spacetime program: useful diagnostics and falsification output; multiple exploratory branches remain open
- Workbench app: operational and now includes an evolution layer with explicit model caveats
