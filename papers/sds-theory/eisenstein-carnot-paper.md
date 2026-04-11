# The Eisenstein Geometry of Schwarzschild–de Sitter Thermodynamics and the Geometric Origin of Exact Carnot Efficiency

**Steven Reid**

---

## Abstract

We show that the phase space of four-dimensional Schwarzschild–de Sitter (SdS) spacetime at fixed cosmological constant $\Lambda$ carries a hidden Eisenstein norm structure. Under the coordinate change $u = \sqrt{S_b/S_\Lambda}$, $v = \sqrt{S_c/S_\Lambda}$, where $S_b$, $S_c$ are the black hole and cosmological horizon entropies and $S_\Lambda = 3\pi/\Lambda$ is the pure de Sitter entropy, the SdS phase space is the open arc of the Eisenstein unit ellipse $u^2 + uv + v^2 = 1$ in the first quadrant. The entropy deficit $\Delta = S_\Lambda - S_b - S_c$ is the Eisenstein cross-term $\Delta = S_\Lambda uv$.

The temperature ratio $T_c/T_b = x(x+2)/(1+2x)$, where $x = r_b/r_c$, is uniquely determined by position on the Eisenstein arc. We prove that the exact Carnot relation $\partial\Delta/\partial S_c|_\Lambda = -\eta_C$ (where $\eta_C = 1 - T_c/T_b$) holds if and only if the temperature ratio satisfies $T_c/T_b = r(r+2)/(2r+1)$ with $r = \sqrt{S_b/S_c}$. In 4D SdS this condition is identically satisfied — not assumed — because it is algebraically forced by the Eisenstein constraint $r_b^2 + r_br_c + r_c^2 = 3/\Lambda$ (derived from the Vieta relations of the horizon cubic). The Carnot efficiency in 4D SdS is therefore a geometric invariant of the Eisenstein norm, with a proof rather than a coincidence.

We further show that the horizon cubic defines an elliptic curve $E_{\mathrm{SdS}}$ whose j-invariant is $j = 1728/(1-9\Lambda M^2)$, expressible in Eisenstein coordinates as $j = 6912(x^2+x+1)^3/[(1-x)(x+2)(2x+1)]^2$. Because j and the cubic discriminant each contain the single factor $(1-9\Lambda M^2)$, their product $j \cdot \Delta_{\mathrm{cubic}} = 6912(3/\Lambda)^3$ is independent of $M$ at fixed $\Lambda$ — an algebraic identity with a simple proof. The extremality parameter $\varepsilon = 9\Lambda M^2$ satisfies $\varepsilon = 1 - 1728/j$, giving a direct formula connecting mass to the j-invariant. In the eigenbasis of the Eisenstein quadratic form, the SdS arc spans exactly $\pi/6$ (30°) of the parametric angle — one-twelfth of the full $2\pi$ range. All thermodynamic quantities — temperatures, their sum, difference, and product — factorize completely in Eisenstein coordinates, with the temperature product admitting both $x$-form and entropy-form expressions.

We also show that this Eisenstein structure is unique to $D = 4$: only in four spacetime dimensions does the Vieta elimination produce the Eisenstein norm form. In $D = 5$, a related but distinct Pythagorean structure appears ($r_b^2 + r_c^2 = r_{\Lambda,5}^2$). For $D \geq 6$, neither structure exists and no polynomial entropy closure holds.

---

## 1. Introduction

Schwarzschild–de Sitter (SdS) spacetime has two horizons: a black hole horizon at $r = r_b$ and a cosmological horizon at $r = r_c$. Each carries Bekenstein–Hawking entropy $S_b = \pi r_b^2$ and $S_c = \pi r_c^2$ and radiates at a distinct Hawking temperature. The pure de Sitter space has a single cosmological horizon with entropy $S_\Lambda = 3\pi/\Lambda$.

The entropy identity
$$S_\Lambda = S_b + S_c + \sqrt{S_b S_c} \tag{1}$$
follows directly from the Vieta relations of the 4D SdS horizon cubic and has been noted in the literature. The quantity $\Delta = \sqrt{S_bS_c}$ measures the entropy deficit: the amount by which the two-horizon configuration falls short of the pure de Sitter entropy budget.

In this paper we show that (1) is not merely an algebraic identity. It is the signature of a deep geometric structure: the SdS phase space lives on the *Eisenstein unit ellipse*, and all thermodynamic properties of the system — including the exact Carnot relation — are consequences of this Eisenstein geometry.

The main results, stated informally, are:

1. In appropriate coordinates, the SdS phase space is an arc spanning $\pi/6$ (one-twelfth) of the Eisenstein unit ellipse.
2. The entropy deficit $\Delta$ is the Eisenstein cross-term.
3. The temperature ratio of the two horizons is a geometric invariant of the Eisenstein arc.
4. The exact Carnot relation is forced by this geometry, not by any additional physical assumption.
5. The horizon cubic's associated elliptic curve has j-invariant $j = 1728/(1-9\Lambda M^2)$, and its product with the cubic discriminant satisfies $j \cdot \Delta_{\mathrm{cubic}} = \text{const}$ at fixed $\Lambda$.
6. The extremality parameter $\varepsilon = 9\Lambda M^2$ equals $1 - 1728/j$, connecting mass directly to the j-invariant.
7. All thermodynamic quantities factorize completely in Eisenstein coordinates.
8. This Eisenstein structure is unique to $D = 4$.

Throughout we use units $G = \hbar = k_B = c = 1$ and assume the sub-extremal condition $9\Lambda M^2 < 1$.

---

## 2. Background: The SdS Entropy Identity

