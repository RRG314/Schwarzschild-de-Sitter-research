import { SDSState } from '../../engine/types';
import { fmtPct, fmt } from '../../engine/format';
import { Mode } from '../../engine/types';

export function EntropyBudget({ state, mode }: { state: SDSState; mode: Mode }) {
  const segments = [
    { key: 'Sb', label: 'S_b', desc: 'Black hole entropy', pct: state.fb, color: 'var(--amber)', colorDim: 'var(--amber-dim)', value: state.S_b },
    { key: 'Delta', label: 'Δ', desc: 'Entropy deficit', pct: state.fDelta, color: 'var(--violet)', colorDim: 'var(--violet-dim)', value: state.Delta },
    { key: 'Sc', label: 'S_c', desc: 'Cosmological entropy', pct: state.fc, color: 'var(--teal)', colorDim: 'var(--teal-dim)', value: state.S_c },
  ];

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--sp-4)' }}>
      <div style={{ fontSize: '0.8125rem', color: 'var(--text-secondary)', fontFamily: 'var(--font-mono)', textAlign: 'center' }}>
        S_Λ &nbsp;=&nbsp; <span style={{ color: 'var(--amber-text)' }}>S_b</span>
        &nbsp;+&nbsp; <span style={{ color: 'var(--violet-text)' }}>Δ</span>
        &nbsp;+&nbsp; <span style={{ color: 'var(--teal-text)' }}>S_c</span>
      </div>

      <div style={{ display: 'flex', height: 32, borderRadius: 'var(--radius-sm)', overflow: 'hidden', border: '1px solid var(--border-subtle)' }}>
        {segments.map(seg => (
          <div key={seg.key} style={{
            width: `${seg.pct * 100}%`,
            background: seg.color,
            opacity: 0.85,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            fontSize: '0.6875rem', fontWeight: 700, color: 'white',
            transition: 'width 0.2s ease',
            overflow: 'hidden', whiteSpace: 'nowrap',
          }}>
            {seg.pct > 0.07 && seg.label}
          </div>
        ))}
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 'var(--sp-2)' }}>
        {segments.map(seg => (
          <div key={seg.key} style={{
            background: seg.colorDim,
            borderRadius: 'var(--radius-sm)',
            padding: 'var(--sp-3)',
            borderLeft: `2px solid ${seg.color}`,
          }}>
            <div style={{ fontFamily: 'var(--font-mono)', fontSize: '0.75rem', fontWeight: 700, color: seg.color }}>{seg.label}</div>
            <div style={{ fontFamily: 'var(--font-mono)', fontSize: '1rem', fontWeight: 700, color: 'var(--text-primary)' }}>{fmtPct(seg.pct)}</div>
            <div style={{ fontSize: '0.6875rem', color: 'var(--text-muted)' }}>{seg.desc}</div>
            {mode === 'technical' && (
              <div style={{ fontSize: '0.625rem', fontFamily: 'var(--font-mono)', color: 'var(--text-muted)', marginTop: 2 }}>{fmt(seg.value, 4)}</div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
