# Core SdS Formula Sheet

This document collects the principal formulas used by the foundational theory layer.

## Variables

- `r_b`: black-hole horizon radius
- `r_c`: cosmological horizon radius
- `x = r_b / r_c`
- `S_b, S_c`: horizon entropies
- $S_{\Lambda} = 3\pi/\Lambda$: pure de Sitter entropy at fixed $\Lambda$
- $\Delta$: entropy deficit

## Foundational Identities (4D SdS)

Horizon relation:

$$
r_b^2 + r_b r_c + r_c^2 = \frac{3}{\Lambda}
$$

Entropy identity:

$$
S_{\Lambda} = S_b + S_c + \sqrt{S_b S_c}
$$

Deficit definition:

$$
\Delta = S_{\Lambda} - S_b - S_c = \sqrt{S_b S_c}
$$

Entropy definitions:

$$
S_b = \pi r_b^2, \qquad S_c = \pi r_c^2
$$

## Temperature and Carnot Structure

Hawking temperatures:

$$
T_b = \frac{1-\Lambda r_b^2}{4\pi r_b}, \qquad
T_c = \frac{\Lambda r_c^2-1}{4\pi r_c}
$$

Exact temperature ratio:

$$
\frac{T_c}{T_b} = \frac{x(x+2)}{1+2x}
$$

Carnot efficiency:

$$
\eta_C = 1 - \frac{T_c}{T_b}
$$

Exact deficit derivative relation:

$$
\left.\frac{\partial \Delta}{\partial S_c}\right|_{\Lambda} = -\eta_C
$$

## Interpretation Notes

- These formulas are classified as `exact` within the stated SdS model assumptions.
- Spectral/QNM outputs use additional approximation and empirical layers.
- Evolution mode in the app is a simplified semiclassical parameter model.

## Canonical Sources

- `papers/sds-theory/sds-entropy-paper.md`
- `papers/sds-theory/eisenstein-carnot-paper.md`
- `docs/theory/core-sds-results.md`
