# Changelog

All notable changes to this repository are documented here.

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
