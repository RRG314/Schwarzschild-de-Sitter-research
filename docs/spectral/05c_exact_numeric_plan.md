# Exact Numerics Plan: Leaver Continued-Fraction Method for SdS

**Project:** Spectral Horizon Research
**Date:** April 2026
**Purpose:** Specify the implementation plan for computing exact SdS quasinormal mode frequencies using Leaver's continued-fraction method. This is needed to resolve the questions that WKB cannot answer reliably (particularly: exact Q values, overtone ratios, and the physical Q-Carnot question).

---

## 1. Motivation

The WKB approximation has two hard limitations in this project:

1. **Convergence at small l:** At l=2, n=0, the 3rd-order correction is 44-79%. Results are qualitative.
2. **Accuracy for overtones:** At l=2, n=1, the convergence criterion |Δ₂| < |ν_n|/2 fails for most x values. The n=1 frequency is not reliably computed.

These limitations directly affect the open questions:

- Is G_l(x) = Re(ω_{l,1})/Re(ω_{l,0}) monotone? (Requires reliable n=1 computation)
- What is the true Q(x) at l=2 (beyond WKB-1)?
- Does Q correlate with η_C at the exact level?

Leaver's method (1985) computes QNM frequencies to machine precision for any l and n.

---

## 2. Background: Leaver's Method

Leaver (1985) showed that the QNM problem for Schwarzschild can be written as a three-term recurrence relation in the coefficients of a power-series expansion of the wavefunction about the black-hole horizon. The QNM condition is that the recurrence has a minimal solution, which is equivalent to the continued-fraction expression for the recurrence being satisfied.

The result for Schwarzschild is a single continued-fraction equation in ω. For SdS, the situation is more complex: there are two horizons, and the boundary conditions at r_b (ingoing) and r_c (outgoing) must both be imposed. The standard approach (Moss & Norman 2002; Zhidenko 2004) leads to two separate continued-fraction equations that must be simultaneously satisfied.

---

## 3. The Leaver Recurrence for SdS

### 3.1 Setup

The SdS radial equation (after separating angular variables) is:

```
f(r) d/dr [f(r) dR/dr] + [ω²/f(r) − V_angular(r)] R = 0
```

where V_angular = l(l+1)/r² for scalar perturbations.

Introduce the variable z = (r − r_b)/(r_c − r_b) ∈ [0,1] mapping the static region to the unit interval, with z=0 at the BH horizon and z=1 at the cosmological horizon.

Near z=0 (r → r_b):

```
R ~ (r − r_b)^{-iω/(2κ_b)} = z^{−iω/(2κ_b (r_c−r_b))} ≡ z^{α_b}
```

where α_b = −iω/(4π T_b (r_c−r_b)) is the QNM ingoing power at r_b.

Near z=1 (r → r_c):

```
R ~ (r_c − r)^{iω/(2κ_c)} = (1−z)^{iω/(2κ_c (r_c−r_b))} ≡ (1−z)^{α_c}
```

where α_c = iω/(4π T_c (r_c−r_b)) is the outgoing power at r_c.

### 3.2 Ansatz

Write:

```
R(z) = z^{α_b} (1−z)^{α_c} (r_c/r − 1/z) · Σ_{n=0}^∞ a_n z^n
```

or a suitable modification based on the structure of f(r) around the two horizons. The details of the third root r_- (the negative root of the cubic) enter the ansatz.

The explicit SdS form of the Leaver ansatz is given in Moss & Norman (2002) and Zhidenko (2004). The key feature is that f(r) has three roots: r_b, r_c, r_- = −(r_b + r_c), and the ansatz must account for the behavior at all three.

A standard form (following Cardoso, Lemos, Yoshida 2004):

```
R(z) = e^{iω r*} (r/r_c)^{α_b} (r/r_-)^{γ} · Σ_{n=0}^∞ a_n (z_0)^n
```

where z_0 = (r − r_b)/(r − r_-) ∈ [0, r_c+r_b)/(r_c+r_b)] maps r_b → 0 and r_c to a finite value, while r_- → 1. The exact form depends on the choice of expansion point.

### 3.3 Three-Term Recurrence

Substituting the series ansatz into the radial equation yields a three-term recurrence for the coefficients a_n:

```
α_n a_{n+1} + β_n a_n + γ_n a_{n−1} = 0,    n = 1, 2, 3, ...
```

with initial condition a_0 = 1 and α_0 a_1 + β_0 a_0 = 0 (from the n=0 equation with a_{-1} = 0).

The coefficients α_n, β_n, γ_n are rational functions of n, ω, r_b, r_c, l (and implicitly Λ through r_b, r_c, M). Their explicit forms are:

In terms of the parameter ξ = r_-/(r_c − r_-) and the scaled frequency σ = ω/(r_c − r_b):

```
α_n = (n+1)(n + 1 − 2iσ r_c/κ_b)     [schematic; actual form is longer]

β_n = −[2n² + n(1 − 4iσ r_b/κ_b) + ...]

γ_n = (n − 2iσ r_-/κ_-)·...
```

(The exact coefficients require careful derivation from the specific ansatz. See Moss & Norman 2002 for the explicit SdS case.)

### 3.4 QNM Condition

The QNM boundary conditions require the series Σ a_n z^n to converge at BOTH z=0 (already built in by the ansatz) AND at z=z_c (the image of r_c under the expansion variable). The convergence condition at z=z_c leads to the continued-fraction equation:

```
β_0 − (α_0 γ_1)/(β_1 − (α_1 γ_2)/(β_2 − (α_2 γ_3)/(β_3 − ...))) = 0
```

This is an equation for ω (since all coefficients depend on ω). The QNM frequencies are the roots of this continued fraction.

---

## 4. Numerical Implementation

### 4.1 Truncation and Evaluation

