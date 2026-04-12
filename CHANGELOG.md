# Changelog

All notable changes to this repository are documented here.

## [v1.1.0] - 2026-04-12

### Added

- SDS-inspired practical tool suite under `src/sds/` with controllers, scheduler, monitor, stopping, and control-family modules.
- Tool benchmark and experiment entry points under `experiments/optimizer`, `experiments/scheduler`, `experiments/diagnostics`, `experiments/early_stopping`, and `experiments/control_family`.
- Tools tab in the workbench with promotion decisions, state-space trace view, control curves, and exports.
- Tool benchmark outputs in `data/benchmark_outputs/tools/`.
- Tool docs and benchmark summary pages:
  - `docs/overview/sds-to-tools-map.md`
  - `docs/tools/`
  - `docs/benchmarks/sds-tools-benchmark-summary.md`
  - `SDS_TOOLS_FINAL_REPORT.md`

### Changed

- Separated exact SdS theory and SDS-inspired applied tools more explicitly in README, status, and orientation docs.
- Added a repo-level validation entry point for the tools suite.
- Updated the root-level GitHub Pages workbench to include the new Tools tab.

### Validation

- Python tool tests: 9 passed
- Workbench tests: 8 passed
- Markdown link validation: passed
- Workbench production build: successful

## [v1.0.0] - 2026-04-10

### Added

- Full SDS-focused repository structure with lane-based navigation (`foundational`, `experimental`, `disproven/retracted`, `open questions`).
- Canonical overview pages and orientation documents.
- Public GitHub Pages landing site with direct workbench entry.
- Interactive SdS workbench evolution mode with:
  - initial-state selection (current/saved)
  - time slider
  - play/pause/reset
  - step forward/backward
  - speed control
  - trajectory export (CSV/JSON)
- Formula-focused theory summaries and release documentation.
- Migration provenance records:
  - `scripts/migrate/sds_migration_map.source.csv`
  - `scripts/migrate/migration-manifest.csv`
  - `scripts/migrate/migration-conflicts.json`

### Changed

- Reorganized research materials into clear evidence classes and reader lanes.
- Standardized presentation language across top-level docs for professional research framing.
- Normalized notation in key entry docs (`\Lambda`, `\Delta`, equation formatting).
- Updated flagship manuscript front matter with reader summary and explicit claim scope.

### Validation

- App unit tests: 5 passed
- App production build: successful
- Selected migrated Python math suite: 61 passed
- Markdown link validation: passed
