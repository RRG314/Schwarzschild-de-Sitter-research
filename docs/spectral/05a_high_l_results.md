# High-l Analysis: Theory, Predictions, and Required Experiments

**Project:** Spectral Horizon Research
**Date:** April 2026
**Purpose:** Establish what the QNM spectrum looks like at higher angular momenta l, both from analytic WKB theory and from the directional trends in the existing l=2,3,4 data. Identify what must be computed with correct methods to resolve the open questions.

---

## Why l=2 Is Not Enough

All five experiments (EXP01-EXP05) used l=2 as the primary case. At l=2, two compounding problems degrade the WKB results:

**Problem 1 — WKB convergence:** The Iyer-Will 3rd-order WKB correction Δ₂ (relative to the 1st-order term) ranges from 44% to 79% across x ∈ [0.2, 0.8] for l=2, n=0. This is far outside the converged regime. In the WKB literature, |Δ₂/ν_n| < 0.1 is considered reliable; at l=2 we have |Δ₂/ν_n| ~ 0.4−0.8. The 1st-order formula is not much worse than the 3rd-order formula in this regime, because the series has not converged.

**Problem 2 — Coordinate artifact in Q:** The tortoise-coordinate bug in the current code means that Im(ω) and Q values at l=2 are unreliable by a factor that depends on f(r_max). This factor varies with x, creating a spurious x-dependence in Q.

At large l, both problems are mitigated:

- The WKB convergence improves as l increases: corrections scale as O(1/l²), so at l=10, the 3rd-order correction is typically < 3−5%.
- The coordinate artifact produces a systematic rescaling of C_{r*} by f(r_max), but f(r_max) does not depend on l (at fixed x), so the artifact affects all l equally at fixed x. This means ratios of Q values at fixed x but different l can reveal the l-dependence cleanly.

---

## Analytic Predictions for Large l

### Potential Scaling with l

At large l, the effective potential is dominated by the centrifugal term:

```
V(r) = f(r)[l(l+1)/r² + f'(r)/r]
     ≈ l(l+1) f(r)/r² + f(r)f'(r)/r
```

At the potential maximum, the centrifugal term dominates when l(l+1)/r_max² >> |f'(r_max)/r_max|. This holds when l is large relative to r_max|f'/f| at the maximum. For l ≥ 6 in the mid-range of x, this condition is reasonably satisfied.

In this regime:

```
V₀ ≈ l(l+1) · f(r_max)/r_max²  + O(1)

d²V/dr²|_{r_max} ≈ l(l+1) · [d²(f/r²)/dr²]_{r_max}  + O(1)
```

Both scale linearly with l(l+1) at large l. Let us write:

```
V₀ = l(l+1) · α(x) + α₀(x) + O(1/l)

d²V/dr²|_{r_max} = l(l+1) · β(x)/r_max^4 + O(1)
```

for some functions α(x), β(x) > 0 (both positive, since the potential is positive at its maximum and concave).

Then the corrected tortoise derivative:

```
V₀''_{r*} = f(r_max)² · d²V/dr²|_{r_max}
           ≈ l(l+1) · f(r_max)² · β(x)/r_max^4
```

and C_{r*} = sqrt(-V₀''_{r*}/2) ≈ sqrt(l(l+1)) · f(r_max) · sqrt(β(x))/(r_max² · sqrt(2)).

### WKB-1 Quality Factor at Large l

At WKB-1 order, ω² = V₀ − i(n+½) C_{r*}. In the limit where C_{r*} << V₀ (which holds when l is large, since C_{r*}/V₀ ~ 1/sqrt(l(l+1))):

```
ω ≈ sqrt(V₀) · [1 − i(n+½) C_{r*}/(2V₀) + ...]

Re(ω) ≈ sqrt(V₀) ≈ sqrt(l(l+1)·α(x))

Im(ω) ≈ −(n+½) C_{r*} / (2 sqrt(V₀))
       ≈ −(n+½) f(r_max) sqrt(β(x)) / (2 sqrt(α(x)) r_max²)
```

Note that in this limit:

```
Im(ω)  →  const(x, n) as l → ∞  [independent of l]

Re(ω)  ∝  sqrt(l(l+1))

Q  =  Re(ω)/|Im(ω)|  ∝  sqrt(l(l+1)) as l → ∞
```

