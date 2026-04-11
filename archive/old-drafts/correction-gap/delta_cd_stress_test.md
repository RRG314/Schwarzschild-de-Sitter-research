# Stress Test: Does Δ_cd = π r_b r_c Represent Anything Beyond Algebra?

**Document type:** Mathematical stress test and critical analysis
**Goal:** Determine whether the entropy deficit in Schwarzschild–de Sitter has nontrivial physical content, or collapses into known algebra
**Method:** Derive new consequences, attempt to break the idea, report without advocacy

---

## PART 1: Validation of Base Mathematics

### 1.1 The SdS Horizon Equation

In natural units G = ħ = c = k_B = 1, the Schwarzschild–de Sitter blackening function is:

    f(r) = 1 - 2M/r - Λ r² / 3

Setting f(r) = 0 and multiplying by r:

    r - 2M - Λ r³ / 3 = 0

Multiplying by -3/Λ:

    r³ - (3/Λ) r + (6M/Λ) = 0                        ... (C)

This is a monic depressed cubic p(r) = r³ + p r + q with p = -3/Λ and q = +6M/Λ.

**Discriminant:** Δ_disc = -4p³ - 27q² = 108/Λ³ - 972M²/Λ² = (108/Λ³)(1 - 9ΛM²).

For 0 < M < M_N := 1/(3√Λ), the discriminant is positive and (C) has three distinct real roots. Call them r_- < 0 < r_b < r_c. The regime M > M_N has no SdS spacetime; at M = M_N the two positive roots coincide (Nariai limit).

**Coordinate invariance:** r_b and r_c are areal radii defined by the bifurcation spheres of each Killing horizon. The areas A_b = 4πr_b² and A_c = 4πr_c² are intrinsic geometric invariants of those surfaces. All subsequent entropy computations rest on these geometric areas, not on the static coordinate representation of f(r). The result is fully coordinate-invariant.

### 1.2 Vieta's Formulas

For the cubic r³ + 0·r² - (3/Λ)r + (6M/Λ) = 0 with roots r_-, r_b, r_c:

    r_- + r_b + r_c = 0                              ... (V1)
    r_- r_b + r_- r_c + r_b r_c = -3/Λ             ... (V2)
    r_- r_b r_c = -6M/Λ                              ... (V3)

### 1.3 Derivation of the Quadratic Identity

From (V1): r_- = -(r_b + r_c). Substitute into (V2):

    -(r_b + r_c) r_b - (r_b + r_c) r_c + r_b r_c = -3/Λ

    -(r_b² + r_b r_c) - (r_b r_c + r_c²) + r_b r_c = -3/Λ

    -r_b² - r_b r_c - r_c² = -3/Λ

    r_b² + r_b r_c + r_c² = 3/Λ                     ... (**)

This is exact. No approximation. It holds for all (M, Λ) with M ∈ (0, M_N).

### 1.4 The Entropy Identity

For pure de Sitter (M = 0): f(r) = 1 - Λr²/3 = 0 gives r_dS = √(3/Λ), so:

    S_dS = π r_dS² = 3π/Λ

Multiply (**) by π:

    π r_b² + π r_b r_c + π r_c² = 3π/Λ

Recognize S_b = π r_b², S_c = π r_c², S_dS = 3π/Λ:

    S_b + π r_b r_c + S_c = S_dS

    S_dS - (S_b + S_c) = π r_b r_c                  ... (***)

**No hidden assumptions.** The derivation uses only the Bekenstein–Hawking formula S = A/4 and Vieta's formulas on the SdS cubic. The pure de Sitter entropy S_dS appears because at M = 0 the single remaining physical root of (C) is r_dS.

Define: Δ_cd := π r_b r_c. The identity (***) is established.

---

## PART 2: Attempt to Derive Nontrivial Consequences

### 2.1 Reformulation: The Deficit is the Geometric Mean of the Two Entropies

**Claim:** Δ_cd = √(S_b · S_c).

**Derivation:**

    √(S_b · S_c) = √(π r_b² · π r_c²) = π r_b r_c = Δ_cd   □

This is immediate from the definitions, but its consequence is nontrivial as a statement about the entropy identity. The identity (***) can be written in a form that involves no horizon radii explicitly:

    S_dS = S_b + S_c + √(S_b S_c)                    ... (GM)

