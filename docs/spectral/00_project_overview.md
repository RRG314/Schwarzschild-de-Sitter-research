# Recursive Spectral Geometry of Horizons: Project Overview

**Project:** Spectral_Horizon_Research
**Date:** April 2026
**Principal focus:** Quasinormal mode spectra of Schwarzschild–de Sitter black holes, with emphasis on Lambda-scaling structure, spectral-thermodynamic correspondences, and prospects for inverse horizon spectroscopy.

---

## What This Project Is

This project investigates whether the known geometric and thermodynamic structure of Schwarzschild–de Sitter (SdS) spacetime — specifically the Eisenstein constraint and the exact entropy identity — is reflected in the observable quasinormal mode (QNM) spectrum of scalar perturbations.

SdS spacetime is the unique two-horizon black hole solution with positive cosmological constant Lambda. Its parameter space is one-dimensional at fixed Lambda: every sub-extremal solution is labeled by the single ratio x = r_b/r_c ∈ (0,1), where r_b is the black-hole horizon radius and r_c is the cosmological horizon radius. Prior work by this group established exact algebraic relations among the entropy, temperature, and mass observables at each point in this space. The natural next question is: does the QNM spectrum — the resonant frequencies of the spacetime — carry analogous algebraic structure?

---

## Connection to Prior Work

This project builds on two completed threads:

**Thread 1 (SdS thermodynamics):** The entropy identity S_Λ = S_b + S_c + √(S_b S_c) is exact and follows from the Eisenstein constraint r_b² + r_b r_c + r_c² = 3/Λ. The temperature ratio T_b/T_c and the Carnot efficiency η_C = (T_b − T_c)/T_b were mapped across the full parameter space. This work is considered complete.

**Thread 2 (RDT scalar field):** The Recursive Depth Transform was studied as a standalone mathematical object producing concentric ring-like level sets in the plane. Prior experiments confirmed RDT is essentially inert when applied naively to SdS thermodynamic quantities.

This project does NOT redo either of those threads. It opens a new direction: the spectral geometry of the two-horizon potential barrier.

---

## Research Questions

The five primary questions investigated are:

1. **Lambda-scaling law:** Does ω/√Λ depend only on x (and l, n), with no residual Λ dependence?

2. **Eisenstein structure:** Do QNM frequencies or their combinations exhibit algebraic simplicity in terms of the Eisenstein variables (r_b, r_c, or S_b, S_c)?

3. **Spectral-thermodynamic correspondence:** Are there combinations of QNM frequencies that directly encode thermodynamic quantities such as the horizon temperatures T_b, T_c, or the Carnot efficiency η_C?

4. **Inverse spectroscopy:** Can the horizon ratio x = r_b/r_c be recovered from observable frequency ratios alone (without knowing Λ)?

5. **RDT overtone hierarchy:** Does grouping QNM overtones by RDT depth of the overtone index n reveal structure beyond the known linear dependence Im(ω_n) ~ n?

---

## Repository Structure

```
spectral_horizon_research/
├── src/
│   ├── sds_physics.py        # SdS spacetime geometry and effective potential
│   ├── wkb_qnm.py            # WKB QNM computation (1st, 3rd, 6th order)
│   ├── rdt_tools.py          # Recursive Depth Transform utilities
│   └── json_utils.py         # NumPy-aware JSON encoder
├── experiments/
│   ├── exp01_wkb_baseline.py      # Potential validation and Schwarzschild limit
│   ├── exp02_lambda_scaling.py    # Lambda-scaling law and Q(x) universality
│   ├── exp03_eisenstein_spectral.py   # Eisenstein structure and QNM-thermodynamics
│   ├── exp04_inverse_spectroscopy.py  # Inverse horizon spectroscopy
│   ├── exp05_rdt_overtone.py          # RDT overtone hierarchy
│   └── run_all.py             # Orchestrator
├── results/
│   └── *.json                 # Numerical results (all 5 experiments)
├── figures/
│   └── *.png                  # Generated figures (all 5 experiments)
└── research_docs/
    ├── 00_project_overview.md     ← this file
    ├── 01_triage_memo.md
    ├── 02_literature_positioning.md
    ├── 03_mathematical_framework.md
    ├── 04_experiment_plan.md
    ├── 05_results_and_analysis.md
    └── 06_next_steps.md
```

---

## Summary of Key Results

All five experiments passed on the first clean run after bug fixes. The headline results are:

| Result | Finding |
|---|---|
| Lambda-scaling law | Confirmed: ω/√Λ constant to < 3.4×10⁻⁵ fractional variation |
| Q universality | Q = Re(ω)/\|Im(ω)\| is Λ-independent; range [2.28, 3.35] across x |
| Q–Carnot correspondence | Q and Carnot efficiency η_C are strongly correlated: r = 0.975 |
| ω_re–T_b correspondence | Re(ω)/√Λ and T_b/√Λ correlated at r = 0.995 |
| Eisenstein norm in ω | NOT constant (std/mean = 2.16); no Eisenstein structure in frequencies |
| x→1−x symmetry | NOT present; max deviation 9.1× for l=2 |
| Overtone ratio inversion | FAILS: G_l(x) not monotone, not Λ-independent at WKB-3rd |
| Cross-mode ratio inversion | FAILS: S₃₂(x) not monotone, range only [1.04, 1.20] |
| RDT overtone analysis | Spurious; confounded by n-dependence of WKB accuracy |

The most significant new finding is the tight spectral-thermodynamic correspondence: the quality factor Q of the fundamental QNM resonance tracks the Carnot efficiency of the thermodynamic "engine" formed by the two-horizon system. This is a genuine connection between spectral and thermodynamic structure that warrants further investigation.

---

*See individual documents 02–06 for full analysis.*
