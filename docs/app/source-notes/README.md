# SdS Workbench

A polished, production-quality interactive scientific workbench for exploring the thermodynamics of 4D Schwarzschild–de Sitter spacetime at fixed cosmological constant Λ.

## Features

- **5-tab interface**: Explore, Geometry, Thermodynamics, Compare, Export
- **Shareable state URLs**: All parameters encoded in query string for instant sharing
- **Saved states**: Persistent local storage (up to 20 states)
- **Parameter sweep mode**: Animated traverse of x from 0→1 (clearly labeled as parameter sweep, not time evolution)
- **Three input modes**: Direct x slider, Mass M, or entropy deficit Δ/S_Λ
- **Beginner/Technical modes**: Contextual help and formula display
- **Live validation**: Residual checks on all exact SdS identities
- **JSON/CSV export**: Current state, parameter sweeps, and state comparisons
- **Polished UI**: Dark theme with semantic color coding (amber=BH, teal=cosmological, blue=geometry, violet=geometry)

## Exact Physics

All computations are based on closed-form analytic solutions for fixed-Λ SdS:

- **Radii**: r_c = √(3/Λ) / √(x²+x+1), r_b = x·r_c
- **Mass**: M = (r_b/2) · (1 - Λr_b²/3)
- **Entropy**: S_Λ = 3π/Λ, S_b = πr_b², S_c = πr_c², Δ = πr_b·r_c
- **Temperatures**: T_b = (1−Λr_b²)/(4πr_b), T_c = (Λr_c²−1)/(4πr_c)
- **Eisenstein constraint**: u² + u·v + v² = 1 where u=√(S_b/S_Λ), v=√(S_c/S_Λ)

All identities are verified live with numerical residuals displayed.

## Setup

```bash
# Install dependencies
npm install

# Development server (localhost:5173)
npm run dev

# Production build
npm run build

# Preview build
npm run preview
```

## File Structure

```
src/
  engine/
    types.ts         - Type definitions
    physics.ts       - SdS computation engine
    format.ts        - Number formatting utilities
  store/
    appStore.ts      - Zustand state management
  utils/
    url.ts           - URL encoding/decoding
    storage.ts       - localStorage persistence
    export.ts        - JSON/CSV export & download
  components/
    layout/
      TopBar.tsx     - Header with mode toggle & share
      Sidebar.tsx    - Parameter controls & saved states
    visuals/
      RadialDiagram.tsx       - Spatial structure visualization
      EntropyBudget.tsx       - Stacked entropy bar chart
      EisensteinArc.tsx       - u-v arc plot
      ValidationPanel.tsx     - Sanity checks
    tabs/
      ExploreTab.tsx          - Overview with radial diagram
      GeometryTab.tsx         - Eisenstein arc & limits
      ThermodynamicsTab.tsx   - Temperature display
      CompareTab.tsx          - Side-by-side state comparison
      ExportTab.tsx           - Data export & sharing
    ui/
      CopyButton.tsx          - Reusable copy-to-clipboard
  styles/
    tokens.css       - Design system variables
    globals.css      - Base styles & component library
  App.tsx            - Tab routing
  main.tsx           - React root
```

## Key Technologies

- **React 18.3** - UI framework
- **TypeScript 5.5** - Type safety
- **Vite 5.4** - Build tool & dev server
- **Zustand 4.5** - State management
- **CSS custom properties** - Themeable design system

## Scientific Accuracy

This tool implements exact solutions from:
- Schwarzschild–de Sitter thermodynamics (Gibbons & Hawking)
- Entropy budget decomposition
- The Eisenstein constraint on horizon fractions

All computed quantities are mathematically exact within floating-point precision (verified by residuals < 10⁻¹⁰).

## License

Open source scientific tool. Use freely in research and education.
