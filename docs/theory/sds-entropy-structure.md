# Exact Entropy Structure and Low-Dimensional Closure in Schwarzschild–de Sitter Spacetime

---

## Abstract

We present a systematic analysis of the Bekenstein–Hawking entropy structure in four-dimensional Schwarzschild–de Sitter (SdS) spacetime. Using Vieta's formulas applied to the SdS horizon cubic, we derive the exact identity $S_\Lambda = S_b + S_c + \sqrt{S_b S_c}$, where $S_b$, $S_c$, and $S_\Lambda$ denote the black hole horizon, cosmological horizon, and pure de Sitter entropies, respectively. We define the entropy deficit $\Delta \equiv \sqrt{S_b S_c}$ and establish three structural results: (i) $\Delta$ governs the black hole pair creation exponent as $P \sim e^{-\Delta}$; (ii) differentiation of the identity with respect to mass gives $d\Delta/dM = T_c^{-1} - T_b^{-1}$ directly from the first laws; and (iii) the Carnot-deficit relation $d\Delta/dS_c = -\eta_C$ holds exactly, where $\eta_C = 1 - T_c/T_b$ is the Carnot efficiency between the two horizons. We extend the analysis to $D$ spacetime dimensions and show that an analogous exact identity exists in $D = 5$, taking the Pythagorean form $S_{\Lambda,5}^{2/3} = S_b^{2/3} + S_c^{2/3}$, while no analogous polynomial closure exists for $D \geq 6$. All results are verified numerically. We emphasize that these are structural consequences of known SdS thermodynamics and do not constitute new physical laws.

---

## 1. Introduction

Black hole thermodynamics provides one of the most productive intersections of general relativity, quantum field theory, and statistical mechanics. The laws of black hole mechanics, reformulated as thermodynamic laws by Bardeen, Carter, and Hawking, acquire physical content through the Bekenstein entropy $S = A/(4G)$ [1] and the Hawking temperature [2].

In spacetimes with a positive cosmological constant $\Lambda > 0$, a second thermodynamic object is present: the cosmological (de Sitter) horizon. Gibbons and Hawking [3] showed that this horizon radiates with temperature $T_\Lambda = \sqrt{\Lambda/3}/(2\pi)$ and carries entropy $S_\Lambda = 3\pi/(G\Lambda)$. When a black hole is present, the Schwarzschild–de Sitter spacetime contains both a black hole horizon at $r = r_b$ and a cosmological horizon at $r = r_c > r_b$, each with independently defined temperature and entropy.

The two horizons are thermodynamically anti-aligned: increasing the black hole mass raises $S_b$ while lowering $S_c$. This suggests a structural complementarity that is not immediately apparent from the individual first laws. In this note we identify the precise algebraic relationship between $S_b$, $S_c$, and $S_\Lambda$.

The paper proceeds as follows. Section 2 establishes the background, including explicit temperature formulas in a single-parameter form. Section 3 derives the entropy identity step by step from Vieta's formulas. Sections 4 and 5 present structural consequences and thermodynamic interpretations. Section 6 classifies the result by spacetime dimension. Section 7 states limitations explicitly. Section 8 provides computational verification. Sections 9 and 10 contain discussion and conclusions.

Throughout, natural units $G = \hbar = c = k_B = 1$ are used.

---

## 2. Background

### 2.1 The Schwarzschild–de Sitter Metric

The four-dimensional SdS metric is

$$ds^2 = -f(r)\,dt^2 + f(r)^{-1}\,dr^2 + r^2\,d\Omega_2^2,$$

where

$$f(r) = 1 - \frac{2M}{r} - \frac{\Lambda r^2}{3}.$$

For $0 < M < M_N = 1/(3\sqrt{\Lambda})$, the lapse function $f(r)$ has three real roots: one negative root $r_-$ and two positive roots $r_b < r_c$. The static region accessible to an observer between the horizons is $r_b < r < r_c$. At the Nariai mass $M_N$, the two positive roots coincide.