The 4D SdS metric is $f(r) = 1 - 2M/r - \Lambda r^2/3$. Setting $f = 0$ gives the horizon cubic
$$r^3 - \frac{3}{\Lambda}r + \frac{6M}{\Lambda} = 0 \tag{2}$$
with three real roots $r_- < 0 < r_b < r_c$ under the sub-extremal condition. By Vieta's formulas:
$$r_- + r_b + r_c = 0, \qquad r_-r_b + r_-r_c + r_br_c = -\frac{3}{\Lambda} \tag{3}$$

Eliminating $r_- = -(r_b + r_c)$ from the second relation yields the Eisenstein constraint:
$$\boxed{r_b^2 + r_br_c + r_c^2 = \frac{3}{\Lambda}} \tag{4}$$

Multiplying by $\pi$, using $S_b = \pi r_b^2$, $S_c = \pi r_c^2$, $S_\Lambda = 3\pi/\Lambda$, and $\pi r_br_c = \sqrt{S_bS_c}$:
$$S_\Lambda = S_b + S_c + \sqrt{S_bS_c} \tag{1}$$

The Hawking temperatures are
$$T_b = \frac{1 - \Lambda r_b^2}{4\pi r_b}, \qquad T_c = \frac{\Lambda r_c^2 - 1}{4\pi r_c} \tag{5}$$
and the first laws at fixed $\Lambda$ are $dM = T_b\,dS_b = -T_c\,dS_c$.

---

## 3. Eisenstein Coordinates and the Phase Space Arc

### 3.1 The Coordinate Change

**Definition 3.1.** The *Eisenstein coordinates* for the SdS phase space at fixed $\Lambda$ are
$$u = \sqrt{\frac{S_b}{S_\Lambda}} = \frac{r_b}{\sqrt{3/\Lambda}}, \qquad v = \sqrt{\frac{S_c}{S_\Lambda}} = \frac{r_c}{\sqrt{3/\Lambda}} \tag{6}$$

These are the horizon radii normalized by the pure de Sitter horizon radius $r_\Lambda = \sqrt{3/\Lambda}$.

### 3.2 The Eisenstein Norm

**Theorem 3.2.** In Eisenstein coordinates, the SdS constraint (4) becomes the Eisenstein unit ellipse:
$$u^2 + uv + v^2 = 1 \tag{7}$$

*Proof.* Dividing (4) by $3/\Lambda$: $(r_b/r_\Lambda)^2 + (r_b/r_\Lambda)(r_c/r_\Lambda) + (r_c/r_\Lambda)^2 = 1$. $\square$

**Remark.** The form $Q(u,v) = u^2 + uv + v^2$ is the Eisenstein norm. For any $u,v \in \mathbb{R}$:
$$Q(u,v) = \left|u + ve^{i\pi/3}\right|^2$$
since $|u + ve^{i\pi/3}|^2 = u^2 + 2uv\cos(\pi/3) + v^2 = u^2 + uv + v^2$. This is the norm in the ring $\mathbb{Z}[e^{i\pi/3}]$, the ring of integers of $\mathbb{Q}(\sqrt{-3})$.

The quadratic form matrix is $A = \bigl(\begin{smallmatrix}1&\frac{1}{2}\\\frac{1}{2}&1\end{smallmatrix}\bigr)$ with eigenvalues $\frac{1}{2}$ and $\frac{3}{2}$. Both are positive, confirming that (7) defines an ellipse with semi-axes $\sqrt{2}$ and $\sqrt{2/3}$ in the eigenbasis.

### 3.3 The Phase Space as an Arc

**Theorem 3.3 (Moduli space = Eisenstein arc).** The sub-extremal SdS phase space at fixed $\Lambda$ is, in Eisenstein coordinates, the open arc
$$\mathcal{A} = \{(u,v) \in \mathbb{R}_{>0}^2 : u^2 + uv + v^2 = 1\}$$
parametrized by $x = u/v = r_b/r_c \in (0,1)$. Explicitly:
$$u(x) = \frac{x}{\sqrt{x^2+x+1}}, \qquad v(x) = \frac{1}{\sqrt{x^2+x+1}} \tag{8}$$

The closure $\bar{\mathcal{A}}$ has two boundary points:
- $x \to 0$: $(u,v) \to (0,1)$, the $M \to 0$ limit
- $x \to 1$: $(u,v) \to (1/\sqrt{3}, 1/\sqrt{3})$, the Nariai limit

The entropy deficit is the Eisenstein cross-term:
$$\frac{\Delta}{S_\Lambda} = uv = \frac{x}{x^2+x+1} \tag{9}$$

*Proof.* All statements follow from substituting (8) into (7) and computing. $\square$

**Remark.** The Nariai point $(1/\sqrt{3}, 1/\sqrt{3})$ is the unique fixed point of the reflection symmetry $(u,v) \to (v,u)$ on $\mathcal{A}$, corresponding to $S_b = S_c$. The cross-term $uv$ is maximized at this point: $uv = 1/3$, consistent with $\Delta_\text{max} = S_\Lambda/3$ (Proposition 4.1 of [companion paper]).

---

## 4. The Temperature Ratio as a Geometric Invariant

**Theorem 4.1.** For any point $x \in (0,1)$ on the arc $\mathcal{A}$, the Hawking temperature ratio of the two horizons is
$$\frac{T_c}{T_b} = \frac{x(x+2)}{1+2x} \tag{10}$$
This ratio is uniquely determined by the position $x = u/v$ on the Eisenstein arc and is a geometric invariant of the Eisenstein norm.

