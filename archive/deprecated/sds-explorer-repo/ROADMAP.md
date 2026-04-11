# Roadmap — SdS Explorer

## Next 5 Improvements (in priority order)

### 1. Shareable URL state (Quick win, ~1 hour)
Add `?x=0.45&lambda=1.0` query parameter support.
On load, parse URL params and initialize the slider to that state.
On any slider change, update `window.history.replaceState` with the new URL.
This makes any state shareable as a link.

### 2. Animation / parameter sweep mode (~2 hours)
Add a "Play" button that sweeps x from 0.01 to 0.99 (or between two pinned states)
with a configurable speed. Crucially: label this "Parameter Sweep" with a clear note
that it is NOT time evolution — just moving through the family.
Useful for presentations and for seeing how each panel changes across the family.

### 3. Export / copy state (~1 hour)
- "Copy as JSON" button: copies full state object to clipboard
- "Copy as LaTeX table" button: copies formatted LaTeX tabular
- "Download CSV" button: downloads a CSV of the full (x, Λ) grid at N points

### 4. Phase diagram (Family overview) (~3 hours)
A new panel showing the entire SdS family as a curve.
Plot: (r_b, r_c) space with the Eisenstein constraint arc shown explicitly.
Plot: (S_b/S_Λ, S_c/S_Λ) triangle.
The current state appears as a dot on these plots.
Optional: sweep over 3 different Λ values and show how the family changes.

### 5. RNdS extension (~8 hours)
Extend to Reissner-Nordström-de Sitter by adding charge Q as a second parameter.
- Quartic solver for the 4-horizon equation
- Three temperatures: T_inner, T_outer, T_cosmo
- Electric potential Φ = Q/r at each horizon
- No closed-form entropy identity (the "deficit" is non-zero and non-constant)
- New UI: 2D slider or grid for (x, Q/Q_max) space
- Clearly label as "RNdS extension" — different physics from SdS

## Medium-term Improvements

### 6. Dark/light theme toggle
Add a light theme option using CSS custom properties (all colors already use CSS vars).

### 7. Real LaTeX rendering
Replace Unicode math with MathJax or KaTeX (CDN-loaded) for the Technical mode formulas.
This improves readability for physicists.

### 8. Pedagogical mode
A "guided tour" mode that walks users through 5–6 key states:
- Pure de Sitter (x = 0.01)
- Small black hole (x = 0.1)
- Equal temperatures?  (not possible in SdS, but explain why)
- Maximum entropy deficit (x = 0.5 approx)
- Near Nariai (x = 0.95)
Each step has a text explanation that highlights what changed.

### 9. Convert to React+Vite project
If the team wants to extend this significantly, convert to a full React+TypeScript
project with Vite. The math engine (`physics.ts`) is already designed as a pure
module — just wrap the HTML in React components. Architecture plan in IMPLEMENTATION_NOTES.md.

### 10. Multi-Λ comparison
Allow up to 3 Λ values simultaneously. Show how the family scales:
- r_Λ ∝ 1/√Λ
- M_Nariai ∝ 1/√Λ
- All temperatures ∝ √Λ
This makes the physical meaning of Λ concrete.

## Known Limitations

- No RNdS, no higher dimensions, no other black hole types
- No time evolution (the slider is NOT dynamics — this is intentional and correct)
- Temperatures near x→0 (T_b → ∞) are suppressed/clamped in display
  to avoid confusing non-technical users — this should be explained better
- The Carnot efficiency η_C is thermodynamic, not a claimed physical process

## Academic Honesty

All future features should continue to:
- Clearly label what is exact vs. approximated
- Clearly label what is physically motivated vs. exploratory
- Not claim generalization beyond 4D SdS without explicit marking
- Not describe the slider as time evolution
