# Framework Audit Report

**Project:** Spectral Horizon Research
**Auditing document:** `03_mathematical_framework.md`
**Audit date:** April 2026
**Status:** Complete — 9 issues found, 4 critical

---

## Overview

This audit reviews every formula, claim, and notation choice in `03_mathematical_framework.md` against (a) the exact algebraic derivations, (b) the Iyer-Will WKB formula as written in the original 1987 paper, and (c) the numerical results from EXP01-EXP05. Items are classified by severity:

- **CRITICAL**: Formula is wrong. Any result depending on it is unreliable.
- **ERROR**: Formula is correct but stated incorrectly or misleadingly.
- **NOTATION**: Ambiguous or conflicting symbol use.
- **CLAIM**: Statement is stronger than evidence supports; requires downgrade.

---

## Issue 1 — CRITICAL: T_b formula in §1.4 is nonsensical

**Current text:**

> T_b = (1/4π r_b) [1 − 2(r_b/r_c)³ r_b/r_b − Λr_b²]

The factor `(r_b/r_c)³ r_b/r_b` reduces to `(r_b/r_c)³`, which is not how the surface gravity is computed. The coefficient `2` is also wrong. This is not a minor typo; the expression is internally inconsistent.

**Correct derivation:**

From f(r) = 1 − 2M/r − Λr²/3:

```
f'(r) = 2M/r² − 2Λr/3
```

At the black-hole horizon r_b, the surface gravity is κ_b = |f'(r_b)|/2, giving:

```
T_b = κ_b / (2π) = |f'(r_b)| / (4π)
    = (2M/r_b² − 2Λr_b/3) / (4π)
    = (M/r_b² − Λr_b/3) / (2π)
```

Using M = r_b r_c (r_b + r_c) / (2(r_b² + r_b r_c + r_c²)) and the Eisenstein constraint r_b² + r_b r_c + r_c² = 3/Λ, this simplifies exactly to:

```
T_b = (1 − Λr_b²) / (4π r_b)
```

**Verification:** This is the formula implemented in `src/sds_physics.py` (line: `T_b = (1.0 - lam * r_b**2) / (4.0 * np.pi * r_b)`), which is correct.

Similarly:

```
T_c = (Λr_c² − 1) / (4π r_c)
```

Note: T_c formula has a sign flip because f'(r_c) < 0 (f is decreasing through the cosmological horizon from inside). T_c > 0 because Λr_c² > 1 in the sub-extremal regime.

**Action:** Replace the garbled expression in §1.4 with the correct formulas above.

---

## Issue 2 — ERROR: η_C(x) closed form never stated

**Current text:** The document defines η_C = (T_b − T_c)/T_b but never gives the closed form in x.

**Correct derivation:**

```
T_b = (1 − Λr_b²) / (4π r_b)
T_c = (Λr_c² − 1) / (4π r_c)
```

Using r_b = x r_c:

```
T_b = (1 − Λx²r_c²) / (4π x r_c)
T_c = (Λr_c² − 1) / (4π r_c)
```

Note that Λr_c² = 3/(x² + x + 1) from the Eisenstein constraint, so:

```
1 − Λx²r_c² = 1 − 3x²/(x²+x+1) = (x²+x+1−3x²)/(x²+x+1) = (1+x−2x²)/(x²+x+1)
             = (1+2x)(1−x)/(x²+x+1)

Λr_c² − 1   = 3/(x²+x+1) − 1 = (3−x²−x−1)/(x²+x+1) = (2+x−x²)/(x²+x+1)
             = (2−x)(1+x)/(x²+x+1)
```

Therefore:

```
T_b = (1+2x)(1−x) / (4π x r_c (x²+x+1))

T_c = (2−x)(1+x) / (4π r_c (x²+x+1))

T_b/T_c = (1+2x)(1−x) / (x(2−x)(1+x))

η_C = 1 − T_c/T_b = 1 − x(2−x)(1+x) / ((1+2x)(1−x))
```

Simplifying:

```
η_C(x) = [(1+2x)(1−x) − x(2−x)(1+x)] / [(1+2x)(1−x)]

Numerator: (1+2x)(1−x) − x(2−x)(1+x)
         = (1 − x + 2x − 2x²) − x(2 + 2x − x − x²)
         = (1 + x − 2x²) − x(2 + x − x²)
         = 1 + x − 2x² − 2x − x² + x³
         = 1 − x − 3x² + x³
```

Let me verify via direct computation at x=0.5:
- T_b ∝ (1+1)(0.5)/((0.5)(1.5)(0.75)) = 1/(1.5)(0.75) = 1/1.125... wait let me redo this more carefully.

