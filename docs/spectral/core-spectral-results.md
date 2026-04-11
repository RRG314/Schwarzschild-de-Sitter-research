# Core Spectral Results

This document summarizes the current status of the spectral/QNM program.

## Scope

- scalar QNM analysis in SdS settings,
- derivation-level structural statements,
- WKB-based numerical program and audit outcomes.

## Exact / Derivation-Level Elements

- $\Lambda$-scaling structure in the current derivation pipeline.
- Thermodynamic identities integrated as structural context for spectral comparisons.

## Empirical Program

- WKB experiments (`exp01`-`exp05`) with retained outputs and figures.
- Reproducible data artifacts in `data/generated/spectral/`.

## Disproven or Retracted Findings

- No robust $x \to 1-x$ spectral symmetry in current audited results.
- No stable Eisenstein-structure signature in audited spectral outputs.
- Prior Q-Carnot correspondence claim was retracted as a computational artifact.

These outcomes remain visible as part of the canonical research record.

## Open Questions

- Exact-method (non-WKB) QNM behavior.
- Whether any thermodynamic correspondence survives exact treatment.
- Utility limits of mode-ratio inversion constructions.

## Canonical Files

- `docs/spectral/04b_exact_derivations.md`
- `docs/spectral/04c_negative_results_formalized.md`
- `docs/spectral/06a_proof_status_map.md`
- `docs/spectral/06b_research_synthesis_revised.md`
- `experiments/spectral/run_all.py`

## Classification

- Evidence class: mixed `exact` + `approximation-based` + `empirical` + `disproven`
- Maturity: audited numerical program with open exact-method phase