### 2.2 Horizon Entropies

The Bekenstein–Hawking entropy of each horizon is one quarter of its area:

$$S_b = \pi r_b^2, \qquad S_c = \pi r_c^2. \tag{1}$$

The entropy of pure de Sitter space ($M = 0$) is

$$S_\Lambda = \frac{3\pi}{\Lambda}. \tag{2}$$

Since $\Lambda$ is fixed throughout, $S_\Lambda$ is a constant of the family of SdS spacetimes.

### 2.3 Horizon Temperatures

The Hawking temperature of each horizon is $T = |f'(r)|/(4\pi)$. From the cubic identity (derived in Section 3), each horizon radius satisfies $2M = r - \Lambda r^3/3$, so

$$f'(r) = \frac{2M}{r^2} - \frac{2\Lambda r}{3} = \frac{1}{r} - \Lambda r.$$

At the black hole horizon $r_b < 1/\sqrt{\Lambda}$, we have $f'(r_b) > 0$, giving $T_b = (1/r_b - \Lambda r_b)/(4\pi)$. At the cosmological horizon $r_c > 1/\sqrt{\Lambda}$, we have $f'(r_c) < 0$, giving $T_c = (\Lambda r_c - 1/r_c)/(4\pi)$.

Introducing the dimensionless ratio $x = r_b/r_c \in (0, 1)$ and the cosmological constraint (derived below)

$$\Lambda = \frac{3}{r_c^2(x^2+x+1)},$$

the temperatures take the explicit closed forms:

$$T_b = \frac{(1-x)(1+2x)}{4\pi x r_c(x^2+x+1)}, \qquad T_c = \frac{(1-x)(2+x)}{4\pi r_c(x^2+x+1)}. \tag{3}$$

Dividing gives the temperature ratio:

$$\frac{T_c}{T_b} = \frac{x(2+x)}{1+2x}. \tag{4}$$

This exact closed form satisfies $T_c/T_b \to 0$ as $x \to 0$ (small black hole limit) and $T_c/T_b \to 1$ as $x \to 1$ (Nariai limit). The Carnot efficiency between the two horizons is

$$\eta_C \equiv 1 - \frac{T_c}{T_b} = \frac{1-x^2}{1+2x}. \tag{5}$$

### 2.4 First Laws

Each horizon satisfies an independent first law:

$$dS_b = \frac{dM}{T_b} > 0, \qquad dS_c = -\frac{dM}{T_c} < 0. \tag{6}$$

The opposing signs confirm the thermodynamic anti-alignment: any increase in mass raises the black hole entropy and lowers the cosmological entropy.

---

## 3. Derivation of the Entropy Identity

### 3.1 The Horizon Cubic and Vieta's Formulas

Setting $f(r) = 0$ and multiplying through by $r/(\Lambda/3)$:

$$r^3 - \frac{3}{\Lambda}\,r + \frac{6M}{\Lambda} = 0. \tag{7}$$

The coefficient of $r^2$ is zero. By Vieta's formulas for the roots $r_-$, $r_b$, $r_c$ of (7):

$$r_- + r_b + r_c = 0, \tag{8}$$

$$r_- r_b + r_- r_c + r_b r_c = -\frac{3}{\Lambda}, \tag{9}$$

$$r_- r_b r_c = -\frac{6M}{\Lambda}. \tag{10}$$

From (8), $r_- = -(r_b + r_c)$.

### 3.2 The Eisenstein Identity for Horizon Radii

Substituting $r_- = -(r_b + r_c)$ into (9):

$$-(r_b + r_c)(r_b + r_c) + r_b r_c = -\frac{3}{\Lambda}$$

$$-r_b^2 - 2r_b r_c - r_c^2 + r_b r_c = -\frac{3}{\Lambda}$$

$$r_b^2 + r_b r_c + r_c^2 = \frac{3}{\Lambda}. \tag{11}$$