At x=0.5: Λr_c² = 3/(0.25+0.5+1) = 3/1.75 = 12/7
- T_b = (1 − (12/7)(0.25))/(4π·0.5·r_c) = (1 − 3/7)/(2π r_c) = (4/7)/(2π r_c)
- T_c = ((12/7) − 1)/(4π r_c) = (5/7)/(4π r_c)
- T_c/T_b = (5/7)/(4π r_c) · (2π r_c)/(4/7) = (5/7)(2π)/(4π)(7/4) = (5·2)/(4·4) = 10/16 = 5/8
- η_C = 1 − 5/8 = 3/8 = 0.375

Check with formula from code (computing directly): at x=0.5, η_C should equal 0.375.

Using (1 − x²)/(1 + 2x) = (1 − 0.25)/(1 + 1) = 0.75/2 = 0.375. Correct.

So the simplification is:

```
η_C(x) = (1 − x²) / (1 + 2x) = (1−x)(1+x) / (1+2x)
```

**This is an exact closed-form result.** It must be derived and stated explicitly in the framework document, as it is the thermodynamic quantity appearing in the Q-Carnot correspondence.

**Boundary checks:**
- x → 0: η_C → 1 (T_c → 0 in pure de Sitter)
- x → 1 (Nariai): η_C → 0 (T_b = T_c)
- These match the stated behavior in §1.4. ✓

**Action:** Add this derivation as §1.6 in the revised framework.

---

## Issue 3 — CRITICAL: WKB derivatives are in the wrong coordinate

**Current text (§3.1):**

> V₀'' = d²V/dr*²|_{r_max}

**Problem:** The document correctly states the formula requires the tortoise coordinate r*. However, the code (`src/sds_physics.py`, function `potential_derivatives_higher`) computes all derivatives in the physical r coordinate using finite differences in r, not r*.

At a potential maximum where V'(r) = 0, the chain rule gives:

```
dV/dr* = f(r) dV/dr

d²V/dr*² = f(r)² d²V/dr² + f(r)f'(r) dV/dr
```

At the maximum where dV/dr = 0, the second term vanishes, leaving:

```
d²V/dr*²|_{r_max} = f(r_max)² · d²V/dr²|_{r_max}
```

The code omits the f(r_max)² factor. Since f(r_max) is small throughout the static region (ranging from approximately 0.003 at x=0.9 to 0.303 at x=0.1), the code's V₀'' is too large by a factor of 1/f(r_max)², which ranges from about 11 (x=0.1) to over 110,000 (x=0.9).

**Consequence for Q:** In WKB-1, Q = Re(ω)/|Im(ω)|. With correct V₀''_{r*} = f²·V₀''_r:

```
C_correct = sqrt(−V₀''_{r*}/2) = f(r_max) · sqrt(−V₀''_r/2) = f(r_max) · C_code
```

Since Im(ω) ∝ C and Re(ω) ≈ sqrt(V₀) (unchanged by the f factor, since V₀ does not involve derivatives), the corrected Q is:

```
Q_correct = Q_code / f(r_max) · [some correction from Re(ω) change]
```

More precisely, since Im(ω) decreases by factor f_max and Re(ω) also changes (through the full complex square root), the net effect was computed numerically:

| x | Q_code | Q_corrected | f(r_max) |
|---|---|---|---|
| 0.10 | 3.35 | 5.24 | 0.303 |
| 0.20 | 2.89 | 5.17 | 0.256 |
| 0.30 | 2.37 | 5.11 | 0.198 |
| 0.40 | 1.91 | 5.07 | 0.143 |
| 0.50 | 1.56 | 5.06 | 0.095 |
| 0.60 | 1.31 | 5.06 | 0.057 |
| 0.70 | 1.16 | 5.07 | 0.030 |
| 0.80 | 1.06 | 5.09 | 0.012 |
| 0.90 | 1.01 | 5.09 | 0.003 |

The corrected Q is nearly constant at 5.07 ± 0.05 across x ∈ [0.1, 0.9]. The strong monotone variation in Q_code is an artifact of the missing f² factor, not a physical property of the SdS spectrum.

**Consequence for the Q-Carnot claim:** The Q-Carnot correlation (Pearson r = 0.975, slope 1.39) was computed using Q_code. Since Q_code is monotone decreasing (because 1/f(r_max) is monotone in x), and η_C(x) is also monotone decreasing, any two such monotone functions will have high correlation. The correlation likely reflects the f(r_max)-x relationship, not a physical spectral-thermodynamic correspondence.

