import { useAppStore } from '../../store/appStore';
import { SDSState } from '../../engine/types';
import { fmt, fmtPct, fmtTemp } from '../../engine/format';

function diff(a: number, b: number): string {
  const d = b - a;
  if (Math.abs(d) < 1e-10) return '—';
  const sign = d > 0 ? '+' : '';
  return sign + fmt(d, 3);
}

function diffColor(a: number, b: number): string {
  if (Math.abs(b - a) < 1e-10) return 'var(--text-muted)';
  return b > a ? 'var(--text-success)' : 'var(--text-danger)';
}

const ROWS: { label: string; key: keyof SDSState; format: (v: number) => string }[] = [
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

function StateCard({ state, label, accent }: { state: SDSState; label: string; accent: string }) {
  return (
    <div style={{ background: 'var(--bg-elevated)', borderRadius: 'var(--radius-md)', padding: 'var(--sp-4)', flex: 1, borderTop: `3px solid ${accent}` }}>
      <div style={{ fontSize: '0.75rem', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.08em', color: accent, marginBottom: 'var(--sp-3)' }}>{label}</div>
      <div style={{ fontFamily: 'var(--font-mono)', fontSize: '0.875rem' }}>
        x = <strong>{state.x.toFixed(4)}</strong> · Λ = <strong>{state.lambda.toFixed(3)}</strong>
      </div>
      <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: 4 }}>r_b = {fmt(state.r_b)} · r_c = {fmt(state.r_c)}</div>
    </div>
  );
}

export function CompareTab() {
  const { compareA, compareB, setCompareA, setCompareB, pinCurrentAsA, pinCurrentAsB } = useAppStore();

  return (
    <div className="tab-content">
      <div className="card">
        <h2 style={{ marginBottom: 'var(--sp-4)' }}>Pin States</h2>
        <div style={{ display: 'flex', gap: 'var(--sp-3)', flexWrap: 'wrap' }}>
          <button className="btn btn-primary" onClick={pinCurrentAsA}>Pin current as A</button>
          <button className="btn" onClick={pinCurrentAsB} style={{ borderColor: 'var(--teal)', color: 'var(--teal-text)' }}>Pin current as B</button>
          {(compareA || compareB) && (
            <button className="btn btn-ghost" onClick={() => { setCompareA(null); setCompareB(null); }}>Clear</button>
          )}
        </div>
      </div>

      {(compareA || compareB) && (
        <div style={{ display: 'flex', gap: 'var(--sp-4)' }}>
          {compareA ? <StateCard state={compareA} label="State A" accent="var(--blue)" /> : (
            <div style={{ flex: 1, background: 'var(--bg-elevated)', borderRadius: 'var(--radius-md)', padding: 'var(--sp-4)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'var(--text-muted)', fontSize: '0.8125rem' }}>A not pinned</div>
          )}
          {compareB ? <StateCard state={compareB} label="State B" accent="var(--teal)" /> : (
            <div style={{ flex: 1, background: 'var(--bg-elevated)', borderRadius: 'var(--radius-md)', padding: 'var(--sp-4)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'var(--text-muted)', fontSize: '0.8125rem' }}>B not pinned</div>
          )}
        </div>
      )}

      {compareA && compareB ? (
        <div className="card">
          <h2 style={{ marginBottom: 'var(--sp-4)' }}>Comparison</h2>
          <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '0.8125rem' }}>
            <thead>
              <tr style={{ borderBottom: '1px solid var(--border-default)' }}>
                {['Quantity', 'State A', 'State B', 'B − A'].map(h => (
                  <th key={h} style={{ padding: 'var(--sp-2) var(--sp-3)', textAlign: 'left', color: 'var(--text-muted)', fontWeight: 600, fontSize: '0.6875rem', textTransform: 'uppercase', letterSpacing: '0.06em' }}>{h}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {ROWS.map(row => {
                const va = compareA[row.key] as number;
                const vb = compareB[row.key] as number;
                return (
                  <tr key={row.label} style={{ borderBottom: '1px solid var(--border-subtle)' }}>
                    <td style={{ padding: 'var(--sp-2) var(--sp-3)', fontFamily: 'var(--font-mono)', color: 'var(--text-secondary)' }}>{row.label}</td>
                    <td style={{ padding: 'var(--sp-2) var(--sp-3)', fontFamily: 'var(--font-mono)', color: 'var(--blue-text)' }}>{row.format(va)}</td>
                    <td style={{ padding: 'var(--sp-2) var(--sp-3)', fontFamily: 'var(--font-mono)', color: 'var(--teal-text)' }}>{row.format(vb)}</td>
                    <td style={{ padding: 'var(--sp-2) var(--sp-3)', fontFamily: 'var(--font-mono)', color: diffColor(va, vb), fontWeight: 600 }}>{diff(va, vb)}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      ) : (
        <div className="empty-state">
          <div className="empty-icon">⇌</div>
          <div className="empty-title">No states to compare yet</div>
          <div className="empty-body">Pin the current state as A, adjust the slider, then pin as B to compare.</div>
        </div>
      )}
    </div>
  );
}
