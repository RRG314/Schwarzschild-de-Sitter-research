import { SDSState } from '../../engine/types';
import { fmt } from '../../engine/format';

export function RadialDiagram({ state, height = 120 }: { state: SDSState; height?: number }) {
  const W = 560, H = height;
  const cy = H / 2;
  const pad = 20;
  const usable = W - 2 * pad;

  const scale = usable / state.r_lambda;
  const rb_px = state.r_b * scale;
  const rc_px = state.r_c * scale;

  const cx0 = pad;

  return (
    <div>
      <svg viewBox={`0 0 ${W} ${H}`} style={{ width: '100%', height: 'auto', overflow: 'visible' }}>
        <defs>
          <radialGradient id="bhGrad" cx="0" cy="0.5" r="1">
            <stop offset="0%" stopColor="var(--amber)" stopOpacity="0.3" />
            <stop offset="100%" stopColor="var(--amber)" stopOpacity="0" />
          </radialGradient>
        </defs>

        <line x1={cx0 + usable} y1={10} x2={cx0 + usable} y2={H - 10}
          stroke="var(--border-default)" strokeWidth="1" strokeDasharray="4,3" />
        <text x={cx0 + usable} y={8} textAnchor="middle" fontSize="10" fill="var(--text-muted)">r_Λ</text>

        <rect x={cx0 + rb_px} y={cy - 24} width={rc_px - rb_px} height={48}
          fill="rgba(88,166,255,0.06)" rx="2" />

        <rect x={cx0} y={cy - 20} width={rb_px} height={40}
          fill="var(--amber-dim)" rx="2" />

        <line x1={cx0} y1={cy} x2={cx0 + usable + 10} y2={cy}
          stroke="var(--border-strong)" strokeWidth="1" />

        <line x1={cx0 + rb_px} y1={cy - 30} x2={cx0 + rb_px} y2={cy + 30}
          stroke="var(--amber)" strokeWidth="2" />
        <circle cx={cx0 + rb_px} cy={cy} r="5" fill="var(--amber)" />
        <text x={cx0 + rb_px} y={cy - 35} textAnchor="middle" fontSize="11" fill="var(--amber-text)" fontWeight="600">r_b</text>
        <text x={cx0 + rb_px} y={cy + 46} textAnchor="middle" fontSize="9" fill="var(--amber-text)">{fmt(state.r_b, 3)}</text>

        <line x1={cx0 + rc_px} y1={cy - 30} x2={cx0 + rc_px} y2={cy + 30}
          stroke="var(--teal)" strokeWidth="2" />
        <circle cx={cx0 + rc_px} cy={cy} r="5" fill="var(--teal)" />
        <text x={cx0 + rc_px} y={cy - 35} textAnchor="middle" fontSize="11" fill="var(--teal-text)" fontWeight="600">r_c</text>
        <text x={cx0 + rc_px} y={cy + 46} textAnchor="middle" fontSize="9" fill="var(--teal-text)">{fmt(state.r_c, 3)}</text>

        <circle cx={cx0} cy={cy} r="4" fill="var(--text-muted)" />
        <text x={cx0} y={cy + 46} textAnchor="middle" fontSize="9" fill="var(--text-muted)">0</text>

        {rc_px - rb_px > 80 && (
          <text x={cx0 + rb_px + (rc_px - rb_px) / 2} y={cy + 5} textAnchor="middle"
            fontSize="10" fill="var(--blue-text)" opacity="0.8">static patch</text>
        )}
      </svg>

      <div style={{ display: 'flex', gap: 'var(--sp-4)', marginTop: 'var(--sp-3)', flexWrap: 'wrap' }}>
        {[
          { color: 'var(--amber)', label: 'Black hole region', sub: `r < r_b = ${fmt(state.r_b, 3)}` },
          { color: 'var(--blue)', label: 'Static patch', sub: 'observable region' },
          { color: 'var(--teal)', label: 'Cosmological horizon', sub: `r_c = ${fmt(state.r_c, 3)}` },
        ].map(({ color, label, sub }) => (
          <div key={label} style={{ display: 'flex', alignItems: 'center', gap: 'var(--sp-2)', fontSize: '0.75rem' }}>
            <div style={{ width: 10, height: 10, borderRadius: 2, background: color, flexShrink: 0 }} />
            <div>
              <div style={{ color: 'var(--text-secondary)', fontWeight: 500 }}>{label}</div>
              <div style={{ color: 'var(--text-muted)', fontFamily: 'var(--font-mono)', fontSize: '0.6875rem' }}>{sub}</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