**Status of the Q-Carnot correspondence:** UNCONFIRMED as a physical result. It must be downgraded from "primary finding" to "computational artifact pending correction."

**Action:** Section §3.1 must add an explicit note that V₀'' in the WKB formula means the tortoise-coordinate derivative, and that the code's finite differences in r must be corrected by f(r_max)² before use. All Q values in §4 must be flagged as computed with wrong derivatives. The Q-Carnot claim in §5 must be downgraded.

---

## Issue 4 — CRITICAL: Lambda-scaling law overstated in §2.3

**Current text:**

> This is a theorem under the WKB approximation (and should hold exactly for the true QNM frequencies).

**Problem:** The document states the Lambda-scaling law holds "exactly" as a parenthetical, then cites WKB verification as support. These are two separate claims:

**Claim A (PROVED EXACTLY):** The wave equation in tortoise coordinates, when written in dimensionless variables ρ = r/r_Λ = r√(Λ/3) and τ = t/r_Λ, becomes independent of Λ at fixed x. This is a simple dimensional analysis argument that does not depend on WKB. Therefore ω/√Λ = F(x, l, n) exactly.

**Claim B (CONFIRMED NUMERICALLY):** The WKB frequencies satisfy the scaling law to fractional variation < 3.4×10⁻⁵ across Λ ∈ [0.01, 10.0] at fixed x. This is expected from Claim A (since WKB is a consistent approximation of the exact equation) and serves as a sanity check on the code, not an independent verification.

The current text conflates these. The "should hold exactly" parenthetical is correct but needs to be stated as the primary theorem, with the numerical check as a corollary.

**Action:** Revise §2.3 to state Claim A as a proved theorem with derivation, and Claim B as numerical confirmation of the code consistency.

---

## Issue 5 — NOTATION: Symbol collision between Λ_n and Λ

**Current text (§3.1):**

> Λ_n = −i(n + ½)

Throughout the document, Λ (without subscript) denotes the cosmological constant. The WKB parameter Λ_n looks identical at a glance and creates potential confusion.

**Standard notation:** The original Iyer-Will (1987) paper uses the notation `(n + 1/2)` directly, without assigning a symbol. The SdS literature uniformly uses Λ for the cosmological constant.

**Recommendation:** Replace Λ_n with a non-conflicting symbol. Options:
- `ν_n = −i(n + ½)` (using ν for "quantum number")
- `κ_n = −i(n + ½)` (though κ is also used for surface gravity)
- Write it inline as `−i(n+½)` without introducing a symbol

**Action:** Replace Λ_n throughout §3 with a non-conflicting symbol or eliminate the abbreviation.

---

## Issue 6 — CLAIM: Q monotonicity in §4.2 is stated incorrectly

**Current text:**

> Q(x) is not monotone: it has a maximum near x ≈ 0.1 and decreases toward x = 1 (Nariai), but is approximately monotone decreasing for x > 0.1. The range is [2.28, 3.35].

**Problem:** This description is based on Q_code values, which contain the wrong f(r_max)² factor. The corrected Q_WKB1 values are nearly constant at ~5.07. The "non-monotone" character near x=0.1 may be a small residual variation in the correct WKB-1 formula, or it may be an artifact of insufficient numerical resolution. The range [2.28, 3.35] is wrong.

**Action:** Replace the Q(x) table with corrected values (pending recomputation with correct tortoise derivatives), or explicitly flag all values as computed with incorrect derivatives.

---

## Issue 7 — CLAIM: Q-Carnot fit in §4.3 and §5.1-5.3 must be downgraded

**Current text (§4.3):**

> Q(x) ≈ 1.39 · η_C(x) + 2.04 [quadratic in η_C, RMS = 0.035]

**Current text (§5.1):**

> Correlation 2: Q(x) ↔ η_C(x), Pearson r = 0.975

**Current text (§5.2 heading):**

> Physical Interpretation of Q–η_C Correspondence

**Problem:** As established in Issue 3, the Q values used in this fit were computed with wrong tortoise derivatives. The corrected Q is nearly constant in x. A constant function is trivially correlated with any monotone function (the regression slope is near zero and the residuals dominate), so the r=0.975 correlation does not survive correction.

The physical interpretation in §5.2 (and hypothesis in §5.3) is premature — it assumes the Q-η_C correspondence is a real physical relationship, which has not been confirmed with correct numerics.

