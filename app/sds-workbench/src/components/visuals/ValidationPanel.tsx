import { SDSState } from '../../engine/types';
import { fmtResidual } from '../../engine/format';

export function ValidationPanel({ state }: { state: SDSState }) {
  const tol = 1e-10;
  const checks = [
    { label: 'Eisenstein: r_b² + r_b·r_c + r_c² = 3/Λ', value: state.res_eisenstein, numeric: true },
    { label: 'Entropy: S_Λ = S_b + Δ + S_c', value: state.res_entropy, numeric: true },
    { label: 'Arc: u² + u·v + v² = 1', value: state.res_arc, numeric: true },
    { label: 'T_c/T_b = x(x+2)/(1+2x)', value: state.res_Tratio, numeric: true },
    { label: 'M > 0', value: state.M > 0 ? 0 : 1, numeric: false, bool: state.M > 0 },
    { label: '9Λ·M² < 1 (sub-extremal)', value: 9 * state.lambda * state.M * state.M < 1 ? 0 : 1, numeric: false, bool: 9 * state.lambda * state.M * state.M < 1 },
  ];

  const allPass = checks.every(c => Math.abs(c.value) < tol);

  return (
    <div>
      <div style={{ display: 'flex', alignItems: 'center', gap: 'var(--sp-2)', marginBottom: 'var(--sp-3)' }}>
        <span style={{ fontSize: '0.875rem', fontWeight: 600 }}>Sanity Checks</span>
        <span style={{ fontSize: '0.75rem', color: allPass ? 'var(--text-success)' : 'var(--text-danger)', fontWeight: 600 }}>
          {allPass ? '✓ All pass' : '✗ Failures detected'}
        </span>
      </div>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
        {checks.map(c => {
          const pass = Math.abs(c.value) < tol;
          return (
            <div key={c.label} className="check-row">
              <span className={`check-icon ${pass ? 'pass' : 'fail'}`}>{pass ? '✓' : '✗'}</span>
              <span className="check-label">{c.label}</span>
              {c.numeric && (
                <span className="check-value">{fmtResidual(c.value)}</span>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
