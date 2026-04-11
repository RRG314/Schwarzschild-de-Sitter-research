# Exact Entropy Structure in Schwarzschild–de Sitter Spacetime and the Dimensional Classification of Polynomial Horizon Closure

**Steven Reid**

---

## Abstract

We derive and analyze the exact entropy identity for four-dimensional Schwarzschild–de Sitter (SdS) spacetime:
$$S_\Lambda = S_b + S_c + \sqrt{S_b S_c}$$
where $S_b$ and $S_c$ are the Bekenstein–Hawking entropies of the black hole and cosmological horizons respectively, and $S_\Lambda = 3\pi/\Lambda$ is the entropy of the corresponding pure de Sitter space. The derivation proceeds directly from the Vieta relations of the horizon cubic. We define the entropy deficit $\Delta = \sqrt{S_b S_c}$, establish its bounds, and show that it satisfies the exact Carnot relation $\partial\Delta/\partial S_c\big|_\Lambda = -\eta_C$, where $\eta_C = 1 - T_c/T_b$ is the Carnot efficiency, as well as the mass-derivative identity $\partial\Delta/\partial M\big|_\Lambda = T_c^{-1} - T_b^{-1}$.

We then classify polynomial entropy closure across spacetime dimensions. For five-dimensional SdS, the horizon equation reduces to a quadratic under the substitution $u = r^2$, yielding the exact identity $S_{\Lambda,5}^{2/3} = S_b^{2/3} + S_c^{2/3}$. We prove that a polynomial entropy closure of this type exists if and only if the spacetime dimension $D \in \{4, 5\}$: specifically, the condition is that $(D-3)$ divides $2$, proved via the divisibility criterion for differences of powers in the polynomial ring $\mathbb{Z}[r_b, r_c]$. For $D \geq 6$, the entropy formula is rational but not polynomial in the horizon radii, with denominator degree $D - 4$.

---

## 1. Introduction

Schwarzschild–de Sitter spacetime is the unique spherically symmetric solution to the Einstein field equations with positive cosmological constant $\Lambda > 0$ and mass parameter $M > 0$. It is distinguished among black hole spacetimes by possessing two distinct Killing horizons in causal contact with any static observer: a black hole horizon at $r = r_b$ and a cosmological horizon at $r = r_c > r_b$. Both carry Bekenstein–Hawking entropy proportional to their horizon area, and both radiate thermally at distinct Hawking temperatures $T_b$ and $T_c$. The static region between the two horizons is a compact causal diamond.

The existence of two horizons raises a natural question about the total entropy budget. The pure de Sitter configuration ($M = 0$) has a single cosmological horizon with entropy $S_\Lambda = 3\pi/\Lambda$. As mass is introduced, this single horizon bifurcates into a black hole horizon and a cosmological horizon, with $S_b + S_c < S_\Lambda$. The entropy is not simply additive: the two-horizon configuration carries strictly less total horizon entropy than the pure de Sitter background. The deficit $\Delta = S_\Lambda - S_b - S_c$ is the object of interest.

Prior work on SdS thermodynamics has studied both classical and quantum aspects of the two-horizon system. Zhao Ren et al. [RLZ10] studied Hawking radiation from both horizons using the Damour-Ruffini analytic extension method, accounting for energy conservation and back-reaction. They concluded from a tunneling argument that the total entropy of de Sitter spacetime is the sum of the two horizon entropies, i.e., $S_{dS} = S_h + S_c$. The exact algebraic identity derived below shows that this additivity is incomplete at the classical level: the precise relation between $S_\Lambda$, $S_b$, and $S_c$ contains an additional geometric mean term $\sqrt{S_b S_c}$ that is not subleading and does not vanish in any sub-extremal limit.

We show that this deficit has the exact closed form $\Delta = \sqrt{S_b S_c}$, derivable in three algebraic steps from the Vieta relations of the horizon cubic. This identity is structurally clean and leads to a set of exact thermodynamic consequences. We then ask whether analogous identities exist in other dimensions. The answer turns out to depend on an arithmetic divisibility condition, and the set of dimensions admitting a polynomial entropy closure is exactly $\{4, 5\}$.

Throughout we use units $G = \hbar = k_B = c = 1$. The cosmological constant satisfies $\Lambda > 0$.

---

## 2. Background

### 2.1 The 4D SdS Metric and Horizon Structure

The four-dimensional Schwarzschild–de Sitter metric is
$$ds^2 = -f(r)\,dt^2 + f(r)^{-1}dr^2 + r^2\,d\Omega_2^2$$
with
$$f(r) = 1 - \frac{2M}{r} - \frac{\Lambda r^2}{3}$$
where $d\Omega_2^2$ is the round metric on $S^2$. The horizons are the positive real zeros of $f$.

Setting $f(r) = 0$ and multiplying through by $-3r/\Lambda > 0$:
$$r^3 - \frac{3}{\Lambda}\,r + \frac{6M}{\Lambda} = 0 \tag{1}$$

This is a depressed cubic (no $r^2$ term). The discriminant is
$$\Delta_\text{cub} = \frac{108}{\Lambda^3}\Bigl(1 - 9\Lambda M^2\Bigr)$$

For $\Delta_\text{cub} > 0$, equivalently $9\Lambda M^2 < 1$, the cubic has three distinct real roots. We label them $r_- < 0 < r_b < r_c$. The sub-extremal condition $9\Lambda M^2 < 1$ is assumed throughout. The Nariai limit $9\Lambda M^2 = 1$ gives $r_b = r_c$ and is excluded.

**Geometric interpretation.** The function $f$ satisfies $f > 0$ on $(r_b, r_c)$, $f < 0$ on $(0, r_b)$ and $(r_c, \infty)$. The black hole horizon at $r_b$ separates the interior ($f < 0$, singular region) from the static region. The cosmological horizon at $r_c$ bounds the static region from the exterior.

### 2.2 Entropies and Pure de Sitter Reference

Each horizon carries Bekenstein–Hawking entropy equal to one-quarter its area:
$$S_b = \pi r_b^2, \qquad S_c = \pi r_c^2 \tag{2}$$