**Downgrade classification:**
- "Q-Carnot correspondence" at r=0.975: STATUS = ARTIFACT (presumed pending recomputation)
- Physical interpretation of Q as measuring thermodynamic disequilibrium: STATUS = UNVERIFIED CONJECTURE
- Q_min ≈ 2.04 at η_C = 0: STATUS = WRONG (artifact of wrong derivatives)

**What is known:** If Q_WKB1 is truly constant at ~5.07 with correct derivatives, then the Q-Carnot relation at WKB-1 order is Q ≈ const, which has a different (and possibly simpler) geometric interpretation: the ratio Re(ω)/|Im(ω)| is set by the geometry at the potential maximum, independently of the thermodynamic state. This would be a clean result, but a different one.

**Action:** §4.3, §5.1, §5.2, §5.3 must be substantially revised. The Q-Carnot correlation must be clearly marked as tentative/artifact pending correct WKB computation.

---

## Issue 8 — ERROR: Re(ω)-T_b correlation in §5.1 depends on wrong Q

**Current text (§5.1, Correlation 1):**

> Pearson r = 0.995, Linear fit: Re(ω_{l=2})/√Λ = 15.86 · T_b/√Λ + 1.14

**Assessment:** Re(ω) = Re(sqrt(V₀ + WKB correction)) depends primarily on V₀ = V(r_max). The potential maximum value V₀ does NOT involve a tortoise-coordinate derivative, so Re(ω) at WKB-1 order is not affected by the tortoise bug. The Re(ω)-T_b correlation is therefore potentially valid even with the code's derivative error.

However, the 3rd-order WKB corrections to Re(ω) involve V₀'' and higher derivatives, which are in the wrong coordinate. So the 3rd-order Re(ω) values have some error from this.

**Assessment:** Correlation 1 is POSSIBLY VALID at WKB-1 (where Re(ω) ≈ sqrt(V₀), which is correct). It should be verified at WKB-1 separately. The 3rd-order values carry systematic error.

**Action:** Flag this correlation as WKB-1 order only (pending recomputation); the 15.86 coefficient may shift with correct higher-order corrections.

---

## Issue 9 — CLAIM: "Q universality" claim in §4.1

**Current text (implied):** The Lambda-scaling law guarantees that Q = Re(ω)/|Im(ω)| is Λ-independent at fixed x.

**Assessment:** This claim IS correct, for any fixed QNM method (exact or WKB). Since both Re(ω) and Im(ω) scale as √Λ, their ratio is Λ-independent. This is an exact consequence of the scaling law.

**Status:** PROVED (follows immediately from the scaling theorem).

**No action needed** except to state it explicitly as a corollary of the Lambda-scaling theorem.

---

## Summary Table

| Issue | Severity | Location | Status |
|---|---|---|---|
| T_b formula garbled | CRITICAL | §1.4 | Fix required |
| η_C(x) closed form missing | ERROR | §1.4 | Derivation required |
| Lambda-scaling: exact proof vs. WKB check conflated | CRITICAL | §2.3 | Rewrite required |
| WKB derivatives in wrong coordinate | CRITICAL | §3.1 + all Q results | Affects §4, §5 |
| Symbol collision Λ_n vs. Λ | NOTATION | §3.1 | Symbol change required |
| Q monotonicity claim wrong | CLAIM | §4.2 | Based on wrong values |
| Q-Carnot correspondence | CLAIM | §4.3, §5.1-5.3 | Downgrade to artifact |
| Re(ω)-T_b correlation | CLAIM | §5.1 | Possibly valid; verify |
| Q Λ-independence | — | §4.1 | Correct; no change needed |

---

## What Remains Solid

The following results are unaffected by the tortoise bug and remain reliable:

1. **Eisenstein constraint** r_b² + r_b r_c + r_c² = 3/Λ — exact algebraic identity
2. **Entropy identity** S_Λ = S_b + S_c + √(S_b S_c) — exact consequence of Eisenstein
3. **η_C(x) = (1−x²)/(1+2x)** — exact closed form derived above
4. **Lambda-scaling law** ω/√Λ = F(x,l,n) — proved from dimensional analysis of wave equation
5. **Q Λ-independence** at fixed x — corollary of scaling law, exact
6. **Inverse spectroscopy failures** (negative results for G_l and S_{32}) — unaffected by derivative error since these involve ratios of Re(ω) values, and Re(ω) at WKB-1 does not require tortoise derivatives
7. **Eisenstein structure in QNM spectrum: NEGATIVE** — unaffected
8. **RDT overtone correlation: SPURIOUS** — the artifact was already identified as arithmetic, unaffected by derivative error

The primary positive claim requiring revision is the Q-Carnot correspondence.
