# Δ_cd Discovery Stress Test: A Full Mathematical Forcing

**Objective:** Force the SdS entropy deficit structure to yield either a genuine new result or a proof that none exists.
**Method:** Derive, reparametrize, attack, generalize. No summaries of previous results.

---

## PHASE 1: THREE STRUCTURAL REPRESENTATIONS

### 1A. Geometric Form — What Can Be Found

The identity is:

    Δ_cd = π r_b r_c = √(S_b S_c)

**Attempt: express as a curvature integral.**

The Kretschner scalar of SdS in natural units:

    K = R_μνρσ R^{μνρσ} = 48M²/r⁶ + 8Λ²/3

A volume integral of K over the static patch (r_b ≤ r ≤ r_c, Euclidean period β) would give a function of M and Λ with no reason to equal π r_b r_c. No clean identification is found.

**Attempt: Gauss–Bonnet / topological.**

The Euler characteristic χ of the Euclidean SdS manifold is topological (χ = 2 for the two-horizon geometry). This is M- and Λ-independent. The Gauss–Bonnet theorem in 4D:

    χ = (1/32π²) ∫ (R_μνρσ R^{μνρσ} - 4R_μν R^{μν} + R²) √g d⁴x + boundary

For an Einstein space, R_μν = Λg_μν, the bulk integrand reduces to the Weyl tensor squared. This gives χ = 2 independent of M. Δ_cd is not topological.

**Attempt: Wald entropy generalization.**

For Lagrangian L = R - 2Λ + αR² + βR_μν R^{μν} + ..., the Wald entropy of each horizon acquires curvature corrections. At the black hole horizon: S_b^{Wald} = A_b/4 + corrections(R_μνρσ|_{r_b}). At the cosmological horizon: S_c^{Wald} = A_c/4 + corrections(R_μνρσ|_{r_c}).

The Einstein-gravity identity S_dS = S_b + S_c + √(S_b S_c) rests on the Vieta identity for the cubic, which comes from the Einstein-gravity blackening function f(r). Under higher-derivative corrections, f(r) is modified, the horizon positions shift, and the Vieta structure breaks. **The identity is Einstein-gravity specific and does not survive arbitrary higher-derivative corrections.**

**Conclusion on 1A:** No clean integral or curvature representation of Δ_cd exists. It is algebraically defined by the Vieta structure of the SdS cubic. This is a failure for any claim that Δ_cd has geometric depth beyond its algebraic definition.

---

### 1B. Thermodynamic Form — What Is Real

**Result 1B.1 (established in prior work):** Δ_cd is the Euclidean tunneling exponent:

    P(BH nucleation) ~ exp(-Δ_cd) = exp(-√(S_b S_c))

This follows from the on-shell Euclidean action: I_E[SdS] = -(S_b + S_c), I_E[dS] = -S_dS. The exponent ΔI_E = Δ_cd. This is established in Bousso–Hawking (1996) and Ginsparg–Perry (1983) in the form exp(S_b + S_c - S_dS), and is here stated as exp(-√(S_b S_c)).

**Result 1B.2 (integral representation):** From dΔ_cd/dM = 1/T_c - 1/T_b and boundary condition Δ_cd(M=0) = 0:

    Δ_cd(M) = ∫₀ᴹ [1/T_c(m) - 1/T_b(m)] dm

This is exact. It expresses Δ_cd as cumulative inverse-temperature anti-alignment. This is a rigorous thermodynamic form. Whether it constitutes "new" content depends on whether the first-law combination was previously assembled this way.

---

### 1C. Information-Theoretic Form — What Fails

**Attempt:** Relative entropy between the two horizon thermal states ρ_b (at temperature T_b) and ρ_c (at temperature T_c):

    S(ρ_b || ρ_c) = Tr(ρ_b log ρ_b) - Tr(ρ_b log ρ_c)
                  = (β_c - β_b)⟨H⟩_b + log(Z(β_c)/Z(β_b))

where β = 1/T. This involves ⟨H⟩_b and the partition functions, which require a microscopic Hamiltonian for the horizon degrees of freedom. No such Hamiltonian is established for either SdS horizon. The connection cannot be made rigorous.

**Result:** No rigorous information-theoretic form for Δ_cd exists in the absence of a microscopic model. **This line fails.**

---

## PHASE 2: BREAK PARAMETER DEPENDENCE

