# Negative Results — Formalized

**Project:** Spectral Horizon Research
**Date:** April 2026
**Purpose:** State each negative result as a precise no-go proposition, explain what was tested, what the result showed, and what remains open. Negative results are not failures — they close dead ends and define the boundary of what the evidence supports.

---

## Proposition N1 — No Reflection Symmetry in the QNM Spectrum

**Statement:** The QNM spectrum of the SdS scalar field does NOT possess the symmetry:

```
ω(x, l, n, Λ) = ω(1−x, l, n, Λ)
```

**Tested:** EXP03, Test 1. At l=2, n=0, Λ=1, the ratio Re(ω(x))/Re(ω(1−x)) was computed for x ∈ {0.1, 0.2, 0.3, 0.4}. At x=0.3 vs. x=0.7: Re(ω) = 3.157 vs. 1.789, a ratio of 1.77. At x=0.1 vs. x=0.9: Re(ω) = 8.641 vs. 1.680, a ratio of 5.14.

**Why tested:** The Eisenstein quadratic form Q(a,b) = a²+ab+b² satisfies Q(r_b, r_c) = Q(r_c, r_b) (symmetric in the two entries). One might speculate that this symmetry of the constraint implies a symmetry of physical observables. It does not.

**Why it fails:** The spacetime x = r_b/r_c is physically distinct from 1−x = (r_c − r_b)/r_c (which is not the same as swapping r_b and r_c). Swapping the two horizons (x → 1/x, or equivalently exchanging r_b and r_c) would map one spacetime to another, but x → 1−x is not the same transformation and has no physical interpretation in terms of the SdS parameter space.

**What remains open:** Whether ω(x) has the inversion symmetry ω(x) = ω(1/x) (after accounting for scaling by r_c). This would correspond to exchanging the two horizons. It is a different and more physically motivated question.

**Strength of result:** STRONG. The disagreement is a factor of 5 at x=0.1, far outside any WKB error. The absence of this symmetry is established.

---

## Proposition N2 — No Eisenstein Structure in the QNM Spectrum

**Statement:** The Eisenstein quadratic form E(ω) = Re(ω)² + Re(ω)Im(ω) + Im(ω)² evaluated on QNM frequencies is NOT constant in x, and is NOT a meaningful invariant of the SdS QNM spectrum separate from |ω|².

**Tested:** EXP03, Test 3. The quantity E(ω) was computed and found to correlate with |ω|² = Re(ω)²+Im(ω)² at Pearson r = 0.999997.

**Why this correlation is trivial:** E(ω) = |ω|² + Re(ω)Im(ω). Since |Re(ω)| >> |Im(ω)| across the parameter range (Q ≈ 2−5, meaning Re(ω) ≈ 2−5 times larger than |Im(ω)|), the cross term Re(ω)Im(ω) is small compared to |ω|² ≈ Re(ω)². Therefore E(ω) ≈ |ω|² to within a few percent. The r = 0.999997 correlation simply reflects this near-equality.

**Interpretation:** The Eisenstein quadratic form carries geometric meaning in the state space (r_b, r_c) — specifically, the constraint r_b²+r_br_c+r_c² = 3/Λ is the zero locus of the Eisenstein form. But evaluating the same algebraic form on (Re(ω), Im(ω)) does not produce a conserved or constrained quantity. The QNM spectrum is not organized by the Eisenstein form.

**Strength of result:** STRONG — but note the result would be slightly different with correct tortoise derivatives (Im(ω) would change, altering the cross-term). With correct WKB-1 Q ≈ 5, |Im(ω)| ≈ Re(ω)/5, and the cross-term contributes about 20% to E(ω). The conclusion (E is not constant in x, and does not provide a spectral invariant distinct from |ω|²) still holds.

**What remains open:** Whether there exists ANY quadratic form in (Re(ω), Im(ω)) that is conserved along x-slices of the SdS state space. This is a more general question not tested here.

---

## Proposition N3 — No Useful Inversion via Overtone Ratio (at WKB-3rd)

**Statement:** At WKB-3rd order, the ratio G_l(x) = Re(ω_{l,1})/Re(ω_{l,0}) is NOT monotone in x for l=2, and is NOT Λ-independent (fractional variation ~12% across Λ ∈ [0.05, 10]).