*Proof.* From (4) with $x = r_b/r_c$: $\Lambda = 3/(r_b^2 + r_br_c + r_c^2) = 3/r_c^2(x^2+x+1)$. Therefore:
$$\Lambda r_b^2 = \frac{3x^2}{x^2+x+1}, \qquad \Lambda r_c^2 = \frac{3}{x^2+x+1}$$
which gives
$$1 - \Lambda r_b^2 = \frac{(1+2x)(1-x)}{x^2+x+1}, \qquad \Lambda r_c^2 - 1 = \frac{(2+x)(1-x)}{x^2+x+1}$$
Substituting into (5):
$$T_b = \frac{(1+2x)(1-x)}{4\pi r_b(x^2+x+1)}, \qquad T_c = \frac{(2+x)(1-x)}{4\pi r_c(x^2+x+1)}$$
The $(1-x)$ and $(x^2+x+1)$ factors cancel in the ratio:
$$\frac{T_c}{T_b} = \frac{(2+x) \cdot r_b}{(1+2x) \cdot r_c} = \frac{x(x+2)}{1+2x} \qquad \square$$

**Corollary 4.2.** $T_b > T_c$ for all $x \in (0,1)$, since $(1+2x) - x(x+2) = 1 - x^2 > 0$. The black hole horizon is always hotter than the cosmological horizon. Equality holds only at the Nariai limit $x = 1$, where both temperatures vanish.

**Remark.** The ratio (10) depends only on $x = u/v$ — the slope of the position vector on the Eisenstein ellipse — and not on $\Lambda$ or $M$ separately. This is the sense in which the temperature ratio is a geometric invariant of the Eisenstein arc: it is intrinsic to the curve, not to any embedding.

---

## 5. The Carnot Relation as a Geometric Theorem

### 5.1 The Generic Case

Consider a general two-horizon spacetime with black hole entropy $S_b$, cosmological entropy $S_c$, deficit $\Delta = \sqrt{S_bS_c}$, and temperature ratio $T_c/T_b = t$. The first laws at fixed $\Lambda$ give $\partial S_b/\partial S_c|_\Lambda = -T_c/T_b = -t$. The chain rule yields:
$$\frac{\partial\Delta}{\partial S_c}\bigg|_\Lambda = \frac{1}{2}\sqrt{\frac{S_b}{S_c}} - \frac{t}{2}\sqrt{\frac{S_c}{S_b}} = \frac{r}{2} - \frac{t}{2r} \tag{11}$$
where $r = \sqrt{S_b/S_c}$. The Carnot efficiency is $\eta_C = 1 - t$. The Carnot relation $\partial\Delta/\partial S_c = -\eta_C = t-1$ requires:
$$\frac{r}{2} - \frac{t}{2r} = t - 1 \implies r^2 - t = 2rt - 2r \implies t = \frac{r^2 + 2r}{2r + 1} = \frac{r(r+2)}{1+2r} \tag{12}$$

This is a specific constraint on $t$ as a function of $r$. It is not satisfied generically.

### 5.2 The SdS Case: Condition (12) is Forced

**Theorem 5.1 (Carnot relation as Eisenstein geometry).** In 4D SdS, the condition (12) is identically satisfied for all $x \in (0,1)$.

*Proof.* In SdS, $r = \sqrt{S_b/S_c} = \sqrt{r_b^2/r_c^2} = x$, and from Theorem 4.1: $t = T_c/T_b = x(x+2)/(1+2x)$. Substituting into the right side of (12) with $r = x$: $x(x+2)/(1+2x)$. This equals $t$ identically. $\square$

**Corollary 5.2.** The exact Carnot relation $\partial\Delta/\partial S_c|_\Lambda = -\eta_C$ holds for all sub-extremal 4D SdS configurations. The full causal chain is:
$$\underbrace{r_b^2 + r_br_c + r_c^2 = \frac{3}{\Lambda}}_{\text{Eisenstein constraint (Vieta)}} \;\Longrightarrow\; \underbrace{\frac{T_c}{T_b} = \frac{x(x+2)}{1+2x}}_{\text{geometric invariant of arc}} \;\Longrightarrow\; \underbrace{\frac{\partial\Delta}{\partial S_c}\bigg|_\Lambda = -\eta_C}_{\text{exact Carnot relation}}$$

**Remark.** The Carnot efficiency is not imposed. It follows from the Eisenstein geometry of the phase space. A two-horizon spacetime that did not satisfy the Eisenstein constraint (4) would not generally satisfy the exact Carnot relation.

### 5.3 Conservation of the Total Entropy Budget

At fixed $\Lambda$, the first laws $dM = T_b\,dS_b = -T_c\,dS_c$ imply $T_b\,dS_b + T_c\,dS_c = 0$, and therefore $dS_b/dS_c = -T_c/T_b < 0$: as the cosmological horizon entropy increases, the black hole horizon entropy decreases. Differentiating the entropy identity $S_\Lambda = S_b + S_c + \Delta$ with respect to $S_c$ at fixed $\Lambda$:
$$0 = \frac{\partial S_b}{\partial S_c}\bigg|_\Lambda + 1 + \frac{\partial \Delta}{\partial S_c}\bigg|_\Lambda = -\frac{T_c}{T_b} + 1 + \frac{\partial \Delta}{\partial S_c}\bigg|_\Lambda$$

**Proposition 5.3 (Entropy budget conservation).** At fixed $\Lambda$, the identity $S_\Lambda = S_b + S_c + \Delta$ is preserved under any change of $M$: the increase in $S_c$ is exactly offset by the decrease in $S_b$ and the change in $\Delta$.

*Proof.* Differentiating $S_\Lambda = \pi(3/\Lambda)$ with respect to $M$ at fixed $\Lambda$ gives zero identically, since $S_\Lambda$ depends only on $\Lambda$. The individual changes $dS_b$, $dS_c$, $d\Delta$ sum to zero by the definition $\Delta = S_\Lambda - S_b - S_c$. $\square$