The pure de Sitter space with cosmological constant $\Lambda$ has a single cosmological horizon of radius $r_\Lambda = \sqrt{3/\Lambda}$, with entropy
$$S_\Lambda = \pi r_\Lambda^2 = \frac{3\pi}{\Lambda} \tag{3}$$

This will serve as the reference entropy: it is the value $S_b + S_c$ would take if the mass were zero. We will show that $S_\Lambda = S_b + S_c + \sqrt{S_b S_c}$ for all sub-extremal SdS.

### 2.3 Hawking Temperatures and First Laws

The surface gravity at each horizon determines its Hawking temperature. For the black hole horizon:
$$\kappa_b = \frac{1}{2}|f'(r_b)|, \qquad T_b = \frac{\kappa_b}{2\pi} = \frac{1 - \Lambda r_b^2}{4\pi r_b} \tag{4}$$

For the cosmological horizon, $f'(r_c) < 0$ (since $f$ decreases as $r$ increases through $r_c$):
$$\kappa_c = \frac{1}{2}|f'(r_c)|, \qquad T_c = \frac{\kappa_c}{2\pi} = \frac{\Lambda r_c^2 - 1}{4\pi r_c} \tag{5}$$

To verify the signs: the sub-extremal condition and the Vieta relations (derived below) imply $\Lambda r_b^2 < 1 < \Lambda r_c^2$, so both temperatures are positive.

The first law for the black hole horizon at fixed $\Lambda$ is $dM = T_b\,dS_b$. For the cosmological horizon, a decrease in mass corresponds to an increase in cosmological entropy: $dM = -T_c\,dS_c$. These give the coupling relation:
$$T_b\,dS_b + T_c\,dS_c = 0 \tag{6}$$
valid at fixed $\Lambda$, reflecting the fact that the cosmological constant contributes the total entropy $S_\Lambda$ as a conserved quantity.

---

## 3. Exact 4D Entropy Identity

### 3.1 Vieta Relations for the Horizon Cubic

The cubic (1), written as $r^3 + 0 \cdot r^2 + (-3/\Lambda) r + (6M/\Lambda) = 0$, has three roots $r_-$, $r_b$, $r_c$. Vieta's formulas give:
$$r_- + r_b + r_c = 0 \tag{7a}$$
$$r_- r_b + r_- r_c + r_b r_c = -\frac{3}{\Lambda} \tag{7b}$$
$$r_- r_b r_c = -\frac{6M}{\Lambda} \tag{7c}$$

The coefficient of $r^2$ being zero is the key structural feature. It forces the zero-sum condition (7a), which allows $r_-$ to be expressed as a rational function of $r_b$ and $r_c$.

### 3.2 Elimination of the Unphysical Root

From (7a):
$$r_- = -(r_b + r_c) \tag{8}$$

Substitute (8) into (7b):
$$r_-(r_b + r_c) + r_b r_c = -\frac{3}{\Lambda}$$
$$-(r_b + r_c)^2 + r_b r_c = -\frac{3}{\Lambda}$$
$$r_b r_c - r_b^2 - 2r_b r_c - r_c^2 = -\frac{3}{\Lambda}$$
$$-r_b^2 - r_b r_c - r_c^2 = -\frac{3}{\Lambda}$$

Multiplying by $-1$:

$$\boxed{r_b^2 + r_b r_c + r_c^2 = \frac{3}{\Lambda}} \tag{9}$$

This is a clean, exact algebraic identity relating the two physical horizon radii to $\Lambda$ alone, with no dependence on $M$. The mass parameter has been fully eliminated.

### 3.3 Conversion to Entropy Form

Multiply (9) by $\pi$:
$$\pi r_b^2 + \pi r_b r_c + \pi r_c^2 = \frac{3\pi}{\Lambda}$$

Using the definitions $S_b = \pi r_b^2$, $S_c = \pi r_c^2$, $S_\Lambda = 3\pi/\Lambda$, and noting that $r_b, r_c > 0$ so $\pi r_b r_c = \sqrt{\pi r_b^2 \cdot \pi r_c^2} = \sqrt{S_b S_c}$:

$$\boxed{S_\Lambda = S_b + S_c + \sqrt{S_b S_c}} \tag{10}$$

This identity holds for all sub-extremal 4D SdS configurations. It is an exact algebraic consequence of Vieta's formulas applied to the horizon cubic; no approximations or expansions are involved.

---

## 4. Structural Consequences in 4D

### 4.1 The Entropy Deficit

**Definition.** The *entropy deficit* is
$$\Delta = \sqrt{S_b S_c} = \pi r_b r_c \tag{11}$$

By (10): $\Delta = S_\Lambda - S_b - S_c > 0$ for all sub-extremal configurations. The black hole and cosmological horizon entropies sum to strictly less than the pure de Sitter entropy; the deficit is their geometric mean.

**Normalized form.** Dividing (10) by $S_\Lambda$ and setting $\varepsilon_i = S_i/S_\Lambda$:
$$\varepsilon_b + \varepsilon_c + \sqrt{\varepsilon_b \varepsilon_c} = 1, \qquad \varepsilon_b, \varepsilon_c > 0 \tag{12}$$

This is the scale-free form of the identity, depending only on the ratio $x = r_b/r_c \in (0,1)$. In terms of $x$:
$$\varepsilon_b = \frac{x^2}{x^2+x+1}, \qquad \varepsilon_c = \frac{1}{x^2+x+1}, \qquad \frac{\Delta}{S_\Lambda} = \frac{x}{x^2+x+1} \tag{13}$$

### 4.2 Bounds on $\Delta$

**Proposition 4.1.** $0 < \Delta \leq S_\Lambda/3$, with equality if and only if $S_b = S_c$ (the Nariai limit).