### 2.1 Introduction of the Ratio Variable

Define:

    x = r_b / r_c ∈ (0, 1]

From the Vieta identity r_b² + r_b r_c + r_c² = 3/Λ:

    r_c²(x² + x + 1) = 3/Λ                               ... (B)

From the Vieta product r_- r_b r_c = -6M/Λ with r_- = -(r_b + r_c) = -r_c(1+x):

    r_c³ x(1+x) = 6M/Λ                                   ... (A)

Combining (A) and (B):

    M = r_c x(1+x) / (2(x²+x+1))                         ... (*)

All quantities follow.

### 2.2 Exact Temperatures in Terms of x

Computing T_b = (M/r_b² - Λr_b/3)/(2π) and T_c = (Λr_c/3 - M/r_c²)/(2π) using M from (*) and Λ from (B):

**M/r_b²:**

    M/(x²r_c²) = x(1+x) / (2x²r_c(x²+x+1)) = (1+x)/(2xr_c(x²+x+1))

**Λr_b/3 = Λxr_c/3:**

    [3/(r_c²(x²+x+1))] × xr_c/3 = x/(r_c(x²+x+1))

**Therefore:**

    T_b = [1/(2π)] × [(1+x)/(2xr_c(x²+x+1)) - x/(r_c(x²+x+1))]
        = [1/(4πr_c(x²+x+1))] × [(1+x)/x - 2x]
        = [1/(4πr_c(x²+x+1))] × (1+x-2x²)/x
        = (1-x)(1+2x) / [4πxr_c(x²+x+1)]                ... (Tb)

[Factoring: 1+x-2x² = (1-x)(1+2x). Verified: 1+x-2x² = (1-x)(1+2x) = 1+2x-x-2x² = 1+x-2x². ✓]

**Λr_c/3 - M/r_c²:**

    1/(r_c(x²+x+1)) - x(1+x)/(2r_c(x²+x+1)) = [2-x(1+x)] / (2r_c(x²+x+1))
                                                = (2-x-x²) / (2r_c(x²+x+1))
                                                = (1-x)(2+x) / (2r_c(x²+x+1))

**Therefore:**

    T_c = (1-x)(2+x) / [4πr_c(x²+x+1)]                  ... (Tc)

[Factoring: 2-x-x² = -(x²+x-2) = -(x+2)(x-1) = (1-x)(2+x). Verified. ✓]

### 2.3 The Temperature Ratio: A New Exact Formula

From (Tb) and (Tc), dividing:

    T_c / T_b = [(1-x)(2+x) / (4πr_c(x²+x+1))] / [(1-x)(1+2x) / (4πxr_c(x²+x+1))]
              = x(2+x) / (1+2x)                           ... (TR)

**This is exact. The temperature ratio T_c/T_b is a rational function of x = r_b/r_c only.**

Verification at limits:

    x → 0:   T_c/T_b → 0         ✓ (T_b >> T_c for small black hole)
    x = 1:   T_c/T_b = 3/3 = 1   ✓ (Nariai: T_b = T_c)

Verification: for small x, r_b ≈ 2M, so T_b ≈ 1/(8πM) = 1/(4πr_b). And T_c ≈ √(Λ/3)/(2π). The ratio T_c/T_b ≈ 2M√(Λ/3)/(π) = 2xr_c√(Λ/3)/(π·1) ≈ 2x × (r_c/(r_dS)) × (1/π) × ... at leading order in small x, T_c/T_b ≈ 2x (from (TR)), consistent with T_c/T_b = x(2+x)/(1+2x) ≈ 2x for small x. ✓

### 2.4 All Normalized SdS Thermodynamics as Functions of x

At fixed Λ, every dimensionless thermodynamic ratio is a rational function of x:

| Quantity | Expression in x |
|---|---|
| ε_b = S_b/S_dS | x²/(x²+x+1) |
| ε_c = S_c/S_dS | 1/(x²+x+1) |
| Δ_cd/S_dS | x/(x²+x+1) |
| T_c/T_b | x(2+x)/(1+2x) |
| η_C = 1 - T_c/T_b | (1-x²)/(1+2x) |
| dΔ_cd/dM × r_c / (some scale) | [function of x] |

**The SdS phase space at fixed Λ is a 1-parameter family parametrized by x ∈ (0,1].** All normalized thermodynamics is captured by x.

