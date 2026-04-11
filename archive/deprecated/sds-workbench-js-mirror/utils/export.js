import { computeState } from '../engine/physics';
function stateToRecord(s) {
    return {
        x: s.x.toFixed(6),
        lambda: s.lambda.toFixed(6),
        r_b: s.r_b.toFixed(6),
        r_c: s.r_c.toFixed(6),
        r_lambda: s.r_lambda.toFixed(6),
        M: s.M.toFixed(6),
        M_nariai: s.M_nariai.toFixed(6),
        S_b_over_S_lambda: s.fb.toFixed(6),
        S_c_over_S_lambda: s.fc.toFixed(6),
        Delta_over_S_lambda: s.fDelta.toFixed(6),
        u: s.u.toFixed(6),
        v: s.v.toFixed(6),
        T_b: s.T_b.toExponential(6),
        T_c: s.T_c.toExponential(6),
        T_ratio: s.T_ratio.toFixed(6),
        eta_C: s.eta_C.toFixed(6),
        res_eisenstein: s.res_eisenstein.toExponential(3),
        res_entropy: s.res_entropy.toExponential(3),
    };
}
function recordsToCsv(records) {
    if (!records.length)
        return '';
    const headers = Object.keys(records[0]);
    const rows = records.map(r => headers.map(h => r[h]).join(','));
    return [headers.join(','), ...rows].join('\n');
}
export function exportStateAsJson(s) {
    return JSON.stringify(stateToRecord(s), null, 2);
}
export function exportStateAsCsv(s) {
    return recordsToCsv([stateToRecord(s)]);
}
export function exportSweepAsCsv(lambda, steps = 100) {
    const records = [];
    for (let i = 0; i <= steps; i++) {
        const x = 0.01 + (0.98 * i) / steps;
        records.push(stateToRecord(computeState(x, lambda)));
    }
    return recordsToCsv(records);
}
export function exportComparisonAsCsv(a, b) {
    const ra = stateToRecord(a);
    const rb = stateToRecord(b);
    const headers = Object.keys(ra);
    const lines = [
        ['quantity', 'state_A', 'state_B', 'diff'].join(','),
        ...headers.map(h => [h, ra[h], rb[h], ''].join(',')),
    ];
    return lines.join('\n');
}
export function downloadFile(content, filename, mime = 'text/plain') {
    const blob = new Blob([content], { type: mime });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    URL.revokeObjectURL(url);
}
export async function copyToClipboard(text) {
    try {
        await navigator.clipboard.writeText(text);
        return true;
    }
    catch {
        const el = document.createElement('textarea');
        el.value = text;
        document.body.appendChild(el);
        el.select();
        document.execCommand('copy');
        document.body.removeChild(el);
        return true;
    }
}
