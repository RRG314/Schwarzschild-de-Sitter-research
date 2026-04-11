# Final Report: SDS Research Repository Consolidation

Date: 2026-04-10 (America/New_York)
Repository root: `/Users/stevenreid/Documents/sds-research-repo`
Branch: `steven/sds-professional-repo`
Remote: `https://github.com/RRG314/rdt-research-program.git`

## 1. Final Repository Structure

Top-level layout:

```text
sds-research-repo/
  README.md
  LICENSE
  .gitignore
  CITATION.cff
  CONTRIBUTING.md
  ROADMAP.md
  CHANGELOG.md
  FINAL_REPORT.md

  docs/
    overview/
    theory/
    spectral/
    correction-gap/
    recursive-spacetime/
    app/
    figures/
    references/
    archive-notes/

  papers/
    sds-theory/
    spectral-horizon/
    correction-gap/
    drafts/
    submitted-or-preprint-ready/

  src/
    app/
    math/
    evolution/
    spectral/
    utils/

  app/
    sds-workbench/

  experiments/
    spectral/
    recursive_spacetime/
    rnds/
    archived/

  data/
    generated/
    reference/
    exports/

  notebooks/
    exploratory/
    validated/

  tests/
    math/
    app/
    spectral/

  archive/
    old-drafts/
    deprecated/
    raw-imports/

  scripts/
    migrate/
    validate/
    build/
    export/
```

## 2. Files Migrated

Migration provenance files:

- `scripts/migrate/sds_migration_map.source.csv`
- `scripts/migrate/migration-manifest.csv`
- `scripts/migrate/migration-conflicts.json`

Migration accounting from `migration-manifest.csv`:

- Total inventoried rows (excluding header): **186**
- Copied: **184**
- Conflict archived variants: **2**
- Active/non-archive destinations: **141**
- Archive destinations: **45**

Primary source corpora migrated from local SDS research folders, including Claude local session outputs and SDS PDFs/doc artifacts from Downloads.

## 3. Files Archived

Archived intentionally for provenance/history:

- `archive/deprecated/`:
  - legacy app/tool variants (including old `sds-explorer` style assets)
- `archive/old-drafts/`:
  - superseded drafts
  - conflict variants retained for traceability
- `archive/raw-imports/`:
  - minimally processed imported files requiring future curation

Conflict-variant examples preserved:

- `archive/old-drafts/conflict-variants/README__variant_5a8411f2fd.md`
- `archive/old-drafts/conflict-variants/RESULTS__variant_b4ef883a76.md`

## 4. Strongest Canonical Files Selected

Core SDS theory:

- `papers/sds-theory/sds-entropy-paper.md`
- `papers/sds-theory/eisenstein-carnot-paper.md`
- `docs/theory/core-sds-results.md`

Spectral/QNM:

- `docs/spectral/04b_exact_derivations.md`
- `docs/spectral/06a_proof_status_map.md`
- `docs/spectral/06b_research_synthesis_revised.md`
- `docs/spectral/core-spectral-results.md`

Correction gap:

- `docs/correction-gap/correction_gap_formalization.md`
- `docs/correction-gap/correction_gap_universality.md`
- `docs/correction-gap/core-results.md`

Recursive spacetime / extension:

- `docs/recursive-spacetime/BASELINE_ASSESSMENT.md`
- `docs/recursive-spacetime/recursive-horizon-project-results.md`
- `docs/recursive-spacetime/recursive-spacetime-system-results.md`

Workbench app:

- `app/sds-workbench/src/engine/physics.ts`
- `app/sds-workbench/src/engine/evolution.ts`
- `docs/app/app-overview.md`

## 5. App Changes Made

The app was migrated and upgraded at `app/sds-workbench`.

Major app updates:

- Added dedicated Evolution tab mode:
  - `app/sds-workbench/src/components/tabs/EvolutionTab.tsx`
- Added reusable evolution engine:
  - `app/sds-workbench/src/engine/evolution.ts`
- Added trajectory export helpers (CSV/JSON):
  - `app/sds-workbench/src/utils/export.ts`
- Added tests:
  - `app/sds-workbench/src/engine/__tests__/physics.test.ts`
  - `app/sds-workbench/src/engine/__tests__/evolution.test.ts`
- Updated TypeScript build hygiene (`noEmit`) and Vite Pages base handling.

Existing useful behavior was preserved (state-space workflow, saved states, compare/export/share flows).

## 6. Evolution / Dynamics Features Added

Implemented as a clearly-labeled simplified semiclassical model:

- Explicit model note in UI:
  - “Simplified semiclassical evolution model”
  - “Parameter evolution, not a full GR simulation”
- Dynamics law:
  - `dM/dt = ±k/M^2` (evaporation/reverse flow), integrated in stable cubic-step form
- Controls:
  - start from current or saved state
  - play/pause/reset
  - step forward/back
  - time slider
  - speed control
- Outputs per step:
  - `M(t), x(t), r_b(t), r_c(t), S_b(t), S_c(t), Delta(t), T_b(t), T_c(t), eta_C(t)`
- Export trajectory:
  - CSV and JSON download/copy

## 7. GitHub Pages Status

Deployment support is configured:

- Root branch deployment (no workflow required)
- Root landing page: `index.html`
- App publish path: `workbench/` (built via `scripts/build/publish-pages-root.sh`)
- App build base path set through `BASE_PATH=./` in the publish script

Current branch pushed: `main`.

## 8. Repository URL

- Repository: [RRG314/sds-research](https://github.com/RRG314/sds-research)
- Branch: [`main`](https://github.com/RRG314/sds-research/tree/main)

## 9. Remaining Manual Items to Check

1. In GitHub repo settings, enable Pages with `Deploy from a branch`.
2. Select branch `main`, folder `/(root)`.
3. Verify root page and `/workbench/` load correctly.
4. Optional: curate `archive/raw-imports/` and `papers/drafts/` into paper-ready canonical files.
5. Optional: expand CI to run selected Python tests in GitHub Actions.

## 10. Ambiguous Files and Resolution Decisions

Ambiguity types encountered:

- Same-named recursive docs with different content (`README.md`, `RESULTS.md`) from different source folders.
- Multiple app variants and legacy explorer code paths.
- Mixed maturity artifacts (exact, empirical, exploratory, failed-path notes) in shared source dumps.

How these were handled:

- Preferred stronger/current variants in active docs paths.
- Preserved alternate variants in `archive/old-drafts/conflict-variants/`.
- Preserved deprecated app variants under `archive/deprecated/`.
- Maintained provenance in migration manifest/conflicts files.
- Did not delete ambiguous historical work unless safely archived.

## Validation Snapshot

Local validation run (latest):

- App tests: `npm run test` -> **5 passed**
- App build: `npm run build` -> **success**
- Docs link check: `node scripts/validate/check-doc-links.mjs` -> **no broken local links**
- Python math tests:
  - `61 passed` across selected migrated suites
