import { useAppStore } from '../../store/appStore';
import { RadialDiagram } from '../visuals/RadialDiagram';
import { EntropyBudget } from '../visuals/EntropyBudget';
import { ValidationPanel } from '../visuals/ValidationPanel';
import { fmt, fmtPct } from '../../engine/format';

export function ExploreTab() {
  const { state, mode, x } = useAppStore();

  const regime = x < 0.15 ? 'small black hole' : x > 0.85 ? 'near-Nariai' : 'intermediate';

  return (
    <div className="tab-content">
      {mode === 'beginner' && (
        <div className="callout">
          <strong>What am I looking at?</strong> At fixed Λ, every Schwarzschild–de Sitter spacetime is pinned by one number:
          x = r_b/r_c — the ratio of the black hole horizon to the cosmological horizon. Move the sidebar slider to explore the full family.
          The Radial Diagram shows the spatial structure. The Entropy Budget shows how the total entropy is distributed.
        </div>
      )}

      <div className="card">
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 'var(--sp-4)' }}>
          <h2>Current State</h2>
          <span className="badge badge-blue">x = {x.toFixed(4)} · {regime}</span>
        </div>
        <div className="stat-grid">
          <div className="stat-box stat-amber">
            <div className="stat-label">Black hole horizon</div>
            <div className="stat-value" style={{ color: 'var(--amber-text)' }}>{fmt(state.r_b)}</div>
            <div className="stat-sub">r_b (natural units)</div>
          </div>
          <div className="stat-box stat-teal">
            <div className="stat-label">Cosm. horizon</div>
            <div className="stat-value" style={{ color: 'var(--teal-text)' }}>{fmt(state.r_c)}</div>
            <div className="stat-sub">r_c (natural units)</div>
          </div>
          <div className="stat-box">
            <div className="stat-label">Mass</div>
            <div className="stat-value">{fmt(state.M)}</div>
            <div className="stat-sub">M ({fmtPct(state.M / state.M_nariai)} of M_Nariai)</div>
          </div>
          <div className="stat-box">
            <div className="stat-label">de Sitter radius</div>
            <div className="stat-value">{fmt(state.r_lambda)}</div>
            <div className="stat-sub">r_Λ = √(3/Λ)</div>
          </div>
        </div>
      </div>

      <div className="card">
        <h2 style={{ marginBottom: 'var(--sp-4)' }}>Radial Structure</h2>
        {mode === 'beginner' && (
          <p style={{ marginBottom: 'var(--sp-4)' }}>
            The strip below shows the three regions of SdS spacetime. The <span style={{ color: 'var(--amber-text)' }}>amber</span> region is inside the black hole horizon. The <span style={{ color: 'var(--teal-text)' }}>teal</span> line is the cosmological horizon — the outer boundary of what any observer can see. Between them is the static observable patch.
          </p>
        )}
        <RadialDiagram state={state} />
      </div>

      <div className="card">
        <h2 style={{ marginBottom: 'var(--sp-2)' }}>Entropy Budget</h2>
        {mode === 'beginner' && (
          <p style={{ marginBottom: 'var(--sp-4)' }}>
            The total de Sitter entropy S_Λ is exactly split into three parts. Remarkably, S_Λ = S_b + S_c + Δ is exact — not an approximation.
          </p>
        )}
        <EntropyBudget state={state} mode={mode} />
      </div>

      <div className="card card-sm">
        <ValidationPanel state={state} />
      </div>
    </div>
  );
}