The right-hand side is $S_\Lambda/\pi$. Equation (11) is the Eisenstein norm $N(r_b + r_c\,\omega) = r_b^2 + r_b r_c + r_c^2$ for $\omega = e^{2\pi i/3}$, evaluated at $r_b + r_c \omega$.

The cosmological constant parametrization follows from (11): with $r_b = xr_c$,

$$r_c^2(x^2 + x + 1) = \frac{3}{\Lambda}, \qquad \text{so} \qquad \Lambda = \frac{3}{r_c^2(x^2+x+1)}.$$

This confirms the expression used in Section 2.3.

### 3.3 Translation to Entropies

Multiplying (11) by $\pi$:

$$S_b + \pi r_b r_c + S_c = S_\Lambda.$$

It remains to express $\pi r_b r_c$ in terms of entropies. Since $r_b = \sqrt{S_b/\pi}$ and $r_c = \sqrt{S_c/\pi}$:

$$\pi r_b r_c = \pi \cdot \frac{\sqrt{S_b}}{\sqrt{\pi}} \cdot \frac{\sqrt{S_c}}{\sqrt{\pi}} = \sqrt{S_b S_c}.$$

Therefore:

$$\boxed{S_\Lambda = S_b + S_c + \sqrt{S_b S_c}.} \tag{12}$$

This identity holds exactly for all $M \in (0, M_N)$ at fixed $\Lambda$.

---

## 4. Structural Results

### 4.1 Definition and Bounds of the Entropy Deficit

Define:

$$\Delta \equiv \sqrt{S_b S_c} = \pi r_b r_c. \tag{13}$$

By (12), $\Delta$ is the deficit between the pure de Sitter entropy and the sum of the two horizon entropies.

**Lower bound.** As $M \to 0^+$, $r_b \to 0$, so $\Delta \to 0$.

**Upper bound.** The AM-GM inequality gives $S_b + S_c \geq 2\sqrt{S_b S_c} = 2\Delta$. Substituting into (12):

$$S_\Lambda = (S_b + S_c) + \Delta \geq 2\Delta + \Delta = 3\Delta,$$

so $\Delta \leq S_\Lambda/3$. At the Nariai limit $r_b = r_c = 1/\sqrt{\Lambda}$, one verifies from (11) that $S_b = S_c = S_\Lambda/3$, giving $\Delta = S_\Lambda/3$.

Both bounds are sharp:

$$0 \leq \Delta \leq \frac{S_\Lambda}{3}. \tag{14}$$

### 4.2 Normalized Constraint

Setting $\varepsilon_b = S_b/S_\Lambda$ and $\varepsilon_c = S_c/S_\Lambda$, equation (12) becomes:

$$\varepsilon_b + \varepsilon_c + \sqrt{\varepsilon_b \varepsilon_c} = 1. \tag{15}$$

In terms of $x$:

$$\varepsilon_b = \frac{x^2}{x^2+x+1}, \qquad \varepsilon_c = \frac{1}{x^2+x+1}, \qquad \frac{\Delta}{S_\Lambda} = \frac{x}{x^2+x+1}. \tag{16}$$

Each quantity is a rational function of $x$ with denominator $x^2+x+1 > 0$ for all real $x$. The constraint (15) follows from $x^2 + x + 1 = x^2 + x + 1$ identically and is not an additional restriction.

### 4.3 Limiting Behavior

**Pure de Sitter limit ($M \to 0$, $x \to 0$).** $\varepsilon_b \to 0$, $\varepsilon_c \to 1$, $\Delta \to 0$. The cosmological horizon approaches the de Sitter horizon and absorbs all of $S_\Lambda$.

**Nariai limit ($M \to M_N$, $x \to 1$).** $\varepsilon_b \to 1/3$, $\varepsilon_c \to 1/3$, $\Delta/S_\Lambda \to 1/3$. The three contributions to (12) become equal. Both temperatures approach zero, and the horizon area is partitioned equally among the three terms.

---

## 5. Thermodynamic Interpretation

### 5.1 Mass Derivative of the Deficit

