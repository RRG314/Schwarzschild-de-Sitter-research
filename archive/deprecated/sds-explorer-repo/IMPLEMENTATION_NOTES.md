# Implementation Notes — SdS Explorer

## Architecture

The app is a single HTML file (~1700 lines) with three sections:
- `<style>` block: all CSS, CSS custom properties for theming
- `<body>` block: static HTML structure for all panels
- `<script>` block: math engine + SDSApp class + event wiring

## Key Design Decisions

### Single file vs. React
The user requested a single file deliverable. A React+Vite project would require
npm, a build step, and multiple files. The vanilla JS approach runs instantly
with no setup. Physics calculators of this kind work well without a framework.

### Math engine
All physics is in three pure functions at the top of the script block:
- `computeState(x, lambda)` — no side effects, returns a frozen state object
- `computeStateFromMass(lambda, M)` — bisection in 60 iterations (more than enough)
- `computeStateFromNormalizedDelta(lambda, deltaFrac)` — analytic quadratic formula

The engine is completely separate from rendering. All functions are pure.

### Rendering
The `SDSApp` class owns all state and rendering. It has one method per panel.
The main entry point is `app.update()` which calls all render methods.

SVG diagrams are updated by directly manipulating `element.setAttribute()` —
no virtual DOM or reconciliation. This is fast enough for a slider-driven app.

### Radial diagram
The radial diagram normalizes r_b and r_c to r_Λ = √(3/Λ) as the full width.
This means the diagram automatically rescales when Λ changes, keeping all
features visible. The cosmological horizon r_c is always shown as a fraction
of the de Sitter radius r_Λ.

### Eisenstein arc
The arc is drawn by sampling 120 points in x ∈ [0.001, 0.999] and computing
(u, v) = (x/√(x²+x+1), 1/√(x²+x+1)) for each. The SVG path is rebuilt each
time Λ changes (the arc itself is independent of Λ, but for robustness the
rebuild is triggered by any control change). The moving dot is updated in O(1).

### Temperature computation
Temperatures T_b = (1 - Λr_b²)/(4πr_b) and T_c = (Λr_c² - 1)/(4πr_c) come
directly from the surface gravity formula κ = |f'(r)|/2 at each horizon,
with f(r) = 1 - 2M/r - Λr²/3. T = κ/(2π).

### Color conventions
| Color  | Hex      | Meaning |
|--------|----------|---------|
| Amber  | #f59e0b  | Black hole horizon / S_b |
| Green  | #34d399  | Cosmological horizon / S_c |
| Purple | #a78bfa  | Entropy deficit Δ |
| Blue   | #60a5fa  | Current state marker, accents |

### Mode toggle
The `isTechnical` boolean on `SDSApp` controls visibility of `.technical-only`
and `.beginner-only` CSS classes. This is toggled with a single classList swap.

## What Is NOT Implemented

- LaTeX rendering (MathJax/KaTeX) — uses Unicode math characters instead
- Animation/sweep mode — slider is manual only
- Persistent state (localStorage) — state resets on page reload
- URL query parameters — state not shareable via URL
- RNdS extension (requires charge Q and quartic solver)
- Phase diagram showing the full family as a curve

## Testing

The validation panel in the app itself serves as a live test suite.
All 6 checks should show green checkmarks at all times.

Manual verification: set x=0.5, Λ=1:
- r_Λ = √3 ≈ 1.7321
- r_c = 1/√(0.25+0.5+1) = 1/√1.75 ≈ 0.7559
- r_b = 0.5 × r_c ≈ 0.3780
- S_b/S_Λ = 0.25/1.75 ≈ 0.1429 = 1/7
- S_c/S_Λ = 1/1.75 ≈ 0.5714 = 4/7
- Δ/S_Λ = 0.5/1.75 ≈ 0.2857 = 2/7
- Check: 1/7 + 2/7 + 4/7 = 7/7 = 1 ✓
