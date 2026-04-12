# Research Map

This map summarizes where each research thread lives, what it contains, and how mature it is.

Quick orientation for new readers:

- `docs/overview/start-here.md`
- `docs/overview/glossary.md`
- `docs/overview/status.md`

## 1. Core SdS Theory

- Primary locations:
  - `papers/sds-theory/`
  - `docs/theory/`
  - `papers/submitted-or-preprint-ready/`
- Main content:
  - exact horizon/Vieta identities
  - entropy identity and deficit structure
  - exact temperature ratio and Carnot formula work
  - dimensional closure classification
- Status:
  - mostly `exact` with derivation-first manuscripts
- Strongest canonical files:
  - `papers/sds-theory/sds-entropy-paper.md`
  - `papers/sds-theory/eisenstein-carnot-paper.md`
  - `papers/submitted-or-preprint-ready/eisenstein-coordinate-reformulation-sds-thermodynamics.pdf`
  - `docs/theory/core-sds-results.md`

## 2. Spectral / QNM Program

- Primary locations:
  - `docs/spectral/`
  - `src/spectral/`
  - `experiments/spectral/`
  - `data/generated/spectral/`
  - `docs/figures/spectral/`
- Main content:
  - mathematical framework and derivations
  - WKB experiment series and numerical outputs
  - audits, negative results, and retraction documentation
- Status:
  - mixed `exact` + `approximation-based` + `empirical`
- Strongest canonical files:
  - `docs/spectral/04b_exact_derivations.md`
  - `docs/spectral/06a_proof_status_map.md`
  - `docs/spectral/06b_research_synthesis_revised.md`
  - `docs/spectral/core-spectral-results.md`

## 3. Correction-Gap / Cross-Domain

- Primary locations:
  - `docs/correction-gap/`
  - `papers/correction-gap/` (reserved for future paper-ready consolidation)
- Main content:
  - correction-gap formalization and theorem-schema work
  - category-specific obstructions and no-go framing
  - cross-domain mappings (MHD, SdS, WKB, corner singularity)
- Status:
  - `approximation-based` formalization with explicit limits
- Strongest canonical files:
  - `docs/correction-gap/correction_gap_formalization.md`
  - `docs/correction-gap/correction_gap_universality.md`
  - `docs/correction-gap/core-results.md`

## 4. Recursive Spacetime / Extensions

- Primary locations:
  - `docs/recursive-spacetime/`
  - `src/evolution/`
  - `src/math/recursive_horizon/`
  - `experiments/recursive_spacetime/`
  - `experiments/rnds/`
  - `data/generated/recursive_spacetime/`
  - `data/generated/rnds/`
- Main content:
  - recursive-horizon baseline
  - upgraded (M, Lambda) system
  - RNdS extension tests
  - scalar field and robustness audits
- Status:
  - strong `empirical` program with explicit falsifications and open exploratory branches
- Strongest canonical files:
  - `docs/recursive-spacetime/BASELINE_ASSESSMENT.md`
  - `docs/recursive-spacetime/recursive-horizon-project-results.md`
  - `docs/recursive-spacetime/recursive-spacetime-system-results.md`

## 5. SdS Workbench App

- Primary locations:
  - `app/sds-workbench/`
  - `docs/app/`
- Main content:
  - interactive SdS state exploration and diagnostics
  - compare, saved states, exports, share links
  - evolution mode (simplified semiclassical parameter evolution)
- Status:
  - production-style interactive tool with validated build/tests
- Strongest canonical files:
  - `app/sds-workbench/src/engine/physics.ts`
  - `app/sds-workbench/src/engine/evolution.ts`
  - `docs/app/app-overview.md`

## 6. SDS-Inspired Practical Tools

- Primary locations:
  - `src/sds/`
  - `experiments/optimizer/`
  - `experiments/scheduler/`
  - `experiments/diagnostics/`
  - `experiments/early_stopping/`
  - `experiments/control_family/`
  - `docs/tools/`
  - `docs/benchmarks/`
- Main content:
  - dual-reservoir optimizer control
  - deficit-driven scheduling
  - state-space monitoring
  - equilibrium-style early stopping
  - one-parameter control families
- Status:
  - mixed `empirical` with explicit supported vs experimental separation
- Strongest canonical files:
  - `src/sds/benchmarks/suite.py`
  - `docs/overview/sds-to-tools-map.md`
  - `docs/benchmarks/sds-tools-benchmark-summary.md`
  - `SDS_TOOLS_FINAL_REPORT.md`

## 7. Archive and History

- Primary locations:
  - `archive/old-drafts/`
  - `archive/deprecated/`
  - `archive/raw-imports/`
- Main content:
  - superseded drafts
  - deprecated app variants
  - raw imports and migration conflict variants
- Status:
  - `artifact` / historical provenance only

## 8. Provenance and Migration Records

- `scripts/migrate/sds_migration_map.source.csv`
- `scripts/migrate/migration-manifest.csv`
- `scripts/migrate/migration-conflicts.json`

These provide source path, hash, status label, and destination for each migrated file.
