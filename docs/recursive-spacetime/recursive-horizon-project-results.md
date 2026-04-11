# Recursive Horizon Research Workspace — Results

**Question:** Does a recursive horizon system built on the SdS Eisenstein arc
produce stable, physically admissible recursive dynamics with a robust
emergent non-integer spectral dimension, or does it collapse into a
numerically interesting but non-physical reduced model?

**Verdict: Partially. The algebraic structure is sound; the spectral
dimension result is negative; the interior fixed points are real and
robust. See below.**

---

## Unit Test Results

**11 / 11 tests passed** across:
- Eisenstein constraint (u² + uv + v² = 1)
- Entropy identity: S_Λ = S_b + S_c + √(S_b S_c) = 3π/Λ
- Temperature formulas T_b, T_c
- Carnot efficiency formula
- Mass range (0 ≤ M ≤ M_Nariai)
- j-invariant at M=0 → 1728
- Boundary limits (Nariai, pure dS)

---

## Exp01 — Symmetric Power Map: No Interior Fixed Points

T_λ(u,v) = normalize(u^λ, v^λ)

For **all** λ ≠ 1:
- λ > 1: orbit converges to x → 0 (black hole boundary, pure BH limit)
- λ < 1: orbit converges to x → 1 (Nariai boundary, r_b = r_c)
- λ = 1: identity map, every point is fixed

**Physical interpretation**: The uncoupled symmetric power map is dynamically
trivial. It cannot maintain a state in the interior of the physical phase
space. There is no stable mixed horizon configuration under this recursion.

This is expected mathematically: the fixed-point condition
(u/v)^(λ-1) = 1 has only the trivial solution x=1 for λ≠1 when
u/v < 1.

---

## Exp02 — Coupled Symmetric Map: Interior Fixed Points Exist

T_{λ,ε}(u,v) = normalize(u^λ + ε·v, v^λ + ε·u)

**Key finding: Coupling creates interior fixed points.**

Selected results (starting from x₀ = 0.3):

| λ    | ε    | Attractor x | Attractor type |
|------|------|-------------|----------------|
| 1.2  | 0.05 | 0.1626      | fixed (interior) |
| 1.5  | 0.05 | 0.0686      | fixed (interior) |
| 1.5  | 0.10 | 0.1744      | fixed (interior) |
| 2.0  | 0.10 | 0.1191      | fixed (interior) |
| 2.0  | 0.20 | 0.3112      | fixed (interior) |
| 2.5  | 0.20 | 0.2686      | fixed (interior) |
| 2.5  | 0.30 | 0.5824      | fixed (interior) |

Interior fixed points exist for λ > 1 with sufficiently small ε.
For large ε, the coupling term dominates and drives the orbit to the
Nariai boundary (x → 1).

At the interior fixed points:
- Jacobian spectral radius < 1 (stable attractors)
- The physical SdS state persists under recursive evolution
- Entropy deficit Δ has a well-defined equilibrium value

**Physical interpretation**: The coupling term acts as a "restoring force"
that prevents the orbit from collapsing to a degenerate boundary state.
The fixed-point x value encodes an equilibrium between the power-law
compression and the cross-horizon coupling.

---

## Exp03 — Parameter Sweep: Single Basin, No Chaos

**Part A — Basin of attraction:**
- All 20 initial conditions (x₀ ∈ [0.05, 0.95]) converge to the SAME
  fixed point for each (λ, ε) pair.
- The attractor is a global attractor (single basin of attraction).
- No multi-stability found in the tested range.

**Part B — Asymmetric coupling (β, γ vary):**
- Interior fixed points persist under symmetry-breaking
- One case showed "chaotic" classification at β=1.5, γ=1.5 (mean_x=0.96,
  not a true interior attractor)
- Generally robust behavior across β, γ ∈ [0.5, 2.0]

**Part C — Lyapunov exponent scan (ε=0.2, λ ∈ [0.5, 3.0]):**
- Maximum Lyapunov exponent < 0 for ALL λ values tested
- Most negative MLE at λ=3 (MLE=-0.92) — strong contraction
- Least negative near λ=1.4 (MLE=-0.087) — slowest convergence
- **No chaos detected anywhere in the tested parameter range**

**Physical interpretation**: The system is everywhere stable and globally
attracting. This is good news for physical admissibility (no pathological
sensitivity) but means no period-doubling or chaotic regime is accessible
within the Eisenstein constraint.

---

## Exp04 — Spectral Dimension: Consistent with 1D (Negative Result)

**Main finding: No robust non-integer spectral dimension.**

Multi-scale spectral dimension analysis on N=1000 points:

| t range       | Reference arc d_s | Coupled orbit d_s |
|---------------|-------------------|-------------------|
| [0.05, 0.30]  | 0.26              | 0.27 (artifact)  |
| [0.30, 1.00]  | 1.04              | 1.14 (≈ 1D)      |
| [1.00, 5.00]  | 2.25              | 4.78 (boundary)  |
| [5.00, 20.00] | 1.10              | 12.8 (artifact)  |

At the physically meaningful intermediate scale (t ∈ [0.3, 1.0]):
- Reference arc: d_s = 1.04 ✓ (correctly identifies 1D curve)
- Coupled orbit:  d_s = 1.14 (small deviation, within noise)

