# Baseline Assessment — Before Building Anything

## What the previous model proved

From recursive_horizon_project (confirmed by 11/11 unit tests + 5 experiments):

1. Eisenstein constraint r_b² + r_b·r_c + r_c² = 3/Λ is algebraically exact (Vieta on SdS cubic).
2. Entropy identity S_Λ = S_b + S_c + √(S_b S_c) is algebraically exact.
3. S_Λ is conserved by construction under Eisenstein normalization (to 10⁻¹⁵).
4. Symmetric power map T_λ(u,v) = normalize(u^λ, v^λ) has NO interior fixed points — always drifts to boundary.
5. Coupled map T_{λ,ε}(u,v) = normalize(u^λ + εv, v^λ + εu) creates stable interior fixed points (confirmed, single global basin).
6. No chaos in tested parameter range (all Lyapunov exponents < 0).
7. Spectral dimension ≈ 1 at all scales — orbit stays on 1D arc. Falsified.

## What failed

- Spectral dimension hypothesis: completely falsified — orbit is topologically 1D.
- RDT weighting: does not change qualitative behavior.
- Fractal geometry: not observed.

The fundamental reason everything is 1D: the Eisenstein constraint fixes Λ and reduces the
SdS phase space to a single parameter x = r_b/r_c ∈ (0,1). Working in Eisenstein coordinates
(u,v) does not escape this 1D constraint — it's just a reparameterization of the same arc.

## What variables are trustworthy

All of these are derived from exact Vieta formulas, confirmed numerically:
- M, Λ — the two independent SdS physical parameters
- r_b, r_c — from solving the depressed cubic given (M, Λ)
- T_b = (1 - Λr_b²)/(4πr_b), T_c = (Λr_c² - 1)/(4πr_c)
- S_b = πr_b², S_c = πr_c²
- Δ = √(S_b S_c) = πr_b r_c
- ∂Δ/∂M = 1/T_c - 1/T_b  (proved exactly in sds_entropy_paper.md, Prop 4.2)
- ∂Δ/∂S_c = -η_C = -(1-x²)/(1+2x)  (proved exactly, Prop 4.3)
- x = r_b/r_c ∈ (0,1) parameterizes the SdS arc

## Scalar field usefulness audit

### RDT scalar field (from uploaded code screenshots and PDF)

**What it is**: φ(x,y) = R(⌊√(x²+y²)⌋), where R(n) = RDT depth of n =
number of times you divide by ⌊log(n)^α⌋ before reaching ≤ 1.

**What it produces**: An integer-valued step function on Euclidean 2D space.
Level sets are approximately circular (shown in the contour plots). The function
takes values in {0, 1, 2, 3, 4} over r ∈ [0, 200].

**Mathematical compatibility with SdS**:
- For Λ = 1: r_b, r_c ∈ (0, √3) ≈ (0, 1.73). So floor(r_b) ∈ {0, 1}, floor(r_c) ∈ {0, 1}.
  The RDT depth is R(0)=0 or R(1)=0 — the field takes value 0 everywhere in the SdS phase space.
  **USELESS as a state variable at Λ=1.**
- For Λ = 0.001: r_b, r_c ∈ (0, ~54.8). Then floor(r) ∈ {0,...,54}. R takes values 0-2.
  Still only 3 possible values — discontinuous step function.
- The function is NOT a scalar field in the physics sense (not smooth, not satisfying any field equation).
- Contours are circles (isotropy of the RDT depth in r), NOT the same geometry as SdS horizons.
- There is no natural coupling of φ to the SdS metric or thermodynamics.
- Adding φ as a state variable would add at most 2-3 discrete values — not genuine independent degrees of freedom.

**VERDICT: NOT USEFUL. The RDT field is a number-theoretic visualization tool
on Euclidean space. It has no physical connection to curved spacetime thermodynamics
and takes only 0-2 distinct values over the SdS parameter space.**

### Recursive Entropy in Geometric Subdivision (docx)

**What it is**: A framework for Shannon entropy on recursively binary-subdivided
geometric spaces. Main result: S(d)/(nd) → 1 for uniform distributions. "Geometric
constants" = surface-to-volume ratios of standard shapes.

**Relevance to this project**:
- This is Shannon entropy of probability distributions, NOT Bekenstein-Hawking entropy.
- The "normalization theorem" S(d)/(nd) = 1 is proved in one line and is trivially true.
- Surface-to-volume ratios are standard geometry, irrelevant to SdS horizon thermodynamics.
- The framework cannot be coupled to the SdS entropy identity without arbitrary ad hoc assumptions.

**VERDICT: NOT RELEVANT. Wrong type of entropy. Results are trivially true for
uniform distributions. No connection to the physics of this project.**

### Reid Law of Recursive Entropy (docx, "5/4 constant")

**What it is**: A hypothesis that entropy grows as Ω_n ∝ (5/4)^n, giving
S_n = k_B * n * ln(5/4). The "Reid Constant" ℜ = 5/4 is introduced without derivation
from physical principles.

**Compatibility with SdS results**:
- The SdS entropy identity S_Λ = S_b + S_c + √(S_b S_c) is a fixed algebraic relation,
  not a growth law.
- The constant 5/4 appears nowhere in the exact SdS thermodynamics.
- The claim that entropy grows at a fixed rate per recursive step contradicts the exact
  result that entropy budget S_Λ is CONSTANT under our Eisenstein recursion (not growing).
- This is an unsupported speculation; the "proof" just substitutes the assumed form into
  Boltzmann entropy without derivation of the 5/4 from anything.

**VERDICT: NOT INCORPORATED. Unsupported speculation with no physical derivation.
The 5/4 constant is arbitrary and inconsistent with the exact SdS entropy structure.**

## What the upgrade must actually do

The old model's limitation: works in Eisenstein coordinates (u,v) on a 1D arc at FIXED Λ.

The only genuine ways to escape the 1D limitation:
1. Allow Λ to vary → work in 2D (M, Λ) parameter space
2. Add charge Q → work in (M, Q, Λ) for RNdS (genuinely 3D parameter space)
3. Both simultaneously

A recursive flow in 2D or 3D parameter space traces a genuinely higher-dimensional orbit.
If the orbit has intrinsic dimension > 1, the spectral dimension test will measure > 1.

## Labeling of flows to be built

Following the requirement to label every flow:

A. **Physically motivated flows** (derived from exact SdS/RNdS identities):
   - M-gradient flow: dM = -η * (1/T_c - 1/T_b) with fixed Λ
     (∂Δ/∂M = 1/T_c - 1/T_b is PROVED in sds_entropy_paper.md Prop 4.2)
   - RNdS charge-gradient flow: uses ∂(total deficit)/∂Q derived numerically

B. **Mathematically convenient flows** (preserve structure but not uniquely derived):
   - Eisenstein-normalized flows in (u,v) at fixed Λ (old model, baseline)
   - Constant-x ratio flow: M_{d+1} = F(M_d) with r_b/r_c fixed

C. **Exploratory / constructed flows** (no derivation from first principles):
   - Coupled (M, Λ) flows
   - (M, Q) cross-coupled flows in RNdS
   - Any map that involves free parameters beyond the physical gradient

All flows will be clearly labeled with one of these three categories in code comments.
