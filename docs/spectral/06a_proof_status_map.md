# Proof Status Map

**Project:** Spectral Horizon Research
**Date:** April 2026
**Purpose:** Single-page master status of every mathematical claim in the project. One row per claim. This is the reference for deciding what goes into the paper as a result, a conjecture, or a negative finding.

---

## Status Codes

| Code | Meaning |
|---|---|
| T | Theorem: proved with full rigorous derivation |
| C | Corollary: follows immediately from a theorem |
| E | Empirical: confirmed numerically, not proved analytically |
| J | Conjecture: plausible, not confirmed |
| N | Negative: tested and found false, with mechanism identified |
| A | Artifact: confirmed as a computational error |
| O | Open: insufficient evidence to classify |

---

## Master Table

| ID | Claim | Status | Confidence | Evidence | Key limitation | Document |
|---|---|---|---|---|---|---|
| 1.1 | Eisenstein constraint r_b²+r_br_c+r_c²=3/Λ | T | 100% | ALG (Vieta) | None | 04b §Der.1 |
| 1.2 | Entropy identity S_Λ=S_b+S_c+√(S_bS_c) | C | 100% | From 1.1 | None | 04b §Der.2 |
| 1.3 | Horizon parametrization by x | T | 100% | ALG | None | 04b §Der.3 |
| 1.4 | T_b = (1−Λr_b²)/(4πr_b), T_c = (Λr_c²−1)/(4πr_c) | T | 100% | ALG (f') | None | 04b §Der.4 |
| 1.5 | η_C(x) = (1−x²)/(1+2x) [exact closed form] | T | 100% | ALG | None | 04b §Der.5 |
| 2.1 | Lambda-scaling law ω = √Λ·F(x,l,n) | T | 100% | DIM analysis | None | 04b §Der.6 |
| 2.2 | Lambda-scaling confirmed numerically (<3.4×10⁻⁵) | C+E | 99% | WKB3 (EXP02) | WKB accuracy | EXP02 |
| 2.3 | Q = Re(ω)/|Im(ω)| is Λ-independent | C | 100% | From 2.1 | None | 04b §Der.7 |
| 3.1 | WKB-1 formula (Schutz-Will) with tortoise V₀'' | E | N/A | Formula from literature | WKB approximation | 03b §3.3 |
| 3.2 | Tortoise correction V₀''_{r*}=f²·V₀''_r at maximum | T | 100% | ALG (chain rule) | None | 04b §Der.8 |
| 3.3 | F_re^{2,0}(x) monotone decreasing, range [1.68,8.64] | E | Moderate | WKB3 (EXP02) | F_re reliable (V₀ not affected by tort. bug) | EXP02 table |
| 3.4 | Q_WKB1(x) ≈ 5.07 ± 0.09 at l=2, n=0 (corrected) | E | Moderate | WKB1 + correction | WKB-1 accuracy at l=2 | 05b |
| 3.5 | Q(x,l) ~ √(l(l+1)) at large l | J | Low-moderate | Analytic WKB-1 estimate | Not computed; requires EXP06 | 05a |
| 4.1 | Q-Carnot correspondence (Q≈1.39η_C+2.04, r=0.975) | A | N/A | Artifact (coord error) | Wrong tortoise coordinate in code | 05b, 03a |
| 4.2 | Re(ω)/√Λ ≈ 15.86·T_b/√Λ+1.14 (r=0.995) | J | Low | WKB3+possible artifact | Monotone correlation; no analytic derivation | 04a Iss.8 |
| 4.3 | Eisenstein norm E(ω) ≈ |ω|² (r=0.999997) | E | High | WKB3 (EXP03) | Cross-term ~20% with correct Q | EXP03 |
| N1 | No x→1-x symmetry in QNM spectrum | N | High | WKB3 (EXP03); factor-5 mismatch | WKB accuracy; conclusion robust | 04c §N1 |
| N2 | Eisenstein form is NOT a spectral invariant | N | High | From 4.3 + analysis | See 04c §N2 | 04c §N2 |
| N3 | G_l not monotone at WKB-3rd; not Λ-indep. | N (conditional) | Moderate | WKB3 (EXP04) | WKB artifact for n=1; exact level open | 04c §N3 |
| N4 | S_{32} not useful for inversion (adjacent l) | N | High | WKB3 (EXP04) | Monotone correlation issue; large l gap untested | 04c §N4 |
| N5 | RDT overtone correlation = arithmetic artifact | N | High | WKB1 (EXP05) | Mechanism confirmed | 04c §N5 |
| O1 | Exact G_l(x) monotonicity | O | — | Requires Leaver | — | 04a §5.1, 05c |
| O2 | Exact Q(x, l=2) and its correlation with η_C | O | — | Requires Leaver | — | 05b §4, 05c |
| O3 | Q̃(x) = Q/√(l(l+1)) universal (l-independent) | O | — | Requires EXP06 | — | 05a §theory |
| O4 | Analytic derivation of Re(ω)-T_b slope 15.86 | O | — | Analytic WKB study | — | 05a §F_re |
| O5 | x→1/x symmetry in QNM spectrum | O | — | Not tested | — | 04c §N1 |

---

## Claims That Are Paper-Ready

These can appear in the paper without further computation:

| ID | Status | What to say in paper |
|---|---|---|
| 1.1 | T | Theorem 1: Eisenstein constraint (with proof) |
| 1.2 | C | Corollary: Entropy identity |
| 1.3 | T | Standard parametrization |
| 1.4 | T | Hawking temperatures (corrected formulas from 04b) |
| 1.5 | T | Theorem 2: η_C = (1−x²)/(1+2x) — new exact result |
| 2.1 | T | Theorem 3: Lambda-scaling law (with proof from dimensional analysis) |
| 2.3 | C | Corollary: Q is Λ-independent |
| 3.2 | T | Lemma: tortoise coordinate correction at maximum |
| 3.3 | E | F_re table at l=2, n=0 (reliable; V₀ not affected by bug) |
| 3.4 | E | Q_WKB1 ≈ const after correction (with caveat: WKB-1 at l=2) |
| 4.1 | A | Retraction: Q-Carnot correspondence was a coordinate artifact |
| N1 | N | No x→1-x symmetry |
| N2 | N | No Eisenstein structure in spectrum |
| N5 | N | RDT structure confirmed absent |

---

## Claims Requiring More Work Before Paper

| ID | What is needed |
|---|---|
| N3 | Leaver computation of exact G_l |
| O1 | Same |
| 3.5, O3 | EXP06: WKB-1 Q at l=6,10,20 with corrected tortoise |
| 4.2, O4 | EXP07: Re(ω)-T_b at multiple l; analytic WKB-1 derivation |
| O2 | Leaver implementation (EXP09) |

---

## Paper Structure Implication

Given the current status, a paper can be written now containing:

**Part 1 — Exact results (publishable immediately):**
- Theorems 1.1-1.5, 2.1, 2.3
- The η_C(x) = (1−x²)/(1+2x) closed form appears new in this parametrization
- Lambda-scaling law stated and proved (dimensional analysis)
- All are rigorous and require no additional computation

**Part 2 — Numerical results at WKB level:**
- F_re table (reliable)
- Lambda-scaling confirmation (reliable)
- All WKB Q and Im(ω) results flagged as WKB-1 approximations with coordinate notes

**Part 3 — Negative results:**
- No x→1-x symmetry (strong)
- No Eisenstein structure in spectrum (strong)
- No RDT structure (strong)
- No reliable inverse spectroscopy at WKB-3rd (conditional)
- Q-Carnot retracted as artifact (strong)

**Part 4 — Open questions and future directions:**
- Exact numerics needed (Leaver)
- High-l WKB needed for Q scaling
- Re(ω)-T_b correlation: physical content unclear
