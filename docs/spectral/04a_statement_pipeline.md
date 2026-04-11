# Formal Statement Pipeline

**Project:** Spectral Horizon Research
**Date:** April 2026
**Purpose:** Every mathematical claim in this project is catalogued here with: exact statement, proof status, evidence type, confidence level, and required next action. This is the authoritative list for the paper.

---

## How to Read This Document

**Proof Status codes:**
- PROVED: Complete proof exists, written in `04b_exact_derivations.md`
- DISPROVED: Counterexample or derivation showing the claim is false
- EMPIRICAL: Confirmed numerically but not proved analytically
- ARTIFACT: Numerical result confirmed to be a computational error
- CONJECTURE: Plausible from evidence, not proved, not disproved
- OPEN: Not enough evidence to classify

**Evidence type codes:**
- ALG: Exact algebraic / combinatorial argument
- DIM: Dimensional analysis
- WKB1: WKB 1st-order approximation (reliable for l ≥ 6; qualitative for l=2)
- WKB3: WKB 3rd-order (carries coordinate error in current code; further flagged)
- NUM: Numerical computation other than WKB
- NONE: No supporting computation

---

## Group 1: Exact Algebraic Results

These results depend only on the structure of f(r) and Vieta's formulas. They require no approximation.

---

### Statement 1.1 — Eisenstein Constraint

**Claim:** For any SdS spacetime with M > 0 and Λ > 0 in the sub-extremal regime, the two horizon radii satisfy:

```
r_b² + r_b r_c + r_c² = 3/Λ
```

**Status:** PROVED

**Evidence:** ALG — follows directly from Vieta's formulas applied to f(r) = 1 − 2M/r − Λr²/3. See `04b_exact_derivations.md`, Derivation 1.

**Confidence:** 100% — this is a polynomial identity.

**Next action:** None. Cite in paper as Theorem 1.

---

### Statement 1.2 — Entropy Identity

**Claim:** The Bekenstein-Hawking entropies S_b = πr_b² and S_c = πr_c² and the de Sitter entropy S_Λ = πr_Λ² = 3π/Λ satisfy:

```
S_Λ = S_b + S_c + sqrt(S_b S_c)
```

**Status:** PROVED

**Evidence:** ALG — immediate corollary of Statement 1.1. See `04b_exact_derivations.md`, Derivation 2.

**Confidence:** 100%.

**Next action:** None. Cite in paper as Corollary 1.

---

### Statement 1.3 — Parametrization by x

**Claim:** Writing x = r_b/r_c ∈ (0,1), the horizons and mass are:

```
r_c = r_Λ / sqrt(x²+x+1),    r_b = x r_Λ / sqrt(x²+x+1)

M = r_Λ · x(1+x) / (2(x²+x+1)^{3/2})
```

**Status:** PROVED

**Evidence:** ALG — direct substitution into the Eisenstein constraint and f(r_b) = 0. See `04b_exact_derivations.md`, Derivation 3.

**Confidence:** 100%.

**Next action:** None. Used throughout paper.

---

### Statement 1.4 — Hawking Temperatures

**Claim:**

```
T_b = (1+2x)(1−x) / (4π x r_Λ sqrt(x²+x+1)) = (1 − Λr_b²) / (4π r_b)

T_c = (2+x)(1−x) / (4π r_Λ sqrt(x²+x+1)) = (Λr_c² − 1) / (4π r_c)
```

**Status:** PROVED

**Evidence:** ALG — from f'(r) = 2M/r² − 2Λr/3, substituting M and using the Eisenstein constraint. Full derivation in `03b_mathematical_framework_revised.md` §1.4 and `04b_exact_derivations.md`, Derivation 4.

**Confidence:** 100%.

**Note:** The formula T_b = (1−Λr_b²)/(4πr_b) is the compact form; the expanded form in x is also exact. The original framework document §1.4 contained a garbled version of this formula. The correct formula is derived in the revised framework.

**Next action:** None. Confirm in paper.

---

### Statement 1.5 — Carnot Efficiency Closed Form

**Claim:**

```
η_C(x) = (T_b − T_c)/T_b = (1 − x²)/(1 + 2x)
```

exactly, as a function of x alone.

**Status:** PROVED

**Evidence:** ALG — derived in `03b_mathematical_framework_revised.md` §1.5 using Statements 1.3 and 1.4. See `04b_exact_derivations.md`, Derivation 5.

**Confidence:** 100%.

**Properties:** η_C(0) = 1, η_C(1) = 0, strictly decreasing on (0,1). Also: T_c/T_b = x(2+x)/(1+2x).