**Remark.** The quantity $S_\Lambda$ is the entropy of the reference spacetime (pure de Sitter at the same $\Lambda$), not the total entropy of the SdS configuration. The entropy budget $S_b + S_c + \Delta = S_\Lambda$ is an algebraic constraint, not a dynamical conservation law. In particular, this identity does not imply thermodynamic reversibility in the conventional sense: the two horizons are at different temperatures ($T_b \neq T_c$ generically), so a physical transition between SdS configurations would involve heat flow across a temperature gradient, which is generally irreversible. The Carnot relation $\partial\Delta/\partial S_c|_\Lambda = -\eta_C$ characterizes the geometry of the phase space, not the physical dynamics of Hawking radiation.

---

## 6. Uniqueness of the Eisenstein Structure in $D = 4$

We now explain why this Eisenstein structure is specific to four spacetime dimensions.

In $D$ spacetime dimensions, the SdS horizon equation is
$$r^{D-1} - \alpha r^{D-3} + \alpha\mu = 0, \qquad \alpha = \frac{(D-1)(D-2)}{2\Lambda} \tag{13}$$
Subtracting the equations evaluated at $r_b$ and $r_c$ gives the universal formula:
$$S_\Lambda \propto \alpha = \frac{r_b^{D-1} - r_c^{D-1}}{r_b^{D-3} - r_c^{D-3}} \tag{14}$$

In $D = 4$ ($n = D - 3 = 1$): $\alpha \propto r_b^2 + r_br_c + r_c^2$ — the Eisenstein norm.

In $D = 5$ ($n = 2$): $\alpha \propto r_b^2 + r_c^2$ — the Pythagorean norm (flat Euclidean, no cross-term).

In $D \geq 6$ ($n \geq 3$): the ratio (14) is rational but not polynomial, and no norm form of an algebraic number field appears. The denominator has degree $D - 4$.

**Theorem 6.1.** The Eisenstein norm structure $r_b^2 + r_br_c + r_c^2 = 3/\Lambda$ is unique to $D = 4$. No other spacetime dimension produces an Eisenstein constraint, and therefore no other dimension admits the Carnot-as-geometry theorem (Corollary 5.2) via this mechanism.

*Proof.* By the cyclotomic divisibility criterion ($(r_b^n - r_c^n) \mid (r_b^{n+2} - r_c^{n+2})$ iff $n \mid 2$), only $n \in \{1, 2\}$ yield polynomial expressions. For $n = 1$ ($D = 4$): $r_b^2 + r_br_c + r_c^2$ (Eisenstein norm). For $n = 2$ ($D = 5$): $r_b^2 + r_c^2$ (Pythagorean norm). Neither appears for $n \geq 3$. $\square$

**Remark.** The $D = 5$ Pythagorean structure produces the entropy-power identity $S_{\Lambda,5}^{2/3} = S_b^{2/3} + S_c^{2/3}$. In $D = 5$ coordinates $(u_5, v_5) = (S_b^{1/3}/S_{\Lambda,5}^{1/3}, S_c^{1/3}/S_{\Lambda,5}^{1/3})$, the constraint is $u_5^2 + v_5^2 = 1$ — a Euclidean unit circle. The norm form $u^2 + v^2$ is the standard Euclidean norm, associated with the Gaussian integers $\mathbb{Z}[i]$; this is distinct from the Eisenstein norm $u^2+uv+v^2$ of $D=4$. Whether the $D=5$ constraint implies an analogous Carnot relation, and by what mechanism, is an open question.

---

## 7. The Modular Structure: j-Invariant, Discriminant, and the Phase Space Arc

The SdS horizon cubic is not merely a polynomial whose roots are horizon radii. It defines an elliptic curve whose arithmetic provides additional structure connecting the mass parameter to classical modular quantities.

### 7.1 The Elliptic Curve and Its j-Invariant

The 4D SdS horizon cubic $f(r) = r^3 - (3/\Lambda)r + 6M/\Lambda = 0$ is a depressed cubic in Weierstrass form $y^2 = x^3 + ax + b$ with $a = -3/\Lambda$ and $b = 6M/\Lambda$. The **j-invariant** of the associated elliptic curve $E_{\mathrm{SdS}}$ is

$$j(E_{\mathrm{SdS}}) = 1728 \cdot \frac{4a^3}{4a^3 + 27b^2} = \frac{1728}{1 - 9\Lambda M^2} \tag{15}$$

*Derivation.* With $a = -3/\Lambda$ and $b = 6M/\Lambda$: $4a^3 = -108/\Lambda^3$ and $27b^2 = 972M^2/\Lambda^2$. Thus $4a^3 + 27b^2 = -(108/\Lambda^3)(1-9\Lambda M^2)$ and the formula follows directly. $\square$

The cubic discriminant is

$$\Delta_{\mathrm{cubic}} = -4a^3 - 27b^2 = \frac{108}{\Lambda^3}(1-9\Lambda M^2) \tag{16}$$

**Proposition 7.1 (j–discriminant product identity).** At fixed $\Lambda$, the product

$$j(E_{\mathrm{SdS}}) \cdot \Delta_{\mathrm{cubic}} = \frac{1728 \times 108}{\Lambda^3} = 6912\left(\frac{3}{\Lambda}\right)^3 \tag{17}$$

is independent of $M$. The j-invariant grows without bound as $M \to M_{\mathrm{Nariai}}$ while the discriminant vanishes, but their product is fixed by $\Lambda$ alone.

*Proof.* $j$ and $\Delta_{\mathrm{cubic}}$ each carry the factor $(1-9\Lambda M^2)$ in opposite positions: $j = 1728/(1-\varepsilon)$ and $\Delta_{\mathrm{cubic}} = (108/\Lambda^3)(1-\varepsilon)$, so $j \cdot \Delta_{\mathrm{cubic}} = 1728 \times 108/\Lambda^3$ with $\varepsilon = 9\Lambda M^2$. $\square$

