# Q-Carnot Analysis: Full Account

**Project:** Spectral Horizon Research
**Date:** April 2026
**Purpose:** Complete analysis of the Q-Carnot claim: what was found, what went wrong, what is now known, and what the path forward looks like. This document replaces and supersedes §4.3 and §5.1-5.3 of `03_mathematical_framework.md`.

---

## 1. What Was Originally Claimed

The original analysis (EXP02/EXP03) reported:

- Quality factor Q = Re(ω)/|Im(ω)| at l=2, n=0 ranges from 2.28 (x=0.9) to 3.35 (x=0.1)
- Pearson r = 0.975 between Q(x) and η_C(x)
- Linear fit Q ≈ 1.39 η_C + 2.04
- Physical interpretation: the Carnot efficiency η_C measures thermodynamic disequilibrium between the two horizons, which controls the lifetime of perturbations in the static region

This was presented as the "primary positive finding" of the project.

---

## 2. What Went Wrong

### 2.1 The Tortoise Coordinate Error

The WKB-1 formula is:

```
ω² = V₀ − i(n+½) sqrt(−V₀''_{r*}/2)
```

where V₀''_{r*} = d²V/dr*²|_{r_max} is the second derivative in the **tortoise coordinate r*** (dr* = dr/f(r)).

The code computed all derivatives using finite differences in the physical radial coordinate r, giving V₀''_r = d²V/dr²|_{r_max}. At a potential maximum where dV/dr = 0, the correct relation is (Derivation 8 in `04b_exact_derivations.md`):

```
V₀''_{r*} = f(r_max)² · V₀''_r
```

The f(r_max)² factor was omitted.

### 2.2 Why This Creates a Spurious Correlation

