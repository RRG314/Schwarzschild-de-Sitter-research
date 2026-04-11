# Experiment Plan

**Project:** Spectral Horizon Research
**Date:** April 2026
**Status:** All 5 experiments complete and passed.

---

## Design Philosophy

The experiment plan was organized around five sequentially deeper questions. Each experiment is self-contained: it runs, writes JSON output to `results/`, and generates figures in `figures/`. A master orchestrator (`run_all.py`) runs all five and records pass/fail status.

The experiments were designed to be honest about expected outcomes. Three were expected to be negative (symmetry check, full Eisenstein structure, RDT correlation), and the design explicitly planned to quantify *how negative* rather than seeking to confirm positive results. The Lambda-scaling law was expected positive and was used as a validation benchmark. The spectral-thermodynamic correspondence (EXP03 TEST 4) was genuinely exploratory.

---

## Experiment Descriptions

### EXP01: WKB Baseline

**File:** `exp01_wkb_baseline.py`
**Goal:** Validate the WKB implementation and establish baseline QNM properties.

**Tests:**
1. *Potential boundary conditions:* Verify V(r_b) = V(r_c) = 0 to floating-point precision. This is a necessary condition for the WKB boundary conditions.
2. *Schwarzschild limit:* At x = 0.02, Λ = 10⁻⁴, compare to known Schwarzschild QNMs (Leaver 1985). This tests whether the implementation is consistent with the known literature.
3. *WKB order convergence:* Compare 1st-order to 3rd-order; the relative correction should be < 20% for reliable results.

**Expected outcome:** Tests 1 and 3 should pass. Test 2 may show large error because the SdS potential at small Λ is numerically different from the Schwarzschild potential even at small Λ (the f(r) correction terms are different).

**Actual outcome:** See §05_results_and_analysis.

---

### EXP02: Lambda-Scaling Law

**File:** `exp02_lambda_scaling.py`
**Goal:** Confirm or refute the dimensional prediction ω/√Λ = F(x, l, n).

**Tests:**
1. *Scaling law verification:* At each x ∈ {0.1, ..., 0.9}, vary Λ over [0.01, 10.0]. Measure fractional std of ω_re/√Λ across Λ values. Should be < 1% if law holds.
2. *F(x) mapping:* Compute the full curve F_re^{l,n}(x) for l = 2,3,4 and n = 0,1 at Λ = 1.
3. *Q universality:* Show that Q = Re(ω)/|Im(ω)| is Λ-independent at fixed x.
4. *Algebraic structure probe:* Does Q(x) have a simple polynomial form? Does it correlate with η_C(x)?

**Expected outcome:** Scaling law confirmed (it follows from dimensional analysis). Q universality confirmed. Q(x) simple form: unknown.

---

### EXP03: Eisenstein Structure in QNM Spectrum

**File:** `exp03_eisenstein_spectral.py`
**Goal:** Test for Eisenstein algebraic structure in QNM frequencies.

**Tests:**
1. *x → 1−x symmetry:* Is ω(x) ≈ ω(1−x)? (No known reason it should be.)
2. *Overtone ratio:* Is ω_{l,1}/ω_{l,0} algebraically simple in x?
3. *Eisenstein norm:* Is Re(ω)² + Re(ω)Im(ω) + Im(ω)² / Λ constant or simply related to x?
4. *QNM vs thermodynamics:* Correlate Q, Re(ω)/√Λ, Im(ω)/√Λ with T_b, T_c, η_C.

**Expected outcome:** Tests 1–3: negative (the Eisenstein structure of SdS is thermodynamic, not spectral). Test 4: exploratory.

---

### EXP04: Inverse Horizon Spectroscopy

**File:** `exp04_inverse_spectroscopy.py`
**Goal:** Can x = r_b/r_c be recovered from observable frequency ratios?

**Approach:**
1. Build inversion maps G_l(x) = Re(ω_{l,1})/Re(ω_{l,0}) and S_{32}(x) = Re(ω_{3,0})/Re(ω_{2,0}).
2. Test monotonicity. If monotone, build interpolated inverse.
3. Test inversion accuracy (no noise), then under 0.5%–5% frequency noise.
4. Test that G_l is Λ-independent (should hold since both modes scale as √Λ).

**Expected outcome:** The cross-mode ratio S_{32} is likely weakly dependent on x (both l=2 and l=3 fundamental modes shift together with x). The overtone ratio G_l is more variable but less reliable. Invertibility: uncertain.

---

### EXP05: RDT Overtone Hierarchy

**File:** `exp05_rdt_overtone.py`
**Goal:** Honest test of whether RDT depth of overtone index n reveals spectral structure.

**Approach:**
1. Compute ω_n for n = 0..60 using WKB-1 at l = 10, x = 0.5.
2. Assign RDT depth R(n+1) to each overtone.
3. Compare Shannon entropy of RDT grouping vs. uniform grouping of Im(ω).
4. Fit Im(ω) vs. n linearly (the known WKB prediction).
5. Correlate residuals from linear fit with RDT depth.

**Expected outcome:** NEGATIVE. RDT depth of n is arithmetic and has no physical meaning for QNMs. The linear fit to Im(ω) should absorb essentially all variation.

**Caveat built into design:** At WKB-1, Im(ω_n) = Im(√(V₀ − i(n+½)C)), which is *not* exactly linear in n because of the sqrt. For large n, the imaginary term dominates and Im(ω_n) deviates from linearity. This nonlinearity also increases with n (growing deviation from linear fit), creating a correlation with RDT depth (which also increases with n) that is an arithmetic artifact.

---

## Technical Notes

**WKB implementation:** 3rd-order Iyer-Will (1987). Derivatives V₀, V₀'', V₀''', V₀'''' computed by finite differences at the potential maximum located by golden-section search.

**Convergence criterion:** `|Δ₂| < 0.5 |Λ_n|` where Δ₂ is the 2nd-order WKB correction and Λ_n = −i(n+½). For n=0 this is almost always satisfied. For n=1 it frequently fails, meaning WKB-3rd is unreliable for n=1. This does not prevent computing the frequency; it means the result carries larger systematic uncertainty.

**JSON serialization:** All experiments write results using a custom `NumpyEncoder` that handles numpy scalar and array types. Complex numbers are serialized as `{re: ..., im: ...}` dicts.

**Runtime:** Full suite runs in approximately 10 seconds on a single core.

---

## How to Re-Run

```bash
cd spectral_horizon_research
python experiments/run_all.py
```

All experiments should complete with status PASS. Results are written to `results/` and figures to `figures/`.