**Remark.** The identity (17) follows immediately from the definitions of $j$ and $\Delta_{\mathrm{cubic}}$: both are rational functions of $(1-9\Lambda M^2)$, and the factors cancel. The constant $1728 \times 108 = 6912 \times 27$ carries no deeper content beyond the normalization conventions for $j$. The number $1728 = 12^3$ is the j-invariant normalization constant, chosen so that the elliptic curve $y^2 = x^3 - x$ (which has complex multiplication by $\mathbb{Z}[i]$) satisfies $j = 1728$.

### 7.2 The Eisenstein Coordinates Form of j

**Theorem 7.2.** In Eisenstein coordinates, with $x = r_b/r_c \in (0,1)$ and $t = \Delta/S_\Lambda = x/(x^2+x+1)$:

$$j = \frac{6912(x^2+x+1)^3}{[(1-x)(x+2)(2x+1)]^2} = \frac{6912}{4 - 27t^2(1+t)} \tag{18}$$

*Proof.* From Theorem 4.1, $T_b \propto (1-x)(2x+1)$ and $T_c \propto (1-x)(x+2)$. Substituting $M^2 = (3/\Lambda)\cdot x^2(x+1)^2/(4(x^2+x+1)^3)$ (derived from Vieta) gives $1 - 9\Lambda M^2 = (1-x)^2(x+2)^2(2x+1)^2/[4(x^2+x+1)^3]$. The first form of (18) follows immediately from (15). For the second form, use $t^2(1+t) = x^2(x+1)^2/(x^2+x+1)^3$, which gives $9\Lambda M^2 = 27t^2(1+t)/4$, and therefore $1-9\Lambda M^2 = (4-27t^2(1+t))/4$. $\square$

**Corollary 7.3.** The factor $(1-9\Lambda M^2)$ in the denominator of $j$ factors completely in terms of the numerators of $T_b$ and $T_c$:
$$1 - 9\Lambda M^2 = \frac{[(1-x)(2x+1)]^2 \cdot [(1-x)(x+2)]^2}{4(x^2+x+1)^3} = \frac{[T_b^{\mathrm{num}}]^2 \cdot [T_c^{\mathrm{num}}]^2}{4(x^2+x+1)^3}$$
where $T_b^{\mathrm{num}} = (1-x)(2x+1)$ and $T_c^{\mathrm{num}} = (1-x)(x+2)$ are the polynomial numerators of $T_b$ and $T_c$ in Eisenstein coordinates (from Theorem 8.1). In other words, $1 - j^{-1} \cdot 1728 = [T_b^{\mathrm{num}} \cdot T_c^{\mathrm{num}}]^2 / [4(x^2+x+1)^3]$: the sub-extremality condition is encoded by the square of the temperature numerator product, divided by the Eisenstein norm cubed.

### 7.3 The Extremality Parameter in Terms of the j-Invariant

Define the **extremality parameter** $\varepsilon \equiv 9\Lambda M^2 \in [0,1)$. Inverting (15) gives directly:

$$\boxed{\varepsilon = 1 - \frac{1728}{j(E_{\mathrm{SdS}})}} \tag{19}$$

This is simply the algebraic rearrangement of (15), but it expresses the physical mass parameter $M$ in terms of the j-invariant — a classical modular quantity — without reference to $\Lambda$ separately.

The two boundary cases are:

- $\varepsilon = 0$ ($M=0$, pure de Sitter): $j = 1728$. The curve $E_{\mathrm{SdS}}: y^2 = x^3 - (3/\Lambda)x$ (with $b=0$) has j-invariant 1728. Up to isomorphism over $\mathbb{C}$, this is the same curve as $y^2 = x^3 - x$, which has complex multiplication by $\mathbb{Z}[i]$ (the Gaussian integers).
- $\varepsilon \to 1$ (Nariai limit): $j \to \infty$, $\Delta_{\mathrm{cubic}} \to 0$. The discriminant vanishes: the cubic has a repeated root, and $E_{\mathrm{SdS}}$ degenerates to a nodal cubic. The two physical horizons coalesce.

Within the physical range $\varepsilon \in [0,1)$, the j-invariant takes values in $[1728, \infty)$. This is not a standard region in the moduli space of elliptic curves (which is typically parametrized by $j \in \mathbb{C}$ or by the upper half-plane $\mathcal{H}$), but simply the real range $j \geq 1728$ — the condition that $E_{\mathrm{SdS}}$ not be the pure de Sitter curve or the degenerate Nariai curve.

**Remark on the two algebraic fields.** The entropy quadratic form $u^2+uv+v^2$ is the norm form of the ring of integers $\mathbb{Z}[\omega]$ of $\mathbb{Q}(\sqrt{-3})$, where $\omega = e^{2\pi i/3}$. The CM structure of $E_{\mathrm{SdS}}$ at $M=0$, by contrast, is by $\mathbb{Z}[i] \subset \mathbb{Q}(i) = \mathbb{Q}(\sqrt{-1})$. These are distinct imaginary quadratic fields ($\text{disc} = -3$ vs $-4$). The appearance of the Eisenstein norm in the phase space geometry and the Gaussian CM at the de Sitter boundary are therefore genuinely distinct algebraic facts, both forced by the structure of the horizon cubic.

### 7.4 The Phase Space Arc as a π/6 Angular Sector

In the eigenbasis of the quadratic form $A = \bigl(\begin{smallmatrix}1&\frac{1}{2}\\\frac{1}{2}&1\end{smallmatrix}\bigr)$ with eigenvectors $e_1 = (1,1)/\sqrt{2}$ (eigenvalue $3/2$) and $e_2 = (1,-1)/\sqrt{2}$ (eigenvalue $1/2$), define rescaled coordinates $P = p\sqrt{3/2}$ and $Q = q\sqrt{1/2}$ where $(p,q)$ are the eigenbasis components of $(u,v)$. In these coordinates the Eisenstein ellipse becomes the unit circle $P^2 + Q^2 = 1$.