### 2.5 Is Δ_cd Independent of M?

**At fixed Λ:** No. x = r_b/r_c is a monotone function of M (x increases from 0 to 1 as M increases from 0 to M_N). At fixed Λ, Δ_cd/S_dS = x/(x²+x+1) is monotone in M. Δ_cd is informationally equivalent to M.

**At fixed x (fixed ratio r_b/r_c):** By varying Λ (and therefore M and r_c simultaneously at fixed x), Δ_cd = 3πx/(Λ(x²+x+1)) scales as 1/Λ. The normalized quantity Δ_cd/S_dS = x/(x²+x+1) is Λ-independent.

**Conclusion:** Δ_cd/S_dS is a function of x only, independent of both M and Λ separately. It is not independent of M; it is the natural M-parametrization at fixed Λ. No hidden structure independent of M is found.

---

## PHASE 3: GENERALIZATION ATTEMPTS

### 3.1 D-Dimensional SdS

In D spacetime dimensions, the SdS blackening function is (in units where the D-dimensional Newton constant is absorbed):

    f_D(r) = 1 - (r_s/r)^{D-3} - r²/r_Λ²

where r_s^{D-3} is proportional to M, and r_Λ² = (D-1)(D-2)/(2Λ). Setting f_D = 0 and multiplying by r^{D-3}/r_Λ²:

    r^{D-1}/r_Λ² - r^{D-3} + r_s^{D-3} = 0

This is a polynomial in r of degree D-1 (the SdS horizon polynomial P_{D-1}(r)).

The Bekenstein–Hawking entropy in D dimensions:

    S = A_{D-2}/4 ∝ r^{D-2}

For the entropy identity to have the geometric-mean form Δ = √(S_b S_c), we need:

    S_dS^D - S_b^D - S_c^D = (S_b^D × S_c^D)^{1/2}

    r_dS^{D-2} - r_b^{D-2} - r_c^{D-2} = r_b^{(D-2)/2} r_c^{(D-2)/2}

    r_dS^{D-2} = r_b^{D-2} + r_b^{(D-2)/2} r_c^{(D-2)/2} + r_c^{D-2}

For this to hold via a Vieta identity, we need the Vieta cross-term for P_{D-1} to equal r_b^{(D-2)/2} r_c^{(D-2)/2}. In 4D: (D-2)/2 = 1, so the cross-term is r_b¹ r_c¹ = r_b r_c. This is the pairwise product of the two positive roots of the cubic, and it appears directly in the D=4 Vieta relation for the sum of pairwise products.

**In D = 5 (quartic polynomial):**

The 5D horizon equation is quadratic in u = r²:

    u_b + u_c = r_b² + r_c² = r_{Λ,5D}² = r_dS^{5D,2}

(where r_dS^{5D} is the 5D de Sitter horizon radius, r_{Λ,5D}² = 12/Λ for the standard convention).

So in 5D: r_b² + r_c² = r_dS², and S ∝ r³.

The 5D entropy relation:
    (S_b)^{2/3} + (S_c)^{2/3} = (S_dS)^{2/3}             ... (5D)

This is a Pythagorean relation in the space of (entropy)^{2/3}, not the Eisenstein norm.

The 5D "deficit": Δ^{5D} = S_dS - S_b - S_c ∝ r_dS³ - r_b³ - r_c³.

Given r_b² + r_c² = r_dS², can Δ^{5D} be written as a simple function of S_b and S_c?

    r_b³ + r_c³ = (r_b + r_c)(r_b² - r_b r_c + r_c²) = (r_b + r_c)(r_dS² - r_b r_c)

And r_dS³ = (r_dS²)^{3/2} = (r_b² + r_c²)^{3/2}. The expression:

    Δ^{5D} ∝ (r_b² + r_c²)^{3/2} - (r_b + r_c)(r_b² - r_b r_c + r_c²)

This does NOT reduce to r_b r_c or (r_b r_c)^{3/2} or any simple product. There is no clean geometric-mean form in 5D.

### 3.2 Exact Identification of the 4D Double Coincidence

The 4D identity Δ_cd = √(S_b S_c) requires simultaneously:

**Condition (i): Entropy quadratic in r.** S ∝ r^{D-2} = r². This requires D = 4.

**Condition (ii): Vieta cross-term is a product of the two positive roots.** For the degree-(D-1) polynomial in r, the sum of pairwise products of the three roots (r_-, r_b, r_c) in 4D is:

    r_- r_b + r_- r_c + r_b r_c = -3/Λ