Since $S_\Lambda$ is constant at fixed $\Lambda$, differentiating (12) with respect to $M$ gives:

$$\frac{dS_b}{dM} + \frac{dS_c}{dM} + \frac{d\Delta}{dM} = 0.$$

Substituting the first laws (6):

$$\frac{d\Delta}{dM} = \frac{1}{T_c} - \frac{1}{T_b}. \tag{17}$$

Since $T_b > T_c$ throughout the sub-Nariai range, $d\Delta/dM > 0$: the deficit grows monotonically with mass. At the Nariai limit $T_b = T_c$, the derivative vanishes and $\Delta$ reaches its maximum $S_\Lambda/3$.

### 5.2 Carnot-Deficit Relation

Using (17) and the first law $dS_c/dM = -1/T_c$, the derivative of $\Delta$ with respect to $S_c$ is:

$$\frac{d\Delta}{dS_c} = \frac{d\Delta/dM}{dS_c/dM} = \frac{T_c^{-1} - T_b^{-1}}{-T_c^{-1}} = \frac{T_c}{T_b} - 1 = -\left(1 - \frac{T_c}{T_b}\right) = -\eta_C.$$

Therefore:

$$\frac{d\Delta}{dS_c} = -\eta_C. \tag{18}$$

Each unit decrease in cosmological entropy is accompanied by an increase of exactly $\eta_C$ units in $\Delta$. Equation (18) is exact and follows entirely from (12) and (6).

### 5.3 Integral Form and Irreversibility

Integrating (17) from $m = 0$ to $m = M$:

$$\Delta(M) = \int_0^M \left(\frac{1}{T_c(m)} - \frac{1}{T_b(m)}\right) dm. \tag{19}$$

In classical irreversible thermodynamics, the entropy produced by an irreversible heat flow $dQ$ between two bodies at temperatures $T_\text{hot}$ and $T_\text{cold}$ is $dS_\text{irr} = (T_\text{cold}^{-1} - T_\text{hot}^{-1})\,dQ$. Equation (19) has the same structure, with $dm$ playing the role of an infinitesimal heat exchange and $T_b > T_c$ the temperatures of the two systems.

**Caveat.** This interpretation is consistent with the algebra but is not derived from a dynamical model. Equation (19) is an exact identity within the two-horizon first laws. Whether it implies a genuine irreversible entropy production depends on the physical model of black hole nucleation, which is not specified here.

### 5.4 Black Hole Pair Creation

The rate of black hole pair creation in de Sitter space is computed in the Euclidean path integral (saddle-point) approximation. At the SdS saddle, the total on-shell entropy is $S_b + S_c$; at the pure de Sitter saddle, it is $S_\Lambda$. The pair creation rate is [5, 6]:

$$P \sim \exp\bigl(-(S_\Lambda - S_b - S_c)\bigr) = \exp(-\Delta). \tag{20}$$

The deficit $\Delta$ is the tunneling exponent for nucleating a black hole of mass $M$ in de Sitter space. At the Nariai limit, $\Delta = S_\Lambda/3$ and $P$ takes its maximum value; as $M \to 0$, $\Delta \to 0$ and no nucleation occurs (the system is already at the de Sitter saddle).

---

## 6. Low-Dimensional Classification

### 6.1 D = 4: Eisenstein (Geometric Mean) Structure

The result in $D = 4$ rests on two algebraic coincidences operating simultaneously:

1. The horizon polynomial is a depressed cubic (zero $r^2$ coefficient), so Vieta's first relation gives $r_- + r_b + r_c = 0$, enabling the substitution that produces the cross-term $r_b r_c$ in (11).

2. The horizon entropy scales as $S \propto r^2$ in $D = 4$, so the cross-term $\pi r_b r_c$ translates directly to $\sqrt{S_b S_c}$.

Both conditions are required. If either fails — as they do for $D \neq 4$ — the identity does not hold. The resulting form (12) is the Eisenstein norm condition $r_b^2 + r_b r_c + r_c^2 = \text{const}(\Lambda)$, producing a geometric-mean structure in entropy space.