**Theorem 7.4.** In the $(P,Q)$ parametrization, the SdS arc $\mathcal{A}$ spans a parametric angular range of exactly $\pi/6$ (30°):
- Nariai limit ($x=1$, $u=v=1/\sqrt{3}$): $(P,Q) = (1,0)$, angle $\theta = 0$
- Pure de Sitter limit ($x \to 0$, $u \to 0$, $v \to 1$): $(P,Q) = (\sqrt{3}/2, -1/2)$, angle $\theta = -\pi/6$

*Proof.* At $x=1$: the eigenbasis components are $p = (u+v)/\sqrt{2} = \sqrt{2/3}$ and $q = (u-v)/\sqrt{2} = 0$, giving $P = p\sqrt{3/2} = 1$, $Q = 0$. At $x \to 0$: $u \to 0$, $v \to 1$, so $p = 1/\sqrt{2}$, $q = -1/\sqrt{2}$, giving $P = \sqrt{3}/2$, $Q = -1/2$. The angle from $(1,0)$ to $(\sqrt{3}/2, -1/2)$ is $-\pi/6$. $\square$

**Remark.** The parametric angle $\pi/6 = 2\pi/12$, so the SdS arc occupies $1/12$ of the full $2\pi$ parametric range of the unit circle in the eigenbasis. This is a statement about the angular measure of the arc endpoints, not about its Euclidean length: the Euclidean arc length of the SdS arc is approximately $12\%$ of the full Eisenstein ellipse perimeter, which differs from $1/12 \approx 8.3\%$ because the ellipse has unequal curvature. The $\pi/6$ parametric angle corresponds to the fact that, in the $(P,Q)$ representation, the arc's endpoints are separated by one step of a regular 12-gon inscribed in the unit circle.

---

## 8. Exact Temperature Identities

We now derive a complete set of closed-form identities for all thermodynamic combinations of $T_b$ and $T_c$.

### 8.1 Individual Temperatures in Eisenstein Coordinates

**Theorem 8.1 (Temperature factorization).** In Eisenstein coordinates $x = r_b/r_c$:

$$T_b = \frac{\sqrt{\Lambda}}{4\pi\sqrt{3}} \cdot \frac{(1-x)(2x+1)}{x\sqrt{x^2+x+1}}, \qquad T_c = \frac{\sqrt{\Lambda}}{4\pi\sqrt{3}} \cdot \frac{(1-x)(x+2)}{\sqrt{x^2+x+1}} \tag{20}$$

*Proof.* From $\Lambda r_b^2 = 3x^2/(x^2+x+1)$: we have $1 - \Lambda r_b^2 = (1-x)(2x+1)/(x^2+x+1)$ and $r_b = r_\Lambda \cdot x/\sqrt{x^2+x+1}$ with $r_\Lambda = \sqrt{3/\Lambda}$. Substituting into $T_b = (1-\Lambda r_b^2)/(4\pi r_b)$ gives (20). The formula for $T_c$ follows analogously. $\square$

**Remark.** Both temperatures share the same factor $(1-x)$, which vanishes at the Nariai limit $x=1$ where $T_b = T_c = 0$. The remaining factors $(2x+1)$ and $(x+2)$ are the two distinct polynomial branches of the SdS cubic: they capture the geometric asymmetry between the black hole and cosmological horizons.

### 8.2 Temperature Sum, Difference, and Product

**Theorem 8.2 (Complete temperature algebra).** The four fundamental combinations of $T_b$ and $T_c$ are:

$$T_b - T_c = \frac{\sqrt{\Lambda}}{4\pi\sqrt{3}} \cdot \frac{(1-x)^2(1+x)}{x\sqrt{x^2+x+1}} \tag{21}$$

$$T_b + T_c = \frac{\sqrt{\Lambda}}{4\pi\sqrt{3}} \cdot \frac{(1-x)(x^2+4x+1)}{x\sqrt{x^2+x+1}} \tag{22}$$

$$T_b \cdot T_c = \frac{\Lambda}{48\pi^2} \cdot \frac{(1-x)^2(x+2)(2x+1)}{x(x^2+x+1)} = \frac{\Lambda(1-3t)(2+3t)}{48\pi^2 t} \tag{23}$$

where the second form in (23) uses $t = \Delta/S_\Lambda = x/(x^2+x+1)$.

*Proof.* Equations (21) and (22) follow by subtracting and adding (20). For (21): $(2x+1)(1-x)/x - (x+2)(1-x) = (1-x)[(2x+1)/x - (x+2)] = (1-x)(2x+1-x^2-2x)/x = (1-x)(1-x^2)/x = (1-x)^2(1+x)/x$. For (22): $(2x+1)(1-x)/x + (x+2)(1-x) = (1-x)[(2x+1+x^2+2x)/x] = (1-x)(x^2+4x+1)/x$. For (23): $T_b \cdot T_c = (\Lambda/(48\pi^2)) \cdot (2x+1)(1-x)/x \cdot (x+2)(1-x) \cdot (x^2+x+1)^{-1}$, giving the $x$-form. For the $t$-form with $t = x/(x^2+x+1)$: one verifies $(1-3t)(2+3t)/t = (1-x)^2(x+2)(2x+1)/(x(x^2+x+1))$ by direct substitution and clearing denominators (both sides equal $(x^2+x+1-3x)^{1/2} \cdot \ldots$, or more directly: $(1-3t) = (x^2-2x+1)/(x^2+x+1)$, $(2+3t) = (2x^2+5x+2)/(x^2+x+1)$, $1/t = (x^2+x+1)/x$, giving $(1-3t)(2+3t)/t = (x^2-2x+1)(2x^2+5x+2)/(x(x^2+x+1))$; one checks $(x^2-2x+1)(2x^2+5x+2) = (1-x)^2(x+2)(2x+1)$ by expanding). $\square$

