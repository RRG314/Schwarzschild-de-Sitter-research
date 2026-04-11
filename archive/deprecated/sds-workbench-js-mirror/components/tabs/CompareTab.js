import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import { useAppStore } from '../../store/appStore';
import { fmt, fmtPct, fmtTemp } from '../../engine/format';
function diff(a, b) {
    const d = b - a;
    if (Math.abs(d) < 1e-10)
        return '—';
    const sign = d > 0 ? '+' : '';
    return sign + fmt(d, 3);
}
function diffColor(a, b) {
    if (Math.abs(b - a) < 1e-10)
        return 'var(--text-muted)';
    return b > a ? 'var(--text-success)' : 'var(--text-danger)';
}
const ROWS = [
    { label: 'x', key: 'x', format: v => v.toFixed(4) },
    { label: 'r_b', key: 'r_b', format: fmt },
    { label: 'r_c', key: 'r_c', format: fmt },
    { label: 'M', key: 'M', format: fmt },
    { label: 'S_b / S_Λ', key: 'fb', format: fmtPct },
    { label: 'Δ / S_Λ', key: 'fDelta', format: fmtPct },
    { label: 'S_c / S_Λ', key: 'fc', format: fmtPct },
    { label: 'T_b', key: 'T_b', format: fmtTemp },
    { label: 'T_c', key: 'T_c', format: fmtTemp },
    { label: 'T_c / T_b', key: 'T_ratio', format: v => v.toFixed(4) },
    { label: 'η_C', key: 'eta_C', format: fmtPct },
];
function StateCard({ state, label, accent }) {
    return (_jsxs("div", { style: { background: 'var(--bg-elevated)', borderRadius: 'var(--radius-md)', padding: 'var(--sp-4)', flex: 1, borderTop: `3px solid ${accent}` }, children: [_jsx("div", { style: { fontSize: '0.75rem', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.08em', color: accent, marginBottom: 'var(--sp-3)' }, children: label }), _jsxs("div", { style: { fontFamily: 'var(--font-mono)', fontSize: '0.875rem' }, children: ["x = ", _jsx("strong", { children: state.x.toFixed(4) }), " \u00B7 \u039B = ", _jsx("strong", { children: state.lambda.toFixed(3) })] }), _jsxs("div", { style: { fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: 4 }, children: ["r_b = ", fmt(state.r_b), " \u00B7 r_c = ", fmt(state.r_c)] })] }));
}
export function CompareTab() {
    const { compareA, compareB, setCompareA, setCompareB, pinCurrentAsA, pinCurrentAsB } = useAppStore();
    return (_jsxs("div", { className: "tab-content", children: [_jsxs("div", { className: "card", children: [_jsx("h2", { style: { marginBottom: 'var(--sp-4)' }, children: "Pin States" }), _jsxs("div", { style: { display: 'flex', gap: 'var(--sp-3)', flexWrap: 'wrap' }, children: [_jsx("button", { className: "btn btn-primary", onClick: pinCurrentAsA, children: "Pin current as A" }), _jsx("button", { className: "btn", onClick: pinCurrentAsB, style: { borderColor: 'var(--teal)', color: 'var(--teal-text)' }, children: "Pin current as B" }), (compareA || compareB) && (_jsx("button", { className: "btn btn-ghost", onClick: () => { setCompareA(null); setCompareB(null); }, children: "Clear" }))] })] }), (compareA || compareB) && (_jsxs("div", { style: { display: 'flex', gap: 'var(--sp-4)' }, children: [compareA ? _jsx(StateCard, { state: compareA, label: "State A", accent: "var(--blue)" }) : (_jsx("div", { style: { flex: 1, background: 'var(--bg-elevated)', borderRadius: 'var(--radius-md)', padding: 'var(--sp-4)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'var(--text-muted)', fontSize: '0.8125rem' }, children: "A not pinned" })), compareB ? _jsx(StateCard, { state: compareB, label: "State B", accent: "var(--teal)" }) : (_jsx("div", { style: { flex: 1, background: 'var(--bg-elevated)', borderRadius: 'var(--radius-md)', padding: 'var(--sp-4)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'var(--text-muted)', fontSize: '0.8125rem' }, children: "B not pinned" }))] })), compareA && compareB ? (_jsxs("div", { className: "card", children: [_jsx("h2", { style: { marginBottom: 'var(--sp-4)' }, children: "Comparison" }), _jsxs("table", { style: { width: '100%', borderCollapse: 'collapse', fontSize: '0.8125rem' }, children: [_jsx("thead", { children: _jsx("tr", { style: { borderBottom: '1px solid var(--border-default)' }, children: ['Quantity', 'State A', 'State B', 'B − A'].map(h => (_jsx("th", { style: { padding: 'var(--sp-2) var(--sp-3)', textAlign: 'left', color: 'var(--text-muted)', fontWeight: 600, fontSize: '0.6875rem', textTransform: 'uppercase', letterSpacing: '0.06em' }, children: h }, h))) }) }), _jsx("tbody", { children: ROWS.map(row => {
                                    const va = compareA[row.key];
                                    const vb = compareB[row.key];
                                    return (_jsxs("tr", { style: { borderBottom: '1px solid var(--border-subtle)' }, children: [_jsx("td", { style: { padding: 'var(--sp-2) var(--sp-3)', fontFamily: 'var(--font-mono)', color: 'var(--text-secondary)' }, children: row.label }), _jsx("td", { style: { padding: 'var(--sp-2) var(--sp-3)', fontFamily: 'var(--font-mono)', color: 'var(--blue-text)' }, children: row.format(va) }), _jsx("td", { style: { padding: 'var(--sp-2) var(--sp-3)', fontFamily: 'var(--font-mono)', color: 'var(--teal-text)' }, children: row.format(vb) }), _jsx("td", { style: { padding: 'var(--sp-2) var(--sp-3)', fontFamily: 'var(--font-mono)', color: diffColor(va, vb), fontWeight: 600 }, children: diff(va, vb) })] }, row.label));
                                }) })] })] })) : (_jsxs("div", { className: "empty-state", children: [_jsx("div", { className: "empty-icon", children: "\u21CC" }), _jsx("div", { className: "empty-title", children: "No states to compare yet" }), _jsx("div", { className: "empty-body", children: "Pin the current state as A, adjust the slider, then pin as B to compare." })] }))] }));
}
