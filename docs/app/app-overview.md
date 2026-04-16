# SdS Workbench Overview

## Purpose

`app/sds-workbench` provides an interactive interface for SdS parameter exploration while reusing a shared exact-identity engine for derived quantities.

## Core Capabilities

- Explore tab: state-space interpretation and horizon/entropy summaries
- Geometry and thermodynamics tabs: formula-aligned diagnostics
- Compare tab: side-by-side state comparison
- Export tab: JSON/CSV export for states, sweeps, and comparisons
- Tools tab: benchmarked SDS-inspired practical tools with promotion / demotion decisions
- Share URLs: reproducible parameterized links
- Saved states: local persistence for repeated workflows

## Evolution Mode

The Evolution tab is a simplified semiclassical parameter-evolution mode.

- explicit model statement: parameter evolution, not full GR simulation
- model equation: `dM/dt = \pm k/M^2` (evaporation or reverse-flow mode)

### Controls

- initial state source: current state or saved state
- time slider
- play/pause/reset
- step backward / step forward
- speed control
- trajectory export (CSV/JSON)

### Tracked Quantities

- `M(t)`
- `x(t)`
- `r_b(t), r_c(t)`
- $S_b(t), S_c(t), \Delta(t)$
- `T_b(t), T_c(t)`
- $\eta_C(t)$

All trajectory quantities are reconstructed through the shared SdS engine at each step.

## Public Access

- Pages landing: `https://rrg314.github.io/Schwarzschild-de-Sitter-research/`
- Direct workbench: `https://rrg314.github.io/Schwarzschild-de-Sitter-research/workbench/`

## Local Verification

```bash
cd app/sds-workbench
npm install
npm run test
npm run build
```

## Key Source Files

- `app/sds-workbench/src/engine/physics.ts`
- `app/sds-workbench/src/engine/evolution.ts`
- `app/sds-workbench/src/engine/tools.ts`
- `app/sds-workbench/src/store/appStore.ts`
- `app/sds-workbench/src/components/tabs/EvolutionTab.tsx`
- `app/sds-workbench/src/components/tabs/ToolsTab.tsx`
- `app/sds-workbench/src/utils/export.ts`