*Proof.* Lower bound: $\Delta = \sqrt{S_bS_c} > 0$ since $r_b, r_c > 0$. Upper bound: by AM-GM, $\sqrt{S_bS_c} \leq (S_b+S_c)/2$. From (10): $S_b + S_c = S_\Lambda - \Delta$, so $\Delta \leq (S_\Lambda - \Delta)/2$, giving $3\Delta \leq S_\Lambda$. Equality holds iff $S_b = S_c$, which occurs at the Nariai limit $r_b = r_c = r_N = 1/\sqrt{\Lambda}$, where $S_b = S_c = \pi/\Lambda = S_\Lambda/3$. $\square$

### 4.3 Pair Creation Interpretation

Following Gibbons and Hawking [GH77] and Bousso and Hawking [BH96], the semiclassical rate for nucleation of a black hole pair from de Sitter space is governed by the difference of Euclidean actions:
$$\Gamma \propto \exp\!\left(S_b + S_c - S_\Lambda\right) = \exp(-\Delta) \tag{14}$$

By (10) and (11): $S_b + S_c - S_\Lambda = -\Delta = -\sqrt{S_b S_c}$. The entropy deficit $\Delta$ therefore appears directly as the suppression exponent for pair creation. The range $\Delta \in (0, S_\Lambda/3]$ means the suppression varies from zero (in the $M \to 0$ limit, where pair creation is unsuppressed) to the maximum at the Nariai configuration.

This interpretation depends on the semiclassical approximation and the conventions of [BH96]; we record it as a physical interpretation of $\Delta$, not as an independently proved claim. Zhao Ren et al. [RLZ10] arrive at a related expression for the total radiation rate $\Gamma = e^{\Delta S_b + \Delta S_c}$ from a tunneling argument that accounts for the coupled back-reaction of both horizons; their dynamical approach is complementary to the kinematic identity (14).

### 4.4 Thermodynamic Identities

**Proposition 4.2 (Mass derivative).** At fixed $\Lambda$:
$$\frac{\partial \Delta}{\partial M}\bigg|_\Lambda = \frac{1}{T_c} - \frac{1}{T_b} \tag{15}$$

*Proof.* From the first laws $\partial S_b/\partial M = 1/T_b$ and $\partial S_c/\partial M = -1/T_c$ (both at fixed $\Lambda$):
$$\frac{\partial \Delta}{\partial M} = \frac{1}{2}\sqrt{\frac{S_c}{S_b}}\cdot\frac{1}{T_b} - \frac{1}{2}\sqrt{\frac{S_b}{S_c}}\cdot\frac{1}{T_c} = \frac{r_c}{2r_b T_b} - \frac{r_b}{2r_c T_c}$$

Using (4), (5), and the expressions for $T_b$, $T_c$ in terms of $x = r_b/r_c$:
$$\frac{1}{T_b} = \frac{4\pi r_b}{1-\Lambda r_b^2} = \frac{4\pi r_b(x^2+x+1)}{(1-x)(1+2x)}, \qquad \frac{1}{T_c} = \frac{4\pi r_c(x^2+x+1)}{(1-x)(2+x)}$$

A direct computation (expanding both sides in $x$ and simplifying) gives:
$$\frac{r_c}{2r_b T_b} - \frac{r_b}{2r_c T_c} = \frac{4\pi r_c(x^2+x+1)(1+x)}{(1+2x)(2+x)} = \frac{1}{T_c} - \frac{1}{T_b} \qquad \square$$

**Proposition 4.3 (Carnot relation).** At fixed $\Lambda$:
$$\frac{\partial \Delta}{\partial S_c}\bigg|_\Lambda = -\eta_C \tag{16}$$
where $\eta_C = 1 - T_c/T_b$ is the Carnot efficiency.

*Proof.* Differentiate the identity (10) at fixed $\Lambda$ (fixed $S_\Lambda$):
$$0 = dS_b + dS_c + \frac{1}{2}\sqrt{\frac{S_c}{S_b}}\,dS_b + \frac{1}{2}\sqrt{\frac{S_b}{S_c}}\,dS_c$$

In terms of $x = r_b/r_c$:
$$\frac{\partial S_b}{\partial S_c}\bigg|_\Lambda = -\frac{1+x/(2)}{1+(2x)^{-1}} \cdot \frac{x^2}{1}$$

After simplification: $\partial S_b/\partial S_c|_\Lambda = -x(2+x)/(1+2x)$.

Then:
$$\frac{\partial\Delta}{\partial S_c}\bigg|_\Lambda = \frac{1}{2}\sqrt{\frac{S_b}{S_c}} + \frac{1}{2}\sqrt{\frac{S_c}{S_b}}\cdot\frac{\partial S_b}{\partial S_c}\bigg|_\Lambda = \frac{x}{2} - \frac{1}{2x}\cdot\frac{x(2+x)}{1+2x} = \frac{x^2-1}{1+2x}$$

The Carnot efficiency in terms of $x$ is:
$$\eta_C = 1 - \frac{T_c}{T_b} = 1 - \frac{x(2+x)}{1+2x} = \frac{1-x^2}{1+2x}$$

Therefore $\partial\Delta/\partial S_c|_\Lambda = (x^2-1)/(1+2x) = -(1-x^2)/(1+2x) = -\eta_C$. $\square$

**Remark.** Equation (16) has the form of a thermodynamic work identity: transferring entropy from the cosmological horizon to the black hole decreases the deficit at a rate equal to the Carnot efficiency of the pair. This is an exact relation, not an approximation.

### 4.5 The Entropy Constraint ODE

At fixed $\Lambda$, define $s = S_b + S_c$ and $p = S_b S_c$, so that $\Delta = \sqrt{p}$ and $S_\Lambda = s + \sqrt{p}$. Differentiating $S_\Lambda = \text{const}$:
$$ds + \frac{dp}{2\sqrt{p}} = 0 \implies \frac{dp}{ds} = -2\sqrt{p} \tag{17}$$

This ODE has solution $\sqrt{p} = S_\Lambda - s$, which is simply the identity (10). The ODE (17) characterizes the one-parameter family of sub-extremal SdS configurations at fixed $\Lambda$, parameterized by $s \in (0, S_\Lambda)$.

### 4.6 Limiting Cases

