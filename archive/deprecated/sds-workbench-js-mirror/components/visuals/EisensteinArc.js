import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
export function EisensteinArc({ state, mode }) {
    const W = 300, H = 300, pad = 40;
    const chartW = W - 2 * pad, chartH = H - 2 * pad;
    const N = 120;
    const arcPoints = [];
    for (let i = 0; i <= N; i++) {
        const t = 0.001 + (0.998 * i) / N;
        const denom = Math.sqrt(t * t + t + 1);
        const u = t / denom;
        const v = 1 / denom;
        arcPoints.push([u, v]);
    }
    const toSvg = (u, v) => [
        pad + u * chartW,
        pad + (1 - v) * chartH,
    ];
    const pathD = arcPoints.map(([u, v], i) => {
        const [sx, sy] = toSvg(u, v);
        return i === 0 ? `M ${sx} ${sy}` : `L ${sx} ${sy}`;
    }).join(' ');
    const [dotX, dotY] = toSvg(state.u, state.v);
    const gridVals = [0.2, 0.4, 0.6, 0.8, 1.0];
    return (_jsxs("div", { children: [_jsxs("svg", { viewBox: `0 0 ${W} ${H}`, style: { width: '100%', maxWidth: 340, display: 'block', margin: '0 auto' }, children: [gridVals.map(g => {
                        const [gx] = toSvg(g, 0);
                        const [, gy] = toSvg(0, g);
                        return (_jsxs("g", { children: [_jsx("line", { x1: gx, y1: pad, x2: gx, y2: pad + chartH, stroke: "var(--border-subtle)", strokeWidth: "1" }), _jsx("line", { x1: pad, y1: gy, x2: pad + chartW, y2: gy, stroke: "var(--border-subtle)", strokeWidth: "1" }), _jsx("text", { x: gx, y: pad + chartH + 14, textAnchor: "middle", fontSize: "9", fill: "var(--text-muted)", children: g.toFixed(1) }), _jsx("text", { x: pad - 6, y: gy + 3, textAnchor: "end", fontSize: "9", fill: "var(--text-muted)", children: g.toFixed(1) })] }, g));
                    }), _jsx("line", { x1: pad, y1: pad, x2: pad, y2: pad + chartH, stroke: "var(--border-default)", strokeWidth: "1" }), _jsx("line", { x1: pad, y1: pad + chartH, x2: pad + chartW, y2: pad + chartH, stroke: "var(--border-default)", strokeWidth: "1" }), _jsx("text", { x: pad + chartW / 2, y: H - 4, textAnchor: "middle", fontSize: "10", fill: "var(--text-secondary)", children: "u = \u221A(S_b / S_\u039B)" }), _jsx("text", { x: 10, y: pad + chartH / 2, textAnchor: "middle", fontSize: "10", fill: "var(--text-secondary)", transform: `rotate(-90, 10, ${pad + chartH / 2})`, children: "v = \u221A(S_c / S_\u039B)" }), _jsx("path", { d: pathD, fill: "none", stroke: "var(--blue)", strokeWidth: "2", opacity: "0.7" }), _jsx("text", { x: toSvg(0.001, 1)[0] + 8, y: toSvg(0.001, 1)[1], fontSize: "9", fill: "var(--text-muted)", children: "Pure dS" }), _jsx("text", { x: toSvg(1 / Math.sqrt(3), 1 / Math.sqrt(3))[0] + 4, y: toSvg(1 / Math.sqrt(3), 1 / Math.sqrt(3))[1] - 6, fontSize: "9", fill: "var(--text-muted)", children: "Nariai" }), _jsx("circle", { cx: dotX, cy: dotY, r: "6", fill: "var(--blue)", opacity: "0.3" }), _jsx("circle", { cx: dotX, cy: dotY, r: "4", fill: "var(--blue)" }), _jsx("circle", { cx: dotX, cy: dotY, r: "2", fill: "white" }), _jsx("line", { x1: dotX, y1: pad, x2: dotX, y2: pad + chartH, stroke: "var(--blue)", strokeWidth: "1", opacity: "0.3", strokeDasharray: "3,2" }), _jsx("line", { x1: pad, y1: dotY, x2: pad + chartW, y2: dotY, stroke: "var(--blue)", strokeWidth: "1", opacity: "0.3", strokeDasharray: "3,2" })] }), mode === 'technical' && (_jsx("div", { style: { display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 'var(--sp-2)', marginTop: 'var(--sp-3)' }, children: [
                    { label: 'u', value: state.u.toFixed(4) },
                    { label: 'v', value: state.v.toFixed(4) },
                    { label: 'u/v = x', value: (state.u / state.v).toFixed(4) },
                ].map(({ label, value }) => (_jsxs("div", { style: { background: 'var(--bg-elevated)', borderRadius: 'var(--radius-sm)', padding: 'var(--sp-2) var(--sp-3)', textAlign: 'center' }, children: [_jsx("div", { style: { fontSize: '0.625rem', color: 'var(--text-muted)', fontFamily: 'var(--font-mono)' }, children: label }), _jsx("div", { style: { fontSize: '0.875rem', fontFamily: 'var(--font-mono)', color: 'var(--blue-text)' }, children: value })] }, label))) }))] }));
}
