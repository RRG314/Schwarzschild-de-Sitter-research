import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import { fmtPct, fmt } from '../../engine/format';
export function EntropyBudget({ state, mode }) {
    const segments = [
        { key: 'Sb', label: 'S_b', desc: 'Black hole entropy', pct: state.fb, color: 'var(--amber)', colorDim: 'var(--amber-dim)', value: state.S_b },
        { key: 'Delta', label: 'Δ', desc: 'Entropy deficit', pct: state.fDelta, color: 'var(--violet)', colorDim: 'var(--violet-dim)', value: state.Delta },
        { key: 'Sc', label: 'S_c', desc: 'Cosmological entropy', pct: state.fc, color: 'var(--teal)', colorDim: 'var(--teal-dim)', value: state.S_c },
    ];
    return (_jsxs("div", { style: { display: 'flex', flexDirection: 'column', gap: 'var(--sp-4)' }, children: [_jsxs("div", { style: { fontSize: '0.8125rem', color: 'var(--text-secondary)', fontFamily: 'var(--font-mono)', textAlign: 'center' }, children: ["S_\u039B \u00A0=\u00A0 ", _jsx("span", { style: { color: 'var(--amber-text)' }, children: "S_b" }), "\u00A0+\u00A0 ", _jsx("span", { style: { color: 'var(--violet-text)' }, children: "\u0394" }), "\u00A0+\u00A0 ", _jsx("span", { style: { color: 'var(--teal-text)' }, children: "S_c" })] }), _jsx("div", { style: { display: 'flex', height: 32, borderRadius: 'var(--radius-sm)', overflow: 'hidden', border: '1px solid var(--border-subtle)' }, children: segments.map(seg => (_jsx("div", { style: {
                        width: `${seg.pct * 100}%`,
                        background: seg.color,
                        opacity: 0.85,
                        display: 'flex', alignItems: 'center', justifyContent: 'center',
                        fontSize: '0.6875rem', fontWeight: 700, color: 'white',
                        transition: 'width 0.2s ease',
                        overflow: 'hidden', whiteSpace: 'nowrap',
                    }, children: seg.pct > 0.07 && seg.label }, seg.key))) }), _jsx("div", { style: { display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 'var(--sp-2)' }, children: segments.map(seg => (_jsxs("div", { style: {
                        background: seg.colorDim,
                        borderRadius: 'var(--radius-sm)',
                        padding: 'var(--sp-3)',
                        borderLeft: `2px solid ${seg.color}`,
                    }, children: [_jsx("div", { style: { fontFamily: 'var(--font-mono)', fontSize: '0.75rem', fontWeight: 700, color: seg.color }, children: seg.label }), _jsx("div", { style: { fontFamily: 'var(--font-mono)', fontSize: '1rem', fontWeight: 700, color: 'var(--text-primary)' }, children: fmtPct(seg.pct) }), _jsx("div", { style: { fontSize: '0.6875rem', color: 'var(--text-muted)' }, children: seg.desc }), mode === 'technical' && (_jsx("div", { style: { fontSize: '0.625rem', fontFamily: 'var(--font-mono)', color: 'var(--text-muted)', marginTop: 2 }, children: fmt(seg.value, 4) }))] }, seg.key))) })] }));
}
