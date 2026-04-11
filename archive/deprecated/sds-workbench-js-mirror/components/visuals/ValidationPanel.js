import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import { fmtResidual } from '../../engine/format';
export function ValidationPanel({ state }) {
    const tol = 1e-10;
    const checks = [
        { label: 'Eisenstein: r_b² + r_b·r_c + r_c² = 3/Λ', value: state.res_eisenstein, numeric: true },
        { label: 'Entropy: S_Λ = S_b + Δ + S_c', value: state.res_entropy, numeric: true },
        { label: 'Arc: u² + u·v + v² = 1', value: state.res_arc, numeric: true },
        { label: 'T_c/T_b = x(x+2)/(1+2x)', value: state.res_Tratio, numeric: true },
        { label: 'M > 0', value: state.M > 0 ? 0 : 1, numeric: false, bool: state.M > 0 },
        { label: '9Λ·M² < 1 (sub-extremal)', value: 9 * state.lambda * state.M * state.M < 1 ? 0 : 1, numeric: false, bool: 9 * state.lambda * state.M * state.M < 1 },
    ];
    const allPass = checks.every(c => Math.abs(c.value) < tol);
    return (_jsxs("div", { children: [_jsxs("div", { style: { display: 'flex', alignItems: 'center', gap: 'var(--sp-2)', marginBottom: 'var(--sp-3)' }, children: [_jsx("span", { style: { fontSize: '0.875rem', fontWeight: 600 }, children: "Sanity Checks" }), _jsx("span", { style: { fontSize: '0.75rem', color: allPass ? 'var(--text-success)' : 'var(--text-danger)', fontWeight: 600 }, children: allPass ? '✓ All pass' : '✗ Failures detected' })] }), _jsx("div", { style: { display: 'flex', flexDirection: 'column', gap: 2 }, children: checks.map(c => {
                    const pass = Math.abs(c.value) < tol;
                    return (_jsxs("div", { className: "check-row", children: [_jsx("span", { className: `check-icon ${pass ? 'pass' : 'fail'}`, children: pass ? '✓' : '✗' }), _jsx("span", { className: "check-label", children: c.label }), c.numeric && (_jsx("span", { className: "check-value", children: fmtResidual(c.value) }))] }, c.label));
                }) })] }));
}
