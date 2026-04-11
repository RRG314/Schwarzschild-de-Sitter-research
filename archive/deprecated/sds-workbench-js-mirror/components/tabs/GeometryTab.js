import { jsx as _jsx, jsxs as _jsxs, Fragment as _Fragment } from "react/jsx-runtime";
import { useAppStore } from '../../store/appStore';
import { EisensteinArc } from '../visuals/EisensteinArc';
import { fmt } from '../../engine/format';
export function GeometryTab() {
    const { state, mode } = useAppStore();
    return (_jsxs("div", { className: "tab-content", children: [_jsxs("div", { className: "card", children: [_jsx("h2", { style: { marginBottom: 'var(--sp-4)' }, children: "Eisenstein Arc" }), _jsx("p", { style: { marginBottom: 'var(--sp-4)' }, children: "Define u = \u221A(S_b/S_\u039B) and v = \u221A(S_c/S_\u039B). These coordinates satisfy the exact algebraic identity u\u00B2 + u\u00B7v + v\u00B2 = 1. Every valid SdS state lies on this arc. Moving the slider traces the dot from the pure de Sitter end (top) to the Nariai end (upper-right)." }), _jsx(EisensteinArc, { state: state, mode: mode }), mode === 'technical' && (_jsxs(_Fragment, { children: [_jsx("div", { className: "divider" }), _jsxs("div", { className: "formula-block", children: ["u\u00B2 + u\u00B7v + v\u00B2 = 1", '\n', "u = x / \u221A(x\u00B2+x+1)", '\n', "v = 1 / \u221A(x\u00B2+x+1)", '\n', "x = u/v = r_b/r_c"] })] }))] }), _jsxs("div", { className: "card", children: [_jsx("h2", { style: { marginBottom: 'var(--sp-4)' }, children: "Closed-Form Radii" }), mode === 'technical' && (_jsxs("div", { className: "formula-block", style: { marginBottom: 'var(--sp-4)' }, children: ["r_c = \u221A(3/\u039B) / \u221A(x\u00B2+x+1)", '\n', "r_b = x \u00B7 r_c", '\n', "r_\u039B = \u221A(3/\u039B) = ", fmt(state.r_lambda)] })), _jsx("div", { className: "stat-grid", children: [
                            { label: 'r_b / r_Λ', value: (state.r_b / state.r_lambda).toFixed(4), sub: 'black hole fraction' },
                            { label: 'r_c / r_Λ', value: (state.r_c / state.r_lambda).toFixed(4), sub: 'cosm. fraction' },
                            { label: 'r_b / r_c = x', value: state.x.toFixed(4), sub: 'the parameter' },
                            { label: '1 - x', value: (1 - state.x).toFixed(4), sub: 'patch gap ratio' },
                        ].map(s => (_jsxs("div", { className: "stat-box", children: [_jsx("div", { className: "stat-label", children: s.label }), _jsx("div", { className: "stat-value", children: s.value }), _jsx("div", { className: "stat-sub", children: s.sub })] }, s.label))) })] }), _jsxs("div", { className: "card", children: [_jsx("h2", { style: { marginBottom: 'var(--sp-4)' }, children: "Physical Limits" }), _jsx("div", { style: { display: 'flex', flexDirection: 'column', gap: 'var(--sp-4)' }, children: [
                            {
                                label: 'Pure de Sitter (x → 0)',
                                color: 'var(--teal)',
                                body: 'The black hole mass vanishes. The spacetime approaches pure de Sitter space. S_b → 0, S_c → S_Λ. T_b → ∞ (naively; the point-like BH limit breaks down).',
                            },
                            {
                                label: 'Small black hole (x ≪ 1)',
                                color: 'var(--amber)',
                                body: 'The entropy is dominated by the cosmological horizon. Δ ≪ S_Λ. The black hole is a small perturbation of de Sitter space.',
                            },
                            {
                                label: 'Nariai limit (x → 1)',
                                color: 'var(--violet)',
                                body: 'The two horizons merge at r = 1/√Λ. Both temperatures vanish. The entropy deficit Δ reaches its maximum (1/3 of S_Λ). Mass = M_Nariai = 1/(3√Λ).',
                            },
                        ].map(l => (_jsxs("div", { style: { borderLeft: `3px solid ${l.color}`, paddingLeft: 'var(--sp-4)' }, children: [_jsx("h3", { style: { marginBottom: 'var(--sp-2)', color: 'var(--text-primary)' }, children: l.label }), _jsx("p", { children: l.body })] }, l.label))) }), _jsxs("div", { className: "callout", style: { marginTop: 'var(--sp-4)' }, children: [_jsx("strong", { children: "Note:" }), " The slider selects different ", _jsx("em", { children: "spacetimes" }), " in the SdS family. It does not represent time evolution."] })] })] }));
}
