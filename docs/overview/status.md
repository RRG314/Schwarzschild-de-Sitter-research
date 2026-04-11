# Project Status

## Proved / Exact

- 4D SdS Eisenstein-style horizon constraint and entropy identity (core theory manuscripts).
- Exact SdS parametrization formulas (x-based horizon and entropy fractions).
- Exact temperature ratio and Carnot-efficiency expressions in the theory layer.
- Algebraic/dimensional closure classification claims explicitly argued for D=4 and D=5 vs D>=6.

Primary files:
- `papers/sds-theory/sds-entropy-paper.md`
- `papers/sds-theory/eisenstein-carnot-paper.md`
- `docs/theory/sds-entropy-structure.md`

## Empirical / Numerical

- Spectral/QNM WKB experiment outputs with figures and JSON result sets.
- Recursive-horizon and recursive-spacetime experiment suites.
- RNdS extension scans, robustness checks, and orbit data exports.

Primary files:
- `docs/spectral/05_results_and_analysis.md`
- `data/generated/spectral/*.json`
- `docs/recursive-spacetime/recursive-horizon-project-results.md`
- `docs/recursive-spacetime/recursive-spacetime-system-results.md`

## Approximation-Based

- WKB-based spectral inference and associated uncertainty notes.
- Correction-gap theorem-schema formalization where abstraction choices matter.
- Simplified semiclassical evolution model in app mode (`dM/dt = ±k/M^2`).

Primary files:
- `docs/spectral/04b_exact_derivations.md` (contains both exact and approximation context)
- `docs/correction-gap/correction_gap_formalization.md`
- `app/sds-workbench/src/engine/evolution.ts`

## Retracted / Artifact / Superseded

- Q-Carnot correspondence claim in spectral program is explicitly documented as a computational artifact.
- Legacy single-file app variants (`sds-explorer`) are retained in `archive/deprecated/`.
- Draft and conflict-variant docs preserved in archive for traceability.

Primary files:
- `docs/spectral/06b_research_synthesis_revised.md`
- `archive/deprecated/sds-explorer/`
- `archive/old-drafts/`

## Open Questions

- Exact (non-WKB) SdS QNM structure and whether any robust thermodynamic correspondence survives.
- Higher-dimensional recursive flow behavior under physically grounded updates.
- Which correction-gap statements can be elevated from schema/proposition to theorem with stable assumptions.

Primary files:
- `docs/spectral/06_next_steps.md`
- `docs/spectral/06a_proof_status_map.md`
- `ROADMAP.md`

## Immediate Next Steps

1. Implement exact-method spectral solver path (Leaver-style) and compare against WKB outputs.
2. Expand evolution-mode validation (edge-case integrator checks, trajectory consistency tests).
3. Continue canonicalization of archived variants into paper-ready documents with explicit status labels.
