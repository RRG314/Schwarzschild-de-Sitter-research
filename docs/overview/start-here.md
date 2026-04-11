# Start Here (No Background Required)

If this is your first time looking at this project, use this guide.

## What this project is

This repository studies Schwarzschild-de Sitter (SdS) black hole thermodynamics.

In plain language, it asks:

- How two horizons (black-hole and cosmological) share entropy and temperature.
- Which relationships are exact formulas versus numerical approximations.
- What fails, what remains open, and what can be tested next.

## What to read first

1. `README.md` for the high-level map.
2. `docs/overview/status.md` to see what is exact, empirical, artifact, or open.
3. `docs/theory/core-sds-results.md` for core theory results.
4. `docs/spectral/core-spectral-results.md` for spectral/QNM status.
5. `docs/app/app-overview.md` for the interactive workbench.

## How to interpret claims safely

Use evidence labels everywhere in this repo:

- `exact`: proved/algebraic derivation in the stated model.
- `empirical`: numerical experiment output.
- `approximation-based`: relies on approximation assumptions.
- `exploratory`: idea under development.
- `artifact` or `retracted`: result no longer trusted.
- `open`: unresolved question.

## Fastest way to explore interactively

1. Run `cd app/sds-workbench && npm install && npm run dev`.
2. Open the app and inspect `Explore` then `Evolution` tabs.
3. Treat evolution as a simplified semiclassical parameter model, not full GR simulation.

## If you only have 30 minutes

1. Read `docs/overview/status.md`.
2. Read `docs/theory/core-sds-results.md`.
3. Open the app overview and run one trajectory in Evolution mode.
