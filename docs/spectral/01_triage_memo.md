# Triage Memo: Repository Scan and Direction Selection

**Project:** Recursive Spectral Geometry of Horizons
**Date:** 2026-04-10
**Status:** Phase 1 complete

---

## A. Relevant Prior Work in the Repository

### What Exists

**1. SdS entropy identity and Eisenstein geometry (DONE, strong)**
- `sds_entropy_paper.md`: Derives S_Λ = S_b + S_c + sqrt(S_b S_c) from Vieta relations. Proves polynomial closure exists iff D ∈ {4, 5}.
- `eisenstein_carnot_paper.md`: Shows SdS phase space is an arc of the Eisenstein ellipse u² + uv + v² = 1. Carnot efficiency is a geometric invariant. j-invariant formula j = 1728/(1 − 9ΛM²). Product j · Δ_cubic = const at fixed Λ.
- `sds_entropy_structure.md`: Supplementary notes.
- **Status: Complete and published-quality. Do not redo.**

**2. Recursive parameter flows and spectral dimension (DONE, negative result)**
- `recursive_spacetime_system/`: Full (M, Λ)/(M, Q, Λ) parameter space system.
- `RESULTS.md`: All physically motivated flows have d_s ≈ 1. RDT scalar field φ = 0 everywhere on SdS. Scalar field NOT USEFUL. Reid Law NOT SUPPORTED.
- **Status: Honest negative result. Useful as contrast only.**

**3. Recursive horizon project (DONE, preliminary)**
- `recursive_horizon_project/`: Graph spectral analysis on recursively sampled horizon state space.
- RDT weighting experiment (exp05) tested whether RDT-weighted graph Laplacian spectrum differs from uniform weighting.
- **Status: Preliminary. Findings: RDT weighting does not add detectable structure over uniform weighting on the SdS arc.**

**4. Correction gap principle (DONE, partial)**
- `correction_gap_formalization.md`: Theorem schema for when naive approximations cannot be exactly corrected within an operator class.
- SdS gap theorem: S_b + S_c ≠ S_Λ (additivity fails), and the gap Δ = sqrt(S_b S_c) is not in the span of polynomial operators of degree < 2 in (S_b, S_c).
- **Status: Useful as a structural principle. Not directly relevant to spectral geometry.**

**5. RDT scalar field (uploaded PDF + screenshots)**
- `rdt_log_depth(n, alpha=1.5)`: Depth by repeated division by floor(log(n)^alpha). Minimum divisor 2.
- Scalar field φ(x, y) = R(floor(sqrt(x² + y²))): concentric annular level sets. R(n) ∈ {0, 1, 2, 3, 4} for n ≤ 1000.
- R(n) is slow-growing, non-monotone, integer-valued, discontinuous. Level sets are annuli at integer radii.
- **Key fact from EXP04:** On SdS, r_b, r_c < sqrt(3/Λ) ≈ 1.73 at Λ = 1. So floor(r) ∈ {0, 1}, R = 0 everywhere. RDT is inert on the natural SdS coordinate scale.
- **Status: Useful in a different coordinate regime. See Section B.**

**6. MHD closure documents (uploaded)**
- `MHD_closure.pdf`, `MHD_draft.pdf`: MHD Euler potential closure problem.
- Not relevant to black hole spectral geometry.

**7. Recursive Entropy in Geometric Subdivision (uploaded docx)**
- Title suggests connection to RDT in geometric subdivision contexts.
- Content not readable as text. Assumed to contain recursive partition entropy results.
- **Status: Potentially relevant for understanding RDT's geometric depth structure, but not directly applicable to QNM spectral analysis.**

---

### What is Useful

| Material | Usefulness | Why |
|---|---|---|
| SdS entropy identity + Eisenstein geometry | High (as background) | Establishes exact algebraic structure of SdS phase space. Coordinates (u, v) and x = r_b/r_c are the right parameterization. |
| j-invariant formula | High | Connects mass parameter to algebraic invariant. |
| Correction gap paper | Moderate | Structural template: shows how to prove "exact reconstruction is possible iff..." |
| Recursive parameter flows | High (as negative contrast) | Confirms d_s ≈ 1, RDT scalar field fails. Avoids wasting time on those dead ends. |
| RDT scalar field code | Moderate | Usable for overtone hierarchy analysis at large overtone numbers (n >> 1) where floor(n) is nontrivial. |
| RDT depth function R(n) | Moderate | Provides a hierarchical labeling of integer sequences. Applicable to overtone towers at large n. |