**Next action:** None. This is a new exact result (not in prior literature at this parametrization). Highlight in paper.

---

## Group 2: Lambda-Scaling Law

---

### Statement 2.1 — Lambda-Scaling Law (Exact)

**Claim:** The exact QNM frequencies of the SdS massless scalar field satisfy:

```
ω(x, l, n, Λ) = sqrt(Λ) · F(x, l, n)
```

for some dimensionless complex function F independent of Λ.

**Status:** PROVED

**Evidence:** DIM — the wave equation in dimensionless coordinates ρ = r/r_c, ρ* = r*/r_c, τ = t·sqrt(Λ) has no explicit Λ-dependence. Proof in `04b_exact_derivations.md`, Derivation 6.

**Confidence:** 100%. This is a theorem independent of WKB or any approximation.

**Next action:** None. State as Theorem 2 in the paper.

---

### Statement 2.2 — Lambda-Scaling: Numerical Verification

**Claim:** At WKB-3rd order, the fractional variation of Re(ω)/sqrt(Λ) across Λ ∈ [0.01, 10.0] at fixed x is less than 3.4×10⁻⁵.

**Status:** EMPIRICAL

**Evidence:** WKB3 — EXP02 result. Expected from Statement 2.1 (WKB is consistent with the scaled equation).

**Confidence:** High as a numerical consistency check; the theorem (2.1) is stronger.

**Next action:** None. Cite as numerical sanity check in paper.

---

### Statement 2.3 — Q is Lambda-independent

**Claim:** Q = Re(ω)/|Im(ω)| is a function of x, l, n only, independent of Λ.

**Status:** PROVED

**Evidence:** Follows immediately from Statement 2.1 since Re(ω) and Im(ω) both scale as sqrt(Λ). Proof in `04b_exact_derivations.md`, Derivation 7.

**Confidence:** 100%.

**Next action:** None.

---

## Group 3: WKB Approximation Results

These results hold under WKB approximation only. They carry the WKB-level uncertainty and, for the current code, the tortoise coordinate error (see §4 of the Framework Audit).

---

### Statement 3.1 — WKB-1 Potential Formula

**Claim (WKB-1 approximation):**

```
ω² ≈ V₀ − i(n+½) sqrt(−V₀''_{r*}/2)

where V₀ = V(r_max) and V₀''_{r*} = f(r_max)² · d²V/dr²|_{r_max}
```

**Status:** EMPIRICAL (as an approximation to the exact QNMs)

**Evidence:** WKB1 — Schutz-Will (1985). The formula is standard; accuracy at l=2 is approximately 40-80% relative error vs. 3rd order.

**Coordinate note:** All WKB derivatives must be in the tortoise coordinate r*. At the maximum, d²V/dr*² = f(r_max)² · d²V/dr².

**Confidence:** The formula is correct as stated; the question is how well it approximates exact frequencies.

**Next action:** Use this formula for analytic estimates. Do not rely on current code Q values.

---

### Statement 3.2 — F_re is Approximately Monotone in x

**Claim:** Re(ω)/sqrt(Λ) at l=2, n=0, WKB-3rd is monotone decreasing in x from approximately 8.6 (x=0.1) to 1.7 (x=0.9).

**Status:** EMPIRICAL (WKB3, but F_re is relatively reliable since it depends primarily on V₀, not on tortoise derivatives)

**Evidence:** WKB3 — EXP02/EXP03 Table 4.2. The F_re values do not require tortoise-coordinate second derivatives at WKB-1 order.

**Confidence:** Moderate. The qualitative behavior (monotone decrease with x) is expected from the potential structure.

**Next action:** Confirm at WKB-1 order and at higher l.

---

### Statement 3.3 — Q_WKB1 is Approximately Constant in x

**Claim (WKB-1 with corrected tortoise derivatives):** The quality factor Q at WKB-1 order is approximately 5.07 ± 0.05 for l=2, n=0, x ∈ [0.1, 0.9].

**Status:** EMPIRICAL (WKB1, with correct tortoise derivatives applied analytically)

**Evidence:** WKB1 (corrected) — computed by applying d²V/dr*² = f(r_max)² · d²V/dr² to the WKB-1 formula. Table in `03b_mathematical_framework_revised.md` §4.2b.

**Confidence:** Moderate — the WKB-1 formula itself is only an approximation, but within WKB-1 the calculation is done correctly.

**Open question:** Does Q_WKB1 ≈ const persist at higher l? If Q_WKB1(x, l) → const as l → ∞, this would be a clean geometric result. If it is l-dependent, the l=2 value of 5.07 is a single data point.

