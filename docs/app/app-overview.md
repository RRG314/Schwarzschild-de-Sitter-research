# SdS Workbench Overview

## Purpose

`app/sds-workbench` is the interactive lab interface for exploring SdS states and derived thermodynamic quantities while preserving exact core formulas in the computation engine.

## Core Capabilities

- Explore tab: state-space interpretation and horizon/entropy summaries
- Geometry and thermodynamics tabs: structural diagnostics and formula-aligned readouts
- Compare tab: side-by-side state comparisons
- Export tab: JSON/CSV export for states, sweeps, and comparisons
- Share URLs: reproducible parameterized links
- Saved states: local persistence for repeated workflows

## Evolution Mode (New)

The Evolution tab adds a clearly labeled simplified model:

- simplified semiclassical parameter evolution model
- explicit caveat: parameter evolution, not full GR simulation
- model equation: `dM/dt = ±k/M^2` (evaporation or reverse-flow/injection mode)

### Evolution controls

- initial state source: current state or saved state
- time slider
- play/pause/reset
- step back / step forward
- speed control
- trajectory export (CSV/JSON)

### Derived quantities tracked over time

- `M(t)`
- `x(t)`
- `r_b(t), r_c(t)`
- `S_b(t), S_c(t), Delta(t)`
- `T_b(t), T_c(t)`
- `eta_C(t)`

All are computed through the shared exact SdS engine at each step, avoiding duplicate formula implementations.

## Build and Deploy

### Local

```bash
cd app/sds-workbench
npm install
npm run dev
npm run test
npm run build
```

### GitHub Pages (Simple Root Deployment)

This repository uses a root-level deployment path (no GitHub Actions workflow required).

1. Build and publish app assets into `/workbench`:

```bash
./scripts/build/publish-pages-root.sh
```

2. Commit and push the generated `workbench/` folder.
3. In GitHub: `Settings -> Pages -> Deploy from a branch`.
4. Select `main` and `/(root)`.

## Key Source Files

- `app/sds-workbench/src/engine/physics.ts`
- `app/sds-workbench/src/engine/evolution.ts`
- `app/sds-workbench/src/store/appStore.ts`
- `app/sds-workbench/src/components/tabs/EvolutionTab.tsx`
- `app/sds-workbench/src/utils/export.ts`
