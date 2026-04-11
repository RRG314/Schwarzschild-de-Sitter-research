# Migration Notes

This repository was consolidated from local SDS-related source trees and standalone documents.

## Key principles used

- Preserve strongest canonical versions in active docs/papers/app paths.
- Preserve superseded/conflicting variants in `archive/` with provenance.
- Keep raw-import and conflict records machine-traceable.

## Provenance files

- `scripts/migrate/sds_migration_map.source.csv`
- `scripts/migrate/migration-manifest.csv`
- `scripts/migrate/migration-conflicts.json`

## Notable conflict handling

- Recursive-spacetime README/RESULTS collisions were resolved by preserving both variants:
  - recursive-horizon baseline documents
  - recursive-spacetime-system documents
- Legacy single-file app variants (`sds-explorer`) retained under `archive/deprecated/`.