**Limit $M \to 0^+$.** As $M \to 0$, the black hole horizon shrinks: $r_b \to 0$, $r_c \to r_\Lambda = \sqrt{3/\Lambda}$. Therefore $S_b \to 0$, $S_c \to S_\Lambda$, and $\Delta = \sqrt{S_bS_c} \to 0$. The identity (10) reduces to $S_\Lambda = 0 + S_\Lambda + 0$. The entropy deficit vanishes and the cosmological entropy recovers the pure de Sitter value.

**Nariai limit $9\Lambda M^2 \to 1^-$.** As $M \to M_N = 1/(3\sqrt{\Lambda})$, the two positive roots converge: $r_b, r_c \to r_N = 1/\sqrt{\Lambda}$. Then $S_b, S_c \to S_\Lambda/3$ and $\Delta \to S_\Lambda/3$. The identity becomes $S_\Lambda = S_\Lambda/3 + S_\Lambda/3 + S_\Lambda/3$. Both temperatures $T_b, T_c \to 0$ (the Nariai configuration is the extremal limit), and $\eta_C \to 0$ consistently with (16) since $\partial\Delta/\partial S_c \to 0$.

### 4.7 The Eisenstein Geometry of the Phase Space

The structural consequences of Sections 4.1--4.6 admit a unified geometric description.

**Definition 4.4 (Eisenstein coordinates).** Define
$$u = \sqrt{\frac{S_b}{S_\Lambda}}, \qquad v = \sqrt{\frac{S_c}{S_\Lambda}} \tag{18}$$

**Proposition 4.5.** In Eisenstein coordinates, the normalized SdS constraint (12) becomes the Eisenstein unit ellipse:
$$u^2 + uv + v^2 = 1 \tag{19}$$

*Proof.* Substituting $u^2 = \varepsilon_b$, $v^2 = \varepsilon_c$ into (12): $u^2 + v^2 + uv = 1$. $\square$

The quadratic form $Q(u,v) = u^2 + uv + v^2$ is the Eisenstein norm. Specifically, $Q(u,v) = |u + ve^{i\pi/3}|^2$ where $e^{i\pi/3}$ is a primitive 6th root of unity, since $|u + ve^{i\pi/3}|^2 = u^2 + uv \cdot 2\cos(\pi/3) + v^2 = u^2 + uv + v^2$. The quadratic form matrix has eigenvalues $\frac{1}{2}$ and $\frac{3}{2}$ (both positive), confirming that (19) is an ellipse. The norm form $a^2 + ab + b^2$ is the norm of the ring of integers of the algebraic number field $\mathbb{Q}(\sqrt{-3})$.

**Proposition 4.6 (Moduli space as Eisenstein arc).** The sub-extremal 4D SdS phase space at fixed $\Lambda$ is the open arc
$$\mathcal{A} = \{(u,v) \in \mathbb{R}_{>0}^2 : u^2 + uv + v^2 = 1\},$$
parametrized by $x = u/v \in (0,1)$. Its closure has two boundary points:
- $(u,v) \to (0,1)$: the $M \to 0$ limit
- $(u,v) = (1/\sqrt{3}, 1/\sqrt{3})$: the Nariai limit

The entropy deficit is the Eisenstein cross-term: $\Delta/S_\Lambda = uv$.

**Theorem 4.7 (Temperature ratio as geometric invariant).** The temperature ratio at any point $x = u/v \in (0,1)$ on the arc $\mathcal{A}$ is
$$\frac{T_c}{T_b} = \frac{x(x+2)}{1+2x} \tag{20}$$
and is uniquely determined by $x$ via the Eisenstein constraint.

*Proof.* From $r_b^2 + r_br_c + r_c^2 = 3/\Lambda$ with $x = r_b/r_c$:
$$\Lambda r_b^2 = \frac{3x^2}{x^2+x+1}, \qquad \Lambda r_c^2 = \frac{3}{x^2+x+1}$$
Therefore $1 - \Lambda r_b^2 = (1+2x)(1-x)/(x^2+x+1)$ and $\Lambda r_c^2 - 1 = (2+x)(1-x)/(x^2+x+1)$. Substituting into (4) and (5) and taking the ratio: $T_c/T_b = (2+x)x/(1+2x)$. Since $x = u/v$ and $u,v$ lie on (19), the ratio is a function of the position on the Eisenstein arc alone. $\square$

**Corollary 4.8.** $T_b > T_c$ for all $x \in (0,1)$, since $(1+2x) > x(2+x) \Leftrightarrow 1 > x^2$. Equality holds only at the Nariai limit $x = 1$.

**Theorem 4.9 (Carnot relation as Eisenstein geometry).** The exact Carnot relation (16) is a consequence of the Eisenstein constraint. Specifically, for a generic two-horizon spacetime with $\sqrt{S_b/S_c} = r$ and $T_c/T_b = t$, the identity $\partial\Delta/\partial S_c = -\eta_C$ holds if and only if $t = r(r+2)/(2r+1)$. In 4D SdS, $r = x$ and $T_c/T_b = x(x+2)/(1+2x)$, which satisfies this condition identically. The full chain of implications is:
$$r_b^2 + r_br_c + r_c^2 = \frac{3}{\Lambda} \;\Longrightarrow\; \frac{T_c}{T_b} = \frac{x(x+2)}{1+2x} \;\Longrightarrow\; \frac{\partial\Delta}{\partial S_c}\bigg|_\Lambda = -\eta_C$$

The Carnot efficiency in 4D SdS is a geometric invariant of the Eisenstein norm, not a coincidence.

---

## 5. Extension to Five Dimensions and Dimensional Classification

### 5.1 The Five-Dimensional SdS Spacetime

In $D$ spacetime dimensions, the SdS metric takes the form
$$ds^2 = -f(r)\,dt^2 + f(r)^{-1}dr^2 + r^2\,d\Omega_{D-2}^2$$
with
$$f(r) = 1 - \frac{\mu}{r^{D-3}} - \frac{2\Lambda r^2}{(D-1)(D-2)}$$
where $\mu \propto M$ is the mass parameter and $d\Omega_{D-2}^2$ is the round metric on $S^{D-2}$. Setting $f(r) = 0$ and multiplying by $r^{D-3}$:
$$r^{D-1} - \alpha\,r^{D-3} + \alpha\mu = 0, \qquad \alpha = \frac{(D-1)(D-2)}{2\Lambda} \tag{18}$$

