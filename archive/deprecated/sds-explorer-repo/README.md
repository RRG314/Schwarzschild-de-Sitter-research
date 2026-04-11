# 4D Schwarzschild–de Sitter Explorer

An exact interactive calculator and visualizer for the thermodynamic family of
4D Schwarzschild–de Sitter (SdS) spacetimes at fixed cosmological constant Λ.

## How to Open

1. Download `sds-explorer.html`
2. Double-click it, or open it in any browser via File → Open
3. No installation, no internet required

## What This Is

At fixed Λ, the SdS family is a **one-parameter system**. Every spacetime
in the family is determined by a single number: x = r_b/r_c ∈ (0, 1),
the ratio of the black hole horizon to the cosmological horizon.

The explorer lets you move through this family with a slider and see all
derived quantities update in real time.

## What's Implemented

| Feature | Status |
|---------|--------|
| Core math engine (computeState, mass conversion, delta conversion) | ✅ Complete |
| Main slider (x ∈ [0.01, 0.99]) | ✅ Complete |
| Lambda input with validation | ✅ Complete |
| Input by x, by mass M, by Δ/S_Λ | ✅ Complete |
| Preset buttons (Pure dS, Midpoint, Near Nariai) | ✅ Complete |
| Beginner / Technical mode toggle | ✅ Complete |
| Radial static patch diagram (SVG) | ✅ Complete |
| Entropy budget (stacked bar) | ✅ Complete |
| Eisenstein arc (SVG plot with moving point) | ✅ Complete |
| Thermodynamics panel (T_b, T_c, η_C) | ✅ Complete |
| Complete values table | ✅ Complete |
| Compare mode (Pin A, Pin B, diff table) | ✅ Complete |
| Limits / interpretation panel | ✅ Complete |
| Validation / sanity check panel (6 checks) | ✅ Complete |
| Mobile responsive layout | ✅ Complete |

## Math Engine Functions

```javascript
computeState(x, lambda)              // All quantities from (x, Λ)
computeStateFromMass(lambda, M)      // Bisection: M → x → state
computeStateFromNormalizedDelta(lambda, deltaFrac)  // Analytic: Δ/S_Λ → x → state
```

## Exact Identities Verified at Runtime

- r_b² + r_b·r_c + r_c² = 3/Λ  (Eisenstein constraint)
- S_Λ = S_b + S_c + Δ  (entropy identity)
- u² + u·v + v² = 1  (Eisenstein arc)
- T_c/T_b = x(x+2)/(1+2x)  (temperature ratio)

All residuals should be < 1e-12.

## Top 5 Next Improvements

1. **Phase diagram view**: Plot all states simultaneously in (r_b, r_c) or (u, v) space
   with a sweep across Λ values
2. **RNdS extension**: Add charge Q as a second parameter (Reissner-Nordström-de Sitter),
   with the quartic solver and 3-horizon thermodynamics
3. **Animation mode**: Sweep x from 0 to 1 with a play button (labeled "parameter sweep,"
   not "time evolution")
4. **Export**: Copy-to-clipboard JSON, CSV download, or shareable URL with ?x=0.4&lambda=1.0
5. **Entropy flow diagram**: Show ΔS_b and ΔS_c as the slider moves, with interpretation
   of the first law δM = T_b dS_b = T_c dS_c at the horizon

## Academic Honesty Notes

- This is a visualization of the *known* SdS thermodynamic family, not new physics
- All formulas are standard GR results for 4D SdS
- The slider selects *different spacetimes*, not time evolution
- Nothing is claimed beyond fixed-Λ 4D SdS
- Temperature formulas use surface gravity: T = κ/(2π)
- The Carnot efficiency η_C is the thermodynamic efficiency of a reversible engine
  operating between the two horizon temperatures — it is not a claimed physical process