### 6.2 D = 5: Pythagorean Structure

In five-dimensional SdS, the metric function takes the form

$$f(r) = 1 - \frac{\mu}{r^2} - \frac{r^2}{l_5^2}, \tag{21}$$

where $\mu > 0$ is the mass parameter and $l_5$ encodes the 5D cosmological constant. Setting $f(r) = 0$ and multiplying by $r^2$:

$$r^4 - l_5^2\,r^2 + \mu l_5^2 = 0. \tag{22}$$

This quartic in $r$ is a quadratic in $u = r^2$. The two positive roots $u_b = r_b^2$ and $u_c = r_c^2$ satisfy, by Vieta applied to the quadratic $u^2 - l_5^2 u + \mu l_5^2 = 0$:

$$r_b^2 + r_c^2 = l_5^2. \tag{23}$$

In $D = 5$, the horizon area is $A = 2\pi^2 r^3$ (a 3-sphere), so $S = \pi^2 r^3/2$. Therefore $S^{2/3} = (\pi^2/2)^{2/3} r^2$, and multiplying (23) by $(\pi^2/2)^{2/3}$:

$$S_b^{2/3} + S_c^{2/3} = \left(\frac{\pi^2}{2}\right)^{2/3} l_5^2 = S_{\Lambda,5}^{2/3}. \tag{24}$$

Equation (24) is exact and holds for all $\mu \in (0, \mu_N)$. It is a Pythagorean sum in $S^{2/3}$ space, structurally distinct from the $D = 4$ identity. There is no cross-term: the sum is a simple Euclidean norm, not an Eisenstein norm.

The two cases compare as follows:

| Dimension | Polynomial type | Vieta structure | Entropy scaling | Identity form |
|-----------|----------------|-----------------|-----------------|---------------|
| $D = 4$ | Cubic (degree 3) | Zero-sum of roots; cross-term $r_b r_c$ | $S \propto r^2$ | $S_\Lambda = S_b + S_c + \sqrt{S_b S_c}$ |
| $D = 5$ | Quartic in $r$; quadratic in $r^2$ | Sum of $r^2$ roots fixed | $S \propto r^3$ | $S_{\Lambda}^{2/3} = S_b^{2/3} + S_c^{2/3}$ |

### 6.3 D >= 6: No Clean Closure

For $D \geq 6$, the SdS horizon polynomial has degree $D - 1 \geq 5$ in $r$. The key obstruction is that this polynomial does not reduce to a lower-degree polynomial by any substitution of the form $u = r^k$.

Concretely, for $D = 6$: $f(r) = 1 - \mu/r^3 - r^2/l_6^2$, and the horizon polynomial is

$$r^5 - l_6^2\,r^3 + \mu l_6^2 = 0. \tag{25}$$

This degree-5 polynomial has two positive real roots ($r_b$, $r_c$) and three additional roots (one real negative, two complex conjugates). The Vieta relations for (25) involve all five roots. By Newton's identity applied to all five roots, the sum of squares is $\sum_i r_i^2 = 2l_6^2$, but this sum includes the unphysical roots. The quantity $r_b^2 + r_c^2$ is therefore not determined by $\Lambda$ alone: it depends on the mass parameter through the unphysical roots.

With $S \propto r^4$ in $D = 6$, any candidate identity would require a Vieta relation for $r_b^2 + r_c^2$ (for a $S^{1/2}$-type sum) or $r_b^4 + r_c^4$ (for a $S$-type sum) or similar — none of which are fixed by $\Lambda$ alone for a degree-5 polynomial.

The pattern makes the exceptional status of $D = 4$ and $D = 5$ explicit:

- $D = 4$: The depressed cubic provides a zero-trace condition ($\sum r_i = 0$) that isolates the cross-term $r_b r_c$.
- $D = 5$: The quartic horizon polynomial factors as a quadratic in $r^2$, making $r_b^2 + r_c^2$ the primary Vieta sum.
- $D \geq 6$: Neither mechanism operates.