After eliminating r_- = -(r_b + r_c), the cross-term r_b r_c appears linearly. This linear appearance comes from the cubic having exactly three roots and no r² term, placing the cross-term as the last Vieta sum. This structure is specific to the cubic (D=4 horizon polynomial).

For D=5 (quartic): the pairwise product sum has six terms from four roots, and the structure is different.

**Both conditions require D = 4.** The geometric-mean identity is a "double coincidence" of spacetime dimension. It is not a consequence of any principle that generalizes to other dimensions. The result is 4D specific by necessity, not by choice.

### 3.3 Charged Case: RNdS

The RNdS horizon equation f = 0 gives a quartic in r with no r³ term:

    r⁴ - (3/Λ)r² + (6M/Λ)r - (3Q²/Λ) = 0               ... (RN)

Four roots: r_1 < r_2 < 0, r_- (unphysical), r_b (Cauchy), r_+ (outer BH), r_c (cosmological). Wait, actually: two roots can be positive and two negative, or other configurations depending on Q and M. For small Q: three real positive roots (inner, outer, cosmological) and one negative.

For the outer BH horizon r_+ and cosmological r_c, the Vieta sum of pairwise products for the quartic (four roots r_1, r_-, r_+, r_c with sum = 0) is:

    r_1 r_- + r_1 r_+ + r_1 r_c + r_- r_+ + r_- r_c + r_+ r_c = -3/Λ

The term r_+ r_c is entangled with all other cross-terms, including those involving r_b (Cauchy) and the unphysical root. No clean analogue of the SdS identity survives for the outer horizon pair alone.

**Define:** Δ^{RN} = S_dS^{Q=0} - S_+ - S_c (using the Q=0 de Sitter entropy).

This mixes the Q=0 background with the charged solution and is not a meaningful entropy deficit for the RNdS system.

**Define instead:** Δ^{RN} = S_dS^{RN} - S_+ - S_c, where S_dS^{RN} = π r_dS^{RN,2} with r_dS^{RN} the de Sitter horizon at the same Λ and Q=0.

In this case, the deficit is not √(S_+ S_c) because the RNdS Vieta structure gives:

    r_+² + r_+ r_c + r_c² ≠ 3/Λ    (extra terms from charge Q appear)

Specifically, from the quartic (RN) with inner horizon r_-, outer horizon r_+, cosmological r_c, and unphysical root r_u (with r_u + r_- + r_+ + r_c = 0):

    The sum of pairwise products involving r_+ and r_c is not isolated cleanly.

No clean generalization of the geometric-mean identity exists in RNdS.

### 3.4 Summary: Generalization Completely Fails

The geometric-mean identity is 4D, uncharged, non-rotating, Einstein gravity. Every extension attempted — higher D, charge, rotation, higher-derivative gravity — breaks it. **The identity is structurally confined to the minimal SdS case.**

---

## PHASE 4: SEARCH FOR A NEW RESULT

### 4.1 Attempt: Lyapunov Function for Hawking Evaporation

Under Hawking evaporation in a de Sitter background, the black hole loses mass: dM/dt < 0. From dΔ_cd/dM = 1/T_c - 1/T_b > 0 (in the generic regime T_b > T_c):

    dΔ_cd/dt = (dΔ_cd/dM)(dM/dt) < 0

Δ_cd decreases monotonically during Hawking evaporation (as M → 0, Δ_cd → 0). **Δ_cd is a Lyapunov function for Hawking evaporation in de Sitter:** it is positive, monotonically decreasing, and its zero (Δ_cd = 0) corresponds to the fixed point (pure de Sitter).

This is a legitimate dynamical characterization, but it follows immediately from dΔ_cd/dM > 0 and dM/dt < 0. It is not a new result in any deep sense — it is a consequence of the two known facts.

**Status: true but trivial consequence of known results.**

### 4.2 Attempt: New Inequality Beyond AM-GM

All normalized quantities are rational functions of x. Can I find a tighter bound than Δ_cd ≤ S_dS/3?

From (TR): T_c/T_b = x(2+x)/(1+2x). Can I bound Δ_cd/S_dS in terms of T_c/T_b?