### What is Not Useful

- SdS entropy identity derivation itself (done).
- Eisenstein arc visualization (done).
- Scalar field as horizon state variable (proved inert).
- Reid Law (5/4 constant) (no physical basis found).
- MHD documents (different problem).

---

## B. Best-Fit Uses of RDT for This Project

The RDT function R(n) counts the number of recursive division steps to reduce an integer n to 1. It creates a hierarchy of depth levels on positive integers. For large n, R(n) reaches depths 3-4. Level sets are annular bands.

**B.1 Adaptive partitioning of the QNM overtone tower**
Classification: **moderate fit**
The overtone sequence {ω_n : n = 0, 1, 2, ...} is an infinite tower. RDT provides a natural recursive grouping: overtones at RDT depth 0 (n = 1), depth 1 (small n), depth 2 (medium n), depth 3-4 (large n approaching Motl-Neitzke asymptotic). This can be tested: do overtones at the same RDT depth share spectral properties?

**B.2 Multiscale decomposition of the effective potential**
Classification: **weak fit**
The effective potential V(r) is a smooth bump. An RDT-inspired decomposition would sample it at radii r = 1, 2, 3, ... with depth labels R(floor(r)). For SdS at Λ = 1 the relevant radii are < 2, so this has the same floor-of-r problem as before. At Λ << 1 (large BH regime), r_b, r_c can be >> 1 and RDT becomes nontrivial.

**B.3 Recursive indexing of the QNM spectrum across (l, n)**
Classification: **weak fit**
The 2D array ω_{l,n} could be organized by RDT of the pair (l, n), but there is no physical reason this decomposition would reveal structure that simple (l, n) ordering does not.

**B.4 Inverse reconstruction from partial spectral data**
Classification: **no fit**
Inverse spectroscopy (recovering x from QNM frequencies) is a standard numerical inversion problem. RDT adds nothing here.

**B.5 Parameter-space segmentation of (M, Λ) flows**
Classification: **no fit**
Already tested in recursive_spacetime_system. Negative result.

**Summary of RDT fit:**
RDT has a moderate fit in the overtone hierarchy analysis at large overtone numbers, and a weak fit for multiscale potential decomposition in the large-BH (small Λ) regime. RDT has no fit for the core spectral inversion problem. This should be stated clearly in the documents: the project is primarily a spectral geometry project, and RDT contributes a supplementary analysis of the overtone tower hierarchy.

---

## C. Candidate Research Directions

**Direction 1: Λ-scaling laws and Eisenstein invariants in SdS QNM spectra (PRIMARY)**
Observation: Under r → λr with M → λM and Λ → Λ/λ², the SdS potential scales as V → V/λ², so ω → ω/λ. Since r_c ∝ Λ^{−1/2} at fixed x, this predicts ω ∝ Λ^{1/2}. The dimensionless QNM frequency ω/sqrt(Λ) should depend only on x = r_b/r_c (and l, n).
- **Novel question:** Is ω/sqrt(Λ) an algebraic function of x? Does it respect the Eisenstein arc? Is there a QNM-level identity analogous to the entropy identity?
- **Testable:** Compute WKB QNMs over the (x, Λ) parameter grid, verify scaling, study the x-dependence.
- **Potentially novel:** The Eisenstein constraint has not been studied in the context of QNM frequencies. An exact or approximate algebraic relation among QNM frequencies analogous to S_Λ = S_b + S_c + sqrt(S_b S_c) would be new.

