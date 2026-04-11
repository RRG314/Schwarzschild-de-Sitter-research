# Exact Derivations

**Project:** Spectral Horizon Research
**Date:** April 2026
**Purpose:** Complete step-by-step proofs for all statements classified as PROVED in `04a_statement_pipeline.md`. No approximations are used in this document except where explicitly noted.

---

## Derivation 1 — Eisenstein Constraint

**Theorem 1 (Eisenstein constraint):** In any sub-extremal SdS spacetime with M > 0 and Λ > 0, the two positive roots r_b < r_c of f(r) = 1 − 2M/r − Λr²/3 satisfy:

```
r_b² + r_b r_c + r_c² = 3/Λ
```

**Proof:**

Multiply f(r) through by r to clear the denominator:

```
r · f(r) = r − 2M − Λr³/3
```

Set this equal to zero to get a cubic whose roots are {r_b, r_c} and a third root r_- < 0. Write the cubic in standard form:

```
(Λ/3) r³ − r + 2M = 0

⟺ r³ − (3/Λ) r + 6M/Λ = 0
```

By Vieta's formulas for the monic cubic with roots r_b, r_c, r_-:

```
r_b + r_c + r_- = 0                    [coefficient of r²; it is zero here]

r_b r_c + r_b r_- + r_c r_- = −3/Λ    [coefficient of r]

r_b r_c r_- = −6M/Λ                   [constant term, negated]
```

From the first equation, r_- = −(r_b + r_c).

Substituting into the second equation:

```
r_b r_c + (r_b + r_c) r_- = −3/Λ

r_b r_c − (r_b + r_c)² = −3/Λ

r_b r_c − r_b² − 2r_b r_c − r_c² = −3/Λ

−(r_b² + r_b r_c + r_c²) = −3/Λ

r_b² + r_b r_c + r_c² = 3/Λ
```

This completes the proof. ∎

**Note:** This is an exact algebraic identity. It holds for all (M, Λ) in the sub-extremal range, with no approximation.

---

## Derivation 2 — Entropy Identity

**Corollary 1 (Entropy identity):**

```
S_Λ = S_b + S_c + sqrt(S_b S_c)

where S_b = π r_b², S_c = π r_c², S_Λ = 3π/Λ = π r_Λ²
```

**Proof:**

From Theorem 1:

```
r_b² + r_b r_c + r_c² = 3/Λ = r_Λ²
```

Multiply both sides by π:

```
π r_b² + π r_b r_c + π r_c² = π r_Λ²

S_b + π r_b r_c + S_c = S_Λ
```

Now observe: sqrt(S_b S_c) = sqrt(π r_b² · π r_c²) = π r_b r_c (taking positive square root since r_b, r_c > 0). Therefore:

```
S_b + S_c + sqrt(S_b S_c) = S_b + S_c + π r_b r_c = S_Λ
```

∎

**Note:** This identity is a direct restatement of the Eisenstein constraint in terms of entropies. It was noted in prior work by this group.

---

## Derivation 3 — Parametrization by x

**Theorem 3 (Parametrization):** Define x = r_b/r_c ∈ (0,1) and r_Λ = sqrt(3/Λ). Then:

```
r_c(x, Λ) = r_Λ / sqrt(x² + x + 1)

r_b(x, Λ) = x r_Λ / sqrt(x² + x + 1)

M(x, Λ) = r_Λ · x(1+x) / (2(x²+x+1)^{3/2})
```

**Proof of r_c formula:**

Substituting r_b = x r_c into the Eisenstein constraint:

```
(xr_c)² + (xr_c)r_c + r_c² = r_Λ²

r_c² (x² + x + 1) = r_Λ²

r_c = r_Λ / sqrt(x²+x+1)
```

Then r_b = xr_c = xr_Λ/sqrt(x²+x+1). ∎

**Proof of M formula:**

From Vieta's formulas, r_b r_c r_- = −6M/Λ and r_- = −(r_b+r_c):

```
r_b r_c (r_b + r_c) = 6M/Λ

M = r_b r_c (r_b + r_c) / (6/Λ) = r_b r_c (r_b+r_c) Λ / 6
```

But also, from the Eisenstein constraint, 3/Λ = r_b²+r_br_c+r_c², so Λ = 3/(r_b²+r_br_c+r_c²):