**Consequence:** G_l cannot be used to invert x = r_b/r_c from an observed frequency ratio at WKB-3rd accuracy.

**Tested:** EXP04, build_inversion_maps and test_lambda_independence_of_inversion.

**Why the Λ-dependence is a WKB artifact:** Statement 2.1 (proved exactly) guarantees that G_l = Re(ω_{l,1})/Re(ω_{l,0}) is Λ-independent exactly, since both scale as sqrt(Λ). The observed 12% variation is therefore an error of the WKB-3rd approximation for the n=1 overtone, where the convergence criterion |Δ₂| < |ν_n|/2 frequently fails.

**What this means for the paper:** The WKB-3rd failure tells us about WKB inaccuracy at small l and n=1. It does not rule out G_l as an inversion tool in principle; it rules it out for the specific approximation used.

**Remaining question:** Is G_l monotone in x for the exact QNM frequencies? If yes, the inversion is possible with better numerics. If no, the inversion fails for a physical reason, not a numerical one. This requires Leaver's continued-fraction method (see `05c_exact_numeric_plan.md`).

**Strength of result:** CONDITIONAL. The negative conclusion holds at WKB-3rd. The exact result is open.

---

## Proposition N4 — No Useful Inversion via Cross-Mode Ratio (Adjacent l)

**Statement:** The ratio S_{32}(x) = Re(ω_{l=3,n=0})/Re(ω_{l=2,n=0}) varies only from 1.04 to 1.20 across x ∈ [0.1, 0.9], and is not monotone. This provides insufficient discriminating power for inverse spectroscopy.

**Tested:** EXP04, build_inversion_maps.

**Why it fails:** Both F_re^{3,0}(x) and F_re^{2,0}(x) decrease monotonically with x. Their ratio is close to constant because both are governed by the same potential maximum r_max and both shift together as x varies. The ratio of two nearly-identical monotone functions is nearly flat.

**What might work instead:** A cross-mode ratio using a larger l gap (e.g., S_{10,2} = Re(ω_{10,0})/Re(ω_{2,0})). At large l, F_re^{l,0}(x) ≈ l · h(x) for some function h(x), making the ratio approximately l-ratio-independent — still uninformative. Alternatively, comparing modes that probe different geometric structures (e.g., photon sphere modes vs. near-horizon modes) might provide x-sensitive ratios.

**Strength of result:** STRONG for adjacent l, CONDITIONAL for larger gaps.

---

## Proposition N5 — No RDT Structure in QNM Overtones

**Statement:** The Recursive Depth Transform (RDT) depth of the overtone index n has no physical relationship to the QNM imaginary frequencies. The apparent Pearson r = −0.62 correlation between RDT depth and Im(ω_n) residuals from a linear fit is a statistical artifact.

**Tested:** EXP05.

**Why the correlation is an artifact:**

1. At WKB-1, Im(ω_n) = Im(sqrt(V₀ − i(n+½)C)) where C = sqrt(−V₀''/2). This is not exactly linear in n (it involves a square root). For large n, Im(ω_n) deviates from the linear trend in a specific way: it becomes more negative than the linear fit predicts, with deviation growing as n increases.

2. RDT depth of n also grows monotonically with n (though not uniformly).

3. Therefore: the correlation between RDT depth and Im(ω_n) residuals is a correlation between two quantities that both increase with n. This is an arithmetic artifact of using n as a common independent variable, not evidence of any structural relationship.

**Why RDT has no physical relevance here:** The RDT depth of an integer n is a property of the number n in the integers — it counts something about the binary or recursive structure of n. The overtone index n in QNM physics is an ordering label for eigenvalues. There is no physical mechanism by which the number-theoretic properties of the integer n could influence the frequency of the corresponding QNM. The correlation would be equally present in any series where the residuals grow with n.

**Strength of result:** STRONG. The artifact mechanism is identified and quantified. The conclusion (RDT has no role in QNM physics) is definitive given the EXP05 analysis.

---

## Proposition N6 — Q-Carnot Correspondence is Not Confirmed

**Statement:** The previously reported correlation Q ≈ 1.39 η_C + 2.04 (Pearson r = 0.975) is NOT a confirmed physical result. It was computed using an incorrect coordinate system for the WKB second derivative.

