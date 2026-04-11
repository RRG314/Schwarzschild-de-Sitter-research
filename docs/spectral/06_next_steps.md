# Next Steps and Open Problems

**Project:** Spectral Horizon Research
**Date:** April 2026

---

## Immediate Priorities (High Confidence)

### 1. Improve WKB Accuracy: Use Higher Angular Momenta

All current results use l = 2, where WKB-3rd has 44–79% corrections — far outside the convergent regime. Before drawing quantitative conclusions, the following should be done:

- Rerun EXP02–EXP04 with l = 6, 8, 10.
- At l = 10, WKB-3rd corrections are typically < 5%, making the results quantitatively reliable.
- The Q–Carnot correlation should be checked at higher l to see whether the slope (1.39) and intercept (2.04) are l-dependent.

**Expected effort:** 1–2 hours. The code infrastructure is in place; just change the l parameter in the experiments.

### 2. Verify Q–Carnot Correspondence at Higher l

The Q–Carnot correlation (r = 0.975) was found at l = 2, n = 0. Three questions:

- Does the correlation persist at l = 6, 10?
- Does the slope change with l (suggesting Q ~ η_C · f(l))?
- Is there a derivation from the WKB formula: Q = Re(ω)/|Im(ω)| = Re(√(V₀+...))/|Im(√(V₀+...))|?

At leading WKB order: Q ≈ Re(√(V₀ − iC/2)) / |Im(√(V₀ − iC/2))| ≈ √(2V₀/C) − ... where C = √(−V₀''/2). This is a function of V₀ and V₀'' at r_max, both of which depend on x and l. If V₀(x,l) ≈ l(l+1) · h(x) and V₀''(x,l) ≈ l(l+1) · g(x) for some functions h, g, then Q would be independent of l. The empirical check at several l values would clarify this.

### 3. Implement Continued-Fraction (Leaver) Method

The most important accuracy limitation is WKB at l = 2 and n ≥ 1. Leaver's (1985) continued-fraction method gives exact QNMs (up to numerical precision) for any l and n. The SdS generalization is standard:

- **Leaver for SdS:** the radial equation in the tortoise coordinate leads to a 3-term recurrence at each horizon. The QNM condition is that both recurrences simultaneously converge. See Moss & Norman (2002) for the SdS adaptation.
- This would allow reliable computation of n=1 overtones for l=2, enabling a proper test of the overtone ratio and inverse spectroscopy.

**Expected effort:** 2–4 hours for a basic implementation; 1–2 days for a validated one.

---

## Medium-Term Research Directions

### 4. Derive the Q–Carnot Correspondence from First Principles

The empirical fit Q ≈ 1.39 η_C + 2.04 begs an analytic explanation. The approach:

1. Start with the WKB-1 formula: Q = Re(ω)/|Im(ω)| = Re(√(V₀ − iC/2)) / |Im(√(V₀ − iC/2))|.
2. Express V₀ and C in terms of x using the SdS potential at r_max.
3. Express η_C in terms of x.
4. Show (or disprove) that Q(x) = a · η_C(x) + b for some constants a, b.

If this works at leading WKB order, it would provide a clean analytic result connecting spectral and thermodynamic structure. Even a perturbative derivation (valid for small x or x near 1) would be valuable.

### 5. Study the Q–η_C Correspondence Across l

At l = 2 (WKB inaccurate): Q ∈ [2.28, 3.35], correlation r = 0.975.
**Prediction:** At l = 10 (WKB accurate): Q should scale as ~√(l(l+1)/6) · Q_{l=2}(x). At leading WKB order, Q is proportional to √(l(l+1)) (since V₀ ~ l(l+1) and C ~ l(l+1)^{1/2}). More precisely:

```
Q(x, l) ≈ A(l) · η_C(x) + B(l)

where A(l) → const, B(l) → const as l → ∞ (if Q is dominated by geometry, not l)
```

This would establish a universal spectral-thermodynamic relationship independent of angular momentum.

### 6. Investigate the Re(ω)–T_b Correspondence More Deeply

The correlation r = 0.995 between Re(ω)/√Λ and T_b/√Λ suggests a near-linear relationship. At leading WKB order:

```
Re(ω) ≈ √V₀ = √(f(r_max) · [l(l+1)/r_max² + f'(r_max)/r_max])
```

while T_b = |f'(r_b)| / (4π). Both involve f' but evaluated at different points (r_max vs r_b). The empirical slope of 15.86 suggests Re(ω) ≈ 16 T_b at leading order. Is there a simple geometric argument for why these are proportional?

