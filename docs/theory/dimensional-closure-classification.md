# Dimensional Closure Classification

## Exact low-dimensional closures

### D = 4
The exact 4D identity is

$$
S_\Lambda = S_b + S_c + \sqrt{S_b S_c}.
$$

### D = 5
The 5D horizon equation is quadratic in `u=r^2`, producing the exact closure

$$
r_b^2 + r_c^2 = l_5^2,
$$

which translates into the Pythagorean entropy relation in `S^{2/3}`.

## What survives beyond D = 5

The repo currently keeps a strong but careful statement:
- D=4 and D=5 have exact low-degree closure structure
- D>=6 currently has explicit nonclosure witnesses for tempting two-root candidate quantities at fixed `Lambda`

What is **not** yet claimed:
- a full theorem that no exact irrational or nonpolynomial two-root closure can ever exist in every higher dimension

## Why this matters

The D=4 and D=5 cases look similar at first glance, but they come from different algebraic coincidences. Treating them as the start of a universal dimensional sequence is not currently justified.

## Small-`mu` dimensional isolation lane for `D>=6`

The repo now keeps a sharper asymptotic reason for the higher-dimensional failure of the tempting candidate

$$
r_b^2 + r_c^2 = \text{constant depending only on } \Lambda.
$$

For `D>=6` and small positive mass parameter `mu`, the horizon polynomial gives:

- a small black-hole root with
  $$
  r_b^2 \sim \mu^{2/(D-3)},
  $$
- a cosmological root with
  $$
  r_c^2 \sim l^2 - \mu / l^{D-5}.
  $$

So

$$
r_b^2 + r_c^2
\sim
l^2 + \mu^{2/(D-3)} - \mu / l^{D-5},
$$

which varies with `mu` for every `D>=6`.

This does not yet classify every imaginable higher-dimensional closure quantity, but it does give a clean asymptotic explanation for why the simple 5D quadratic closure mechanism does not persist.

See also [Dimensional Isolation Asymptotics](dimensional-isolation-asymptotics.md).