Let R = T_c/T_b ∈ (0,1]. Inverting (TR): x(2+x) = R(1+2x), so x² + (2-2R)x - R = 0:

    x = (R-1) + √(R²-R+1)                               ... (XI)

(taking the positive root).

Then Δ_cd/S_dS = x/(x²+x+1). Using x from (XI), this is a closed-form expression in R, but it is complicated. No clean inequality independent of AM-GM is found.

**Attempt: lower bound involving T_c/T_b.**

At fixed T_c/T_b = R, Δ_cd/S_dS = x(R)/(x(R)² + x(R) + 1) is uniquely determined by R through (XI). There are no inequalities to state — the value is exact, not bounded.

**Status: no new inequality found.**

### 4.3 The Carnot–Deficit Exact Identity: A New Explicit Result

**Derivation.** From the first laws dS_b/dM = 1/T_b and dS_c/dM = -1/T_c, and dΔ_cd/dM = 1/T_c - 1/T_b:

    dΔ_cd/dS_c := (dΔ_cd/dM) / (dS_c/dM) = (1/T_c - 1/T_b) / (-1/T_c)

    = -T_c(1/T_c - 1/T_b) = -(1 - T_c/T_b) = -(1 - R)

But 1 - T_c/T_b = η_C (Carnot efficiency of a heat engine operating between T_b and T_c). Therefore:

    dΔ_cd / dS_c = -η_C                                  ... (CD-I)

**This is exact.** Similarly:

    dΔ_cd / dS_b := (dΔ_cd/dM) / (dS_b/dM) = (1/T_c - 1/T_b) × T_b = T_b/T_c - 1 = 1/R - 1

Using (TR): 1/R = (1+2x)/(x(2+x)), so:

    dΔ_cd / dS_b = (1+2x-x(2+x))/(x(2+x)) = (1-x²)/(x(2+x))   ... (CD-II)

**Verification:** The consistency check is dΔ_cd = -dS_b - dS_c (from Δ_cd = S_dS - S_b - S_c at fixed Λ), i.e., dΔ_cd/dM = -dS_b/dM - dS_c/dM. This gives:

    (1/T_c - 1/T_b) = -(1/T_b) - (-1/T_c) = 1/T_c - 1/T_b ✓

Now, the ratio of the two derivatives:

    (dΔ_cd/dS_b) / (dΔ_cd/dS_c) = -[(1-x²)/(x(2+x))] / η_C
    = -[(1-x²)/(x(2+x))] / [(1-x²)/(1+2x)]
    = -(1+2x)/(x(2+x)) = -1/R = -T_b/T_c

So: **(dΔ_cd/dS_b) / (dΔ_cd/dS_c) = -T_b/T_c**, i.e., the ratio of the two marginal rates of Δ_cd change equals the negative inverse temperature ratio.

**Physical reading of (CD-I):** The rate of entropy deficit destruction per unit of cosmological entropy gained is the Carnot efficiency of the effective horizon heat engine. As the black hole evaporates (dS_c > 0, dS_b < 0, dM < 0), the deficit decreases at rate η_C per unit of cosmological entropy gain. The more efficient the horizon heat engine (higher η_C, lower R), the faster the deficit dissipates per unit of cosmological entropy gained.

**Is (CD-I) new?** It follows by combining two known first-law expressions. However, it connects three distinct quantities — entropy deficit rate, cosmological entropy change, and Carnot efficiency — in a single exact formula. This exact combination does not appear to be explicitly stated in the SdS thermodynamics literature. Whether it is known implicitly or not, it is a clean result that is not immediately obvious.

### 4.4 Attempt: Ruppeiner Thermodynamic Geometry

The Ruppeiner metric on the one-dimensional parameter space of SdS states (at fixed Λ) is:

    g_{MM} = -∂²(S_b + S_c)/∂M²

Since d(S_b + S_c)/dM = 1/T_b - 1/T_c = -dΔ_cd/dM:

    g_{MM} = -d/dM(-dΔ_cd/dM) = d²Δ_cd/dM²

The Ruppeiner metric for the total SdS entropy is the second derivative of Δ_cd. In x-parametrization:

    d²Δ_cd/dM² = d/dM(1/T_c - 1/T_b)

Using (Tb) and (Tc) and (*), this can be computed explicitly in terms of x, but the expression is lengthy and does not simplify to a clean form. The Ruppeiner curvature scalar would characterize the nature of thermodynamic fluctuations, but computing it for SdS is a separate project. **No new result here beyond the setup.**