**Next action:** Compute Q_WKB1 analytically at leading order in l (large l expansion). Compute at l=6,10 numerically with the corrected formula.

---

## Group 4: Previously Claimed Correspondences

---

### Statement 4.1 — Q-Carnot Correspondence

**Claim (previous):** Q ≈ 1.39 · η_C + 2.04, with Pearson r = 0.975.

**Status:** ARTIFACT

**Evidence (for artifact classification):** The Q values used in the fit were computed with d²V/dr² (physical r coordinate) rather than d²V/dr*² (tortoise coordinate). The corrected Q_WKB1 values are approximately constant at 5.07. A constant function correlated with a monotone function gives an artifact correlation: the slope 1.39 and intercept 2.04 are artifacts of the coordinate error, not physical properties. The physical interpretation in §5.2 of the original framework is therefore unconfirmed.

**What is not an artifact:** The existence of η_C(x) as a thermodynamic quantity is real. The near-constancy of Q_WKB1 is (if true) also real. The claim that Q and η_C are linearly related is what is unconfirmed.

**Current status:** Open question — is there ANY correlation between the correct Q and η_C? With Q_WKB1 ≈ const, the answer at WKB-1 is no (constant functions have zero correlation with anything). At higher WKB order or exact numerics, there may be a small x-dependence in Q that could correlate with η_C.

**Action for paper:** Do not state a Q-Carnot correspondence. The coordinate bug removes this claim. State the situation honestly: the initial finding was an artifact; the corrected WKB-1 gives Q ≈ const; whether a physical correspondence exists requires exact numerics.

---

### Statement 4.2 — Re(ω) − T_b Correlation

**Claim:** Re(ω_{l=2})/sqrt(Λ) and T_b/sqrt(Λ) are strongly correlated (Pearson r = 0.995) with approximate linear fit Re(ω)/sqrt(Λ) ≈ 15.86 · T_b/sqrt(Λ) + 1.14.

**Status:** POSSIBLY VALID — needs verification

**Evidence:** WKB3 (EXP03). Re(ω) is primarily determined by V₀ = V(r_max), which does not require a tortoise-coordinate derivative. Thus this correlation is less affected by the coordinate error than the Q correlation.

**Potential issues:**
1. Both Re(ω) and T_b are monotone functions of x. High Pearson r between two monotone functions of the same parameter does not require a mechanistic relationship — it is expected for any smooth monotone functions.
2. The WKB-3rd correction to Re(ω) does involve V₀'' terms, so there is some contamination from the coordinate error.
3. The coefficient 15.86 has not been derived analytically.

**Classification:** CONJECTURE — may be a trivially-expected correlation between two monotone functions of x, or may have geometric content.

**Next action:** Test at WKB-1 (where Re(ω) ≈ sqrt(V₀) is cleanest). Compute the Pearson r at l=6, 10 to see if the slope 15.86 changes. Attempt analytic derivation.

---

### Statement 4.3 — Eisenstein Structure Absent from Spectrum

**Claim:** The Eisenstein norm E(ω) = Re(ω)² + Re(ω)Im(ω) + Im(ω)² is not constant in x and is essentially equal to |ω|² (correlation r = 0.999997, slope ≈ 1.0 after small correction).

**Status:** EMPIRICAL — not affected by coordinate bug (it is a statement about numerical values of ω, not about Q or Im(ω) separately)

**Interpretation:** The Eisenstein quadratic form evaluated on QNM frequencies has no structural meaning — it simply tracks the L² norm. The Eisenstein structure of SdS is thermodynamic, not spectral.

**Confidence:** Moderate. The specific Pearson r value uses the wrong Q implicitly, but the conclusion (Eisenstein norm ≈ L² norm since |Re(ω)| >> |Im(ω)|) is transparent from the data — F_re >> |F_im| at l=2.

**Next action:** State as a clear negative result. No further computation needed for this claim.

---

### Statement 4.4 — x-to-1-x Symmetry Absent

**Claim:** The QNM frequency ω(x) is not symmetric under x → 1−x; i.e., ω(x) ≠ ω(1−x).

**Status:** EMPIRICAL (WKB3; not affected by coordinate bug since it is a statement about Re(ω) at two x values)

**Evidence:** EXP03 Test 1. The symmetry would require Re(ω(x)) = Re(ω(1−x)). From Table 4.2, Re(ω_{l=2})/sqrt(Λ) at x=0.3 is 3.157 and at x=0.7 is 1.789 — these differ by 77%. The asymmetry is large and not a numerical artifact.

**Confidence:** High for the qualitative conclusion (no symmetry). The exact degree of asymmetry is WKB-dependent.

