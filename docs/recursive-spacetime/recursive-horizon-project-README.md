# Recursive Horizon Research Workspace

Falsification-first prototype testing whether recursive maps on the
Schwarzschild–de Sitter Eisenstein arc produce emergent non-integer
spectral dimension.

## Physical Setup

Schwarzschild–de Sitter spacetime (BH + cosmological constant) has two
physical horizons: r_b (black hole) and r_c (cosmological). Their radii
satisfy the exact Eisenstein constraint:

    r_b² + r_b·r_c + r_c² = 3/Λ

Rescaling to unit Eisenstein coordinates u = r_b/√(3/Λ), v = r_c/√(3/Λ):

    u² + u·v + v² = 1   (unit Eisenstein ellipse)

The physical phase space is the arc 0 < x = u/v < 1, parameterized by
x = r_b/r_c ∈ (0,1).

## Quick Start

```bash
# Install dependencies
pip install numpy scipy --break-system-packages

# Run unit tests
python tests/test_state_space.py

# Run a single experiment
python experiments/exp01_symmetric_fixed_points.py

# Run all experiments
python experiments/run_all.py
```

## Project Structure

```
src/
  state_space.py        Eisenstein coordinates, temperatures, observables
  recursion_models.py   Three map families (symmetric, coupled, asymmetric)
  observables.py        Physical observables along orbits
  depth_weights.py      RDT (Recursive Depth Transform) weighting
  graph_spectral.py     Graph Laplacian, spectral dimension estimation
  stability_analysis.py Jacobians, Lyapunov exponents, bifurcation scan
  utils.py              I/O, timing, JSON serialization

experiments/
  exp01_symmetric_fixed_points.py   Symmetric map dynamics
  exp02_coupled_orbits.py           Coupled map interior fixed points
  exp03_parameter_sweep.py          Robustness and basin analysis
  exp04_spectral_dimension.py       Spectral dimension (main test)
  exp05_rdt_weighting.py            RDT weighting and conservation
  run_all.py                        Run all experiments

tests/
  test_state_space.py   11 unit tests (all pass)

outputs/
  exp01_symmetric_fixed_points.json
  exp02_coupled_orbits.json
  exp02_detail_orbit.csv
  exp03_parameter_sweep.json
  exp04_spectral_dimension.json
  exp05_rdt_weighting.json

RESULTS.md              Full honest results analysis
```

## Key Results (Summary)

- **Symmetric map**: always drifts to boundary (x→0 or x→1). No interior attractor.
- **Coupled map**: interior fixed points exist for λ > 1, small ε. Stable, globally attracting.
- **No chaos**: Lyapunov exponents negative everywhere tested.
- **Spectral dimension**: consistently d_s ≈ 1 (1D curve). No non-integer emergence.
- **S_Λ conservation**: exact to machine precision (10⁻¹⁵) — the Eisenstein normalization guarantees this.

## Main Formula Reference

    Entropy identity:  S_Λ = S_b + S_c + √(S_b S_c) = 3π/Λ
    Entropy deficit:   Δ = √(S_b S_c) = π r_b r_c
    Temperatures:      T_b = √Λ/(4π√3) · (1-x)(2x+1)/[x√(x²+x+1)]
                       T_c = √Λ/(4π√3) · (1-x)(x+2)/√(x²+x+1)
    Carnot efficiency: η_C = (1-x²)/(1+2x)
    j-invariant:       j = 6912(x²+x+1)³/[(1-x)(x+2)(2x+1)]²