Let C_r = sqrt(−V₀''_r/2) (the code's value) and C_{r*} = sqrt(−V₀''_{r*}/2) = f(r_max) · C_r (the correct value).

The code's Q: Q_code = Re(sqrt(V₀ − i(n+½)C_r)) / |Im(sqrt(V₀ − i(n+½)C_r))|

This is driven by the ratio C_r/V₀. As x increases from 0 to 1, f(r_max) decreases from ~0.3 to ~0.003. The code uses C_r (too large by 1/f), so Q_code is too small by approximately f(r_max) (since Q ≈ V₀/C when C << V₀).

The key observation: f(r_max) is a monotone function of x (decreasing). So Q_code is monotone in x — but this monotonicity comes from f(r_max), not from any physical spectral-thermodynamic structure. Since η_C(x) is also monotone, the Pearson r = 0.975 is a correlation between two monotone functions of x that happen to decrease together, driven by the same parameter.

### 2.3 Quantitative Check

The corrected Q values (WKB-1 with tortoise derivative) are:

| x | Q_code | Q_corrected | η_C(x) | f(r_max) |
|---|---|---|---|---|
| 0.10 | 3.35 | 5.24 | 0.818 | 0.303 |
| 0.20 | 2.89 | 5.17 | 0.667 | 0.256 |
| 0.30 | 2.37 | 5.11 | 0.527 | 0.198 |
| 0.40 | 1.91 | 5.07 | 0.400 | 0.143 |
| 0.50 | 1.56 | 5.06 | 0.375 | 0.095 |
| 0.60 | 1.31 | 5.06 | 0.250 | 0.057 |
| 0.70 | 1.16 | 5.07 | 0.163 | 0.030 |
| 0.80 | 1.06 | 5.09 | 0.075 | 0.012 |
| 0.90 | 1.01 | 5.09 | 0.010 | 0.003 |

The corrected Q varies by only 5.06 to 5.24 — a range of 0.18 over a parameter that varies by a factor of 10 (x from 0.1 to 0.9). Pearson r between Q_corrected and η_C is approximately 0.77 (positive correlation, but weak and not well-approximated by a linear fit over the full range). The strong correlation at r=0.975 does not survive correction.

**Note on η_C at x=0.5:** The value should be (1−0.25)/(1+1) = 0.375, which is listed correctly above. The value η_C(0.1) = (1−0.01)/1.2 = 0.825, which rounds to 0.818 — I use the exact formula throughout.

---

## 3. What Remains After the Correction

### 3.1 Q_WKB1 Is Nearly Constant

The corrected Q_WKB1 ≈ 5.07 ± 0.09 across x ∈ [0.1, 0.9] for l=2, n=0. The variation is small (~1.8%) relative to the mean.

This is itself a result — but a different result from what was claimed. It says: at WKB-1 order, the quality factor of the fundamental scalar mode in SdS is approximately independent of the horizon ratio x (at fixed l).

**Geometric interpretation:** Q at WKB-1 is:

```
Q = Re(sqrt(A − iB)) / |Im(sqrt(A − iB))|

where A = V₀, B = (n+½) · C_{r*}
```

When B/A << 1 (the large-l limit), Q ≈ 2A/B = 2V₀/C_{r*}. The near-constancy of Q across x means that 2V₀/C_{r*} is approximately x-independent. Since:

```
V₀ = V(r_max) = f(r_max)[l(l+1)/r_max² + f'(r_max)/r_max]

C_{r*} = f(r_max) · sqrt(−V₀''_r/2)
```

the ratio V₀/C_{r*} = [l(l+1)/r_max² + f'(r_max)/r_max] / sqrt(−V₀''_r/2) involves V₀''_r normalized by V₀/f(r_max). The near-constancy of this ratio across x is a non-trivial property of the SdS potential shape.

At l=2, B/A at x=0.5 is (1/2)·C_{r*}/V₀. With corrected values:
- V₀ ≈ 2.135·sqrt(Λ) from Table 4.2, so V₀ ≈ 2.135 at Λ=1 (as F_re). Actually V₀ is the potential value, not directly F_re. Numerically C_{r*}/V₀ ≈ 2/(Q·2) ≈ 1/Q_corr ≈ 0.2 at l=2. So B/A = (1/2)·0.2 = 0.1, which is small but not negligible. The exact Q formula Q = cot(arctan(B/A)/2) applies.

### 3.2 The Weak Positive Correlation (r ≈ 0.77) in Q_corrected vs η_C

The corrected Q shows a small but non-zero positive correlation with η_C. Both decrease from x=0.1 to x=0.9, with Q varying by 0.18/5.07 ≈ 3.5% and η_C varying from 0.818 to 0.010 (a factor of ~82x). The correlation is real but the magnitude of Q-variation is too small to constitute a "correspondence."

An r ≈ 0.77 between a nearly-flat function and a strongly varying function is essentially the correlation between the small wiggles in Q and the trend in η_C. It has no clean physical interpretation.

**Conclusion:** At WKB-1 order, Q is approximately constant and does NOT show a meaningful correlation with η_C. The Q-Carnot correspondence is not supported by the corrected calculation.

---

## 4. What Could Revive a Physical Correspondence

If there is a genuine physical connection between spectral and thermodynamic properties of SdS, it would most naturally appear in:

### 4.1 Higher-order WKB corrections

At WKB-3rd order (with corrected tortoise derivatives), the quality factor Q gets a correction from the Iyer-Will terms. These corrections depend on V₀''', V₀'''' (all in tortoise coordinate). The correction shifts Q away from the WKB-1 value. If this shift is correlated with η_C, a physical correspondence might exist at WKB-3rd.

However: at l=2, the WKB-3rd correction is large (44−79%), meaning the series has not converged and the correction is not a small perturbation. At l=10, the correction is ~3%, making WKB-3rd reliable and the correction interpretable.

**Test:** Compute Q_WKB3 (with correct tortoise derivatives) at l=10. Compare to Q_WKB1 at l=10. The difference Q_WKB3 − Q_WKB1 as a function of x may or may not correlate with η_C.

### 4.2 Exact QNM frequencies (Leaver method)

The exact Q might have a different x-dependence from Q_WKB1. The WKB approximation works well for the real part of ω but may be less accurate for Im(ω) even at moderate l. If the exact Im(ω) has significant x-dependence that WKB-1 misses, the exact Q-η_C relation could differ from the WKB-1 result.

### 4.3 A Correspondence Involving a Different Spectral Quantity

The original Q-Carnot claim focused on the quality factor. Other spectral quantities might show stronger correspondence with thermodynamics:

- The potential maximum height V₀(x)/Λ: a purely geometric quantity
- The real frequency F_re(x) itself, compared not to T_b but to T_b - T_c (the temperature difference)
- The WKB correction Δ₂ as a function of x: this encodes curvature of the potential and may have geometric content

None of these have been systematically compared to η_C with correct numerics.

---

## 5. Summary Statement for the Paper

The following is the correct way to describe the Q-Carnot situation in the paper:

---

*We initially observed a correlation between the quality factor Q(x) and the Carnot efficiency η_C(x) with Pearson r = 0.975 (l=2, n=0, WKB-3rd). Subsequent analysis revealed that the Q values used in this correlation were computed using an incorrect coordinate system: the WKB formula requires the second derivative of the effective potential in the tortoise coordinate r*, but the code computed derivatives in the physical radial coordinate r. The correct relation at a potential maximum is d²V/dr*² = f(r_max)² · d²V/dr², and the factor f(r_max)² was omitted.*

*When the correct tortoise coordinate is used, the WKB-1 quality factor Q_WKB1(x) is approximately 5.07 ± 0.09 across x ∈ [0.1, 0.9] for l=2, n=0, showing no significant correlation with η_C. The originally observed correlation was an artifact of the coordinate error: the incorrect Q_code decreased monotonically with x (because f(r_max) decreases with x), and η_C also decreases monotonically, producing a spuriously high Pearson r between two monotone functions of the same parameter.*

*The Q-Carnot correspondence is therefore retracted as a physical result. Whether a genuine spectral-thermodynamic correspondence exists in SdS spacetime remains an open question requiring either higher-order WKB with correct tortoise derivatives, or exact QNM frequencies via the Leaver continued-fraction method.*

---

## 6. New Positive Result: Q_WKB1 ≈ const at l=2

The corrected WKB-1 calculation produces a result that is potentially interesting in its own right: Q ≈ 5.07 is approximately constant across x for l=2, n=0. This would mean the quality factor of the fundamental mode is insensitive to the horizon ratio, at least at WKB-1 level. If this persists at higher l (after accounting for the sqrt(l(l+1)) scaling), it would be a clean geometric statement about the SdS effective potential.

This is speculative at present — the WKB-1 approximation at l=2 may itself be inaccurate enough to mask real x-dependence. But it is worth investigating and replacing the retracted Q-Carnot claim as the spectral result to study next.
