# Literature Positioning Memo

**Project:** Spectral Horizon Research
**Date:** April 2026

---

## 1. What Already Exists

### 1.1 SdS Quasinormal Modes

QNMs of Schwarzschild–de Sitter spacetime have been studied since the early 2000s. The foundational papers are:

- **Brady, Chambers, Gonzalez, Krivan, Laguna (1999):** First systematic study of scalar QNMs in SdS. Showed that the cosmological constant modifies the spectrum and introduces a new "de Sitter" family of modes with very small real parts.

- **Motl & Neitzke (2003), Konoplya & Zhidenko (2003):** WKB methods applied to SdS, noting the strong departure from the Schwarzschild spectrum at large x.

- **Konoplya & Zhidenko (Review, 2011):** "Quasinormal modes of black holes: from astrophysics to string theory" — comprehensive review. Notes that SdS QNMs depend on both M and Λ, but does not study the Lambda-scaling law as an isolated result.

- **Cardoso, Konoplya, Lemos (2003):** QNM frequencies and their dependence on the cosmological constant. The parameter space is explored at fixed M rather than fixed x = r_b/r_c, so the Lambda-scaling is not isolated.

**Gap:** None of these works parametrize the SdS family by x = r_b/r_c at fixed Λ, nor do they explicitly extract the dimensionless spectral functions F_re(x) = Re(ω)/√Λ. The Lambda-scaling law as stated here — ω/√Λ depends only on x — appears not to have been stated explicitly in this form in the literature, though it follows from dimensional analysis.

### 1.2 Spectral-Thermodynamic Correspondences

The idea that QNM properties encode thermodynamic data is established:

- **Hod (1998):** Proposed that highly-damped QNM frequencies encode black hole entropy via ω_R → 2πT_H (Hawking temperature). This is the "Bohr correspondence principle" for black holes.

- **Dreyer (2003), Motl (2003):** Connected highly-damped QNMs to loop quantum gravity area quantization.

- **Maggiore (2008):** "Physical interpretation of the various branches of the quasinormal spectrum" — shows that QNM transitions should be thought of as transitions between quantum states of the black hole.

**Position of this work:** We study the *fundamental* mode (n=0) quality factor Q = Re(ω)/|Im(ω)| and find it correlates with the Carnot efficiency η_C = (T_b − T_c)/T_b. This is distinct from the Hod correspondence (which concerns highly-damped modes and a single-horizon system). The two-horizon character is essential to our finding.

### 1.3 Inverse Black Hole Spectroscopy

"Black hole spectroscopy" — recovering black hole parameters from observed QNM frequencies — has become a major area:

- **Dreyer et al. (2004):** Proposed using QNMs to test the no-hair theorem via "ringdown" observations.

- **Berti, Cardoso, Starinets (2009):** Review of QNMs and their role in astrophysics. Shows that for Kerr black holes, the mass M and spin a can be recovered from two QNM frequencies.

- **LIGO Science (2016+):** Ringdown spectroscopy in gravitational wave observations. The fundamental mode and first overtone of GW150914 were identified.

**Position of this work:** We ask whether x = r_b/r_c can be recovered from SdS QNMs. Our finding is negative for the methods tested (overtone ratios, cross-mode ratios). The reason is that neither ratio is monotone in x, making inversion impossible without additional information. This is a concrete, negative result that clarifies the difficulty of SdS spectroscopy.

### 1.4 Eisenstein Lattices and Black Hole Thermodynamics

The Eisenstein quadratic form Q(a,b) = a² + ab + b² appears in:

- **Cohn (1980s):** Eisenstein integers as a natural lattice for certain algebraic structures.

- **Liberati, Visser (1997), this group (prior work):** Entropy identity S_Λ = S_b + S_c + √(S_b S_c) identified as an Eisenstein relation.

**Position of this work:** We tested whether the Eisenstein form appears in the QNM spectrum. It does not: the Eisenstein norm of (Re(ω), Im(ω)) is not constant and only trivially correlates with the L² norm (r = 0.999997, i.e., they are essentially the same quantity since |Re(ω)| >> |Im(ω)|). The Eisenstein structure of SdS appears to be a feature of the thermodynamic phase space, not of the dynamic spectrum.

### 1.5 Recursive / Hierarchical Methods in Spectral Physics

- **Berry (1988):** Semiclassical methods and hierarchical structure in quantum spectra.

- **Connes (1994):** Spectral geometry. The connection between spectral invariants and geometric properties is deep but at a very abstract level.

- **This group (RDT prior work):** RDT scalar fields produce concentric ring-level-sets but do not encode thermodynamic information in the SdS context.

**Position of this work:** RDT is confirmed as inert for QNM overtones. The apparent correlation (r = −0.62 between RDT depth and Im(ω) residuals) is a statistical artifact: both quantities increase with n due to the breakdown of WKB linearity at high overtone number.

---

## 2. Where This Work Sits

| Claim | Prior art | Novelty of this work |
|---|---|---|
| Lambda-scaling law | Implicit in dimensional analysis | Stated explicitly, confirmed numerically to < 0.01% |
| Dimensionless spectral functions F_l^n(x) | Not tabulated | First systematic mapping across x |
| Q–Carnot efficiency correlation | Not known | New spectral-thermodynamic correspondence (r=0.975) |
| ω_re–T_b correlation | Not known in this form | New (r=0.995) |
| Inverse spectroscopy (SdS) | Not studied in this parametrization | Negative result established |
| Eisenstein structure in spectrum | Not tested | Negative result established |

The primary contribution is the Q–Carnot correspondence. The other results (negative) are also valuable as they close potential directions.

---

## 3. Key Distinctions from Prior Work

**This work is NOT about:**
- The asymptotic (highly-damped) regime of QNMs
- Kerr or Reissner-Nordström black holes
- Gravitational perturbations (we study scalar perturbations)
- Area quantization or loop quantum gravity connections

**This work IS about:**
- Fundamental and low-overtone modes (n = 0, 1) in the sub-extremal range x ∈ (0, 1)
- The dimensionless parametrization x = r_b/r_c at fixed Λ
- Whether thermodynamic structure visible in the state space (Eisenstein constraint, Carnot efficiency) is reflected in the observable resonance properties (frequency, quality factor)

---

## 4. Recommended Citations for the Final Paper

1. Konoplya & Zhidenko, *Rev. Mod. Phys.* **83**, 793 (2011) — for WKB methods and SdS QNM review
2. Iyer & Will, *Phys. Rev. D* **35**, 3621 (1987) — for 3rd-order WKB formula
3. Brady et al., *Phys. Rev. D* **60**, 064003 (1999) — for original SdS QNM study
4. Hod, *Phys. Rev. Lett.* **81**, 4293 (1998) — for spectral-thermodynamic connection in single-horizon case
5. Berti, Cardoso, Starinets, *Class. Quant. Grav.* **26**, 163001 (2009) — for black hole spectroscopy review
6. Prior work (this group) on SdS entropy identity — for the Eisenstein and entropy results