This means Q grows approximately as sqrt(l(l+1)) for large l. At l=2: sqrt(6) ≈ 2.45; at l=10: sqrt(110) ≈ 10.5 — roughly a factor of 4 increase.

**Key prediction:** Q is NOT approximately constant across l. The corrected Q_WKB1 ≈ 5.07 at l=2 is specific to l=2. At l=6, we would predict Q_WKB1 ≈ 5.07 · sqrt(42/6) ≈ 5.07 · sqrt(7) ≈ 13.4. At l=10, Q_WKB1 ≈ 5.07 · sqrt(110/6) ≈ 5.07 · 4.28 ≈ 21.7.

This prediction assumes the large-l asymptotic applies, which may not hold well at l=6. The exact scaling should be tested.

### l-Dependence of F_re

The dimensionless real frequency F_re^{l,0}(x) = Re(ω)/sqrt(Λ) grows approximately as sqrt(l(l+1)) at large l:

```
F_re^{l,0}(x) ≈ sqrt(l(l+1)) · sqrt(α(x)) · r_Λ / r_max(x)   [large l]
```

where r_max(x)/r_Λ is the dimensionless location of the photon sphere. This gives a prediction for how F_re scales with l at fixed x.

**EXP02 data check:** EXP02 computed F_re for l=2,3,4 at each x value. From the l=2 column (Table 4.2 in `03b_mathematical_framework_revised.md`), F_re^{2,0}(0.5) ≈ 2.135. The large-l prediction would give:

```
F_re^{3,0}(0.5) ≈ F_re^{2,0}(0.5) · sqrt(12/6) = 2.135 · sqrt(2) ≈ 3.02
F_re^{4,0}(0.5) ≈ F_re^{2,0}(0.5) · sqrt(20/6) = 2.135 · sqrt(10/3) ≈ 3.90
```

These are the large-l predictions. The actual l=3,4 values from EXP02 should be close to these if the large-l approximation applies by l=3, or somewhat lower if the O(1) correction term is significant.

---

## Q-Carnot at Higher l: What To Expect

The key open question from the Q-Carnot retraction is: does Q correlate with η_C at any l, when computed correctly?

### Case 1: Q is l-universal (possible but unlikely)

If Q_WKB1(x, l)/sqrt(l(l+1)) = Q̃(x) for some function Q̃ independent of l, then the x-dependence of Q at any fixed l would be Q̃(x). Whether Q̃ correlates with η_C would then be a well-posed question about a single function of x.

At large l:

```
Q(x, l) ≈ sqrt(l(l+1)) · Re(sqrt(α(x))) / Im_coeff(x)
```

where Im_coeff(x) = (n+½) f(r_max) sqrt(β(x)) / (2 sqrt(α(x)) r_max²). So:

```
Q(x, l)/sqrt(l(l+1)) ≈ 2 α(x) r_max² / (f(r_max) sqrt(β(x)))
```

This quantity depends on x through α(x) (potential height), r_max (location of maximum), f(r_max) (value of f at maximum), and β(x) (curvature of potential). Whether this function of x correlates with η_C = (1−x²)/(1+2x) is an analytic question about these geometric quantities.

### Case 2: Q is not universal

If Q(x,l)/sqrt(l(l+1)) depends on l (not just x), then even corrected Q values at l=2 would not be representative of the large-l behavior, and the question "does Q correlate with η_C?" would have different answers at different l.

**Resolution:** Compute Q_WKB1 at l=2,4,6,10,20 with corrected tortoise derivatives. If Q(x,l)/sqrt(l(l+1)) collapses onto a single curve Q̃(x) independent of l, Case 1 applies. If not, the l-dependence is non-trivial.

---

## F_re-T_b Correlation at Higher l

The correlation Re(ω)/sqrt(Λ) ≈ A · T_b/sqrt(Λ) + B was found at l=2 with slope A ≈ 15.86. Since Re(ω) ~ sqrt(l(l+1)) and T_b ~ 1/r_b ~ const(x)/r_Λ (independent of l), the coefficient A should scale as sqrt(l(l+1)):

```
A(l) ≈ A(l=2) · sqrt(l(l+1)/6)
```

At l=2: A ≈ 15.86. Predicted at l=6: A ≈ 15.86·sqrt(42/6) = 15.86·sqrt(7) ≈ 41.9.