**What this means:** The pure de Sitter entropy is the sum of the two horizon entropies plus their geometric mean. This relation is quadratic in √S_b and √S_c. Specifically, defining x = √S_b and y = √S_c:

    S_dS = x² + xy + y²                              ... (GM')

This is the norm form N(x + y ω) = x² + xy + y² where ω = e^{2πi/3} is a primitive cube root of unity. Equivalently, x² + xy + y² = 0 defines the ring of Eisenstein integers Z[ω]. The entropy relation is the statement that N(√S_b + ω√S_c) = S_dS in this norm.

**Is this physically meaningful?** The mathematical structure is an Eisenstein norm. There is no known physical reason why SdS horizon entropies should be related to Eisenstein norms. This observation is algebraically clean but physically inert unless a deeper connection to the complex structure of the problem is identified. Setting it aside.

**What is useful about (GM):** The reformulation in terms of entropies alone (no explicit radii or Λ) means that any researcher who knows S_b, S_c, and S_dS can immediately read off Δ_cd without solving the cubic. It also makes the bound in Section 2.2 transparent.

### 2.2 An Exact Entropy Inequality with Sharp Bounds

**Claim:**

    0 ≤ Δ_cd ≤ S_dS / 3

with equality Δ_cd = 0 iff M = 0, and equality Δ_cd = S_dS/3 iff M = M_N (Nariai).

**Derivation of the upper bound.**

By the AM–GM inequality applied to S_b and S_c (both positive):

    (S_b + S_c) / 2 ≥ √(S_b S_c) = Δ_cd

Therefore S_b + S_c ≥ 2 Δ_cd. Substituting S_b + S_c = S_dS - Δ_cd:

    S_dS - Δ_cd ≥ 2 Δ_cd
    S_dS ≥ 3 Δ_cd
    Δ_cd ≤ S_dS / 3                                  □

**Sharpness at Nariai:** At the Nariai limit, r_b = r_c = 1/√Λ (derived in Part 4), so S_b = S_c = π/Λ.

    √(S_b S_c) = π/Λ = (1/3)(3π/Λ) = S_dS/3   ✓

AM–GM is saturated when S_b = S_c, which occurs exactly at Nariai. The bound is sharp.

**Derivation of the lower bound.** Δ_cd = π r_b r_c > 0 for M > 0 (both radii are positive). In the limit M → 0, r_b → 0 and Δ_cd → 0. The bound is sharp.

**Compact form.** For all M ∈ [0, M_N]:

    0 ≤ Δ_cd ≤ S_dS / 3

    0 ≤ S_b + S_c ≤ S_dS  (from Δ_cd ≥ 0)

    (2/3) S_dS ≤ S_b + S_c ≤ S_dS  (from Δ_cd ≤ S_dS/3 and S_b + S_c = S_dS - Δ_cd)

The last line is a clean result: the total horizon entropy in any SdS spacetime is at least two-thirds of the pure de Sitter entropy. Equality holds at the Nariai limit.

**Assessment:** This inequality and its sharpness are exact and follow from AM–GM plus the Vieta identity. Whether this has appeared explicitly in the SdS literature is unclear; the result is simple enough that it may be known but not prominently stated.

### 2.3 Euclidean Action and the Pair Creation Instanton

**Claim:** Δ_cd is the Euclidean tunneling exponent for black hole pair creation in de Sitter.

**Setup.** In the semiclassical (saddle-point) approximation to the Hartle–Hawking no-boundary path integral, the probability of nucleating a Schwarzschild–de Sitter configuration from pure de Sitter background is:

    P(M) ~ exp(-B)

where B = ΔI_E is the difference in on-shell Euclidean actions between the SdS instanton and the de Sitter background.

**Euclidean action at saddle points.** In the Gibbons–Hawking formalism, the on-shell Euclidean action for a solution with total horizon entropy S_total is:

    I_E = -S_total

(at the appropriate saddle point). This is the standard result for stationary black hole thermodynamics: the free energy I_E = βF = βE - S, and at the saddle point the dominant contribution gives I_E = -S at the extremum.

For pure de Sitter: I_E[dS] = -S_dS.

For the SdS configuration: I_E[SdS] = -(S_b + S_c).

**Tunneling exponent:**

    B = ΔI_E = I_E[SdS] - I_E[dS] = -(S_b + S_c) - (-S_dS) = S_dS - S_b - S_c = Δ_cd

Therefore:

    P(M) ~ exp(-Δ_cd) = exp(-π r_b r_c)             ... (PC)

**Verification at Nariai.** The Nariai instanton (dominant nucleation channel -- Ginsparg–Perry 1983) has:

    B_Nariai = Δ_cd|_Nariai = π/Λ

    P_Nariai ~ exp(-π/Λ)

This matches the Bousso–Hawking (1996) formula for the nucleation rate of the largest possible black hole (Nariai) in de Sitter.

**Monotonicity.** Since Δ_cd is monotonically increasing in M (shown in Part 1, derivative section), smaller black holes nucleate with higher probability than larger ones. The maximum probability (approaching 1) occurs as M → 0, which is the trivial limit of no nucleation.

**Is this new?** No. The formula P ~ exp(S_b + S_c - S_dS) appears in Ginsparg–Perry (1983), Bousso–Hawking (1996, 1998), and subsequent literature on pair creation. What may be mildly useful: identifying the object that controls pair creation as Δ_cd = √(S_b S_c), giving P ~ exp(-√(S_b S_c)). This makes the parametric dependence on the two horizon entropies explicit and symmetric.

**Conclusion from 2.3:** Δ_cd has an established physical meaning in the semiclassical path integral. It is the suppression exponent for black hole pair creation in de Sitter. This is known, but the clean form P ~ exp(-√(S_b S_c)) has not, to our knowledge, been stated this way.

### 2.4 Integral Representation from the Combined First Law

**Derivation.** From the individual horizon first laws (derived by implicit differentiation of f(r_b) = f(r_c) = 0 with respect to M, as derived in the companion document):

    dS_b / dM = 1/T_b > 0
    dS_c / dM = -1/T_c < 0

Differentiating Δ_cd = S_dS - S_b - S_c at fixed Λ (so dS_dS/dM = 0):

    dΔ_cd / dM = 1/T_c - 1/T_b                       ... (D)

Since Δ_cd(0) = 0 (pure de Sitter has no mass and zero deficit), integrating from 0 to M:

    Δ_cd(M) = ∫₀ᴹ [1/T_c(m) - 1/T_b(m)] dm         ... (I)

**Physical reading.** In the typical regime T_b > T_c, the integrand 1/T_c - 1/T_b > 0, so Δ_cd accumulates monotonically. The deficit at any mass M equals the cumulative integral of the inverse-temperature gap between the cosmological (cold) and black hole (hot) sectors.

This is an exact integral identity, not an approximation. It follows from combining (D) with the boundary condition Δ_cd(0) = 0.

**Connection to irreversibility.** The integrand 1/T_c - 1/T_b is the entropy cost per unit mass added. In classical nonequilibrium thermodynamics, entropy production in an irreversible process between systems at temperatures T_h (hot) and T_c (cold) is proportional to (1/T_c - 1/T_h) per unit heat transferred. The integral (I) is the analog of cumulative entropy production as mass is incrementally "deposited" from the de Sitter background into the black hole sector.

**Is this new?** The identity (D) has been noted (implicitly or explicitly) in treatments of SdS first laws. The integral form (I) with the explicit boundary condition and physical interpretation as cumulative irreversibility may not be standard, but it follows immediately from (D). It is not a major result, but it is a clean restatement.

### 2.5 Attempted Connection to Entropy Bounds

**The Bousso covariant entropy bound.** For a light sheet L bounded by a surface of area A, the bound states S(L) ≤ A/4. In the SdS static patch:
- The cosmological horizon bounds the observable region from outside. Its area A_c = 4π r_c² bounds the entropy observable by a static observer.
- The black hole contributes entropy S_b = π r_b² inside the causal patch.

The Bousso bound applied to the inward-directed light sheet from r_c gives S_b ≤ S_c. This is a separate statement from Δ_cd ≥ 0, which follows from S_b + S_c ≤ S_dS.

**Is Δ_cd a Bousso bound saturation measure?** No. The Bousso bound compares entropy on a light sheet to its bounding area. Δ_cd compares horizon entropies to pure de Sitter entropy. These are related but distinct statements. No clean reformulation of Δ_cd as a Bousso bound quantity is found.

### 2.6 Attempted Connection to Entanglement Entropy or Mutual Information

**Setup.** The SdS static patch is bounded by the two horizons. In the semiclassical picture, the black hole interior and the cosmological exterior are causally disconnected from the static region. If the global quantum state on the full SdS geometry is pure, then the entropy of any subregion should be interpretable as entanglement entropy between complementary regions.

**Attempt.** Let H_b = degrees of freedom of the black hole sector, H_c = degrees of freedom of the cosmological sector, H_int = interior + exterior. For a pure global state:

    S(H_b) + S(H_c) = 2 S_{entanglement}   (if BH and cosmological are maximally entangled)

In the thermofield double construction (for black holes): S_{BH} = S_{entanglement}. For de Sitter, proposals exist (Anninos-Denef-Harlow, 2012) but are not established.

If Δ_cd = S_dS - S_b - S_c were interpretable as mutual information I(H_b; H_c) = S_b + S_c - S(H_b ∪ H_c), this would require S(H_b ∪ H_c) = 2(S_b + S_c) - S_dS or some similar formula. There is no known derivation of such a relation.

**Result: No rigorous connection to mutual information or entanglement entropy found.** Without a specific microscopic model of the SdS Hilbert space, any such identification is speculative. The geometric identity Δ_cd = π r_b r_c does not, by itself, imply any statement about quantum entanglement. Setting this connection aside as unestablished.

---

## PART 3: Attempting to Break the Idea

### 3.1 Is Δ_cd Just a Monotone Function of M?

**Test:** If Δ_cd = h(M) for some simple function h, it adds no information beyond M.

Define s = r_b + r_c and p = r_b r_c. From the Vieta relations:

    s² - p = 3/Λ           ... (from V1 and V2)
    s · p = 6M/Λ           ... (from V1 and V3, since r_- = -s)

Eliminating p: p = s² - 3/Λ, so:

    s(s² - 3/Λ) = 6M/Λ
    s³ - 3s/Λ - 6M/Λ = 0    ... (C_s)

This is a cubic in s. Solving it for general M requires solving a cubic; s(M,Λ) is a transcendental function of M at fixed Λ.

Then p = r_b r_c = s² - 3/Λ, giving Δ_cd = π(s² - 3/Λ).

**Is Δ_cd a simple monotone function of M?** Δ_cd = Δ_cd(M, Λ) depends on both parameters through the transcendental cubic (C_s). It is NOT a simple function of M alone: at fixed M, different values of Λ give different Δ_cd. At fixed Λ, it is a monotone function of M (shown by dΔ_cd/dM = 1/T_c - 1/T_b > 0 in the typical regime), but the function is transcendental, not polynomial.

**Verdict:** Δ_cd is not trivially equivalent to M. It encodes both M and Λ in a nontrivial way. However, at fixed Λ it is monotone in M and contains the same information as M. Knowing Δ_cd at fixed Λ uniquely determines M (within the range [0, M_N]). So at fixed Λ, Δ_cd is a reparametrization of M, not an independent quantity.

**Partial failure:** At fixed Λ, Δ_cd is informationally equivalent to M. This weakens its status as an independent quantity, though it may still be a more natural parametrization for some purposes (e.g., pair creation rates).

### 3.2 Coordinate Dependence Test

The horizon radii r_b, r_c are areal radii. The area of a 2-sphere at radius r in the SdS geometry is 4πr², and this is an intrinsic geometric quantity of the sphere, not a coordinate artifact. The entropy S = A/4 is the Bekenstein–Hawking entropy, which is a Noether charge in Einstein gravity and is defined independently of coordinates as a property of the bifurcation surface.

Δ_cd = π r_b r_c = √(S_b S_c) is a function of two horizon entropies. Both are coordinate-invariant by the Wald entropy theorem (for Einstein gravity: Wald entropy = A/4, which is the area of the bifurcation surface divided by 4G). Therefore:

**Δ_cd is fully coordinate-invariant.** This test does not break the idea.

### 3.3 Test: Different Thermodynamic Conventions for the Cosmological Horizon

**Issue:** Some authors dispute that the cosmological horizon has a thermodynamic entropy in the same sense as a black hole. Arguments: (a) the cosmological horizon is observer-dependent; (b) there is no canonical notion of "inside" vs. "outside"; (c) de Sitter space has no conserved energy (no timelike Killing vector globally), making the first law of the cosmological horizon ambiguous.

If S_c is NOT a genuine thermodynamic entropy but merely a geometric area/4, then Δ_cd is NOT an entropy deficit but merely a geometric quantity. The identity (***) holds in either interpretation (it is algebraically exact), but the thermodynamic meaning collapses.

**Assessment.** The Gibbons–Hawking interpretation (S_c is a genuine entropy) is the dominant convention in the current literature and is well-motivated by the fact that a static observer in de Sitter experiences a thermal bath at T_c. The Euclidean path integral produces exp(-I_E) = exp(S_c) for the de Sitter saddle, giving thermodynamic weight to S_c. Accepting this convention (which we do), the thermodynamic interpretation of Δ_cd is consistent.

**However:** If one takes the conservative view that the cosmological horizon entropy is a geometric bookkeeping quantity and not a physical entropy (as some authors do), then Δ_cd loses its thermodynamic meaning, retaining only its geometric content. The algebraic identity survives; the interpretation does not.

**This is a genuine fragility.** The meaning of Δ_cd as an "entropy deficit" is convention-dependent in a way that the algebraic identity is not.

### 3.4 Test: Higher Dimensions

Does the identity generalize to D spacetime dimensions? This is a necessary condition for the idea to be fundamental rather than an accident of 4D.

**5D SdS.** The blackening function in 5D (with appropriate normalization):

    f(r) = 1 - M/r² - Λ r² / 6

Setting f(r) = 0 and multiplying by r²:

    r² - M - Λ r⁴ / 6 = 0

Multiplying by -6/Λ:

    r⁴ - (6/Λ) r² + (6M/Λ) = 0

This is a quadratic in u = r²:

    u² - (6/Λ) u + (6M/Λ) = 0

By Vieta for the quadratic:

    u_b + u_c = r_b² + r_c² = 6/Λ = r_dS²  (where r_dS = √(6/Λ) for 5D de Sitter)
    u_b u_c = r_b² r_c² = 6M/Λ

The 5D entropy: S^{5D} = A^{5D}/4 = 2π² r³ / 4 = π² r³ / 2 (area of 3-sphere: 2π² r³).

The entropy identity in 5D would require computing S_dS^{5D} - (S_b^{5D} + S_c^{5D}):

    S_dS^{5D} = (π²/2) r_dS³ = (π²/2)(6/Λ)^{3/2}
    S_b^{5D} + S_c^{5D} = (π²/2)(r_b³ + r_c³)

Now: r_b² + r_c² = 6/Λ = r_dS² (from the Vieta sum of the 5D quadratic).

But r_b³ + r_c³ ≠ simple function of r_dS alone. We have:

    r_b³ + r_c³ = (r_b + r_c)(r_b² - r_b r_c + r_c²) = (r_b + r_c)((6/Λ) - r_b r_c)

And r_b r_c = √(6M/Λ) (from u_b u_c = 6M/Λ, taking positive root).

The 5D deficit would be:

    Δ^{5D} = (π²/2)[r_dS³ - r_b³ - r_c³]

This does not reduce to a clean product of r_b and r_c. There is no 5D analogue of π r_b r_c. The structure is fundamentally different.

**The root cause:** In 4D, S ∝ r² and the Vieta quadratic identity (**) translates directly into an entropy identity because entropy is quadratic in r. In 5D, S ∝ r³ and the Vieta relation for the 5D quadratic gives r_b² + r_c² = const, which translates into entropies only via complicated cube-root expressions.

**D-dimensional summary.** In D dimensions, the horizon equation is a polynomial in r of degree D-1. The Vieta relations for this polynomial give algebraic relations among the horizon radii. Only in D = 4 does the specific combination S ∝ r² × (Vieta quadratic identity) yield a clean entropy product Δ_cd = √(S_b S_c). For D ≠ 4, no analogous clean identity exists.

**VERDICT: The identity fails to generalize to D ≠ 4. It is a 4D algebraic coincidence.**

This is a significant weakness. If the identity were fundamental, it should hold in D dimensions (possibly with a D-dependent prefactor). The failure of a clean generalization suggests the 4D form is special to the cubic structure of the 4D horizon equation, not to any deep thermodynamic principle.

### 3.5 Test: Reissner–Nordström–de Sitter (RNdS)

The RNdS blackening function with charge Q:

    f(r) = 1 - 2M/r + Q²/r² - Λ r²/3

Setting f(r) = 0 and multiplying by r²:

    r² - 2Mr + Q² - Λ r⁴/3 = 0

Multiplying by -3/Λ:

    r⁴ - (3/Λ) r² + (6M/Λ) r - (3Q²/Λ) = 0     ... (Q)

This quartic (with no r³ term) has four roots: r₁ < r₂ = r_- < 0 (one or two negative roots), r_b (inner Cauchy horizon), r_+ (outer black hole horizon), r_c (cosmological horizon). The Vieta relations for the quartic:

    r_- + r_b + r_+ + r_c = 0   (sum = 0, since no r³ term)
    Sum of pairwise products = -3/Λ
    Sum of triple products = -6M/Λ
    Product of all four = -3Q²/Λ

Defining the deficit Δ_cd = S_dS - (S_+ + S_c) (using only the outer BH horizon and cosmological horizon, as in the uncharged case):

    Δ^{RN} = π r_dS² - π r_+² - π r_c² = π(r_dS² - r_+² - r_c²)

Using the pairwise Vieta sum with four roots: the sum of pairwise products includes cross terms from all four roots, not just r_+ and r_c. The clean identity (**) does not survive. One obtains a more complex expression involving Q.

Specifically, from Vieta for the quartic:

    (r_-)(r_b) + (r_-)(r_+) + (r_-)(r_c) + (r_b)(r_+) + (r_b)(r_c) + (r_+)(r_c) = -3/Λ

Denote r_- + r_b = -(r_+ + r_c) (from sum = 0). The algebra becomes significantly more complex and Q-dependent. No clean analogue of π r_b r_c is obtained.

**VERDICT: The identity does not generalize to the charged case without significant modification.** The RNdS deficit depends on Q in a nontrivial way and the clean geometric mean structure is broken.

### 3.6 Test: Kerr–de Sitter

The Kerr–de Sitter metric introduces angular momentum J. The horizon structure is more complex (ergosphere, two horizons), the thermodynamic first law has additional terms for angular momentum, and the Killing horizons are not spherical (so the simple r² area formula does not apply). The entropy is still A/4, but A is the area of a squashed sphere.

The horizon equation for Kerr–dS is a polynomial in r² (for the equatorial radius) that does not reduce to the simple SdS cubic. No direct analogue of (**) is expected.

**VERDICT: The Kerr–dS case is substantially more complex. The identity does not generalize cleanly.**

### 3.7 Summary of Breaking Attempts

| Test | Result |
|---|---|
| Is Δ_cd just a function of M? | At fixed Λ: yes (monotone reparametrization). At variable Λ: no. |
| Coordinate invariance | Passes. Δ_cd is fully coordinate-invariant. |
| Thermodynamic convention dependence | Fragile. Fails if S_c is not treated as a genuine entropy. |
| Higher dimensions (D≠4) | Fails. The clean form is 4D specific. |
| Charged case (RNdS) | Fails. No clean analogue found. |
| Rotating case (KdS) | Fails. Structure is qualitatively different. |

---

## PART 4: Scaling and Limits

### 4.1 Pure de Sitter: M → 0

From the cubic (C): r_b → 0, r_c → √(3/Λ) = r_dS.

    S_b → 0,   S_c → S_dS,   Δ_cd → 0

The pair creation probability P → exp(0) = 1 (trivially: no black hole, no tunneling suppression).

### 4.2 Small Black Hole: M << M_N

From V3 and V1 to leading order:

    r_b ≈ 2M + O(M³ Λ)        (approaches Schwarzschild)
    r_c ≈ √(3/Λ)[1 - (M/r_dS²) + ...] = r_dS - M/r_dS + O(M²Λ)

Product:

    r_b r_c ≈ 2M · r_dS = 2M √(3/Λ)

Deficit to leading order:

    Δ_cd ≈ 2πM √(3/Λ) = 2πM r_dS / √3     ... (small M)

This is linear in M. The subleading correction requires solving the cubic perturbatively.

Individual entropies:

    S_b ≈ π(2M)² = 4πM²        (quadratic in M, small)
    S_c ≈ 3π/Λ - 2πM/r_dS + ...  = S_dS - 2πM r_dS^(-1) ...

Wait, let me redo S_c:
    S_c = π r_c² ≈ π(r_dS - M/r_dS)² ≈ π r_dS² - 2πM + O(M²) = S_dS - 2πM + O(M²Λ)

Check: S_b + S_c + Δ_cd ≈ 4πM² + (S_dS - 2πM) + 2πM = S_dS + 4πM² ≈ S_dS for small M. ✓ (the M² correction from S_b is subleading)

Pair creation probability for small black holes:

    P ≈ exp(-2πM r_dS / √3) ≈ exp(-2πM √(3/Λ))

This can also be written P ≈ exp(-M/T_c) to leading order, since T_c ≈ H/(2π) = (1/(2π r_dS)) and:
    M/T_c = 2πM r_dS ≠ 2πM r_dS/√3... not quite.

Actually: T_c ≈ √(Λ/3)/(2π) = 1/(2π r_dS). Then 1/T_c = 2π r_dS.

    Δ_cd ≈ 2πM r_dS/√3 ≠ M/T_c = 2πM r_dS.

The factor of 1/√3 is genuine, not a convention artifact.

### 4.3 Nariai Limit: M → M_N = 1/(3√Λ)

Setting r_b = r_c = r_N in (**): 3r_N² = 3/Λ, so:

    r_N = 1/√Λ

Entropy values:

    S_b = S_c = π/Λ
    S_b + S_c = 2π/Λ = (2/3) S_dS
    Δ_cd = π r_N² = π/Λ = (1/3) S_dS

The entropy budget at Nariai partitions into three equal thirds:

    S_dS = S_b + S_c + Δ_cd = (π/Λ) + (π/Λ) + (π/Λ) = 3π/Λ   ✓

Surface gravities: kappa_b = M_N/r_N² - Λ r_N/3 = (√Λ/3) - (√Λ/3) = 0. Similarly kappa_c = 0.

Both temperatures vanish at Nariai: T_b = T_c = 0. The integrand of (I) has both terms diverge (1/T → ∞), but the integral (I) converges to the finite value π/Λ. The limit must be taken carefully; near Nariai, T_b ≈ T_c ≈ κ/(2π) with κ ∝ ε (where ε = r_c - r_b → 0), and 1/T_c - 1/T_b ∝ 1/ε is integrable.

Pair creation probability at Nariai:

    P_Nariai ~ exp(-π/Λ)

This is the minimum probability over all M (since Δ_cd is maximal at Nariai). It matches the Ginsparg–Perry result.

### 4.4 Scaling with Λ at Fixed M

At fixed M, as Λ → 0 (small cosmological constant):

    r_dS = √(3/Λ) → ∞,   r_c ≈ r_dS → ∞,   r_b ≈ 2M (fixed)
    Δ_cd ≈ 2πM√(3/Λ) → ∞

But S_dS = 3π/Λ → ∞ faster, so Δ_cd/S_dS → 0. The relative deficit vanishes in the asymptotically flat limit. This is physical: for very small Λ, the cosmological horizon is astronomically far away and the black hole is essentially Schwarzschild. The "coupling" in relative terms is negligible.

At fixed M, as Λ → Λ_max = 1/(9M²) (approaching Nariai from below):

    r_b → r_c → 1/√Λ
    Δ_cd → π/Λ = Δ_cd^{max}

### 4.5 Nontrivial Invariant Along the Phase Space

In the (r_b, r_c) plane at fixed Λ, all SdS spacetimes lie on the ellipse:

    α² + αβ + β² = 1        where α = r_b/r_dS,  β = r_c/r_dS

This is a compact algebraic curve with α ∈ [0, 1/√3] and β ∈ [1/√3, 1], parameterizing all allowed mass values.

The endpoints: (α,β) = (0,1) corresponds to M=0 (pure de Sitter), and (α,β) = (1/√3, 1/√3) corresponds to M=M_N (Nariai).

The "phase space" of SdS spacetimes at fixed Λ is an arc of this ellipse. The ellipse x² + xy + y² = 1 is an ellipse in the (x,y) plane, tilted at 45°, with semi-axes 1 (along x+y direction) and 1/√3 (along x-y direction). This is the standard "hexagonal" metric or Eisenstein integer norm.

**Is this useful?** As a geometric picture of the SdS phase space, it is clean and possibly useful for visualization. As a physical statement, it is equivalent to (**) and adds no new information.

---

## PART 5: Search for a Surviving Real Result

### 5.1 Assessment of Each Candidate

**Candidate A: A new invariant.**

Δ_cd = π r_b r_c = √(S_b S_c) is a function of (M, Λ) with no new information beyond these parameters. At fixed Λ it is monotone in M. It is coordinate-invariant, but it is not a new conserved charge or topological invariant. It is a specific function of the two horizon entropies.

**Verdict: No new invariant. Δ_cd is a known function of known quantities.**

**Candidate B: A new thermodynamic relation not explicitly known.**

The identity d(Δ_cd)/dM = 1/T_c - 1/T_b (equation D) combines the two horizon first laws in a single expression. The formula is exact and probably not written down explicitly in the SdS thermodynamics literature, though it follows immediately from the first laws. **This is a minor new explicit statement.**

The integral form Δ_cd = ∫₀ᴹ (1/T_c - 1/T_b) dm is also exact and probably not stated explicitly. **This too is minor but clean.**

**Candidate C: A new inequality.**

The bound 0 ≤ Δ_cd ≤ S_dS/3, with equality at M=0 (lower) and M=M_N (upper), derived from AM–GM. **This is exact, simple, and probably not stated with this sharpness in the literature.** Corollary: the total SdS horizon entropy satisfies (2/3)S_dS ≤ S_b + S_c ≤ S_dS.

**Candidate D: A connection to known physics that is not obvious.**

The pair creation probability P ~ exp(-√(S_b S_c)) = exp(-Δ_cd) is an explicit and clean reformulation of the known nucleation rate formula. **Writing it as exp(-√(S_b S_c)) makes the geometric-mean structure of the tunneling exponent explicit.** This is a modest reformulation of known physics.

### 5.2 The One Result That Survives as Nontrivial (Modestly)

Taking stock of Parts 2–4, the following constitutes the most defensible nontrivial content:

**Theorem (exact, combinatorial):**

In 4D Schwarzschild–de Sitter spacetime at fixed Λ > 0, define ε_b = S_b/S_dS and ε_c = S_c/S_dS (the normalized horizon entropies). Then:

    ε_b + ε_c + √(ε_b ε_c) = 1                      ... (N)

with:
(a) The only solution with ε_b = 0 is ε_c = 1 (pure de Sitter).
(b) The only solution with ε_b = ε_c (symmetric solution) is ε_b = ε_c = 1/3 (Nariai).
(c) √(ε_b ε_c) = Δ_cd/S_dS ∈ [0, 1/3] over the full parameter range.
(d) The AM–GM bound gives ε_b + ε_c ≥ 2√(ε_b ε_c), so ε_b + ε_c ≥ 2/3, i.e., S_b + S_c ≥ (2/3) S_dS.

This is an exact algebraic characterization of the SdS entropy budget in terms of normalized entropy fractions.

**Corollary (exact):** The black hole pair creation probability in de Sitter satisfies:

    P(M) ~ exp(-S_dS · √(ε_b ε_c))

where ε_b ε_c ∈ [0, 1/9] with maximum at Nariai.

**What is new here, precisely:** Writing (N) as a constraint on normalized entropies ε_b, ε_c eliminates Λ explicitly. Any SdS spacetime (whatever Λ) has its normalized entropies satisfying the single universal constraint (N). This is a scale-free statement. The Nariai limit ε_b = ε_c = 1/3 is the unique interior point of the constraint surface where the deficit fraction takes its maximum value 1/3. **The result (N) with its bounds and limits is a clean, universal, and probably underappreciated characterization of 4D SdS thermodynamics.**

Whether this has been stated exactly in this form in the literature: unlikely, though it follows from known results. The claim of novelty is modest.

---

## PART 6: Final Verdict

**The answer to the central question:** Does Δ_cd represent anything deeper than the algebra of the SdS cubic?

**Partially yes, but within strict limits.**

Here is what is established:

1. **Δ_cd is coordinate-invariant** (passes this test cleanly).

2. **Δ_cd = √(S_b S_c)** is the geometric mean of the two horizon entropies. The entropy identity S_dS = S_b + S_c + √(S_b S_c) is exact and scale-free. In normalized form (N), it characterizes all 4D SdS spacetimes by a single algebraic constraint with no free parameters.

3. **Δ_cd is the Euclidean instanton action** for black hole pair creation in de Sitter. The known formula P ~ exp(S_b + S_c - S_dS) is equivalent to P ~ exp(-√(S_b S_c)). This is a concrete, established physical meaning, not merely algebra.

4. **The bound 0 ≤ Δ_cd ≤ S_dS/3** is exact, follows from AM–GM, and saturates at both endpoints. It implies S_b + S_c ≥ (2/3) S_dS for all SdS spacetimes.

5. **The integral representation Δ_cd = ∫₀ᴹ (1/T_c - 1/T_b) dm** is exact and interprets Δ_cd as cumulative inverse-temperature anti-alignment, i.e., the entropy cost of irreversibly building up a black hole from a de Sitter background.

Here is what fails:

1. **The identity does not generalize to D ≠ 4.** The 4D form is specific to the cubic structure of the 4D horizon equation and the quadratic dependence of entropy on horizon radius. This is a fundamental weakness.

2. **The identity does not generalize cleanly to RNdS or KdS.** Charge and rotation break the simple structure.

3. **No connection to mutual information or entanglement entropy** can be established without a microscopic model.

4. **At fixed Λ, Δ_cd is monotone in M** and encodes the same information as M. It is a reparametrization of the mass at fixed Λ.

5. **The "compression-dilution" interpretation** is physically suggestive but not mathematically derivable from Δ_cd alone. The sign asymmetry of the first laws (dS_b > 0, dS_c < 0) is real, but calling it "compression vs. dilution" adds no predictive content.

**Classification: "Minor novel structure — short note possible."**

The reasons: The algebraic content is entirely derivable from known SdS geometry. The physical meaning (instanton action for pair creation) is known since Ginsparg–Perry 1983. However, the specific reformulations — the geometric mean identity, the scale-free constraint (N), the AM–GM bound on the entropy budget, and the integral representation — constitute a modest, clean, and self-consistent package that is likely not assembled in this way in the existing literature. A compact note (5–8 pages) that honestly presents these results without overclaiming would be publishable and modestly useful.

The idea is not trivial. The entropy deficit is not merely an algebraic identity; it controls black hole nucleation rates and has a clean structure in terms of the geometric mean of horizon entropies. But it is also not a major result. It is a useful repackaging of 4D SdS thermodynamics.

**The critical caveat:** The failure of the identity to extend beyond 4D, uncharged, non-rotating SdS is a strong signal that the result is a 4D algebraic coincidence tied to the specific structure of the cubic horizon equation, not a fundamental thermodynamic principle. Any attempt to elevate Δ_cd to a status comparable to Hawking temperature or Bekenstein–Hawking entropy would be unjustified by the evidence.

---

## Appendix: Key Equations

| Label | Equation | Status |
|---|---|---|
| (**) | r_b² + r_b r_c + r_c² = 3/Λ | Exact, from Vieta |
| (***) | S_dS - (S_b + S_c) = πr_br_c | Exact, from (**) × π |
| (GM) | S_dS = S_b + S_c + √(S_b S_c) | Exact reformulation |
| (N) | ε_b + ε_c + √(ε_b ε_c) = 1, ε_i = S_i/S_dS | Exact, scale-free |
| (D) | dΔ_cd/dM = 1/T_c - 1/T_b | Exact, from first laws |
| (I) | Δ_cd(M) = ∫₀ᴹ [1/T_c - 1/T_b] dm | Exact, integrating (D) |
| (PC) | P(nucleation) ~ exp(-Δ_cd) | Known, from Euclidean action |
| (B) | 0 ≤ Δ_cd ≤ S_dS/3 | Exact, from AM-GM |

All equations in natural units G = ħ = c = k_B = 1.

---

*End of stress test.*

*Classification: "Minor novel structure — short note possible."*

*The idea partially survives. The algebraic identity is exact and coordinate-invariant. It controls black hole nucleation. The scale-free form (N) and the AM–GM entropy bound are clean results. The generalization failures (higher D, charge, rotation) are real and indicate this is not a fundamental principle. Proceed with intellectual honesty: a note is warranted; a major claim is not.*