```
M = r_b r_c (r_b+r_c) · 3 / (6(r_b²+r_br_c+r_c²))
  = r_b r_c (r_b+r_c) / (2(r_b²+r_br_c+r_c²))
```

In terms of x and r_c:

```
r_b r_c = x r_c²
r_b + r_c = (1+x) r_c
r_b² + r_b r_c + r_c² = r_c² (x²+x+1)

M = x r_c² · (1+x) r_c / (2 r_c² (x²+x+1))
  = x(1+x) r_c / (2(x²+x+1))
  = x(1+x) · [r_Λ/sqrt(x²+x+1)] / (2(x²+x+1))
  = r_Λ x(1+x) / (2(x²+x+1)^{3/2})
```

∎

---

## Derivation 4 — Hawking Temperatures

**Theorem 4 (Hawking temperatures):**

```
T_b = (1+2x)(1−x) / (4π x r_Λ sqrt(x²+x+1))

T_c = (2+x)(1−x) / (4π r_Λ sqrt(x²+x+1))
```

Equivalently:

```
T_b = (1 − Λr_b²) / (4π r_b)

T_c = (Λr_c² − 1) / (4π r_c)
```

**Proof of T_b in x-form:**

The Hawking temperature is T_b = |f'(r_b)|/(4π) where f'(r) = 2M/r² − 2Λr/3.

From Derivation 3:

```
M = r_Λ x(1+x) / (2(x²+x+1)^{3/2})

r_b = x r_Λ / sqrt(x²+x+1)

r_b² = x² r_Λ² / (x²+x+1)

Λ = 3/r_Λ²
```

Computing each term:

```
2M/r_b² = 2 · [r_Λ x(1+x) / (2(x²+x+1)^{3/2})] / [x²r_Λ²/(x²+x+1)]
         = [r_Λ x(1+x) / (x²+x+1)^{3/2}] · [(x²+x+1)/(x²r_Λ²)]
         = (1+x) / (x r_Λ sqrt(x²+x+1))

2Λr_b/3 = 2 · (3/r_Λ²) · [x r_Λ/sqrt(x²+x+1)] / 3
         = 2x / (r_Λ sqrt(x²+x+1))
```

Therefore:

```
f'(r_b) = 2M/r_b² − 2Λr_b/3
         = (1+x)/(x r_Λ sqrt(x²+x+1)) − 2x/(r_Λ sqrt(x²+x+1))
         = [(1+x)/x − 2x] / (r_Λ sqrt(x²+x+1))
         = [(1+x − 2x²)/x] / (r_Λ sqrt(x²+x+1))
         = (1+2x)(1−x) / (x r_Λ sqrt(x²+x+1))
```

Since this is positive for x ∈ (0,1), we have T_b = f'(r_b)/(4π). ∎

**Proof of T_b in compact form:**

We show 1 − Λr_b² = (1+2x)(1−x)/(x²+x+1):

```
Λr_b² = (3/r_Λ²) · (x²r_Λ²/(x²+x+1)) = 3x²/(x²+x+1)

1 − Λr_b² = (x²+x+1 − 3x²)/(x²+x+1) = (1 + x − 2x²)/(x²+x+1) = (1+2x)(1−x)/(x²+x+1)
```

And 4πr_b = 4π · xr_Λ/sqrt(x²+x+1).

Therefore:

```
(1−Λr_b²)/(4πr_b) = [(1+2x)(1−x)/(x²+x+1)] / [4πxr_Λ/sqrt(x²+x+1)]
                   = (1+2x)(1−x) / (4π x r_Λ sqrt(x²+x+1))
```

which matches the x-form. ∎

**Proof of T_c formula:**

By the same method with f'(r_c):

```
2M/r_c² = [r_Λ x(1+x)/(2(x²+x+1)^{3/2})] / [r_Λ²/(x²+x+1)]
         = x(1+x) / (r_Λ sqrt(x²+x+1)) · (1/2) · 2
         = x(1+x) / (r_Λ sqrt(x²+x+1))

2Λr_c/3 = 2 · (3/r_Λ²) · [r_Λ/sqrt(x²+x+1)] / 3
         = 2 / (r_Λ sqrt(x²+x+1))
```

Therefore:

```
f'(r_c) = x(1+x)/(r_Λ sqrt(x²+x+1)) − 2/(r_Λ sqrt(x²+x+1))
         = (x+x²−2) / (r_Λ sqrt(x²+x+1))
         = −(2−x−x²) / (r_Λ sqrt(x²+x+1))
         = −(2+x)(1−x) / (r_Λ sqrt(x²+x+1))
```

Since f'(r_c) < 0 (f is decreasing through the cosmological horizon), T_c = |f'(r_c)|/(4π):

```
T_c = (2+x)(1−x) / (4π r_Λ sqrt(x²+x+1))
```

**Compact form:** Λr_c² − 1 = 3/(x²+x+1) − 1 = (2−x²−x)/(x²+x+1) = (2+x)(1−x)/(x²+x+1), and 4πr_c = 4πr_Λ/sqrt(x²+x+1), giving:

```
T_c = [(2+x)(1−x)/(x²+x+1)] / [4πr_Λ/sqrt(x²+x+1)]
    = (2+x)(1−x) / (4π r_Λ sqrt(x²+x+1))
```

which matches. Also (Λr_c²−1)/(4πr_c) = same. ∎

**Note:** T_b > T_c requires showing f'(r_b) > f'(r_c) in absolute value:

```
T_b/T_c = [(1+2x)(1−x)/(xr_Λ)] / [(2+x)(1−x)/r_Λ]
         = (1+2x) / (x(2+x))
```

This is > 1 iff 1+2x > x(2+x) = 2x + x², iff 1 > x², which holds for x ∈ (0,1). So T_b > T_c throughout the sub-extremal range. ∎

---

## Derivation 5 — Carnot Efficiency

**Theorem 5 (Carnot efficiency, exact closed form):**

```
η_C(x) = (T_b − T_c)/T_b = (1−x²)/(1+2x)
```

**Proof:**

From Derivation 4:

```
T_c/T_b = [(2+x)(1−x)/(4πr_Λ sqrt(x²+x+1))] / [(1+2x)(1−x)/(4πxr_Λ sqrt(x²+x+1))]
         = x(2+x) / (1+2x)
```

Therefore:

```
η_C = 1 − T_c/T_b = 1 − x(2+x)/(1+2x)
    = (1+2x − x(2+x)) / (1+2x)
    = (1+2x − 2x−x²) / (1+2x)
    = (1−x²) / (1+2x)
    = (1−x)(1+x) / (1+2x)
```

∎

**Properties:**

```
η_C(0) = 1       [pure de Sitter limit; T_c → 0]
η_C(1) = 0       [Nariai limit; T_b = T_c]

η_C'(x) = d/dx [(1−x²)/(1+2x)]
         = [−2x(1+2x) − 2(1−x²)] / (1+2x)²
         = [−2x − 4x² − 2 + 2x²] / (1+2x)²
         = [−2 − 2x − 2x²] / (1+2x)²
         = −2(1+x+x²) / (1+2x)²
```

Since 1+x+x² > 0 for all real x, η_C'(x) < 0 for all x ∈ (0,1): η_C is strictly decreasing. ∎

---

## Derivation 6 — Lambda-Scaling Law (Exact)

**Theorem 6 (Lambda-scaling law):** The exact QNM frequencies of the SdS massless scalar field satisfy ω = sqrt(Λ) · F(x,l,n) for some dimensionless F independent of Λ.

**Proof:**

The scalar field equation □Φ = 0 in static SdS coordinates with the decomposition Φ = Y_{lm}(θ,φ)ψ(t,r)/r reduces to:

```
∂²ψ/∂t² − ∂²ψ/∂r*² + V(r)ψ = 0

V(r) = f(r)[l(l+1)/r² + f'(r)/r]

dr* = dr/f(r)
```

**Step 1: Show V scales as Λ at fixed x.**

Express r in units of r_c: write r = r_c ρ where r_c = r_Λ/sqrt(x²+x+1) and r_Λ = sqrt(3/Λ).

Then r_c ∝ 1/sqrt(Λ), so for fixed ρ and x:

```
2M/r = 2M/(r_c ρ) ∝ [r_Λ · x(1+x)/(x²+x+1)^{3/2}] / [r_Λ ρ/sqrt(x²+x+1)]
      = x(1+x) / [ρ (x²+x+1)]     [Λ-independent!]

Λr²/3 = Λ r_c² ρ² / 3 = (Λ · 3/Λ · ρ²) / ((x²+x+1) · 3)
       = ρ² / (x²+x+1)             [Λ-independent!]
```