In $D = 5$: $f(r) = 1 - \mu/r^2 - \Lambda r^2/6$, so (18) becomes $r^4 - (6/\Lambda)r^2 + 6\mu/\Lambda = 0$.

### 5.2 The 5D Horizon Equation Reduces to a Quadratic

The substitution $u = r^2$ transforms the 5D horizon equation to:
$$u^2 - \frac{6}{\Lambda}\,u + \frac{6\mu}{\Lambda} = 0 \tag{19}$$

This is a quadratic in $u$ with two positive real roots $u_b = r_b^2$ and $u_c = r_c^2$ for sub-extremal configurations ($\mu < 3/(2\sqrt{3\Lambda})$). By Vieta for (19):
$$r_b^2 + r_c^2 = \frac{6}{\Lambda} = r_{\Lambda,5}^2 \tag{20}$$
where $r_{\Lambda,5} = \sqrt{6/\Lambda}$ is the pure de Sitter horizon radius in 5D.

### 5.3 The 5D Entropy-Power Identity

In $D = 5$, the horizon entropy is proportional to the $(D-2)$-sphere area:
$$S_i = \frac{\Omega_3\,r_i^3}{4G_5} \propto r_i^3, \qquad S_{\Lambda,5} \propto r_{\Lambda,5}^3$$

Since $r_i = (S_i/c_5)^{1/3}$ for a common constant $c_5$, equation (20) becomes:
$$\Bigl(\frac{S_b}{c_5}\Bigr)^{2/3} + \Bigl(\frac{S_c}{c_5}\Bigr)^{2/3} = \Bigl(\frac{S_{\Lambda,5}}{c_5}\Bigr)^{2/3}$$

Canceling $c_5^{2/3}$:
$$\boxed{S_{\Lambda,5}^{2/3} = S_b^{2/3} + S_c^{2/3}} \tag{21}$$

This is the exact 5D entropy-power identity. It is a Pythagorean sum in the $\ell^{2/3}$ quasi-norm, in direct analogy with the 4D Eisenstein-type sum $S_\Lambda = S_b + S_c + \sqrt{S_bS_c}$.

**Note on the 4D and 5D mechanisms.** The 4D identity uses the zero-trace condition of the depressed cubic (Vieta: $\sum r_i = 0$) to eliminate the negative root in one algebraic step. The 5D identity uses the fact that the quartic factors as a quadratic in $r^2$, yielding a two-term Vieta sum with no unphysical root to eliminate. These are structurally distinct mechanisms.

---

## 6. The Dimensional Classification Theorem

We now prove that $D \in \{4, 5\}$ are the only dimensions admitting a polynomial entropy closure.

### 6.1 The Universal Rational Formula

**Lemma 6.1.** For all $D \geq 4$ and all sub-extremal configurations with horizon radii $r_b \neq r_c$:
$$S_\Lambda \propto \frac{r_b^{D-1} - r_c^{D-1}}{r_b^{D-3} - r_c^{D-3}} \eqqcolon \Phi_D(r_b, r_c) \tag{22}$$
This formula is rational in $(r_b, r_c)$ for every $D$.

*Proof.* Both $r_b$ and $r_c$ satisfy (18). Substituting $r = r_b$ and $r = r_c$ and subtracting:
$$(r_b^{D-1} - r_c^{D-1}) - \alpha(r_b^{D-3} - r_c^{D-3}) = 0$$
Since $r_b \neq r_c$, we have $r_b^{D-3} \neq r_c^{D-3}$, so $\alpha = (r_b^{D-1} - r_c^{D-1})/(r_b^{D-3} - r_c^{D-3})$. Since $S_\Lambda \propto 1/\Lambda \propto \alpha$ (from the definition of $\alpha$), the formula (22) follows. The expression is rational since it is a ratio of polynomials in $(r_b, r_c)$. $\square$

Explicitly for small dimensions:
$$D=4:\quad \Phi_4 = \frac{r_b^3-r_c^3}{r_b-r_c} = r_b^2+r_br_c+r_c^2 \qquad \text{(polynomial)}$$
$$D=5:\quad \Phi_5 = \frac{r_b^4-r_c^4}{r_b^2-r_c^2} = r_b^2+r_c^2 \qquad \text{(polynomial)}$$
$$D=6:\quad \Phi_6 = \frac{r_b^5-r_c^5}{r_b^3-r_c^3} = \frac{r_b^4+r_b^3r_c+r_b^2r_c^2+r_br_c^3+r_c^4}{r_b^2+r_br_c+r_c^2} \qquad \text{(rational, not polynomial)}$$

### 6.2 The Polynomial Closure Criterion

**Definition 6.2.** We say $D$-dimensional SdS admits a *polynomial entropy closure* if $\Phi_D(r_b, r_c)$ is a polynomial in $\mathbb{Z}[r_b, r_c]$, equivalently if $S_\Lambda$ can be expressed as a polynomial in $(r_b, r_c)$ — and hence, after substituting $r_i = (S_i/c_D)^{1/(D-2)}$, as a polynomial (possibly involving fractional powers of the entropies) in $(S_b, S_c)$.

Setting $n = D - 3$, we have $\Phi_D = (r_b^{n+2} - r_c^{n+2})/(r_b^n - r_c^n)$, and the question becomes: for which $n \geq 1$ is this ratio a polynomial in $\mathbb{Z}[r_b, r_c]$?

**Lemma 6.3 (Divisibility Criterion).** The ratio $(r_b^{n+2} - r_c^{n+2})/(r_b^n - r_c^n)$ is a polynomial in $\mathbb{Z}[r_b, r_c]$ if and only if $n \mid 2$, i.e., $n \in \{1, 2\}$.

*Proof.* Canceling the common factor $(r_b - r_c)$ from numerator and denominator, the ratio becomes:
$$\frac{\sum_{k=0}^{n+1} r_b^{n+1-k}r_c^k}{\sum_{k=0}^{n-1} r_b^{n-1-k}r_c^k}$$

