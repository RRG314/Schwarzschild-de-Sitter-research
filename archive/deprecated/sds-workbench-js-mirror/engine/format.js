export function fmt(n, digits = 4) {
    if (!isFinite(n))
        return '—';
    if (Math.abs(n) === 0)
        return '0';
    if (Math.abs(n) < 0.001 || Math.abs(n) >= 1e5) {
        return n.toExponential(2);
    }
    return n.toPrecision(digits);
}
export function fmtPct(n, digits = 1) {
    return (n * 100).toFixed(digits) + '%';
}
export function fmtResidual(n) {
    if (n === 0)
        return '0';
    return n.toExponential(2);
}
export function fmtTemp(T) {
    if (!isFinite(T) || T > 1e6)
        return '∞';
    if (Math.abs(T) < 1e-6)
        return '≈ 0';
    return T.toExponential(3);
}
