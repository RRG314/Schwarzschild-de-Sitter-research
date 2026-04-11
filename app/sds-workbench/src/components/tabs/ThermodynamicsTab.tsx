import { useAppStore } from '../../store/appStore';
import { fmtPct, fmtTemp } from '../../engine/format';

export function ThermodynamicsTab() {
  const { state, mode } = useAppStore();

  const maxT = Math.max(state.T_b, state.T_c);

  return (
    <div className="tab-content">
      {mode === 'beginner' && (
        <div className="callout">
          Each horizon has a temperature set by its surface gravity. The black hole horizon is always hotter than the cosmological horizon. At the Nariai limit (x → 1), both temperatures approach zero.
        </div>
      )}

      <div className="card">
        <h2 style={{ marginBottom: 'var(--sp-4)' }}>Horizon Temperatures</h2>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 'var(--sp-4)' }}>
          <div style={{ background: 'var(--amber-dim)', borderRadius: 'var(--radius-md)', padding: 'var(--sp-4)', borderLeft: '3px solid var(--amber)' }}>
            <div className="stat-label">Black hole horizon</div>
            <div style={{ fontSize: '1.5rem', fontFamily: 'var(--font-mono)', fontWeight: 700, color: 'var(--amber-text)', margin: '8px 0' }}>{fmtTemp(state.T_b)}</div>
            <div style={{ height: 6, background: 'var(--bg-elevated)', borderRadius: 3, overflow: 'hidden' }}>
              <div style={{ height: '100%', width: `${(state.T_b / maxT) * 100}%`, background: 'var(--amber)', transition: 'width 0.2s ease', borderRadius: 3 }} />
            </div>
            <div style={{ fontSize: '0.6875rem', color: 'var(--text-muted)', marginTop: 4 }}>T_b (hotter)</div>
            {mode === 'technical' && (
              <div className="formula-block" style={{ marginTop: 'var(--sp-3)', fontSize: '0.75rem' }}>
                T_b = (1 − Λr_b²) / (4πr_b)
              </div>
            )}
          </div>

          <div style={{ background: 'var(--teal-dim)', borderRadius: 'var(--radius-md)', padding: 'var(--sp-4)', borderLeft: '3px solid var(--teal)' }}>
            <div className="stat-label">Cosmological horizon</div>
            <div style={{ fontSize: '1.5rem', fontFamily: 'var(--font-mono)', fontWeight: 700, color: 'var(--teal-text)', margin: '8px 0' }}>{fmtTemp(state.T_c)}</div>
            <div style={{ height: 6, background: 'var(--bg-elevated)', borderRadius: 3, overflow: 'hidden' }}>
              <div style={{ height: '100%', width: `${(state.T_c / maxT) * 100}%`, background: 'var(--teal)', transition: 'width 0.2s ease', borderRadius: 3 }} />
            </div>
            <div style={{ fontSize: '0.6875rem', color: 'var(--text-muted)', marginTop: 4 }}>T_c (cooler)</div>
            {mode === 'technical' && (
              <div className="formula-block" style={{ marginTop: 'var(--sp-3)', fontSize: '0.75rem' }}>
                T_c = (Λr_c² − 1) / (4πr_c)
              </div>
            )}
          </div>
        </div>
      </div>

      <div className="card">
        <h2 style={{ marginBottom: 'var(--sp-4)' }}>Temperature Ratios</h2>
        <div className="stat-grid">
          <div className="stat-box stat-blue">
            <div className="stat-label">T_c / T_b</div>
            <div className="stat-value">{state.T_ratio.toFixed(4)}</div>
            <div className="stat-sub">always &lt; 1</div>
          </div>
          <div className="stat-box stat-violet">
            <div className="stat-label">Carnot efficiency η_C</div>
            <div className="stat-value">{fmtPct(state.eta_C)}</div>
            <div className="stat-sub">1 − T_c/T_b</div>
          </div>
          <div className="stat-box">
            <div className="stat-label">T_b / T_c</div>
            <div className="stat-value">{(1 / state.T_ratio).toFixed(4)}</div>
            <div className="stat-sub">BH is hotter by this factor</div>
          </div>
          <div className="stat-box">
            <div className="stat-label">x = r_b / r_c</div>
            <div className="stat-value">{state.x.toFixed(4)}</div>
            <div className="stat-sub">controls both temperatures</div>
          </div>
        </div>
        {mode === 'technical' && (
          <div className="formula-block" style={{ marginTop: 'var(--sp-4)' }}>
            T_c/T_b = x(x+2) / (1+2x){'\n'}
            η_C = 1 − T_c/T_b = (1−x²) / (1+2x)
          </div>
        )}
      </div>

      {mode === 'beginner' && (
        <div className="card">
          <h2 style={{ marginBottom: 'var(--sp-3)' }}>What do these temperatures mean?</h2>
          <p style={{ marginBottom: 'var(--sp-3)' }}>
            Quantum field theory on curved spacetime predicts that each horizon radiates like a thermal body. The Hawking temperature T_b is associated with the black hole horizon; the Gibbons-Hawking temperature T_c is associated with the cosmological horizon. These are exact semiclassical results.
          </p>
          <p>
            The Carnot efficiency η_C is the thermodynamic efficiency if a reversible heat engine ran between the two horizon temperatures. It is a bookkeeping tool, not a claim about a physical process.
          </p>
        </div>
      )}
    </div>
  );
}