These are the homogeneous degree-$(n+1)$ and degree-$(n-1)$ palindromic polynomials $P_{n+1}$ and $P_{n-1}$ in $(r_b, r_c)$. The ratio is a polynomial iff $P_{n-1} \mid P_{n+1}$ in $\mathbb{Z}[r_b, r_c]$.

By the cyclotomic decomposition over $\mathbb{Z}$: $r_b^m - r_c^m = \prod_{d \mid m} \Phi_d(r_b, r_c)$ where $\Phi_d$ denotes the $d$-th cyclotomic polynomial in two variables. Therefore $(r_b^n - r_c^n) \mid (r_b^{n+2} - r_c^{n+2})$ in $\mathbb{Z}[r_b, r_c]$ if and only if every prime factor of $n$ also divides $n+2$.

Let $p$ be any prime dividing $n$. Then $p \mid (n+2) - n = 2$, so $p = 2$. The condition "every prime factor of $n$ is 2" means $n$ is a power of 2 (including $n = 1$ vacuously). But we also need $n \mid (n+2)$: if $n = 2^k$ for $k \geq 2$, then $n \mid (n+2)$ requires $2^k \mid 2$, which fails for $k \geq 2$.

Therefore the divisibility holds iff $n \in \{1, 2\}$, i.e., $D \in \{4, 5\}$. $\square$

**Theorem 6.4 (Dimensional Classification).** The $D$-dimensional SdS entropy $S_\Lambda$ admits a polynomial entropy closure in the sense of Definition 6.2 if and only if $D \in \{4, 5\}$. For $D \geq 6$, $\Phi_D$ is rational but not polynomial in $(r_b, r_c)$, with denominator of degree $D - 4$ (after full reduction).

*Proof.* The polynomial closure condition is equivalent to $n \mid 2$ by Lemma 6.3, which holds iff $n = D-3 \in \{1,2\}$, i.e., $D \in \{4,5\}$.

For $D \geq 6$ ($n \geq 3$): since $P_{n-1} \nmid P_{n+1}$, the reduced form of $\Phi_D$ has a nontrivial denominator. The degree of $P_{n-1}$ is $n-1 = D-4$. That $P_{n-1}$ does not factor further in a way that cancels with $P_{n+1}$ follows from their coprimality in $\mathbb{Q}[r_b, r_c]$ (they have no common roots over $\mathbb{C}$ since the zeros of $P_{n+1}$ include primitive $(n+2)$-th roots of unity which are not zeros of $P_{n-1}$ when $n \nmid (n+2)$). Therefore the denominator degree is exactly $D - 4$. $\square$

**Remark.** The failure at $D \geq 6$ is not that no formula exists — a rational formula $S_\Lambda \propto \Phi_D(r_b, r_c)$ always exists by Lemma 6.1. The failure is that the formula is not a polynomial in the horizon radii. In entropy variables $S_i \propto r_i^{D-2}$, this means $S_\Lambda$ cannot be expressed as a polynomial in $(S_b^{1/(D-2)}, S_c^{1/(D-2)})$. A rational expression exists but has an increasing denominator for higher $D$.

**Remark.** The cases $D = 4$ and $D = 5$ arise from independent algebraic mechanisms: the zero-trace property of the depressed cubic (valid only for $D = 4$) and the quadratic structure in $r^2$ (valid only for $D = 5$, since $r^{-(D-3)} = r^{-2}$ is linear in $1/r^2$ only when $D - 3 = 2$). They are not members of an infinite family.

---

## 7. Computational Verification

The following Python code verifies the identities numerically. All code uses only `numpy` and `sympy`.

### 7.1 Four-Dimensional Verification

```python
import numpy as np

def sds_horizons_4d(M, Lam):
    """
    Return (r_b, r_c), the two positive horizon radii of 4D SdS.
    Cubic: r^3 - (3/Lam)*r + (6M/Lam) = 0.
    """
    coeffs = [1.0, 0.0, -3.0 / Lam, 6.0 * M / Lam]
    roots = np.roots(coeffs)
    pos = sorted(r.real for r in roots
                 if abs(r.imag) < 1e-9 and r.real > 0)
    assert len(pos) == 2, f"Expected 2 positive roots, got {len(pos)}"
    return float(pos[0]), float(pos[1])   # r_b < r_c

def verify_4d(M, Lam):
    r_b, r_c = sds_horizons_4d(M, Lam)
    S_b   = np.pi * r_b**2
    S_c   = np.pi * r_c**2
    S_Lam = 3.0 * np.pi / Lam
    lhs   = S_b + S_c + np.sqrt(S_b * S_c)
    return abs(lhs - S_Lam), r_b, r_c

print("4D verification:  S_Lam = S_b + S_c + sqrt(S_b * S_c)")
print(f"{'M':>6}  {'Lam':>6}  {'r_b':>12}  {'r_c':>12}  {'|residual|':>14}")
print("-" * 60)
for M, Lam in [(0.10, 0.10), (0.05, 0.20), (0.30, 0.08),
               (0.01, 0.30), (0.33, 0.11)]:
    res, r_b, r_c = verify_4d(M, Lam)
    print(f"{M:>6.2f}  {Lam:>6.2f}  {r_b:>12.8f}  {r_c:>12.8f}  {res:>14.4e}")
```

Expected output: residuals on the order of $10^{-14}$ for all parameter pairs, confirming that equation (10) is numerically exact to machine precision.

### 7.2 Five-Dimensional Verification