**Next action:** State as a clear negative result in the paper.

---

## Group 5: Inverse Spectroscopy Results

---

### Statement 5.1 — Overtone Ratio G_l is Not Monotone (WKB-3rd)

**Claim:** G_l(x) = Re(ω_{l,1})/Re(ω_{l,0}) is not monotone in x at WKB-3rd for l=2. Its range [0.67, 3.54] also varies with Λ at WKB-3rd (by ~12%), indicating the WKB-3rd overtone is not computing the correct λ-independent ratio.

**Status:** EMPIRICAL (WKB3) with CAVEAT

**Evidence:** EXP04. The non-monotonicity could be a WKB artifact (the n=1 overtone at l=2 is outside the reliable regime of WKB-3rd).

**Consequence:** Inversion via G_l fails at WKB-3rd. Status at exact level: OPEN.

**Next action:** Test with exact QNM methods (Leaver) at l=2 or with WKB at higher l where n=1 is more reliable.

---

### Statement 5.2 — Cross-Mode Ratio S_{32} Not Useful for Inversion

**Claim:** S_{32}(x) = Re(ω_{3,0})/Re(ω_{2,0}) varies from 1.04 to 1.20 (range 0.16) and is not monotone, providing insufficient discriminating power for inverse spectroscopy.

**Status:** EMPIRICAL (WKB3) — more reliable than Statement 5.1 since both are n=0

**Evidence:** EXP04.

**Consequence:** Inversion via adjacent l fails. Larger l gaps are untested.

**Next action:** Test cross-mode ratio with l gap of 4 or larger (e.g., l=2 vs. l=6). If F_re^{6,0}(x)/F_re^{2,0}(x) is monotone and varies enough for inversion, it could serve as a spectroscopic diagnostic.

---

### Statement 5.3 — Root Cause of Inversion Failure

**Claim:** The reason inverse spectroscopy via frequency ratios fails is that all WKB frequencies at fixed n are governed by the same potential maximum r_max. As x varies, r_max shifts, but all F_re^{l,n}(x) track V₀(r_max, x) together. Their ratios are therefore insensitive to x.

**Status:** CONJECTURE (qualitative explanation, not a theorem)

**Evidence:** Analytic argument from the WKB formula. Partial support from EXP04.

**Next action:** Attempt to make this precise: compute d/dx [F_re^{l,n}/F_re^{l',n'}] at WKB-1 order and show it is small.

---

## Group 6: RDT Overtone Hierarchy

---

### Statement 6.1 — RDT Depth Does Not Correlate with QNM Overtones

**Claim:** The Recursive Depth Transform (RDT) depth of the overtone index n shows no physical correlation with Im(ω_n). The apparent correlation (Pearson r = −0.62 between RDT depth and Im(ω) residuals from a linear fit) is a statistical artifact.

**Status:** EMPIRICAL (artifact identified)

**Evidence:** EXP05. The residuals from a linear fit to Im(ω) vs. n grow with n (because the WKB-1 Im(ω_n) is not exactly linear in n for large n). RDT depth also grows with n. Both increasing-with-n quantities will have positive correlation without any physical relationship.

**Confidence:** High. The artifact mechanism is clear and quantified in EXP05.

**Next action:** State as a definitive negative result. No RDT structure in QNM overtones.

---

## Summary by Status

| Status | Count | Statements |
|---|---|---|
| PROVED | 7 | 1.1, 1.2, 1.3, 1.4, 1.5, 2.1, 2.3 |
| EMPIRICAL | 6 | 2.2, 3.1, 3.2, 3.3, 4.3, 4.4, 5.1, 5.2, 6.1 |
| CONJECTURE | 2 | 4.2, 5.3 |
| ARTIFACT | 1 | 4.1 (Q-Carnot) |
| OPEN | 1 | (state of G_l at exact level) |

---

## Priority Actions for the Paper

1. **PROVED results (1.1 through 2.3):** Write up cleanly with full proofs. These form the solid mathematical core.

2. **Statement 3.3 (Q_WKB1 ≈ const):** Compute analytically at large l. If Q_WKB1 → const(l) as l → ∞, state as a WKB theorem. This would replace the retracted Q-Carnot claim with a potentially more interesting result.

3. **Statement 4.2 (Re(ω) − T_b correlation):** Attempt analytic derivation. If it can be derived from the WKB formula, classify it as PROVED at WKB level. If not, state as a strong empirical observation with a caveated interpretation.

4. **All ARTIFACT and NEGATIVE results:** Document clearly and specifically. Negative results with identified mechanisms are a contribution.