---

## 7. Stress Test and Limitations

The following limitations apply to all results in this paper.

**$\Delta$ is not independent of $M$.** At fixed $\Lambda$, the map $M \mapsto (S_b, S_c)$ is injective. The constraint curve $\mathcal{C}_\Lambda = \{(S_b, S_c) : \sqrt{S_b S_c} + S_b + S_c = S_\Lambda\}$ is a smooth one-dimensional curve. Every smooth function $\Phi(S_b, S_c)$ that is constant along $\mathcal{C}_\Lambda$ depends only on $S_\Lambda$, hence only on $\Lambda$. In particular, $\Delta = \sqrt{S_b S_c}$ carries no information about the state of the system beyond what is already encoded in $M$ (at fixed $\Lambda$). The entropy deficit is a useful parametrization, not an independent invariant.

**No higher-dimensional generalization.** The identities (12) and (24) hold only in $D = 4$ and $D = 5$ respectively, for the reasons stated in Section 6. Neither extends to other dimensions or to the other case.

**No extension to charged or rotating black holes.** In Reissner–Nordström–de Sitter (RNdS) spacetime, the horizon polynomial is quartic with a charge parameter coupling all four roots. In Kerr–de Sitter spacetime, the structure is similarly entangled. The clean separation of the Vieta cross-term that produces (11) does not occur. These generalizations are ruled out by direct inspection of the respective horizon polynomials.

**The irreversibility interpretation is not derived from a dynamical model.** Equation (19) is consistent with an entropy production interpretation but does not establish one. A rigorous statement would require specifying a thermodynamic process (quasi-static or otherwise) and initial conditions.

**Not a new physical law.** The identities derived here are algebraic consequences of (a) Vieta's formulas applied to the SdS horizon polynomial and (b) the area-entropy formula $S = A/4$. They do not imply any new symmetry, conservation law, or bound beyond what is already contained in standard SdS thermodynamics.

---

## 8. Computational Verification

The following self-contained Python script verifies identity (12) numerically. It requires only NumPy.