**Direction 2: Inverse horizon spectroscopy from QNM ratios**
Given two QNM frequencies (ω_{l,0}, ω_{l,1}) from the same angular number l, the ratio ω_{l,0}/ω_{l,1} is Λ-independent (Λ cancels in the ratio). This ratio is a function of x alone and can be inverted to recover x. This is a concrete inverse spectroscopy protocol.
- **Novel:** The specific role of the Eisenstein constraint in making this inversion exact vs. approximate has not been studied.
- **Testable:** Construct inversion maps, test accuracy, quantify error.
- This is a secondary result within Direction 1.

**Direction 3: RDT-structured overtone decomposition at large n**
For large overtone number n (>> 100), the SdS QNM spectrum approaches a Motl-Neitzke-like asymptotic. The approach to this asymptotic has corrections in 1/n. Applying RDT to the overtone index n gives a hierarchical grouping. Does the residual structure (deviation from asymptotic) exhibit RDT-correlated patterns?
- **Honest assessment:** This is speculative. The RDT depth of an integer n is not obviously connected to the 1/n power-series expansion of QNM corrections.
- **Role:** A supplementary experiment. Negative result is fine and expected to be honest.

**Direction 4: Spectral dimension of the QNM parameter manifold**
Instead of computing spectral dimension of flows (already done, d_s ≈ 1), compute the spectral dimension of the QNM manifold: the set {ω_{l,n}(x) : l, n fixed} as x sweeps the Eisenstein arc. Does the spectral manifold have nontrivial dimensionality in frequency space?
- **Assessment:** Likely d_s ≈ 1 again (x is 1D), but the embedding in frequency space could be nontrivial.
- **Role:** A diagnostic check, not the primary question.

**Direction 5: Recursive potential reconstruction from spectral data**
Given the QNM spectrum, reconstruct V(r) using a recursive algorithm: Level 0 uses ω_0 to estimate V_max, Level 1 uses ω_0 and ω_1 to estimate V_max and V_max'', Level 2 adds higher-order corrections. This is a recursive inverse spectral reconstruction.
- **Assessment:** Technically interesting but likely replicates known WKB inversion procedures. True novelty would require showing the recursive structure reveals something the direct WKB inversion does not.

---

## D. Direction Choice

**Primary direction: Λ-scaling laws and Eisenstein geometry of SdS QNM spectra, with an inverse horizon spectroscopy protocol.**

**Why this is best:**
1. It is a natural continuation of the existing Eisenstein geometry work — extending from thermodynamic observables (entropy, temperature) to dynamical observables (QNM frequencies).
2. The Λ-scaling law (ω/sqrt(Λ) depends only on x) is a clean, testable prediction with a rigorous dimensional argument supporting it.
3. If the x-dependence of ω/sqrt(Λ) respects the Eisenstein arc structure, that is a new result: the QNM spectrum would carry the same geometric fingerprint as the entropy spectrum.
4. The inverse spectroscopy protocol (recovering x from a frequency ratio) is physically relevant: QNMs are detectable via gravitational waves, and x encodes the ratio of the two horizon radii.
5. The mathematics is clean (WKB for SdS is well-defined) and the computations are tractable.

**Why alternatives were rejected:**
- Direction 3 (RDT overtone hierarchy): Too speculative. The connection between RDT depth and QNM corrections is not motivated. Will run as a supplementary check, expected to return a negative result.
- Direction 4 (spectral dimension of QNM manifold): Almost certainly d_s ≈ 1 since x is 1D. Not worth primary focus.
- Direction 5 (recursive potential reconstruction): Likely to replicate known WKB inversion; would need a strong new angle to be worth pursuing.

**One important caveat:**
The Λ-scaling argument is based on dimensional analysis and is therefore not surprising by itself. The potentially novel contribution is in (a) the specific form of the x-dependence of the dimensionless QNM frequencies and how it relates to the Eisenstein arc, and (b) whether any exact algebraic identity holds (not just approximate). If the numerics show only smooth generic dependence on x with no special algebraic structure, the result reduces to a verification of dimensional analysis, which is useful but not novel.

This risk is explicitly recorded. If experiments return only smooth generic dependence, the honest conclusion is: dimensional scaling holds, Eisenstein structure does not extend to QNMs, and the entropy identity is not mirrored spectrally.