### 4.5 Attempt: Connection to Black Hole Phase Transitions

The Hawking–Page phase transition in AdS involves an entropy discontinuity. For SdS, there is no such transition (the parameter space is connected), but the Nariai limit M → M_N is a degenerate limit where the two horizons merge. Near Nariai (x → 1):

    T_b, T_c → 0    (both temperatures vanish)
    Δ_cd → S_dS/3   (maximum of Δ_cd)
    η_C → 0          (zero Carnot efficiency)
    (CD-I): dΔ_cd/dS_c → 0    (no deficit change per cosmological entropy at Nariai)

This is consistent: at the Nariai degenerate point, the Carnot efficiency vanishes and no thermodynamic work can be extracted. The entropy deficit is at its maximum and is not changing (in the sense that infinitesimally near Nariai, dΔ_cd/dS_c → 0).

---

## PHASE 5: DESTRUCTION TEST

### 5.1 Coordinate Artifact Test

Δ_cd = √(S_b S_c) where S_b = A_b/4, S_c = A_c/4, and A = 4πr² is the area of the bifurcation surface. Bifurcation surface areas are geometric invariants of the Killing horizon (Wald, 1993). **Δ_cd passes: fully coordinate-invariant.**

### 5.2 Reducibility to Trivial Identity Test

**Δ_cd = S_dS - S_b - S_c** is a definition. The content is the claim that this equals √(S_b S_c), which is a consequence of the Vieta identity for the SdS cubic. The Vieta identity is polynomial root algebra. The entropy identity is a linear rescaling of the Vieta identity (multiplied by π). In this sense, the identity is algebraically trivial — it contains the same information as the cubic's Vieta relations.

**However**, the algebraic identity has physical content: S_b, S_c, S_dS are horizon entropies with thermodynamic meaning, and their mutual constraint encodes the pair creation rate, the entropy budget, and the first-law anti-alignment. The triviality of the algebra does not imply triviality of the physics.

**Partial failure:** The identity is algebraically trivial. The physics is not.

### 5.3 Predictive Content Test

Δ_cd predicts: P ~ exp(-Δ_cd). This is a specific, computable prediction for the pair creation rate in terms of two horizon entropies. It is equivalent to known formulas in the literature. Δ_cd also predicts dΔ_cd/dS_c = -η_C, which connects the deficit evolution to the Carnot efficiency. **Predictive content exists, but is equivalent to known results.**

### 5.4 Stability Under Perturbation Test

**Small perturbation:** Let M → M + δM with δM small. Then Δ_cd → Δ_cd + δΔ_cd where δΔ_cd = (1/T_c - 1/T_b) δM ≠ 0. Δ_cd is stable and changes continuously under perturbation. It does not vanish. **Passes.**

**Thermodynamic convention test:** The interpretation of Δ_cd as an entropy deficit requires that both S_b and S_c are genuine thermodynamic entropies. The status of S_c (cosmological horizon entropy) is debated in some approaches:
- Accepting Gibbons–Hawking (standard): S_c is genuine. Δ_cd is an entropy deficit. ✓
- Conservative view (observer-dependent, not canonical): S_c is a geometric area, not entropy. Then Δ_cd loses thermodynamic meaning. ✗

**This remains a fragility.** The algebraic identity survives both conventions; the thermodynamic interpretation does not.

### 5.5 Parameter Independence Test

At fixed Λ, Δ_cd is monotone in M. Knowing Δ_cd and Λ uniquely determines M. At fixed x (fixed r_b/r_c), Δ_cd/S_dS = x/(x²+x+1) is Λ-independent. The normalized deficit is independent of Λ (at fixed x), but x itself depends on both M and Λ.

**Δ_cd carries no information beyond (M, Λ).** It is a function of the same parameters, not an independent quantity. **This is the principal weakness.**

---

## PHASE 6: FINAL OUTPUT

### What Survives

**1. The Carnot–deficit exact identity (probably new as explicit statement):**

    dΔ_cd / dS_c = -η_C

where η_C = 1 - T_c/T_b is the Carnot efficiency of the effective heat engine between the two horizons. Exact, derived from first principles, connects three thermodynamic quantities.

**2. The temperature ratio formula (explicit, clean, not previously highlighted):**

    T_c / T_b = x(2+x) / (1+2x)    where x = r_b/r_c