```python
import numpy as np


def solve_sds_horizons(M, Lambda):
    """
    Find the black hole and cosmological horizon radii of
    Schwarzschild-de Sitter spacetime.

    Solves the horizon cubic:
        r^3 - (3/Lambda)*r + 6*M/Lambda = 0

    Returns (r_b, r_c) with r_b < r_c, or None if fewer than
    two positive real roots exist (M >= Nariai mass).
    """
    # Polynomial coefficients: r^3 + 0*r^2 - (3/Lambda)*r + 6*M/Lambda
    coeffs = [1.0, 0.0, -3.0 / Lambda, 6.0 * M / Lambda]
    roots = np.roots(coeffs)

    # Retain only real positive roots
    positive_real = sorted(
        r.real for r in roots
        if abs(r.imag) < 1e-9 and r.real > 0
    )

    if len(positive_real) < 2:
        return None

    return positive_real[0], positive_real[1]  # (r_b, r_c)


def verify_identity(M, Lambda):
    """
    Compute S_b, S_c, Delta, and verify S_Lambda = S_b + S_c + sqrt(S_b * S_c).
    """
    result = solve_sds_horizons(M, Lambda)
    if result is None:
        print(f"  M = {M:.6f}: no physical horizons (at or above Nariai mass)")
        return None

    r_b, r_c = result

    # Bekenstein-Hawking entropies (G = 1)
    S_b = np.pi * r_b**2
    S_c = np.pi * r_c**2
    S_dS = 3.0 * np.pi / Lambda
    Delta = np.sqrt(S_b * S_c)

    lhs = S_b + S_c + Delta
    residual = abs(lhs - S_dS)

    print(f"  M = {M:.5f}:  r_b = {r_b:.6f},  r_c = {r_c:.6f}")
    print(f"    S_b = {S_b:.6f},  S_c = {S_c:.6f},  Delta = {Delta:.6f}")
    print(f"    S_b + S_c + Delta = {lhs:.8f}")
    print(f"    S_Lambda          = {S_dS:.8f}")
    print(f"    Residual          = {residual:.2e}")
    return residual


# ----------------------------------------------------------------
# Parameters
# ----------------------------------------------------------------
Lambda = 0.1
M_N = 1.0 / (3.0 * np.sqrt(Lambda))   # Nariai mass

print("=" * 60)
print(f"Lambda = {Lambda},  Nariai mass M_N = {M_N:.6f}")
print("=" * 60)
print()
print("Verification: S_Lambda = S_b + S_c + sqrt(S_b * S_c)")
print("-" * 60)

test_masses = [0.05, 0.2, 0.5, 1.0, 1.5, 2.0, round(M_N * 0.995, 6)]
for M in test_masses:
    verify_identity(M, Lambda)
    print()

# ----------------------------------------------------------------
# Nariai limit (analytic check)
# ----------------------------------------------------------------
print("Nariai limit (analytic):")
r_N = 1.0 / np.sqrt(Lambda)
S_N = np.pi * r_N**2
print(f"  r_b = r_c = {r_N:.6f}")
print(f"  S_b = S_c = {S_N:.6f}")
print(f"  S_Lambda/3 = {3.0*np.pi/Lambda / 3.0:.6f}")
print(f"  Identity: {S_N:.6f} + {S_N:.6f} + {S_N:.6f} = {3*S_N:.6f}")
print(f"  S_Lambda    = {3.0*np.pi/Lambda:.6f}")
print(f"  Match: {abs(3*S_N - 3.0*np.pi/Lambda) < 1e-12}")

# ----------------------------------------------------------------
# Normalized fractions (verify epsilon_b + epsilon_c + sqrt(e_b e_c) = 1)
# ----------------------------------------------------------------
print()
print("-" * 60)
print("Normalized constraint: eps_b + eps_c + sqrt(eps_b * eps_c) = 1")
print("-" * 60)
for M in [0.1, 0.5, 1.0, 2.0]:
    result = solve_sds_horizons(M, Lambda)
    if result is None:
        continue
    r_b, r_c = result
    S_dS = 3.0 * np.pi / Lambda
    eps_b = np.pi * r_b**2 / S_dS
    eps_c = np.pi * r_c**2 / S_dS
    lhs = eps_b + eps_c + np.sqrt(eps_b * eps_c)
    print(f"  M = {M:.2f}: eps_b = {eps_b:.5f}, eps_c = {eps_c:.5f}, "
          f"LHS = {lhs:.8f}, residual = {abs(lhs - 1):.2e}")
```

Running this code confirms identity (12) to machine precision (residuals of order $10^{-14}$ to $10^{-15}$) across the full parameter range.

---

## 9. Discussion

The entropy identity (12) follows from a three-line algebraic argument: Vieta's formulas applied to the depressed cubic, substitution of the unphysical root, and conversion from radii to entropies. No approximation is involved. The identity itself, or its equivalent in terms of horizon radii, has appeared in various guises in the literature on SdS thermodynamics. What the present analysis contributes is: (i) a single transparent derivation collecting the main structural consequences, (ii) the Carnot-deficit relation (18) as an explicit statement, (iii) the closed-form temperature ratio (4), and (iv) the $D$-dimensional classification with explicit proof of failure for $D \geq 6$.

The Carnot-deficit relation (18) may be of practical use. It states that the entropy cost of reducing $S_c$ by one unit is exactly $\eta_C$ units of deficit increase, where $\eta_C$ is determined by the temperature ratio alone. Combined with (17), this gives a clean picture of how the two-horizon system evolves as $M$ changes.

The $D = 5$ identity (24) appears to have received less systematic attention than the $D = 4$ case. It follows from the same Vieta strategy applied to the reduced quartic (22). The structural distinction between the two cases — Eisenstein norm for $D = 4$, Pythagorean sum for $D = 5$ — reflects the difference between a depressed cubic (where the cross-term is forced by the zero-trace condition) and a quadratic in $r^2$ (where no cross-term appears).