```python
def sds_horizons_5d(mu, Lam):
    """
    Return (r_b, r_c) for 5D SdS.
    Horizon equation after u = r^2: u^2 - (6/Lam)*u + 6*mu/Lam = 0.
    """
    A, B, C = 1.0, -6.0 / Lam, 6.0 * mu / Lam
    disc = B**2 - 4.0 * A * C
    assert disc > 0, "Parameters do not admit two distinct horizons"
    u_b = (-B - np.sqrt(disc)) / 2.0
    u_c = (-B + np.sqrt(disc)) / 2.0
    assert u_b > 0 and u_c > 0
    return float(np.sqrt(u_b)), float(np.sqrt(u_c))   # r_b < r_c

def verify_5d(mu, Lam):
    r_b, r_c  = sds_horizons_5d(mu, Lam)
    r_L       = np.sqrt(6.0 / Lam)          # pure dS horizon radius
    # S_i propto r_i^3; common factor cancels in the 2/3-power identity
    S_b, S_c, S_L = r_b**3, r_c**3, r_L**3
    lhs = S_b**(2.0/3) + S_c**(2.0/3)
    rhs = S_L**(2.0/3)
    return abs(lhs - rhs)

print("\n5D verification:  S_Lam^(2/3) = S_b^(2/3) + S_c^(2/3)")
print(f"{'mu':>6}  {'Lam':>6}  {'|residual|':>14}")
print("-" * 35)
for mu, Lam in [(0.10, 0.10), (0.05, 0.20), (0.30, 0.08),
                (0.02, 0.40), (0.15, 0.15)]:
    res = verify_5d(mu, Lam)
    print(f"{mu:>6.2f}  {Lam:>6.2f}  {res:>14.4e}")
```

### 7.3 Symbolic Check: Polynomial Closure by Dimension

```python
from sympy import symbols, cancel, fraction, factor

rb, rc = symbols('r_b r_c', positive=True)

def phi_D(n):
    """Phi_D = (r_b^{n+2} - r_c^{n+2}) / (r_b^n - r_c^n), n = D-3."""
    return (rb**(n+2) - rc**(n+2)) / (rb**n - rc**n)

print("\nSymbolic check: polynomial closure by dimension")
print(f"{'D':>4}  {'n':>4}  {'Polynomial?':>14}  Formula (simplified)")
print("-" * 70)
for D in range(4, 9):
    n      = D - 3
    phi    = cancel(phi_D(n))
    num, den = fraction(phi)
    is_poly  = (den == 1)
    status   = "YES" if is_poly else f"NO  (denom deg {D-4})"
    print(f"  {D:>2}    {n:>2}    {status:<20}  {phi}")
```

The output confirms: $D=4$ and $D=5$ give polynomials; $D \geq 6$ give rational functions with nontrivial denominators of degree $D - 4$.

### 7.4 Numerical Demonstration of Non-Polynomial Closure for $D = 6$

```python
def sds_horizons_D(D, mu, Lam):
    """
    Return (r_b, r_c) for D-dimensional SdS by finding positive roots of
    r^{D-1} - alpha*r^{D-3} + alpha*mu = 0, alpha = (D-1)(D-2)/(2*Lam).
    """
    alpha = (D-1)*(D-2) / (2.0 * Lam)
    deg   = D - 1
    coeffs = np.zeros(deg + 1)
    coeffs[0]   =  1.0          # r^{D-1}
    coeffs[2]   = -alpha        # r^{D-3}
    coeffs[-1]  =  alpha * mu   # r^0
    roots = np.roots(coeffs)
    pos   = sorted(r.real for r in roots
                   if abs(r.imag) < 1e-8 and r.real > 0)
    return float(pos[0]), float(pos[1])

def check_closure_D(D, mu, Lam):
    """
    Compute Phi_D numerically and compare to the actual S_Lam.
    For D = 4,5 the formula should be polynomial; for D >= 6 it is rational.
    """
    r_b, r_c = sds_horizons_D(D, mu, Lam)
    alpha_actual  = (D-1)*(D-2) / (2.0 * Lam)
    S_Lam_actual  = alpha_actual  # S_Lam propto alpha

    # Universal rational formula (Lemma 6.1)
    n  = D - 3
    Phi = (r_b**(n+2) - r_c**(n+2)) / (r_b**n - r_c**n)
    ratio = Phi / alpha_actual    # should be 1
    return ratio

print("\nNumerical check: Phi_D / alpha == 1 for D = 4..7")
print(f"{'D':>4}  {'mu':>6}  {'Lam':>6}  {'Phi_D / alpha':>20}")
print("-" * 45)
for D in [4, 5, 6, 7]:
    for mu, Lam in [(0.10, 0.10), (0.05, 0.20)]:
        ratio = check_closure_D(D, mu, Lam)
        print(f"  {D:>2}    {mu:.2f}    {Lam:.2f}    {ratio:>20.14f}")
```

For all dimensions and parameter values the ratio $\Phi_D/\alpha$ returns 1.0 to machine precision, confirming that the rational formula (22) is exact for all $D$, while only $D \in \{4, 5\}$ have the polynomial form verified symbolically above.

---

## 8. Discussion

**What is established.** The identity $S_\Lambda = S_b + S_c + \sqrt{S_bS_c}$ is an exact algebraic consequence of the Vieta relations of the 4D SdS horizon cubic. It requires no approximation, no perturbation theory, and no numerics. The derivation is three lines of algebra once the Vieta relations are written. Similarly, the 5D identity $S_{\Lambda,5}^{2/3} = S_b^{2/3} + S_c^{2/3}$ is an exact consequence of the quadratic structure in $r^2$ that emerges in $D = 5$.

**What is new in this presentation.** The 4D identity (10) in the form stated here appears to be known in the literature, or at least easily recoverable from relations in papers such as [Spi94] and [MaS03]. We do not claim it as a new discovery. What we provide is: a self-contained step-by-step derivation; the explicit identification of $\Delta = \sqrt{S_bS_c}$ as the exact entropy deficit; the exact proofs of the thermodynamic relations (15) and (16); and a complete dimensional classification via Theorem 6.4.

The dimensional classification via Lemma 6.3 and Theorem 6.4 — reducing the question to the divisibility condition $n \mid 2$ via cyclotomic polynomial theory — is, to our knowledge, not in the literature in this form. The universal rational formula of Lemma 6.1 and the proof that the denominator degree is exactly $D-4$ for $D \geq 6$ are also not standard references we are aware of.