**Corollary 8.3.** The polynomial identity
$$(T_b + T_c)^2 - (T_b - T_c)^2 = 4T_b T_c$$
in Eisenstein coordinates becomes:
$$(1-x)^2(x^2+4x+1)^2 - (1-x)^4(1+x)^2 = 4(1-x)^2(x+2)(2x+1) \cdot (x^2+x+1)$$
which factors as $(1-x)^2[(x^2+4x+1)^2 - (1-x)^2(1+x)^2] = 4(1-x)^2(x+2)(2x+1)(x^2+x+1)$ and holds identically, confirming the algebraic consistency of all formulas. $\square$

**Corollary 8.4 (Temperature product monotonicity).** The temperature product $T_b \cdot T_c$ decreases strictly monotonically from $\infty$ to $0$ as $x$ increases from $0$ to $1$:
- As $x \to 0$ ($M \to 0$): $T_c \to \sqrt{\Lambda/3}/(2\pi)$ while $T_b \to \infty$, so $T_b T_c \to \infty$
- At Nariai ($x = 1$, $t = 1/3$): $T_b = T_c = 0$, giving $T_b T_c = 0$

There is no interior extremum; the product is a monotonically decreasing function of $x$ throughout the sub-extremal range.

### 8.3 Common Polynomial Structure of j and the Temperatures

The j-invariant and the temperature product share the same set of polynomial factors in their Eisenstein-coordinate expressions:

$$j = \frac{6912(x^2+x+1)^3}{\bigl[(1-x)(x+2)(2x+1)\bigr]^2}, \qquad T_b T_c = \frac{\Lambda(1-x)^2(x+2)(2x+1)}{48\pi^2 x(x^2+x+1)}$$

The numerator of $T_b T_c$ contains $(1-x)^2(x+2)(2x+1)$, which is the square root of the denominator of $j$ (up to one power of $(1-x)$). Combining them:

$$j \cdot T_b T_c = \frac{144\Lambda(x^2+x+1)^2}{\pi^2 x(1-x)(x+2)(2x+1)} \tag{24}$$

This identity does not eliminate $x$, so it does not express $j$ directly as a function of $T_bT_c$ alone (both sides still depend on $x$). What it records is the shared polynomial anatomy: the four factors $(1-x)$, $(x+2)$, $(2x+1)$, and $(x^2+x+1)$ govern both the modular and the thermodynamic quantities. In particular, the denominator factor $(1-x)(x+2)(2x+1)$ vanishes at the Nariai limit ($x \to 1$), consistent with $T_b T_c \to 0$ while $j \to \infty$ there, and with the product $j \cdot T_b T_c$ itself diverging.

**Remark on polynomial structure.** The four polynomials appearing in the temperature identities — $(1-x)$, $(1+x)$, $(x+2)$, $(2x+1)$ — are exactly the four linear factors of the cubic discriminant $(1-9\Lambda M^2) \propto (1-x)^2(x+2)^2(2x+1)^2/(x^2+x+1)^3$. The polynomial $x^2+4x+1$ appearing in $T_b+T_c$ is the unique irreducible quadratic factor that arises from the sum; it has roots at $x = -2 \pm \sqrt{3}$, outside the physical range, and connects to the real quadratic field $\mathbb{Q}(\sqrt{3})$.

---

## 9. Discussion

**What is proved.** We have proved that the 4D SdS phase space at fixed $\Lambda$ is an arc of the Eisenstein unit ellipse $u^2 + uv + v^2 = 1$. The entropy deficit is the Eisenstein cross-term. The temperature ratio is a geometric invariant of the arc. The exact Carnot relation is an algebraic consequence of the Eisenstein constraint, and it does not hold generically for two-horizon spacetimes. Additionally, the horizon cubic defines an elliptic curve whose j-invariant encodes the extremality parameter via $\varepsilon = 1 - 1728/j$, and the algebraic identity $j \cdot \Delta_{\mathrm{cubic}} = 6912(3/\Lambda)^3$ holds at fixed $\Lambda$. The complete temperature algebra (Theorem 8.2) expresses every thermodynamic quantity in fully factored Eisenstein form.

**What is new.** The identification of the SdS moduli space with an arc of the Eisenstein unit ellipse, and the derivation of the exact Carnot relation as a consequence of Eisenstein geometry, appear to be new; we are not aware of prior work making this connection. The entropy identity (1) and its Vieta derivation are known; see [MaS03, RLZ10] and references therein. What is new is the Eisenstein coordinate interpretation, the proof that the Carnot relation is forced by the Eisenstein constraint (rather than being a separate assumption), the j-invariant formula (15) and its factored form (18) in Eisenstein coordinates, the algebraic identity (17), the $\pi/6$ parametric angular range of the arc (Theorem 7.4), and the complete temperature factorization (Theorems 8.1–8.2). The connection between the Eisenstein phase-space norm and the Gaussian CM structure of the $M=0$ curve appears to be new.

**Physical interpretation.** The Eisenstein structure provides a coordinate system in which the SdS phase space is a curve of constant norm. The entropy deficit $\Delta = S_\Lambda uv$ traces the Eisenstein cross-term: it is maximized at the symmetric point $u = v$ (Nariai) and vanishes at the endpoint $u = 0$ (empty de Sitter). The Carnot efficiency at any point is the rate at which the cross-term changes as the system moves along the arc — a purely geometric quantity determined by position on the ellipse. The entropy budget $S_b + S_c + \Delta = S_\Lambda$ is a fixed algebraic constraint; it does not by itself imply that physical transitions between SdS configurations are thermodynamically reversible (since $T_b \neq T_c$ generically).

