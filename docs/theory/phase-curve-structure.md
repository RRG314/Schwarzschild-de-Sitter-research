# Exact Phase-Curve Structure on the 4D Fixed-Lambda Family

Let `x = r_b / r_c` with `x in (0,1)`.

The normalized exact quantities are

$$
\varepsilon_b = \frac{x^2}{1+x+x^2},
\qquad
\varepsilon_c = \frac{1}{1+x+x^2},
\qquad
\delta = \frac{\Delta}{S_\Lambda} = \frac{x}{1+x+x^2},
$$

$$
\rho = \frac{T_c}{T_b} = \frac{x(x+2)}{1+2x},
\qquad
\eta_C = 1-\rho = \frac{1-x^2}{1+2x}.
$$

## Exact monotonicity

Direct differentiation gives

$$
\delta'(x) = \frac{1-x^2}{(1+x+x^2)^2} > 0,
$$

$$
\eta_C'(x) = -\frac{2(x^2+x+1)}{(1+2x)^2} < 0.
$$

So along the fixed-`Lambda` phase family:
- deficit fraction grows strictly with `x`
- Carnot efficiency falls strictly with `x`

This means either quantity is an exact one-parameter order coordinate on the admissible family.

## Algebraic relation between deficit and efficiency

Eliminating `x` yields the exact polynomial relation

$$
3\delta^2\eta_C^2 - 3\delta^2\eta_C + 3\delta^2 + 2\delta\eta_C^2 - 2\delta\eta_C + 2\delta + \eta_C - 1 = 0.
$$

This is kept as an exact phase-curve identity inside the repo.

## Honest status

The formulas are exact.
The question of whether this packaging is literature-distinct remains open and must not be overstated.
