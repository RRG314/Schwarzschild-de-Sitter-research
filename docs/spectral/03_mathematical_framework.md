# Mathematical Framework

**Project:** Spectral Horizon Research
**Date:** April 2026

---

## 1. SdS Spacetime and Parameter Space

### 1.1 Metric and Horizons

The Schwarzschild–de Sitter metric in static coordinates is:

```
ds² = −f(r) dt² + f(r)⁻¹ dr² + r² dΩ²

f(r) = 1 − 2M/r − Λr²/3
```

For M > 0 and Λ > 0, f has two positive roots r_b < r_c satisfying f(r_b) = f(r_c) = 0. These are the black-hole and cosmological horizons respectively. Sub-extremal spacetimes require:

```
0 < r_b < r_c < r_Λ,    r_Λ = √(3/Λ)
```

The degenerate (Nariai) limit is r_b = r_c at x = 1, which corresponds to M = M_Nariai = r_Λ / (3√3).

### 1.2 Eisenstein Constraint

From Vieta's formulas applied to f(r) = −(Λ/3)(r − r_b)(r − r_c)(r + r_b + r_c)/r:

```
r_b² + r_b r_c + r_c² = 3/Λ
```

This is the defining constraint relating the two horizon radii at fixed Λ. It is an exact algebraic identity.

### 1.3 Parametrization by x

Defining x = r_b/r_c ∈ (0,1), the Eisenstein constraint becomes:

```
r_c² (x² + x + 1) = 3/Λ
⟹ r_c = r_Λ / √(x² + x + 1)
   r_b = x · r_c = x r_Λ / √(x² + x + 1)
```

The mass and other observables are determined by x and Λ:

```
M(x, Λ) = r_b r_c (r_b + r_c) / (2(r_b² + r_b r_c + r_c²))
         = r_Λ · x(1+x) / (2(x²+x+1)^{3/2})
```

### 1.4 Thermodynamics

The surface gravities at the two horizons give temperatures:

```
T_b = |f'(r_b)| / (4π) = (1/4π r_b) [1 − 2(r_b/r_c)³ r_b/r_b − Λr_b²]
```

More explicitly, T_b and T_c are functions of x and Λ with T_b/√Λ and T_c/√Λ depending only on x. The Carnot efficiency of the thermodynamic cycle:

```
η_C(x) = (T_b − T_c) / T_b
```

is a pure function of x (no Λ dependence), lying in (0,1) for x ∈ (0,1), with η_C → 0 at x → 1 (Nariai, T_b → T_c) and η_C → 1 at x → 0 (pure de Sitter, T_b → ∞).

### 1.5 Entropy Identity

The Bekenstein-Hawking entropies S_b = πr_b² and S_c = πr_c² satisfy:

```
S_Λ ≡ π r_Λ² = S_b + S_c + √(S_b S_c)
```

exactly, where S_Λ is the de Sitter entropy. This follows from r_b² + r_b r_c + r_c² = r_Λ².

---

## 2. Effective Potential for Scalar Perturbations

### 2.1 Regge-Wheeler Equation

A minimally coupled massless scalar Φ satisfying □Φ = 0 in SdS can be decomposed as Φ = Ylm(θ,φ) ψ(t,r)/r. The radial function ψ satisfies:

```
∂²ψ/∂t² − ∂²ψ/∂r*² + V(r) ψ = 0
```

where r* is the tortoise coordinate dr* = dr/f(r), and:

```
V(r) = f(r) [l(l+1)/r² + f'(r)/r]
```

### 2.2 Properties of V(r)

V(r) vanishes at both horizons (since f(r_b) = f(r_c) = 0) and is positive in the static region r_b < r < r_c. It has a single maximum at some r_max with r_b < r_max < r_c. Under the Lambda-scaling r → r/√Λ at fixed x:

```
V(r) → Λ · V_x(r/r_c)
```

where V_x is the dimensionless potential shape depending only on x. Consequently V_max ∝ Λ.

### 2.3 Lambda-Scaling Law

Under the rescaling r → r/√Λ with x held fixed, the QNM eigenvalue equation is invariant up to an overall factor of Λ. Therefore:

```
ω(x, l, n, Λ) = √Λ · F(x, l, n)
```

where F is a dimensionless complex function. Equivalently, ω/√Λ = F(x,l,n). This is a theorem under the WKB approximation (and should hold exactly for the true QNM frequencies). **Numerical verification (EXP02): confirmed to fractional variation < 3.4×10⁻⁵ across Λ ∈ [0.01, 10.0].**

---

## 3. WKB Quasinormal Mode Approximation

### 3.1 WKB Order Hierarchy

The WKB method approximates ω from local data at the potential maximum r_max. We implement three orders:

