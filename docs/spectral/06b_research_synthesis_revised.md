# Research Synthesis — Revised

**Project:** Spectral Horizon Research
**Date:** April 2026
**Supersedes:** `00_project_overview.md` (primary synthesis document)
**Status:** Complete through the current phase of work; open questions identified

---

## What This Project Is

This project studied the quasinormal mode (QNM) spectrum of massless scalar perturbations in Schwarzschild-de Sitter (SdS) spacetime. The central question was: does the algebraic and thermodynamic structure of SdS — specifically the Eisenstein constraint, the entropy identity, and the Carnot efficiency of the two-horizon system — leave any imprint on the observable resonance spectrum?

The answer is: some structure does, some does not, and one initially-claimed correspondence was a computational artifact.

---

## Solid Mathematical Results

### The Eisenstein Constraint and Its Consequences

The two horizon radii in any sub-extremal SdS spacetime satisfy:

```
r_b² + r_b r_c + r_c² = 3/Λ    [exact]
```

This is an algebraic identity (Theorem 1 in the paper), derived from Vieta's formulas applied to the lapse function f(r). It implies the entropy identity:

```
S_Λ = S_b + S_c + sqrt(S_b S_c)    [exact]
```

where S_b = πr_b², S_c = πr_c², S_Λ = 3π/Λ.

These were known to this group prior to the project and form the structural background. They are presented as theorems, not new results.

### A New Exact Result: η_C(x) = (1−x²)/(1+2x)

Parametrizing the SdS state space by x = r_b/r_c ∈ (0,1), the Carnot efficiency of the two-horizon thermodynamic system has the exact closed form:

```
η_C(x) = (T_b − T_c) / T_b = (1 − x²) / (1 + 2x)
```

This follows from the exact Hawking temperature formulas:

```
T_b = (1+2x)(1−x) / (4π x r_Λ sqrt(x²+x+1))

T_c = (2+x)(1−x) / (4π r_Λ sqrt(x²+x+1))
```

which are derived in `04b_exact_derivations.md` by substituting the parametrization into f'(r) and using the Eisenstein constraint. The temperature ratio is:

```
T_c / T_b = x(2+x)/(1+2x)
```

giving η_C = 1 − T_c/T_b = (1−x²)/(1+2x) exactly.

This closed form is new in this parametrization. It is a simple, exact expression that connects the thermodynamic state of the two-horizon system to the single parameter x.

### The Lambda-Scaling Law

The QNM frequencies satisfy:

```
ω(x, l, n, Λ) = sqrt(Λ) · F(x, l, n)
```

exactly, where F is a dimensionless complex function independent of Λ. This is proved from dimensional analysis: when the wave equation is written in dimensionless coordinates scaled by r_c ∝ 1/sqrt(Λ), the cosmological constant drops out completely. The proof is in `04b_exact_derivations.md`, Derivation 6.

As a corollary, the quality factor Q = Re(ω)/|Im(ω)| is a function of x, l, n only — independent of Λ. This was confirmed numerically in EXP02 to fractional variation < 3.4×10⁻⁵ across Λ ∈ [0.01, 10.0].

---

## What Was Found Numerically (WKB Level)

### F_re(x) at l=2, n=0

The dimensionless real frequency F_re^{2,0}(x) = Re(ω)/sqrt(Λ) was computed at l=2, n=0 across x ∈ [0.1, 0.9]. It is monotone decreasing from 8.6 (x=0.1, small BH) to 1.7 (x=0.9, near Nariai). This value depends primarily on the potential maximum V₀ = V(r_max), which is well-approximated by WKB without tortoise-coordinate corrections.

The WKB-3rd convergence at l=2 is poor (44-79% correction from WKB-1 to WKB-3rd), so these values carry systematic errors. They are qualitatively correct (correct trend and order of magnitude) but not quantitatively reliable.

### Q_WKB1 ≈ 5.07 After Coordinate Correction

The quality factor at WKB-1 order, computed with the correct tortoise-coordinate second derivative V₀''_{r*} = f(r_max)² · V₀''_r, is approximately 5.07 ± 0.09 across x ∈ [0.1, 0.9] for l=2, n=0. This near-constancy is a potentially interesting property of the SdS potential at WKB-1 level. Whether it persists at higher l or with exact QNM methods remains to be determined.

---

## What Was Ruled Out (Negative Results)

### No x → 1-x Symmetry

The QNM spectrum has no reflection symmetry under x → 1−x. At x=0.1 vs x=0.9, Re(ω) differs by a factor of 5. This was speculated based on the symmetric form of the Eisenstein constraint, but the symmetry does not extend to the spectrum. The explanation is that x → 1−x does not correspond to any physical transformation of the SdS spacetime.

### No Eisenstein Structure in the Spectrum

The Eisenstein quadratic form E(ω) = Re(ω)² + Re(ω)Im(ω) + Im(ω)², evaluated on QNM frequencies, reduces to approximately |ω|² because |Im(ω)| << Re(ω). It is not a conserved or constrained quantity. The Eisenstein structure of the SdS state space is a property of the horizon geometry, not of the perturbation spectrum.

### No RDT Structure in Overtones

The Recursive Depth Transform depth of the overtone index n has no physical relationship to Im(ω_n). The apparent correlation r = −0.62 between RDT depth and Im(ω) residuals from a linear fit is an arithmetic artifact: both quantities increase with n, creating a spurious correlation. This result is definitively negative.

### No Q-Carnot Correspondence (Retracted)

The previously reported correlation Q ≈ 1.39 η_C + 2.04 with Pearson r = 0.975 was identified as a computational artifact. The Q values used in the correlation were computed with the WKB second derivative in the physical radial coordinate r rather than the tortoise coordinate r*. At a potential maximum, the correct relation is d²V/dr*² = f(r_max)² · d²V/dr², and the f(r_max)² factor was missing.