This is an exact closed-form expression for the temperature ratio as a rational function of the horizon radius ratio. With (TR) and (*), every thermodynamic quantity in SdS has an exact closed-form expression in x.

**3. The pair creation formula in geometric-mean form:**

    P(BH nucleation) ~ exp(-√(S_b S_c))

Equivalent to known formulas, but the geometric-mean structure of the tunneling exponent makes the dependence on both horizon entropies explicit and symmetric. Not new physics; cleaner packaging.

**4. The scale-free universal constraint (clean, probably underappreciated):**

    ε_b + ε_c + √(ε_b ε_c) = 1    where ε_i = S_i / S_dS

Every 4D SdS spacetime (any M, any Λ) lies on this algebraic curve in the (ε_b, ε_c) plane. It is the universal, parameter-free characterization of the 4D SdS entropy budget.

**5. Δ_cd is a Lyapunov function for Hawking evaporation in de Sitter (true, trivial):**

Δ_cd > 0 and dΔ_cd/dt < 0 during evaporation. Approaches zero as the system relaxes to pure de Sitter. Not a deep result.

---

### What Fails

| Claim | Status |
|---|---|
| Δ_cd has a geometric integral form | **Fails.** No clean curvature integral found. |
| Δ_cd connects to mutual information | **Fails.** No rigorous connection without microscopic model. |
| The identity generalizes to D≠4 | **Fails.** The 4D structure requires S∝r² AND cubic horizon polynomial, both exclusive to D=4. |
| The identity generalizes to RNdS or KdS | **Fails.** Quartic (or higher) polynomial breaks the structure. |
| The identity survives higher-derivative gravity | **Fails.** Wald entropy corrections modify horizon radii and break the Vieta form. |
| Δ_cd is independent of M | **Fails at fixed Λ.** Monotone in M; equivalent to M as a parameter. |
| The thermodynamic interpretation is convention-free | **Fragile.** Requires accepting S_c as genuine entropy. |
| There is a new bound tighter than AM-GM | **Fails.** All bounds derivable from AM-GM; no improvement found. |

---

### Final Classification

**"Minor novel structure — short note possible."**

The algebraic content is entirely contained in the Vieta identity for the 4D SdS cubic. The physical content (instanton action, pair creation rate) is known from Bousso–Hawking and Ginsparg–Perry.

What is genuinely new as explicit formulated statements: the Carnot–deficit identity dΔ_cd/dS_c = -η_C, the temperature ratio T_c/T_b = x(2+x)/(1+2x) in closed form, and the complete x-parametrization of normalized SdS thermodynamics as rational functions of the horizon ratio.

None of these constitute a fundamental new physical principle. They are exact consequences of the known SdS structure, expressed in a coordinated notation that has not previously been assembled this way.

**The idea does not collapse into complete triviality** — the Carnot–deficit identity and the x-parametrization are real and clean. **The idea does not reach substantive new physics** — all content traces to polynomial root algebra and known thermodynamic first laws. The correct classification is "minor novel structure" in the literal sense: there is structure, it is novel as an explicit package, and it is minor in physical depth.

---

## Appendix: Key Exact Formulas Derived Here

In natural units G = ħ = c = k_B = 1, with x = r_b/r_c ∈ (0,1]:

    T_b = (1-x)(1+2x) / [4πxr_c(x²+x+1)]                        ... (Tb)
    T_c = (1-x)(2+x)  / [4πr_c(x²+x+1)]                          ... (Tc)
    T_c/T_b = x(2+x)/(1+2x)                                        ... (TR)  [new explicit form]
    η_C = (1-x)(1+x)/(1+2x) = (1-x²)/(1+2x)                       ... (EFF)
    dΔ_cd/dS_c = -η_C                                              ... (CD-I) [new explicit form]
    dΔ_cd/dS_b = (1-x²)/(x(2+x)) = (1/R_T - 1)                   ... (CD-II)
    ε_b + ε_c + √(ε_b ε_c) = 1                                    ... (N)   [universal SdS constraint]
    P ~ exp(-S_dS × x/(x²+x+1))                                    ... (PC)
    Δ_cd(M) = ∫₀ᴹ [1/T_c(m) - 1/T_b(m)] dm                       ... (I)

All equations are exact within 4D SdS in Einstein gravity with Gibbons–Hawking thermodynamics for both horizons.