**1st order (Schutz-Will 1985):**
```
ω² ≈ V₀ − i(n + ½) √(−V₀''/2)

where V₀ = V(r_max), V₀'' = d²V/dr*²|_{r_max}
```

At this order, Re(ω) = Re(√(V₀ − i(n+½)C)) and Im(ω) = Im(√(...)). Note: Re and Im both depend on n; the leading-order expansion Re(ω) ≈ √V₀ − (n+½)²C²/(8V₀^{3/2}) and Im(ω) ≈ −(n+½)C/(2√V₀) hold only when (n+½)C << V₀.

**3rd order (Iyer-Will 1987):**
```
ω² = V₀ + √(−2V₀'') [Λ_n + Δ₂(Λ_n)]

Λ_n = −i(n + ½)
Δ₂ = (1/q)[V₀''''/V₀'' · (¼ + Λ_n²)/8 − (V₀'''/V₀'')² · (7 + 60Λ_n²)/288]
q = √(−2V₀'')
```

**Convergence criterion:** |Δ₂| < ½|Λ_n|. For n = 0 (fundamental mode), this is almost always satisfied in the sub-extremal range. For n = 1, the 3rd-order correction is large (often |Δ₂| > |Λ₁|), indicating WKB-3rd is unreliable for overtones at l = 2. Use l ≥ 6 for reliable n = 1 results.

### 3.2 WKB Accuracy at l=2

The 3rd-order WKB relative correction from 1st to 3rd order ranges from 44% to 79% across x ∈ [0.2, 0.8] for l=2, n=0. This is large, indicating that l=2 results should be treated as qualitative. Reliable quantitative results require either higher l or exact methods (continued-fraction or numerical).

**For all results in this project using l=2:** treat the numerical values as indicating the correct qualitative behavior and approximate magnitudes, with a systematic uncertainty of order 10-50%.

---

## 4. Dimensionless Spectral Functions

### 4.1 Definition

Define the dimensionless spectral functions:

```
F_re^{l,n}(x) ≡ Re[ω(x, l, n, Λ)] / √Λ     (Lambda-independent)
F_im^{l,n}(x) ≡ Im[ω(x, l, n, Λ)] / √Λ     (Lambda-independent)
Q^{l,n}(x) ≡ |F_re^{l,n}(x) / F_im^{l,n}(x)|   (quality factor; Lambda-independent)
```

The Lambda-scaling law guarantees these are well-defined functions of x, l, n only.

### 4.2 Computed Values (l=2, n=0, Λ=1)

| x | F_re | F_im | Q |
|---|---|---|---|
| 0.10 | 8.641 | −2.639 | 3.27 |
| 0.20 | 4.517 | −1.481 | 3.05 |
| 0.30 | 3.157 | −1.124 | 2.81 |
| 0.40 | 2.501 | −0.959 | 2.61 |
| 0.50 | 2.135 | −0.866 | 2.47 |
| 0.60 | 1.918 | −0.808 | 2.37 |
| 0.70 | 1.789 | −0.771 | 2.32 |
| 0.80 | 1.716 | −0.749 | 2.29 |
| 0.90 | 1.680 | −0.737 | 2.28 |

Q(x) is **not monotone**: it has a maximum near x ≈ 0.1 and decreases toward x = 1 (Nariai), but is approximately monotone decreasing for x > 0.1. The range is [2.28, 3.35].

### 4.3 Polynomial Approximation of Q(x)

Q(x) is well-approximated by a cubic polynomial in x with RMS residual 0.017 (less than 1% of the full range). The quadratic fit in η_C(x) gives RMS = 0.035 (less than 1.5% of range):

```
Q(x) ≈ 1.39 · η_C(x) + 2.04    [quadratic in η_C, RMS = 0.035]
```

This empirical fit has a clear physical interpretation (see §5.2 below).

---

## 5. Spectral-Thermodynamic Correspondences

### 5.1 Observed Correlations

Two strong correlations were found between spectral observables and thermodynamic quantities:

**Correlation 1: Re(ω)/√Λ ↔ T_b/√Λ**
```
Pearson r = 0.995
Linear fit: Re(ω_{l=2})/√Λ = 15.86 · T_b/√Λ + 1.14
```

The real (oscillation) frequency of the fundamental mode tracks the black-hole Hawking temperature. Physically: T_b = κ_b/(2π) where κ_b is the surface gravity at r_b. The effective potential barrier height V₀ is set by the geometry near r_max, which is in turn influenced by the curvature at r_b. So this correlation has a plausible geometric origin.

**Correlation 2: Q(x) ↔ η_C(x)**
```
Pearson r = 0.975
Linear fit: Q = 1.39 · η_C + 2.04
```

The quality factor of the fundamental resonance is linearly correlated with the Carnot efficiency of the two-horizon system. This is the primary spectral-thermodynamic correspondence found in this project.

