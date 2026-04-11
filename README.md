# Schwarzschild-de Sitter (SdS) Research Repository

This repository is a structured research record for Schwarzschild-de Sitter thermodynamics.

## Start The Tool (Fastest Path)

- GitHub Pages landing page: [https://rrg314.github.io/sds-research/](https://rrg314.github.io/sds-research/)
- Direct workbench link: [https://rrg314.github.io/sds-research/workbench/](https://rrg314.github.io/sds-research/workbench/)

If you want the interactive app, use the direct workbench link above.

It is designed to be readable by both technical readers and newcomers by clearly separating:

- exact/proved results
- numerical/empirical results
- approximation-based work
- exploratory ideas
- artifacts/retracted paths
- open questions

## Start Here (New Readers)

1. [Project landing page](./index.html)
2. [Start Here guide](./docs/overview/start-here.md)
3. [Project status](./docs/overview/status.md)
4. [Research map](./docs/overview/research-map.md)
5. [Glossary](./docs/overview/glossary.md)

## Main Research Areas

1. Core SdS theory
- Entropy structure and horizon identities
- Eisenstein-style formulation
- Exact temperature and Carnot-efficiency relations

2. Spectral / QNM program
- Framework and derivation pipeline
- Numerical scans and audits
- Explicit negative/retracted outcomes where applicable

3. Correction-gap / cross-domain
- Theorem-schema development
- Scope limits and no-go framing

4. Recursive spacetime and extensions
- Recursive-horizon baselines
- RNdS extension experiments
- Robustness and scalar-field audits

5. Interactive SdS Workbench app
- State-space exploration
- Saved states / compare / export / share
- Evolution mode (simplified semiclassical parameter evolution)

## Evidence Labels

- `exact`: algebraic/closed-form derivation in stated assumptions
- `empirical`: numerical result
- `approximation-based`: result depends on approximation method
- `exploratory`: hypothesis or partial path
- `artifact` / `retracted`: known failure or superseded claim
- `open`: unresolved question

## Run The Workbench Locally

```bash
cd app/sds-workbench
npm install
npm run dev
```

## Validate Locally

App tests/build:

```bash
cd app/sds-workbench
npm run test
npm run build
```

Selected Python math tests:

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

## Simple GitHub Pages Deployment (Root, No Workflow)

This repo now supports a simple branch deployment from root.

1. Build and publish the app into `/workbench`:

```bash
./scripts/build/publish-pages-root.sh
```

2. Commit and push the updated `workbench/` files.
3. In GitHub repo settings:
- `Settings` -> `Pages`
- `Source`: `Deploy from a branch`
- `Branch`: `main`
- `Folder`: `/(root)`

Result:
- Root site serves `index.html`
- Workbench app serves from `/workbench/`

## Repository Map

- `docs/overview/`: orientation, status, timeline, index, beginner guides
- `docs/theory/`: theory summaries and core structure
- `docs/spectral/`: spectral/QNM framework, derivations, audits
- `docs/correction-gap/`: correction-gap formalization materials
- `docs/recursive-spacetime/`: recursive system analyses
- `papers/`: draft and preprint-oriented manuscript materials
- `app/sds-workbench/`: source app (React + TypeScript)
- `workbench/`: static build output for root GitHub Pages hosting
- `src/`: Python modules used in experiments
- `experiments/`: experiment scripts and program-specific runs
- `data/generated/`: generated result files
- `tests/`: app and math tests
- `archive/`: preserved superseded/deprecated/raw history
- `scripts/migrate/`: migration provenance data

## Provenance

- `scripts/migrate/sds_migration_map.source.csv`
- `scripts/migrate/migration-manifest.csv`
- `scripts/migrate/migration-conflicts.json`

## Integrity Policy

This repository avoids inflated claims.

- Exploratory work is not presented as proved.
- Retracted or artifact paths are retained and labeled.
- Historical variants are archived rather than hidden.
