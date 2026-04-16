# Schwarzschild-de Sitter (SdS) Research Repository

[![Release](https://img.shields.io/github/v/release/RRG314/sds-research?display_name=tag)](https://github.com/RRG314/sds-research/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Workbench](https://img.shields.io/badge/Workbench-Live-0f8f82)](https://rrg314.github.io/sds-research/workbench/)
[![Evidence Policy](https://img.shields.io/badge/Evidence-Exact%20%7C%20Empirical%20%7C%20Retracted-1f6feb)](./docs/overview/status.md)

This repository presents a structured research program on Schwarzschild-de Sitter thermodynamics, spectral/QNM analysis, correction-gap formalization, recursive extensions, and an interactive workbench.

The editorial standard is explicit claim discipline: exact results, empirical results, approximation-based results, negative findings, and open questions are separated and labeled.

It also includes an SDS-inspired practical tools layer. Those tools reuse structural ideas from the SdS program, but they are documented separately from the exact theory and promoted only when they survive direct baseline comparison.

## Current Release

- Release notes: `docs/releases/v1.1.0.md`
- Changelog: `CHANGELOG.md`
- Live workbench: [https://rrg314.github.io/sds-research/workbench/](https://rrg314.github.io/sds-research/workbench/)

## Interactive Workbench

- Repository landing page: [https://rrg314.github.io/sds-research/](https://rrg314.github.io/sds-research/)
- Direct workbench: [https://rrg314.github.io/sds-research/workbench/](https://rrg314.github.io/sds-research/workbench/)

## SDS-Inspired Practical Tools

Supported tools:

- `Dual-Reservoir Controller`: optimizer control for tuning-sensitive regimes
- `Deficit-Driven Scheduler`: drop-in scheduler driven by an SDS-style useful-imbalance signal

Experimental but kept:

- `State-Space Monitor`
- `Equilibrium Early Stopping`
- `One-Parameter Control Family`

Start here:

- `docs/overview/sds-to-tools-map.md`
- `docs/benchmarks/sds-tools-benchmark-summary.md`
- `SDS_TOOLS_FINAL_REPORT.md`

## Evidence Classes

- `exact`: derivation-level statements within stated assumptions
- `empirical`: numerical or computational outcomes
- `approximation-based`: method-dependent results
- `disproven` / `retracted`: claims no longer supported after audit
- `open`: unresolved questions

## Reading Lanes

- Orientation: `docs/overview/start-here.md`
- Status by evidence type: `docs/overview/status.md`
- Validation entrypoint: `docs/overview/validation-entrypoint.md`
- Formula summary: `docs/theory/core-formula-sheet.md`
- Exact phase-family structure: `docs/theory/phase-curve-structure.md`
- Dimensional closure classification: `docs/theory/dimensional-closure-classification.md`
- Paper navigation: `papers/README.md`
- Foundational lane: `papers/foundational/README.md`
- Experimental lane: `papers/experimental/README.md`
- Disproven/retracted lane: `papers/disproven-or-retracted/README.md`
- Open-questions lane: `papers/open-questions/README.md`

## Main Research Areas

1. Core SdS theory
- horizon identities and entropy structure
- Eisenstein-coordinate formulation
- exact temperature-ratio and Carnot relations in model scope

2. Spectral / QNM program
- formal framework and statement pipeline
- numerical scans and reproducible artifacts
- explicit retention of negative and retracted outcomes

3. Correction-gap / cross-domain program
- theorem-schema construction
- scope limits and no-go framing

4. Recursive spacetime and extensions
- recursive-horizon baselines
- RNdS and extension diagnostics
- robustness and scalar-field audits

5. SdS workbench application
- state-space exploration
- saved states, comparisons, exports
- evolution trajectories under simplified semiclassical parameter flow

6. SDS-inspired practical tools
- benchmarked controllers, schedulers, diagnostics, and stopping rules
- honest promotion/demotion based on baseline comparison
- workbench Tools tab for visual inspection and export

## Repository Map

- `docs/overview/`: orientation, status, timeline, glossary, file index
- `docs/theory/`: foundational summaries and formula sheets
- `docs/research-program/`: branch audit, open problems, novelty assessment
- `docs/spectral/`: spectral framework, derivations, audits, status files
- `docs/correction-gap/`: correction-gap formalization and limits
- `docs/recursive-spacetime/`: recursive and extension analyses
- `docs/releases/`: release notes
- `docs/tools/`: plain-English tool docs with supported vs experimental labeling
- `docs/benchmarks/`: benchmark summaries and promotion decisions
- `papers/`: lane-based navigation and manuscript locations
- `app/sds-workbench/`: React + TypeScript workbench source
- `workbench/`: static build served from GitHub Pages
- `src/`: Python modules used by experiment suites
- `experiments/`: experiment scripts by program area
- `data/generated/`: generated numerical outputs
- `tests/`: app and math tests
- `archive/`: historical variants and deprecated artifacts

## Current Research Program Reports

- `STATUS.md`
- `SYSTEM_REPORT.md`
- `FINAL_REPORT.md`
- `docs/research-program/branch-audit.md`
- `docs/research-program/open-problem-program.md`
- `docs/research-program/novelty-assessment.md`

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

SDS-inspired tool suite:

```bash
./scripts/validate/run_sds_tools_suite.sh
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