If this scaling holds, the correlation Re(ω) ∝ T_b would persist at all l (since both sides scale together), but the slope A would change. A l-independent test of the correlation would require looking at Re(ω)/(T_b · sqrt(l(l+1))), which should be approximately constant in x and l.

---

## Summary of Required Experiments (EXP06-EXP08)

### EXP06: Q-Carnot at Multiple l (WKB-1 with corrected tortoise)

```
For l in [2, 4, 6, 8, 10, 15, 20]:
  For x in [0.1, 0.2, ..., 0.9]:
    Compute V₀, V₀''_r (finite differences in r), r_max, f(r_max)
    C_r* = f(r_max) * sqrt(-V₀''_r / 2)
    ω_WKB1 = sqrt(V₀ - i * (1/2) * C_r*)    [n=0]
    Q_corrected = Re(ω_WKB1) / |Im(ω_WKB1)|
    Compute η_C(x) = (1-x²)/(1+2x)

  Fit Q(x, l) vs η_C(x): slope A(l), intercept B(l), Pearson r(l)
  Compute Q(x, l) / sqrt(l(l+1)): check if this collapses to a universal curve

Expected output:
  Table of A(l), B(l), r(l)
  Plot of Q(x,l)/sqrt(l(l+1)) vs x for each l

Key questions:
  Does r(l) remain near 0.975, or drop to near zero?
  Does A(l) ~ sqrt(l(l+1)) (i.e., A(l)/sqrt(l(l+1)) = const)?
  Is the x-dependence of Q̃(x) = Q/sqrt(l(l+1)) correlated with η_C?
```

### EXP07: Re(ω)-T_b Correlation at Multiple l

```
For l in [2, 4, 6, 8, 10]:
  For x in [0.1, 0.2, ..., 0.9]:
    F_re(x, l) = Re(ω_WKB1)/sqrt(Λ)    [from V₀ alone at WKB-1]
    T_b(x)/sqrt(Λ) = (1+2x)(1-x)/(4π*x*sqrt(x²+x+1))  [exact]

  Pearson r between F_re and T_b/sqrt(Λ): call it r_T(l)
  Linear fit: F_re ≈ A_T(l) · T_b/sqrt(Λ) + B_T(l)

Expected output:
  Table of A_T(l), B_T(l), r_T(l)
  Check if A_T(l) ~ sqrt(l(l+1))
  Check if A_T(l)/sqrt(l(l+1)) ~ const (approximately 15.86/sqrt(6) ≈ 6.48)
```

### EXP08: WKB Convergence at Higher l

```
For l in [2, 4, 6, 8, 10]:
  For x in [0.1, 0.2, ..., 0.9]:
    Compute |Δ₂/ν_n| (WKB convergence ratio) at n=0
    Compute |Δ₂/ν_n| at n=1

Expected output:
  Tables of convergence ratio at each (l, x, n)
  Identify minimum l for reliable WKB-3rd results (|Δ₂/ν_n| < 0.1)
```

---

## Theoretical Predictions Summary

| Quantity | Prediction at large l | Basis |
|---|---|---|
| F_re^{l,0}(x) | ∝ sqrt(l(l+1)) | Centrifugal dominance |
| F_im^{l,0}(x) | approximately constant in l | Same |
| Q^{l,0}(x) | ∝ sqrt(l(l+1)) | From above |
| Q(x,l)/sqrt(l(l+1)) | → Q̃(x) (universal) | Hypothesis |
| Slope A_T(l) in Re(ω)=A_T·T_b | ∝ sqrt(l(l+1)) | F_re scaling |
| WKB convergence | Improves as 1/l | Standard WKB theory |

These predictions can be tested without exact QNM methods. If they are correct, they constrain what any physical spectral-thermodynamic correspondence can look like.

---

## What Cannot Be Answered Without Exact Methods

The following questions require Leaver's continued-fraction method or direct numerical integration of the QNM eigenvalue problem:

1. Whether G_l(x) = Re(ω_{l,1})/Re(ω_{l,0}) is monotone at the exact level
2. The exact Q values (not WKB-1 approximations)
3. Whether the corrected Q ≈ const holds beyond the WKB-1 approximation
4. The large-n behavior of Im(ω_n) (relevant to area quantization connections)

These are deferred to the Leaver implementation plan in `05c_exact_numeric_plan.md`.
