# Changelog

## 2026-04-10

### Added
- Full SDS-focused repository scaffold with professional research layout.
- Provenance artifacts:
  - `scripts/migrate/sds_migration_map.source.csv`
  - `scripts/migrate/migration-manifest.csv`
  - `scripts/migrate/migration-conflicts.json`
- Consolidated imports from local SDS corpus (theory, spectral, correction-gap, recursive projects, app code).
- New `Evolution` mode in `app/sds-workbench`:
  - initial-state selection (current/saved)
  - time slider
  - play/pause/reset
  - step forward/back
  - speed control
  - trajectory export (CSV/JSON)
- New evolution engine and tests:
  - `src/engine/evolution.ts`
  - physics and evolution unit tests via Vitest
- Python compatibility layer for reorganized modules under `src/`.

### Changed
- Normalized recursive-spacetime documentation naming to preserve both baseline and extended-system variants.
- Updated Vite configuration for GitHub Pages base-path compatibility.
- Added app test scripts and Vitest setup.

### Validation
- App tests: 5 passed
- App build: successful
- Python migrated math tests: 61 passed (selected suite)