**Hypothesis:** At large l, r_max → r_b (the photon sphere approaches the BH horizon in the small-BH limit). In that regime, Re(ω) ≈ √(f'(r_b) · l(l+1)/r_b²) and T_b = |f'(r_b)|/(4π), giving Re(ω)/T_b ≈ 4π√(l(l+1)/r_b) · f'(r_b)^{-1/2}, which depends on x. But the correlation at l=2 is already 0.995, so the connection is tighter than what this argument would predict.

### 7. Proper Inverse Spectroscopy Study at Higher l and Exact Methods

The failure of G₂_re inversion was partly a WKB artifact (Λ-independence broken for n=1 at WKB-3rd). With exact methods:

- G₂_re should be exactly Λ-independent.
- Test monotonicity at several l values.
- If G₂_re is monotone at l=10 or higher, build the inversion and test its accuracy.

Additionally, the cross-mode ratio S_{ll'} with a larger gap (e.g., l=2 and l=6) would give a wider range and might be monotone.

---

## Speculative / Long-Term Directions

### 8. SdS Spectral Geometry: A New Parametrization

The dimensionless spectral functions F_re^{l,n}(x) and F_im^{l,n}(x) define a map from the parameter space x ∈ (0,1) to the complex QNM frequency plane. For each (l,n), this is a curve in ℂ parameterized by x.

**Question:** What is the geometric shape of this curve? For l=2, n=0: does the (F_re, |F_im|) curve have algebraic structure? Is it part of an ellipse, a hyperbola, or a more general algebraic curve?

This would connect to the Eisenstein ellipse that parametrizes the SdS state space. The prior work showed the state space (r_b, r_c) lives on the ellipse u² + uv + v² = 1 (in normalized Eisenstein variables). The spectral space may live on a different but related algebraic curve.

### 9. Extension to Reissner-Nordström-de Sitter (RNdS)

RNdS has three parameters (M, Q, Λ) and three horizons (inner, outer BH, cosmological). The analog of the Eisenstein constraint is more complex (a quartic in the radii). The entropy identity also generalizes.

**Question:** Does the Q–Carnot correspondence extend to RNdS? The Carnot efficiency would involve three temperatures, and the "spectral" data would include more mode types (vector and scalar, different QNM families).

### 10. Connection to Area Quantization

Hod's conjecture (1998) relates the asymptotic QNM frequency ω_R → 2πT_H to the quantum of area ΔA = 4ℓ²_Planck ln 3 in loop quantum gravity. For SdS, there are two temperatures (T_b and T_c). The asymptotic behavior ω_R → ? as n → ∞ has been studied (Motl 2003, Natário & Schiappa 2004 for de Sitter-like spacetimes), but the two-temperature analog of Hod's formula has not been computed.

**Question:** In the large-n limit, do the SdS QNMs asymptote to combinations of T_b and T_c? If so, is the combination related to the Carnot efficiency?

---

## Implementation Notes for Next Experiments

### EXP06 (suggested): Q–Carnot at Multiple l

```python
# Compute Q(x) vs eta_C(x) for l = 2, 4, 6, 8, 10
# Fit linear model at each l
# Report: slope A(l), intercept B(l), correlation r(l)
# Test: does A(l) ∝ 1/l, const in l, or something else?
```

### EXP07 (suggested): Leaver Baseline Validation

```python
# Implement Leaver continued-fraction for SdS
# Validate against WKB-3rd for l = 2, n = 0 (where WKB has 50% correction)
# Report: how large is the WKB-3rd error, how does it depend on x?
# Use Leaver results to redo EXP02-EXP04 with exact frequencies
```

### EXP08 (suggested): Analytic Q–Carnot at Leading WKB Order

```python
# For l large: Q_WKB1(x, l) = f(V0, V0pp)
# Express V0, V0pp as explicit functions of x (using sds_physics)
# Express eta_C as explicit function of x
# Fit Q_WKB1(x, l) = A(l) * eta_C(x) + B(l)
# Report: A(l), B(l) vs l, look for pattern
```

---

## Summary: Research Roadmap

```
COMPLETED (this work)
├── Lambda-scaling law: confirmed (< 0.01%)
├── Q universality: confirmed
├── Q–Carnot correspondence: r = 0.975 (at l=2, WKB-3rd)
├── Re(ω)–T_b correspondence: r = 0.995 (at l=2, WKB-3rd)
├── Eisenstein structure in spectrum: NEGATIVE
├── Inverse spectroscopy (WKB-3rd): NEGATIVE (partial artifact)
└── RDT overtones: NEGATIVE (spurious)

NEXT (high priority)
├── Repeat EXP02–EXP04 at l = 6, 10 for quantitative accuracy
├── Verify Q–Carnot slope/intercept dependence on l
└── Derive Q–Carnot analytically at leading WKB order

MEDIUM TERM
├── Leaver CF implementation for exact QNMs
├── Proper overtone inversion study
└── Re(ω)–T_b correspondence: analytic derivation

SPECULATIVE
├── Spectral curve geometry (algebraic structure of F(x))
├── RNdS extension
└── Asymptotic QNM → area quantization for two-temperature system
```

The Q–Carnot correspondence is the most promising thread to pursue immediately, because it is a clean numerical result that could become an analytic theorem with modest additional work.
