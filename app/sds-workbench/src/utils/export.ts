import { EvolutionRun, SDSState } from '../engine/types';
import { computeState } from '../engine/physics';

function stateToRecord(s: SDSState): Record<string, string> {
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

function recordsToCsv(records: Record<string, string>[]): string {
  if (!records.length) return '';
  const headers = Object.keys(records[0]);
  const rows = records.map(r => headers.map(h => r[h]).join(','));
  return [headers.join(','), ...rows].join('\n');
}

export function exportStateAsJson(s: SDSState): string {
  return JSON.stringify(stateToRecord(s), null, 2);
}

export function exportStateAsCsv(s: SDSState): string {
  return recordsToCsv([stateToRecord(s)]);
}

export function exportSweepAsCsv(lambda: number, steps = 100): string {
  const records: Record<string, string>[] = [];
  for (let i = 0; i <= steps; i++) {
    const x = 0.01 + (0.98 * i) / steps;
    records.push(stateToRecord(computeState(x, lambda)));
  }
  return recordsToCsv(records);
}

export function exportComparisonAsCsv(a: SDSState, b: SDSState): string {
  const ra = stateToRecord(a);
  const rb = stateToRecord(b);
  const headers = Object.keys(ra);
  const lines = [
    ['quantity', 'state_A', 'state_B', 'diff'].join(','),
    ...headers.map(h => [h, ra[h], rb[h], ''].join(',')),
  ];
  return lines.join('\n');
}

export function exportTrajectoryAsCsv(run: EvolutionRun): string {
  const records = run.points.map(p => ({
    index: String(p.index),
    t: p.t.toFixed(6),
    lambda: run.lambda.toFixed(6),
    model: run.config.direction,
    k: run.config.k.toExponential(6),
    dt: run.config.dt.toFixed(6),
    M: p.M.toExponential(8),
    x: p.x.toFixed(8),
    r_b: p.r_b.toFixed(8),
    r_c: p.r_c.toFixed(8),
    S_b: p.S_b.toExponential(8),
    S_c: p.S_c.toExponential(8),
    Delta: p.Delta.toExponential(8),
    T_b: p.T_b.toExponential(8),
    T_c: p.T_c.toExponential(8),
    eta_C: p.eta_C.toFixed(8),
  }));
  return recordsToCsv(records);
}

export function exportTrajectoryAsJson(run: EvolutionRun): string {
  return JSON.stringify(run, null, 2);
}

export function downloadFile(content: string, filename: string, mime = 'text/plain'): void {
  const blob = new Blob([content], { type: mime });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  a.click();
  URL.revokeObjectURL(url);
}

export async function copyToClipboard(text: string): Promise<boolean> {
  try {
    await navigator.clipboard.writeText(text);
    return true;
  } catch {
    const el = document.createElement('textarea');
    el.value = text;
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);
    return true;
  }
}