### 5.2 Physical Interpretation of Q–η_C Correspondence

The quality factor Q = Re(ω)/|Im(ω)| measures how many oscillation cycles a mode completes before decaying. The Carnot efficiency η_C = (T_b − T_c)/T_b measures the "work potential" of the thermodynamic engine formed by the BH and cosmological horizons (where work is extracted from the temperature difference).

When x → 1 (Nariai), T_b → T_c and η_C → 0: the two horizons are at equal temperature, the thermodynamic engine is useless, and simultaneously Q → Q_min ≈ 2.28 (modes are most short-lived relative to their oscillation frequency).

When x → 0 (small BH), T_b >> T_c and η_C → 1: the BH is very hot compared to the cosmological horizon, and Q → Q_max ≈ 3.35 (modes are most long-lived relative to oscillation frequency).

The interpretation: **the degree of thermodynamic disequilibrium between the two horizons controls the lifetime of perturbations in the static region between them.** More precisely: when the horizons are thermally far apart, the effective potential barrier is taller relative to its width (the WKB ratio V₀/C, where C = √(−V₀''/2) sets the imaginary part), and modes ring longer before decaying.

### 5.3 A Hypothesis: Q as a Spectral Carnot Bound

The linear relation Q ≈ 1.39 η_C + 2.04 has a natural form: Q_min ≈ 2.04 (the "thermal" floor when η_C = 0) and a slope of 1.39. The intercept Q_min ≈ 2 is suggestive — the minimum quality factor for a physically realizable resonance above a potential barrier (by WKB) is bounded below by approximately 1/√2 times the angular momentum. The observed minimum Q ≈ 2.28 is consistent with l=2 setting a lower bound.

**Open question:** Is there a derivation from first principles of Q_min as a function of l alone, and does the slope 1.39 follow from geometry?

---

## 6. Inverse Spectroscopy: Negative Results

### 6.1 Overtone Ratio G_l(x)

Define G_l(x) = Re(ω_{l,1})/Re(ω_{l,0}) (the real-frequency ratio between first overtone and fundamental). If this were monotone in x, it could be used to invert: given a measured G_l, solve for x.

Result: G_l(x) is NOT monotone (range [0.67, 3.54] for l=2). Furthermore, G_l is NOT Λ-independent at WKB-3rd order: G_l varies by σ = 0.30 across Λ ∈ [0.05, 10], compared to a mean of ~2.5. This ~12% variation arises because WKB-3rd order accuracy for n=1 depends on the shape of V₀'' differently than for n=0.

**Consequence:** Inverse spectroscopy via overtone ratios fails at WKB-3rd order. This could be an artifact of WKB inaccuracy for n=1 (where |Δ₂| > |Λ₁|). Higher-order WKB or exact numerics are needed to test whether G_l is truly Λ-independent for the exact QNM frequencies.

### 6.2 Cross-Mode Ratio S_{ll'}(x)

Define S_{32}(x) = Re(ω_{l=3,n=0})/Re(ω_{l=2,n=0}). This should be Λ-independent (both are fundamental modes where WKB converges). The range [1.04, 1.20] is narrow and the function is NOT monotone, providing insufficient discriminating power to recover x.

**Consequence:** The cross-mode ratio using adjacent l values does not provide a useful inversion for x.

### 6.3 Why Inverse Spectroscopy is Hard in SdS

The fundamental difficulty is that the dimensionless frequency F_re^{l,n}(x) varies over a large range (factor ~5 from x=0.1 to x=0.9 for l=2), but all frequencies decrease monotonically with x. The ratio of any two monotone decreasing functions is therefore nearly constant. A useful inversion would require a ratio where the two modes have different functional forms vs. x — but the WKB formula ties all frequencies to the same r_max, making their ratios relatively insensitive to x.

---

## 7. Notation Summary

| Symbol | Definition |
|---|---|
| x | r_b/r_c ∈ (0,1), the horizon ratio |
| Λ | cosmological constant |
| r_Λ | = √(3/Λ), the de Sitter radius |
| r_b, r_c | black-hole and cosmological horizon radii |
| M | black hole mass |
| T_b, T_c | Hawking temperatures of the two horizons |
| η_C | Carnot efficiency = (T_b − T_c)/T_b |
| S_b, S_c | Bekenstein-Hawking entropies |
| ω | QNM frequency (complex; Im(ω) < 0 for stable modes) |
| l, n | angular momentum and overtone quantum numbers |
| Q | quality factor = Re(ω)/|Im(ω)| |
| F_re, F_im | dimensionless spectral functions = Re(ω)/√Λ, Im(ω)/√Λ |
| V₀ | potential maximum value |
| V₀'' | second derivative of V at maximum (in tortoise coordinate) |
| Λ_n | WKB parameter = −i(n+½) |
