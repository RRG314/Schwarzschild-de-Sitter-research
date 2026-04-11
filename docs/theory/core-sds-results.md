# Core SdS Results

This document summarizes foundational SdS identities used across theory, documentation, and tooling.

## Scope

- 4D Schwarzschild-de Sitter thermodynamics at fixed cosmological constant $\Lambda$
- algebraic horizon identities and derived thermodynamic relations
- dimensional context for closure behavior beyond 4D

## Foundational Identities (Exact Within Model)

Horizon relation:

$$
r_b^2 + r_b r_c + r_c^2 = \frac{3}{\Lambda}
$$

Entropy relation:

$$
S_{\Lambda} = S_b + S_c + \sqrt{S_b S_c}
$$

Deficit definition:

$$
\Delta = S_{\Lambda} - S_b - S_c = \sqrt{S_b S_c}
$$

Temperature formulas:

$$
T_b = \frac{1-\Lambda r_b^2}{4\pi r_b}, \qquad
T_c = \frac{\Lambda r_c^2-1}{4\pi r_c}
$$

Exact temperature ratio using $x = r_b/r_c$:

$$
\frac{T_c}{T_b} = \frac{x(x+2)}{1+2x}
$$

Carnot-efficiency relation:

$$
\eta_C = 1 - \frac{T_c}{T_b}, \qquad
\left.\frac{\partial \Delta}{\partial S_c}\right|_{\Lambda} = -\eta_C
$$

## Dimensional Context

- 4D and 5D admit low-dimensional closure structures of different algebraic type.
- For $D \ge 6$, the same polynomial closure structure is not preserved.

## Validation Status

- Symbolic and numerical checks in the imported test suites support these identities in sampled regimes.
- These are model-level exact statements, not observational claims.

## Canonical Source Files

- `papers/sds-theory/sds-entropy-paper.md`
- `papers/sds-theory/eisenstein-carnot-paper.md`
- `docs/theory/sds-entropy-structure.md`
- `papers/submitted-or-preprint-ready/eisenstein-coordinate-reformulation-sds-thermodynamics.pdf`

## Classification

- Evidence class: `exact`
- Maturity: manuscript-level derivation set with computational consistency checks