With the correct tortoise derivative, the WKB-1 quality factor is approximately constant at Q ≈ 5.07 across x, rather than ranging from 3.35 to 1.01. The monotone decrease of Q_code was driven by the monotone decrease of f(r_max) with x — a geometric property of the spacetime that was incorrectly embedded into the quality factor. Since η_C also decreases monotonically, the two quantities correlated spuriously.

The Q-Carnot correspondence does not survive the correction. Whether any physical spectral-thermodynamic correspondence exists in SdS requires exact QNM methods.

### No Reliable Inverse Spectroscopy at WKB-3rd

The ratio G_l = Re(ω_{l,1})/Re(ω_{l,0}) is non-monotone and Λ-dependent at WKB-3rd for l=2 (the n=1 overtone is outside the reliable regime of WKB-3rd at small l). The cross-mode ratio S_{32} = Re(ω_{3,0})/Re(ω_{2,0}) varies by only 15% across the full x range and is not monotone, providing insufficient discriminating power for inversion. These are WKB-level negative results; the exact situation for G_l is open.

---

## The Artifact and What It Teaches

The Q-Carnot artifact arose from a specific, identifiable error in the code. It was caught by analytical cross-checking: the corrected WKB-1 formula was computed directly and the results disagreed strongly with the code's values in a way that tracked f(r_max). This is a reminder that:

1. High Pearson r between two monotone functions of a common parameter is not evidence of a physical relationship.
2. WKB calculations require attention to which coordinate the derivatives are computed in. The tortoise coordinate is non-standard and easy to get wrong.
3. Checking a numerical result analytically (even approximately) is essential before claiming a physical correspondence.

The artifact detection is itself valuable: it identifies the specific error, quantifies its effect, and shows what the correct result is. This is reported in the paper as part of the scientific record.

---

## Open Questions

### Immediate (addressable with existing infrastructure)

**Q1: Q at higher l (WKB-1 corrected).** Is Q_WKB1(x, l)/sqrt(l(l+1)) approximately constant in x and l? If so, state as a WKB theorem. If not, document the l-dependence. Requires EXP06.

**Q2: Re(ω)-T_b correlation at multiple l.** Does the slope A_T(l) scale as sqrt(l(l+1))? If so, the correlation is a consequence of the l-scaling of Re(ω) and the structure of T_b(x), not a spectral-thermodynamic correspondence per se. Requires EXP07.

### Medium-term (requires Leaver implementation)

**Q3: Exact Q(x) at l=2.** The WKB-1 Q ≈ 5.07 is the leading approximation. The exact value may have more x-dependence. Whether any x-dependence correlates with η_C is the key physical question.

**Q4: G_l monotonicity at exact level.** If the exact G_l is monotone, inverse spectroscopy via overtone ratios is possible in principle.

### Long-term (speculative)

**Q5: Algebraic structure of the spectral curve.** The map x → F(x, l, n) ∈ ℂ traces a curve in the complex frequency plane. Does this curve have algebraic structure (elliptic, rational, etc.) related to the Eisenstein ellipse that organizes the SdS state space?

**Q6: RNdS extension.** Reissner-Nordström-de Sitter has three horizons and three parameters. Do the theorems and negative results extend? The η_C formula would involve three temperatures.

**Q7: Area quantization connection.** In the large-n limit, do SdS QNMs asymptote to combinations of T_b and T_c? This is the two-temperature analog of Hod's conjecture.

---

## Research Roadmap Summary

```
PROVED (paper-ready)
├── Eisenstein constraint (Theorem 1)
├── Entropy identity (Corollary 1)
├── Horizon parametrization by x (Theorem)
├── Hawking temperatures T_b, T_c (Theorem)
├── η_C(x) = (1-x²)/(1+2x) (Theorem — new result)
├── Lambda-scaling law ω = √Λ·F(x,l,n) (Theorem)
└── Q Λ-independence (Corollary)

EMPIRICAL — RELIABLE
├── F_re^{2,0}(x): monotone decrease, table in paper
└── Lambda-scaling confirmed numerically < 3.4×10⁻⁵

EMPIRICAL — WKB-1 ONLY
└── Q_WKB1 ≈ 5.07 ± 0.09 at l=2, n=0 (after tortoise correction)

NEGATIVE — STRONG
├── No x→1-x symmetry
├── No Eisenstein structure in spectrum
├── No RDT structure in overtones
└── No Q-Carnot correspondence (retracted as artifact)

NEGATIVE — CONDITIONAL
└── No G_l inversion at WKB-3rd (exact level open)

OPEN (require more work)
├── Q(x,l) scaling with l (EXP06)
├── Re(ω)-T_b correlation: content vs. monotonicity (EXP07)
├── Exact Q(x), G_l (Leaver, EXP09)
└── Long-term: RNdS, area quantization, spectral curve
```

---

## Significance Assessment

The project's mathematical core — the exact results on η_C(x), the Lambda-scaling law, and the entropy identity — is solid and would be of interest to researchers working on SdS thermodynamics and spectral geometry. The η_C(x) = (1−x²)/(1+2x) formula in particular is clean, exact, and not found in this form in the SdS literature we have reviewed.

The negative results are honest and mechanistically explained. Retracted findings, when properly documented, are a contribution to the literature — they save others from repeating the same errors.

The Q-Carnot finding, had it survived, would have been the most interesting result. It did not survive. The correct conclusion is that whether a physical spectral-thermodynamic correspondence exists in SdS is genuinely open, and exact methods are needed to answer it. This is an honest position that does not overstate or understate what is known.
