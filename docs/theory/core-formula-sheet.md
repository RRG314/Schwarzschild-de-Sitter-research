# Core SdS Formula Sheet

This sheet is the fastest way to see the key formulas used across the repository.

## Variables

- `r_b`: black-hole horizon radius
- `r_c`: cosmological horizon radius
- `x = r_b / r_c`
- `S_b, S_c`: horizon entropies
- `S_Λ = 3π/Λ`: pure de Sitter entropy at fixed `Λ`
- `Δ`: entropy deficit

## Foundational Identities (4D SdS)

Horizon relation:

$$
r_b^2 + r_b r_c + r_c^2 = \frac{3}{\Lambda}
$$

Entropy identity:

$$
S_\Lambda = S_b + S_c + \sqrt{S_b S_c}
$$

Deficit definition:

$$
\Delta = S_\Lambda - S_b - S_c = \sqrt{S_b S_c}
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

Exact temperature ratio in `x`:

$$
\frac{T_c}{T_b} = \frac{x(x+2)}{1+2x}
$$

Carnot efficiency:

$$
\eta_C = 1 - \frac{T_c}{T_b}
$$

Exact deficit derivative relation:

$$
\left.\frac{\partial \Delta}{\partial S_c}\right|_\Lambda = -\eta_C
$$

## Interpretation Notes

- The formulas above are treated as **foundational/exact** in this project.
- Spectral/QNM claims are a different track and include approximation-based and negative outcomes.
- Evolution mode in the app is parameter evolution, not a full GR simulation.

## Canonical Sources

- `papers/sds-theory/sds-entropy-paper.md`
- `papers/sds-theory/eisenstein-carnot-paper.md`
- `docs/theory/core-sds-results.md`
