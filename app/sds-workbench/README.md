# SdS Workbench

Interactive Schwarzschild-de Sitter lab for exact state exploration and simplified evolution experiments.

## Features

- Explore, Geometry, Thermodynamics, Evolution, Compare, Export tabs
- Exact SdS engine (`computeState`, `computeStateFromMass`, `computeStateFromDeltaFrac`)
- Saved states and compare workflow
- Shareable state URLs
- CSV/JSON exports for states, sweeps, comparisons, and evolution trajectories

## Evolution mode caveat

Evolution mode uses a simplified semiclassical parameter model:

- `dM/dt = ±k/M^2`
- parameter evolution only, not a full GR simulation

All derived quantities are recomputed through the exact SdS engine at each step.

## Local development

```bash
npm install
npm run dev
```

## Validation

```bash
npm run test
npm run build
```