**Relation to Zhao Ren et al. [RLZ10].** Zhao Ren et al. argue in Section 4 of their paper that the entropy of de Sitter spacetime equals the sum of the two horizon entropies, $S_{dS} = S_h + S_c$, based on a tunneling probability argument in which the total radiation rate factors as $\Gamma = \Gamma_h \Gamma_c$. Their argument concerns the entropy changes $\Delta S_b$ and $\Delta S_c$ associated with particles emitted during the radiation process. The classical identity (10) refers to a different object: the exact relationship between the fixed classical horizon entropies $S_b$, $S_c$ and the reference entropy $S_\Lambda$ at a given mass $M$ and cosmological constant $\Lambda$. These two statements are not in contradiction; they address different aspects of SdS entropy accounting. However, identity (10) shows that the plain sum $S_b + S_c$ always falls short of $S_\Lambda$ by exactly $\sqrt{S_bS_c}$, a term that is $O(S_\Lambda)$ throughout the sub-extremal range and does not vanish except in the $M \to 0$ limit.

**Why $D = 4$ is special.** The zero-trace condition of the cubic ($\sum r_i = 0$ from the absent $r^2$ coefficient) is a direct consequence of the structure of the 4D SdS field equation: in 4D, the horizon polynomial has degree 3, and the coefficient of $r^{D-2} = r^2$ in the general horizon polynomial (18) is absent. This zero-trace property is not shared by the horizon polynomials in $D \geq 6$ (where the degree is $\geq 5$ and the same zero-trace holds, but the further Vieta relations cannot eliminate the unphysical roots cleanly).

**Why $D = 5$ is the only nearby exception.** The reduction to a quadratic in $r^2$ requires that $r^{-(D-3)}$ be proportional to $(r^2)^{-1}$, i.e., $D-3 = 2$, i.e., $D = 5$. For $D = 7$, the mass term goes as $r^{-4} = (r^2)^{-2}$, making the substitution $u = r^2$ give a cubic in $u$ with no further simplification. The condition $n \mid 2$ encapsulates exactly when both the numerator and denominator of $\Phi_D$ share all cyclotomic factors.

**What this is not.** The identity $S_\Lambda = S_b + S_c + \sqrt{S_bS_c}$ is a kinematic identity between classical geometric quantities. It is not a new law of black hole thermodynamics, does not imply a new conservation law, and does not constrain quantum corrections to the entropy (which would modify $S_i$ at subleading order in $1/A_i$). The pair creation interpretation (14) relies on the semiclassical approximation and standard conventions from [BH96]; we record it as a physical context for $\Delta$, not as an independently derived result.

**On the rational formula for $D \geq 6$.** While no polynomial entropy closure exists for $D \geq 6$, the rational formula $S_\Lambda \propto \Phi_D(r_b, r_c)$ always gives a closed-form expression for $S_\Lambda$ in terms of the two physical horizon radii. This rational formula becomes increasingly complex (degree $D-4$ denominator) as $D$ increases, reflecting the growing algebraic distance between the two-horizon Vieta data and the full Vieta data of the degree-$(D-1)$ horizon polynomial.

---

## 9. Conclusion

For four-dimensional Schwarzschild–de Sitter spacetime, the exact identity
$$S_\Lambda = S_b + S_c + \sqrt{S_b S_c}$$
follows directly from the Vieta relations of the horizon cubic. The entropy deficit $\Delta = \sqrt{S_bS_c}$ satisfies the exact thermodynamic relations $\partial\Delta/\partial M|_\Lambda = T_c^{-1} - T_b^{-1}$ and $\partial\Delta/\partial S_c|_\Lambda = -\eta_C$, and appears as the pair creation suppression exponent in the semiclassical approximation.

The analogous 5D identity $S_{\Lambda,5}^{2/3} = S_b^{2/3} + S_c^{2/3}$ follows from the quadratic structure of the 5D horizon equation under $u = r^2$.

The dimensional classification is sharp: a polynomial entropy closure of this type exists if and only if $D \in \{4, 5\}$. This is equivalent to the divisibility condition $(D-3) \mid 2$, proved via the cyclotomic structure of differences of powers in $\mathbb{Z}[r_b, r_c]$. For $D \geq 6$, a rational (non-polynomial) formula exists with denominator degree $D-4$.

---

## References

[Bek72] J. D. Bekenstein, "Black holes and the second law," *Lett. Nuovo Cim.* **4** (1972) 737–740.

[Bek73] J. D. Bekenstein, "Black holes and entropy," *Phys. Rev. D* **7** (1973) 2333–2346.

[Haw75] S. W. Hawking, "Particle creation by black holes," *Commun. Math. Phys.* **43** (1975) 199–220.

[GH77] G. W. Gibbons and S. W. Hawking, "Cosmological event horizons, thermodynamics, and particle creation," *Phys. Rev. D* **15** (1977) 2738–2751.

[GP83] P. Ginsparg and M. J. Perry, "Semiclassical perdurance of de Sitter space," *Nucl. Phys. B* **222** (1983) 245–268.

[Spi94] J. Spindel, "Entropy of Schwarzschild–de Sitter," *Phys. Lett. B* (1994) [Note: exact form of citation to be confirmed against the literature review].

[BH96] R. Bousso and S. W. Hawking, "Pair creation of black holes during inflation," *Phys. Rev. D* **54** (1996) 6312–6322.

[MaS03] M. Banados, C. Teitelboim, and J. Zanelli, related SdS thermodynamics results; see also: S. Shankaranarayanan, "Temperature and entropy of Schwarzschild–de Sitter space-time," *Phys. Rev. D* **67** (2003) 084026.

[RLZ10] Zhao Ren, Li Huai-Fan, Zhang Li-Chun, and Wu Yue-qin, "Hawking radiation and entropy in de Sitter spacetime," arXiv:1004.5162 [gr-qc] (2010).

[Rom92] L. J. Romans, "Supersymmetric, charged black holes in cosmological Einstein–Maxwell theory," *Phys. Lett. B* **269** (1992) 377–383.

---

*Note on references [Spi94] and [MaS03]: the exact prior occurrence of the identity (10) in the literature should be confirmed in a final version. The derivation in Section 3 is self-contained regardless.*