**What was wrong:** The code computed V₀'' = d²V/dr²|_{r_max} in physical r coordinates. The WKB formula requires V₀'' = d²V/dr*²|_{r_max} in tortoise coordinates. The correct value is d²V/dr*² = f(r_max)² · d²V/dr² (Derivation 8 in `04b_exact_derivations.md`).

**What the corrected calculation shows:** With the correct tortoise-coordinate second derivative, the WKB-1 quality factor Q_WKB1(x) is approximately 5.07 ± 0.05 across x ∈ [0.1, 0.9] for l=2, n=0. This near-constancy is consistent with Q being x-independent at WKB-1 (which would be a clean positive result about the SdS geometry, if confirmed at higher l and exact methods).

**Why the artifact arose:** Q_code = Q_WKB1,incorrect decreased monotonically from 3.35 (x=0.1) to 1.01 (x=0.9) because f(r_max)² decreased over that range. η_C also decreases monotonically. Two decreasing functions of the same parameter will have a high Pearson correlation without any causal relationship.

**What remains open:**
1. Is Q_corrected truly constant at WKB-1, or is there a small x-dependence that might (or might not) correlate with η_C?
2. Does Q with exact QNM frequencies (Leaver method) have any x-dependence, and does it correlate with η_C?
3. The Re(ω)−T_b correlation (Proposition N7) is a separate question and may survive correction.

**For the paper:** This result must be retracted. The paper should state plainly that the initially observed Q-Carnot correlation was identified as a coordinate artifact, and that the correct WKB-1 Q is nearly constant. Whether a physical spectral-thermodynamic correspondence exists remains an open question requiring exact numerics.

**Strength of negative result:** STRONG — the artifact mechanism is rigorously identified. The absence of a Q-Carnot correlation at WKB-1 with correct derivatives is confirmed numerically.

---

## Proposition N7 — Re(ω)-T_b Correlation: Status Uncertain

**Statement:** The correlation Re(ω_{l=2})/sqrt(Λ) ≈ 15.86 · T_b/sqrt(Λ) + 1.14 (Pearson r = 0.995) is not directly invalidated by the coordinate bug but requires interpretation.

**This is not a fully negative result.** It is included here because the high Pearson r may be misleading:

Both Re(ω)/sqrt(Λ) and T_b/sqrt(Λ) are smooth, monotone-decreasing functions of x for x ∈ (0,1). Two smooth monotone functions on a compact interval will typically have Pearson r > 0.99 even without any mechanistic relationship — a Pearson r of 0.995 is not surprising for two monotone functions of the same parameter.

To determine whether the Re(ω)−T_b relationship has physical content, one needs:

1. Evidence that the relationship is specifically linear, not just monotone (i.e., that the residuals from the linear fit are small compared to those from other monotone functions)
2. A derivation of the coefficient 15.86 from the WKB formula
3. Verification at multiple l values (if the slope depends on l, the relationship has a different character than if it is l-universal)

**At present:** CONJECTURE, not PROVED. Do not claim in the paper as a correspondence; present as an observation requiring analytic investigation.

---

## Summary of Negative Results

| Proposition | What was ruled out | Strength | What remains open |
|---|---|---|---|
| N1 | x → 1-x symmetry | Strong | x → 1/x symmetry not tested |
| N2 | Eisenstein form as spectral invariant | Strong | Other quadratic forms not tested |
| N3 | G_l inversion at WKB-3rd | Conditional | Exact G_l monotonicity open |
| N4 | Cross-mode ratio for adjacent l | Strong for adjacent l | Large l gaps not tested |
| N5 | RDT structure in overtones | Strong | Definitively closed |
| N6 | Q-Carnot correspondence | Strong | Q x-dependence at exact level open |
| N7 | Re(ω)-T_b as a "correspondence" | Moderate | May survive as approximate relation |

---

## Value of These Results for the Paper

Negative results that identify the mechanism of failure are scientifically more useful than vague positive claims. Each proposition here specifies:

- Exactly what was tested
- Why it fails (or is uncertain)
- What is ruled out definitively vs. conditionally
- What the natural follow-up test is

This structure is appropriate for a rigorous paper and avoids the trap of overfitting patterns in exploratory data.