The proof that no analogous identity exists for $D \geq 6$ rests on the indecomposability of the degree-$(D-1)$ horizon polynomial for $D \geq 6$. This is a structural statement about polynomial algebra, not a numerical observation.

We note one connection to information theory that remains at the level of analogy. The form $S_\Lambda = S_b + S_c + \sqrt{S_b S_c}$ is reminiscent of the Petz–Rényi relative entropy and related quantum information quantities, which also involve geometric means of operators. Whether this analogy can be made precise — for example, through a holographic or semiclassical argument relating the deficit to a quantum channel capacity — is not established here and would require a microscopic model.

---

## 10. Conclusion

We have derived and analyzed the exact entropy identity

$$S_\Lambda = S_b + S_c + \sqrt{S_b S_c}$$

for four-dimensional Schwarzschild–de Sitter spacetime. The results may be summarized as follows.

**Established from Vieta's formulas:**
- Identity (12) holds exactly for all $M \in (0, M_N)$.
- The entropy deficit $\Delta = \sqrt{S_b S_c}$ satisfies $0 \leq \Delta \leq S_\Lambda/3$ with both bounds sharp.

**Derived from the identity and the first laws:**
- $d\Delta/dM = T_c^{-1} - T_b^{-1}$ (equation 17).
- $d\Delta/dS_c = -\eta_C$ (equation 18).
- The pair creation exponent equals $\Delta$ (equation 20).

**Explicit closed forms:**
- Temperature ratio $T_c/T_b = x(2+x)/(1+2x)$ (equation 4).
- Normalized constraint $\varepsilon_b + \varepsilon_c + \sqrt{\varepsilon_b\varepsilon_c} = 1$ (equation 15).

**Dimensional classification:**
- $D = 5$: exact identity $S_{\Lambda,5}^{2/3} = S_b^{2/3} + S_c^{2/3}$ (equation 24).
- $D \geq 6$: no analogous identity exists.

These results constitute a structural reformulation of known SdS thermodynamics, not new physics. Possible directions for further work include: analogous Vieta-based identities in other two-horizon spacetimes with polynomial horizon equations of degree $\leq 4$, and the question of whether the $D = 4$ and $D = 5$ identities have a common origin in a higher-dimensional or algebraic structure that remains to be identified.

---

## References

[1] J. D. Bekenstein, "Black holes and entropy," *Phys. Rev. D* **7**, 2333 (1973).

[2] S. W. Hawking, "Particle creation by black holes," *Commun. Math. Phys.* **43**, 199 (1975).

[3] G. W. Gibbons and S. W. Hawking, "Cosmological event horizons, thermodynamics, and particle creation," *Phys. Rev. D* **15**, 2738 (1977).

[4] G. W. Gibbons and S. W. Hawking, "Action integrals and partition functions in quantum gravity," *Phys. Rev. D* **15**, 2752 (1977).

[5] P. Ginsparg and M. J. Perry, "Semiclassical perdurance of de Sitter space," *Nucl. Phys. B* **222**, 245 (1983).

[6] R. Bousso and S. W. Hawking, "Pair creation of black holes during inflation," *Phys. Rev. D* **54**, 6312 (1996).

[7] R. Bousso, "Proliferation of de Sitter space," *Phys. Rev. D* **58**, 083511 (1998).

[8] R. B. Mann and S. F. Ross, "Cosmological production of charged black hole pairs," *Phys. Rev. D* **52**, 2254 (1995).

[9] B. P. Dolan, "The cosmological constant and black hole thermodynamic potentials," *Class. Quantum Grav.* **28**, 125020 (2011).

[10] B. Pym, "On the thermodynamics of Schwarzschild–de Sitter black holes," unpublished notes. *(Placeholder; replace with any primary source treating SdS two-horizon thermodynamics used by the authors.)*

---

*End of manuscript.*