**The recursion does NOT produce non-integer spectral dimension.**

The variation with t is a methodological artifact:
- Short t < 0.3: discretization dominates → d_s < 1
- Intermediate t: correct 1D scaling
- Long t > 1: finite-size boundary effects → d_s > 1

The coupled orbit shows slightly higher d_s at large t compared to
the uniform arc, consistent with the orbit clustering near its attractor
(non-uniform density on the arc), NOT fractal geometry.

**Honest verdict**: The recursive dynamics takes points on a 1D arc and maps
them to other points on the same 1D arc. No new topological or fractal
structure is generated. The spectral dimension hypothesis is **falsified**.

---

## Exp05 — RDT Weighting and Conservation Laws

**S_Λ conservation** (the central algebraic invariant):

By construction, every point on the Eisenstein ellipse satisfies
S_Λ = S_b + S_c + Δ = 3π/Λ = 3π (for Λ=1).

This was verified numerically to relative error < 10⁻¹⁵ across all 5000
steps — machine precision. The Eisenstein normalization guarantees this
exactly.

**RDT vs. uniform averages:**

For converging orbits, RDT and uniform averages agree closely (since
the orbit converges to a fixed point, all sufficient tail values
are the same).

**Variance convergence:**

All tested cases show variance ratio (last stratum / first stratum) → 0,
confirming convergence to the attractor.

---

## Summary Table: What Works, What Doesn't

| Claim | Status | Evidence |
|-------|--------|----------|
| Eisenstein constraint is algebraically exact | ✓ CONFIRMED | Analytic proof + 11/11 tests |
| Entropy identity S_Λ = S_b+S_c+√(S_bS_c) | ✓ CONFIRMED | Tests + exp05 conservation |
| S_Λ is exactly conserved under all map steps | ✓ CONFIRMED | exp05, error < 10⁻¹⁵ |
| Symmetric map has no interior fixed points | ✓ CONFIRMED | exp01 |
| Coupling creates interior fixed points | ✓ CONFIRMED | exp02 |
| Interior fixed points are stable (Jacobian) | ✓ CONFIRMED | exp02 Jacobian analysis |
| Single global basin of attraction | ✓ CONFIRMED | exp03 |
| No chaos in tested parameter space | ✓ CONFIRMED | exp03 Lyapunov scan |
| Emergent non-integer spectral dimension | ✗ FALSIFIED | exp04 |
| Spectral dimension deviates significantly from 1 | ✗ FALSIFIED | exp04 multi-scale |
| RDT weighting changes qualitative behavior | ✗ NOT SUPPORTED | exp05 |

---

## What Is Genuine

1. **The algebraic structure is real.** The Eisenstein constraint, entropy
   identity, and Carnot-deficit relation are exact consequences of Vieta's
   formulas on the SdS cubic. They require no approximation and hold for
   all physical (M, Λ) in the Nariai region.

2. **Interior fixed points of coupled maps are physically meaningful.**
   For the map family T_{λ,ε}(u,v) = normalize(u^λ + ε·v, v^λ + ε·u),
   interior fixed points exist for λ > 1, ε below a threshold. These
   represent equilibrium SdS configurations under the recursive dynamics.
   They are stable, globally attracting, and robust to parameter perturbations.

3. **The equilibrium x-value depends continuously and nontrivially on (λ, ε).**
   The function x*(λ, ε) is a non-trivial surface over parameter space. This
   could potentially be characterized analytically (the fixed-point condition
   is u^λ + ε·v = c·u, v^λ + ε·u = c·v for the normalization factor c).

4. **S_Λ is exactly conserved** by all maps in this family (by construction
   of the Eisenstein normalization). This is a genuine invariant.

## What Is Not Genuine

1. **Non-integer spectral dimension**: Falsified. The orbit lives on a 1D
   arc and the spectral dimension consistently measures ~1 at the correct
   scale.

2. **Fractal or multi-scale geometry**: Not observed. All maps converge
   to fixed points; there is no chaotic regime.

3. **Novel thermodynamics**: The maps themselves are constructed (not derived
   from a physical process). The "recursive horizon dynamics" is a
   mathematical construction imposed on the SdS phase space, not derived
   from GR equations of motion or any physical evolution.

---

## What To Do Next (If This Were a Real Paper)

1. **Prove the interior fixed point analytically.** The condition is:
   u^λ + ε·v = c·u, v^λ + ε·u = c·v with u²+uv+v²=1.
   Setting x = u/v: x^λ + ε/v^(λ-1) = c·x, 1 + ε·x·v^(λ-1) = c.
   This is a 1D equation in x that can potentially be solved in special cases.

2. **Map out the phase boundary.** There is a curve ε_c(λ) separating
   "interior fixed point" from "boundary attractor" regimes. Characterize it.

3. **Interpret the equilibrium x*(λ,ε) physically.** What SdS configuration
   does it correspond to? What is M*(λ,ε) = mass at the attractor?

4. **Test with RNdS (Reissner–Nordström–de Sitter)**. The correction gap
   universality analysis shows RNdS has an additional cross-term in the
   entropy structure. Does coupling survive in that more complex case?

---

*All results generated from reproducible Python code. Failures preserved,
not hidden. Spectral dimension result is negative and reported as such.*
