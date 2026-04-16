# Dimensional Isolation Asymptotics for `D>=6`

## Main statement kept in the repo

For every tested dimension `D>=6`, the tempting candidate

$$
r_b^2 + r_c^2 = l^2
$$

fails already in the small-`\mu` regime, and it fails in a one-sided way:

$$
r_b^2 + r_c^2 > l^2
$$

for sufficiently small positive mass parameter `\mu`.

## Why

The horizon polynomial is

$$
r^{D-1} - l^2 r^{D-3} + \mu l^2 = 0.
$$

For `D>=6` and small `\mu>0`:

- the black-hole root satisfies
  $$
  r_b^2 \sim \mu^{2/(D-3)},
  $$
- the cosmological root satisfies
  $$
  r_c^2 \sim l^2 - \mu / l^{D-5}.
  $$

So

$$
r_b^2 + r_c^2
\sim
l^2 + \mu^{2/(D-3)} - \mu / l^{D-5}.
$$

Because

$$
\frac{2}{D-3} < 1 \qquad (D>=6),
$$

the positive term `\mu^{2/(D-3)}` dominates the linear correction as `\mu \to 0^+`.

## What this proves and what it does not

Kept:
- a clean asymptotic dimensional-isolation reason why the simple 5D two-root closure mechanism cannot persist for `D>=6`
- a positive-gap small-`\mu` regime for the candidate sum on the tested higher-dimensional families

Not yet claimed:
- a complete classification of every possible higher-dimensional closure quantity
- a global theorem for all `\mu` without further work