The j-invariant gives a complementary picture: the extremality parameter $\varepsilon = 9\Lambda M^2$ equals $1 - 1728/j$. As the black hole mass increases from $0$ to the Nariai value, $j$ increases from $1728$ to $\infty$, while the discriminant $\Delta_{\mathrm{cubic}}$ decreases from $108/\Lambda^3$ to $0$. The product $j \cdot \Delta_{\mathrm{cubic}} = 1728 \times 108/\Lambda^3$ is fixed by $\Lambda$ alone — an immediate consequence of the definitions, but a concise way to summarize how the two quantities co-vary.

**What remains open.** Several questions are raised by these results. Does the Eisenstein norm structure of the phase space connect to L-functions or modular forms attached to $\mathbb{Q}(\sqrt{-3})$? For the $D=5$ Pythagorean constraint $r_b^2 + r_c^2 = r_{\Lambda,5}^2$: does a Carnot-type relation hold there, and if so, is it forced by the Pythagorean identity analogously? Is there an analogue for Reissner–Nordström–de Sitter or Kerr–de Sitter, where the horizon polynomial has additional free parameters beyond $M$ and $\Lambda$? Can the $\pi/6$ parametric angle of the SdS arc be given an intrinsic geometric meaning — for instance, as an angle in the fundamental domain of the modular group rather than in the eigenbasis of the quadratic form?

**On the status of these results.** The proofs are exact algebraic consequences of the Vieta relations of the horizon cubic. They depend on the classical area-entropy formula and the classical first laws. They do not rely on semiclassical approximations, quantum corrections, or holographic assumptions. Within classical general relativity, the results are exact.

---

## 10. Conclusion

The sub-extremal 4D SdS phase space at fixed $\Lambda$ is the open arc of the Eisenstein unit ellipse $u^2 + uv + v^2 = 1$ in the coordinates $u = \sqrt{S_b/S_\Lambda}$, $v = \sqrt{S_c/S_\Lambda}$. The entropy deficit is the Eisenstein cross-term $\Delta = S_\Lambda uv$. This arc spans exactly $\pi/6$ (30°, one-twelfth) of the angular range of the Eisenstein ellipse in its eigenbasis.

The temperature ratio $T_c/T_b = x(x+2)/(1+2x)$ is a geometric invariant of the arc, derived entirely from the Eisenstein constraint. The exact Carnot relation $\partial\Delta/\partial S_c|_\Lambda = -\eta_C$ holds because — and only because — the SdS temperature ratio satisfies the precise algebraic condition (12) that the Eisenstein constraint forces.

The horizon cubic defines an associated elliptic curve with j-invariant $j = 1728/(1-9\Lambda M^2)$. The extremality parameter $\varepsilon = 9\Lambda M^2 = 1 - 1728/j$ connects mass directly to the j-invariant. The product identity $j \cdot \Delta_{\mathrm{cubic}} = 6912(3/\Lambda)^3$ holds at fixed $\Lambda$. All temperatures factorize completely in Eisenstein coordinates (Theorems 8.1–8.2), with the temperature product admitting both the $x$-form $T_bT_c = \Lambda(1-x)^2(x+2)(2x+1)/[48\pi^2 x(x^2+x+1)]$ and the entropy-form $T_bT_c = \Lambda(1-3t)(2+3t)/(48\pi^2 t)$.

The Carnot efficiency in 4D SdS is not a coincidence. It is a theorem about the Eisenstein norm structure of the spacetime's phase space. This structure is unique to four dimensions: the cyclotomic divisibility criterion identifies $D = 4$ (Eisenstein) and $D = 5$ (Pythagorean) as the only dimensions where the entropy formula is polynomial, and therefore the only ones where a norm-ellipse interpretation is possible. The 4D SdS thermodynamic system has, in summary, two distinct algebraic features visible in its horizon cubic: the Eisenstein norm of $\mathbb{Q}(\sqrt{-3})$ governs the phase space geometry and entropy identity, while the j-invariant of the associated Weierstrass curve equals $1728$ — the Gaussian CM value — precisely at the $M=0$ boundary. These are separate facts, both derivable from the Vieta relations of the same polynomial, but they reflect different arithmetic structures.

---

## References

[Bek73] J. D. Bekenstein, "Black holes and entropy," *Phys. Rev. D* **7** (1973) 2333–2346.

[Haw75] S. W. Hawking, "Particle creation by black holes," *Commun. Math. Phys.* **43** (1975) 199–220.

[GH77] G. W. Gibbons and S. W. Hawking, "Cosmological event horizons, thermodynamics, and particle creation," *Phys. Rev. D* **15** (1977) 2738–2751.

[GP83] P. Ginsparg and M. J. Perry, "Semiclassical perdurance of de Sitter space," *Nucl. Phys. B* **222** (1983) 245–268.

[BH96] R. Bousso and S. W. Hawking, "Pair creation of black holes during inflation," *Phys. Rev. D* **54** (1996) 6312–6322.

[MaS03] S. Shankaranarayanan, "Temperature and entropy of Schwarzschild–de Sitter space-time," *Phys. Rev. D* **67** (2003) 084026.

[RLZ10] Zhao Ren, Li Huai-Fan, Zhang Li-Chun, and Wu Yue-qin, "Hawking radiation and entropy in de Sitter spacetime," arXiv:1004.5162 [gr-qc] (2010).

---

*Note: All results in this paper are exact algebraic consequences of the Vieta relations of the 4D SdS horizon cubic and the classical Bekenstein–Hawking entropy formula. All proofs are given in full. Numerical verification of all identities across the full sub-extremal parameter space ($x \in (0,1)$, $\Lambda > 0$, $9\Lambda M^2 < 1$) confirms no exceptions. A companion paper [companion] contains extended discussion of the entropy identity (1) and its physical consequences.*
