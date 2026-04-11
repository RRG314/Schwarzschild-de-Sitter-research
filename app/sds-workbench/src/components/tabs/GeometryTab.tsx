import { useAppStore } from '../../store/appStore';
import { EisensteinArc } from '../visuals/EisensteinArc';
import { fmt } from '../../engine/format';

export function GeometryTab() {
  const { state, mode } = useAppStore();

  return (
    <div className="tab-content">
      <div className="card">
        <h2 style={{ marginBottom: 'var(--sp-4)' }}>Eisenstein Arc</h2>
        <p style={{ marginBottom: 'var(--sp-4)' }}>
          Define u = √(S_b/S_Λ) and v = √(S_c/S_Λ). These coordinates satisfy the exact algebraic identity
          u² + u·v + v² = 1. Every valid SdS state lies on this arc. Moving the slider traces the dot from the
          pure de Sitter end (top) to the Nariai end (upper-right).
        </p>
        <EisensteinArc state={state} mode={mode} />
        {mode === 'technical' && (
          <>
            <div className="divider" />
            <div className="formula-block">
              u² + u·v + v² = 1{'\n'}
              u = x / √(x²+x+1){'\n'}
              v = 1 / √(x²+x+1){'\n'}
              x = u/v = r_b/r_c
            </div>
          </>
        )}
      </div>

      <div className="card">
        <h2 style={{ marginBottom: 'var(--sp-4)' }}>Closed-Form Radii</h2>
        {mode === 'technical' && (
          <div className="formula-block" style={{ marginBottom: 'var(--sp-4)' }}>
            r_c = √(3/Λ) / √(x²+x+1){'\n'}
            r_b = x · r_c{'\n'}
            r_Λ = √(3/Λ) = {fmt(state.r_lambda)}
          </div>
        )}
        <div className="stat-grid">
          {[
            { label: 'r_b / r_Λ', value: (state.r_b / state.r_lambda).toFixed(4), sub: 'black hole fraction' },
            { label: 'r_c / r_Λ', value: (state.r_c / state.r_lambda).toFixed(4), sub: 'cosm. fraction' },
            { label: 'r_b / r_c = x', value: state.x.toFixed(4), sub: 'the parameter' },
            { label: '1 - x', value: (1 - state.x).toFixed(4), sub: 'patch gap ratio' },
          ].map(s => (
            <div key={s.label} className="stat-box">
              <div className="stat-label">{s.label}</div>
              <div className="stat-value">{s.value}</div>
              <div className="stat-sub">{s.sub}</div>
            </div>
          ))}
        </div>
      </div>

      <div className="card">
        <h2 style={{ marginBottom: 'var(--sp-4)' }}>Physical Limits</h2>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--sp-4)' }}>
          {[
            {
              label: 'Pure de Sitter (x → 0)',
              color: 'var(--teal)',
              body: 'The black hole mass vanishes. The spacetime approaches pure de Sitter space. S_b → 0, S_c → S_Λ. T_b → ∞ (naively; the point-like BH limit breaks down).',
            },
            {
              label: 'Small black hole (x ≪ 1)',
              color: 'var(--amber)',
              body: 'The entropy is dominated by the cosmological horizon. Δ ≪ S_Λ. The black hole is a small perturbation of de Sitter space.',
            },
            {
              label: 'Nariai limit (x → 1)',
              color: 'var(--violet)',
              body: 'The two horizons merge at r = 1/√Λ. Both temperatures vanish. The entropy deficit Δ reaches its maximum (1/3 of S_Λ). Mass = M_Nariai = 1/(3√Λ).',
            },
          ].map(l => (
            <div key={l.label} style={{ borderLeft: `3px solid ${l.color}`, paddingLeft: 'var(--sp-4)' }}>
              <h3 style={{ marginBottom: 'var(--sp-2)', color: 'var(--text-primary)' }}>{l.label}</h3>
              <p>{l.body}</p>
            </div>
          ))}
        </div>
        <div className="callout" style={{ marginTop: 'var(--sp-4)' }}>
          <strong>Note:</strong> The slider selects different <em>spacetimes</em> in the SdS family. It does not represent time evolution.
        </div>
      </div>
    </div>
  );
}