In practice, the continued fraction is evaluated by backward recursion to some maximum level N:

```
CF_N = β_N

CF_n = β_n − α_n γ_{n+1} / CF_{n+1},    for n = N−1, N−2, ..., 0

QNM condition: CF_0 = 0
```

The result converges as N increases. For SdS with moderate x, N = 50−200 is typically sufficient for 10-digit precision in ω.

### 4.2 Root Finding

The QNM condition CF_0(ω) = 0 is solved numerically. Starting from a WKB estimate of ω, Newton's method (using numerical derivatives of CF_0) or Müller's method converges quickly.

The WKB values from the current code (even with the coordinate error) provide reasonable starting points for Newton's method, since Re(ω) is more accurately computed than Im(ω) by WKB.

### 4.3 Branch Issues

For overtones n ≥ 1, the WKB starting point is less reliable. Strategies:
- Use n=0 solution as a starting point and track the QNM as a function of some parameter to reach n=1
- Use Nollert's (1993) adaptive truncation method to improve convergence for higher overtones
- For l=2, n=1, start with a large-l WKB estimate (more reliable at l=6) and continue down in l

---

## 5. Validation Strategy

Before using Leaver results for scientific claims, validate against:

1. **Known Schwarzschild QNMs:** Take Λ → 0 (small Λ, fixed M) and compare to Leaver's original results for Schwarzschild. For l=2, n=0: ωM = 0.37367 − 0.08896i (Leaver 1985). The SdS result at small Λ should match to within the Λ correction.

2. **Lambda-scaling:** At fixed x, vary Λ. Confirm that ω/sqrt(Λ) is constant to within numerical precision (this is an exact theorem; any deviation indicates an implementation error).

3. **WKB comparison at high l:** At l=10, n=0, the exact Leaver result should agree with WKB-3rd (with corrected tortoise) to within ~3%. This validates both the Leaver implementation and the corrected WKB.

4. **Real-frequency check:** The Schwarzschild near-extremal QNMs have known analytic properties. For SdS near Nariai (x → 1), the QNM spectrum has been studied analytically (Cardoso, Natário, Schiappa 2004). Compare.

---

## 6. What Leaver Will Resolve

| Open question | How Leaver resolves it |
|---|---|
| Is G_l(x) monotone? | Compute exact ω_{l,0} and ω_{l,1}; form exact ratio; check monotonicity |
| What is exact Q(x, l=2)? | Direct: compute exact Im(ω) and Re(ω) |
| Does exact Q correlate with η_C? | Compute Q at many x values; correlate with η_C = (1−x²)/(1+2x) |
| How accurate is WKB-3rd at l=2? | Compare Leaver vs. WKB-3rd at each x |
| Is Q approximately constant in x (exact)? | Compute Q(x) directly; measure variation |
| Λ-independence check at exact level | Vary Λ at fixed x; confirm ω/sqrt(Λ) = const |

---

## 7. Implementation Timeline and Effort

**EXP09: Leaver baseline (estimate: 3-5 days of implementation + validation)**

Phase 9a (1 day): Implement the three-term recurrence coefficients for SdS. Key references: Moss & Norman (2002), Cardoso et al. (2004). Test against Schwarzschild limit.

Phase 9b (1 day): Implement backward-recursion continued-fraction evaluation with Newton's method for root finding. Test Lambda-scaling numerically to machine precision.

Phase 9c (1 day): Validate against WKB at high l (l=10), against near-Nariai analytic results, and against published SdS tables in the literature.

Phase 9d (1-2 days): Run the full suite — compute Q(x, l, n) for l=2,6,10 and n=0,1 at x ∈ {0.1,...,0.9}. Compute G_l(x) and its monotonicity. Test correlation of exact Q with η_C.

**Expected output:**
- Table: exact Q(x) for l=2, n=0 (primary comparison to WKB-1 corrected result)
- Table: exact G_l(x) for l=2 and l=6 (monotonicity test)
- Correlation: Pearson r between exact Q and η_C
- Plot: exact Q(x) vs. η_C(x) with best-fit line and residuals

---

## 8. Key References for Implementation

1. **Leaver (1985):** E. W. Leaver, *Proc. R. Soc. A* **402**, 285 — original continued-fraction method for Schwarzschild
2. **Moss & Norman (2002):** I. G. Moss and J. P. Norman, *Class. Quant. Grav.* **19**, 2323 — SdS adaptation of Leaver method (contains explicit recurrence coefficients)
3. **Zhidenko (2004):** A. Zhidenko, *Class. Quant. Grav.* **21**, 273 — numerical tables for SdS QNMs using continued fractions
4. **Cardoso, Lemos, Yoshida (2004):** V. Cardoso, J. P. S. Lemos, S. Yoshida, *Phys. Rev. D* **69**, 044004 — near-extremal SdS QNMs, useful for validation near Nariai
5. **Nollert (1993):** H.-P. Nollert, *Phys. Rev. D* **47**, 5253 — improved convergence for Leaver method at high overtone numbers

---

## 9. Alternative: Numerical Integration

If implementing Leaver proves difficult, an alternative is direct numerical integration of the Regge-Wheeler equation in the tortoise coordinate:

1. Specify boundary conditions: u ~ e^{−iωr*} as r* → −∞ (near r_b) and u ~ e^{+iωr*} as r* → +∞ (near r_c)
2. Integrate inward from r_c and outward from r_b and match at some middle point r_mid
3. The QNM condition is that the Wronskian of the two solutions vanishes
4. Search for ω using Newton's method

This requires integrating complex-valued ODEs and dealing with exponentially growing/decaying modes. It is robust but less elegant than the Leaver continued fraction. Typical precision: 6-8 digits with double precision.

For validation purposes at the current project stage, either method is acceptable.