Therefore f(r_c ρ) = 1 − M·correction − Λr²/3·correction is a function of ρ and x only:

```
f(r_c ρ) ≡ g(ρ, x)     [Λ-independent]
```

The potential becomes:

```
V(r_c ρ) = f(r_c ρ) [l(l+1)/(r_c ρ)² + f'(r_c ρ)/(r_c ρ)]
```

Now f'(r) = df/dr = (1/r_c) df/dρ, so f'(r_c ρ) = (1/r_c) g'(ρ,x). Thus:

```
V(r_c ρ) = g(ρ,x) · [l(l+1)/r_c² ρ² + g'(ρ,x)/(r_c² ρ)]
           = (1/r_c²) · g(ρ,x) [l(l+1)/ρ² + g'(ρ,x)/ρ]
           = (Λ(x²+x+1)/3) · Ṽ(ρ, x, l)
           = Λ · V̂(ρ, x, l)
```

where V̂ = (x²+x+1)/3 · g(ρ,x)[l(l+1)/ρ² + g'(ρ,x)/ρ] is Λ-independent.

**Step 2: Rescale time.**

Define τ = t sqrt(Λ). Then ∂/∂t = sqrt(Λ) · ∂/∂τ, so ∂²ψ/∂t² = Λ · ∂²ψ/∂τ².

**Step 3: Rescale the tortoise coordinate.**

dr* = dr/f(r) = r_c dρ / g(ρ,x). Define the dimensionless tortoise coordinate:

```
ρ* = r* / r_c = ∫ dρ/g(ρ,x)
```

This is Λ-independent (g is Λ-independent).

**Step 4: Rewrite the wave equation.**

In coordinates (τ, ρ*):

```
∂²ψ/∂t² = Λ ∂²ψ/∂τ²

∂²ψ/∂r*² = (1/r_c²) ∂²ψ/∂ρ*²
```

The wave equation Λ ∂²ψ/∂τ² − (1/r_c²) ∂²ψ/∂ρ*² + Λ V̂ ψ = 0 becomes (after dividing by Λ = 3/r_Λ² and noting r_c² = r_Λ²/(x²+x+1)):

Dividing through by Λ:

```
∂²ψ/∂τ² − (1/Λr_c²) ∂²ψ/∂ρ*² + V̂ ψ = 0
```

But Λr_c² = Λ · r_Λ²/(x²+x+1) = 3/(x²+x+1) — a Λ-independent constant! Therefore:

```
∂²ψ/∂τ² − [(x²+x+1)/3] ∂²ψ/∂ρ*² + V̂(ρ*, x, l) ψ = 0
```

This equation has no explicit Λ-dependence.

**Step 5: QNM eigenvalue condition.**

With the QNM ansatz ψ(τ, ρ*) = e^{−iΩτ} u(ρ*), the equation becomes:

```
−Ω² u − [(x²+x+1)/3] u'' + V̂(ρ*, x, l) u = 0
```

The QNM boundary conditions (ingoing at r_b, outgoing at r_c in the tortoise coordinate) are also Λ-independent in (τ, ρ*) coordinates.

Therefore the eigenvalue Ω = ω/sqrt(Λ) satisfies an equation that depends only on x and l. Its eigenvalues (labeled by n) are functions of x, l, n only:

```
ω/sqrt(Λ) = F(x, l, n)
```

∎

**Remark:** This proof holds for the exact QNM eigenvalues, not just the WKB approximation. It is a theorem in mathematical physics, not a numerical observation.

---

## Derivation 7 — Q is Lambda-independent (Corollary)

**Corollary 2:** Q = Re(ω)/|Im(ω)| is a function of x, l, n only.

**Proof:** From Theorem 6, ω = sqrt(Λ) · F(x,l,n). Since F is complex-valued:

```
Re(ω) = sqrt(Λ) · Re(F(x,l,n))
Im(ω) = sqrt(Λ) · Im(F(x,l,n))

Q = Re(ω)/|Im(ω)| = Re(F(x,l,n))/|Im(F(x,l,n))|
```

This depends only on x, l, n. ∎

---

## Derivation 8 — Tortoise-Coordinate WKB Derivatives

**Lemma (tortoise derivatives at a potential maximum):** Let V(r) be the SdS effective potential, with r* the tortoise coordinate (dr* = dr/f(r)). At a maximum r_max where dV/dr = 0:

```
d²V/dr*²|_{r_max} = f(r_max)² · d²V/dr²|_{r_max}
```

**Proof:**

The chain rule gives:

```
dV/dr* = (dr/dr*) · dV/dr = f(r) · dV/dr
```

Differentiating again:

```
d²V/dr*² = (dr/dr*) · d/dr [f(r) dV/dr]
           = f(r) · [f'(r) dV/dr + f(r) d²V/dr²]
           = f(r)² d²V/dr² + f(r) f'(r) dV/dr
```

At the maximum where dV/dr = 0, the second term vanishes:

```
d²V/dr*²|_{r_max} = f(r_max)² · d²V/dr²|_{r_max}
```

∎

**Significance:** Since f(r_max) is small in the SdS static region (it must vanish at both horizons, so its maximum in the interior is also relatively small), failing to include this factor leads to a systematic overestimate of |V₀''_{r*}| by a factor 1/f(r_max)², ranging from approximately 11 at x=0.1 to over 100,000 at x=0.9 (for l=2). This was the source of the Q-Carnot artifact.

**Corollary:** The WKB-1 quality factor, with correct tortoise derivatives, is:

```
Q_WKB1 = Re(sqrt(V₀ − i(n+½) f(r_max) sqrt(−V₀''_r/2)))
         / |Im(sqrt(V₀ − i(n+½) f(r_max) sqrt(−V₀''_r/2)))|
```

where V₀''_r = d²V/dr²|_{r_max} (the second derivative in physical r coordinate, as computed by finite differences).

---

## Derivation 9 — Analytic Formula for f(r_max)

For completeness, we give an analytic upper bound on f(r_max). Since f(r) is positive in the static region with f(r_b) = f(r_c) = 0, the maximum of f in (r_b, r_c) satisfies f_max ≤ max f.

At the point where f'(r) = 0: 2M/r² = 2Λr/3, so r³ = 3M/Λ.

This is the "photon sphere" radius (for large l, the potential maximum r_max approaches this). For the SdS photon sphere:

```
r_ps = (3M/Λ)^{1/3} = r_Λ · (x(1+x)/(2(x²+x+1)^{3/2}))^{1/3} · (r_Λ/Λ)^...
```

More explicitly: using M/Λ = [r_Λ x(1+x)/(2(x²+x+1)^{3/2})] · (r_Λ²/3):

```
r_ps = r_Λ · [x(1+x)/(2(x²+x+1)^{3/2})]^{1/3}
```

Note r_ps ∝ r_Λ ∝ 1/sqrt(Λ), consistent with the scaling law.

The value f(r_ps) = 1 − 2M/r_ps − Λr_ps²/3 can be computed in terms of x. This approaches 0 as x → 1 (Nariai limit, where the two horizons merge and r_max → r_b = r_c → r_ps).

For the WKB approximation at finite l, r_max is close to but not exactly equal to r_ps. For l=2, the WKB maximum is somewhat shifted from the photon sphere. The f(r_max) values computed numerically (from 0.003 at x=0.9 to 0.303 at x=0.1) reflect this.

---

## Summary of Proved Results

| Result | Statement | Proof |
|---|---|---|
| Eisenstein constraint | r_b²+r_br_c+r_c² = 3/Λ | Derivation 1 (Vieta's formulas) |
| Entropy identity | S_Λ = S_b + S_c + sqrt(S_bS_c) | Derivation 2 (from Eisenstein) |
| Horizon parametrization | r_c, r_b, M as functions of x, Λ | Derivation 3 |
| Hawking temperatures | T_b, T_c exact formulas in x | Derivation 4 |
| Carnot efficiency | η_C(x) = (1−x²)/(1+2x) | Derivation 5 |
| Lambda-scaling law | ω = sqrt(Λ)·F(x,l,n) | Derivation 6 |
| Q is Λ-independent | Q = Q(x,l,n) | Derivation 7 (corollary) |
| Tortoise coordinate correction | V₀''_{r*} = f²·V₀''_r at maximum | Derivation 8 |
