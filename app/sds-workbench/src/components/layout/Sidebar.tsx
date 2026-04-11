import { useAppStore } from '../../store/appStore';
import { computeStateFromMass, computeStateFromDeltaFrac, PRESETS } from '../../engine/physics';
import { fmt } from '../../engine/format';
import { useState, useRef, useEffect } from 'react';

export function Sidebar() {
  const {
    x, lambda, state, inputMode, setInputMode, sidebarOpen,
    setX, setLambda, savedStates, saveCurrentState, deleteState, loadSavedState,
    isSweeping, sweepSpeed, setSweeping, setSweepSpeed,
  } = useAppStore();

  const [massInput, setMassInput] = useState('');
  const [deltaInput, setDeltaInput] = useState('');
  const [saveNameInput, setSaveNameInput] = useState('');
  const [massError, setMassError] = useState('');
  const [deltaError, setDeltaError] = useState('');
  const sweepRef = useRef<number | null>(null);

  useEffect(() => {
    if (isSweeping) {
      const step = 0.005;
      let dir = 1;
      let cur = x;
      sweepRef.current = window.setInterval(() => {
        cur += step * dir;
        if (cur >= 0.995) { cur = 0.995; dir = -1; }
        if (cur <= 0.005) { cur = 0.005; dir = 1; }
        setX(cur);
      }, 1000 / sweepSpeed);
    } else {
      if (sweepRef.current) clearInterval(sweepRef.current);
    }
    return () => { if (sweepRef.current) clearInterval(sweepRef.current); };
  }, [isSweeping, sweepSpeed]);

  const applyMassInput = () => {
    const M = parseFloat(massInput);
    const s = computeStateFromMass(lambda, M);
    if (s) { setX(s.x); setMassError(''); }
    else setMassError(`M must be in (0, ${fmt(state.M_nariai)})`);
  };

  const applyDeltaInput = () => {
    const d = parseFloat(deltaInput);
    const s = computeStateFromDeltaFrac(lambda, d);
    if (s) { setX(s.x); setDeltaError(''); }
    else setDeltaError('Δ/S_Λ must be in (0, 0.333)');
  };

  if (!sidebarOpen) return null;

  return (
    <aside style={{
      width: 'var(--sidebar-width)',
      flexShrink: 0,
      background: 'var(--bg-surface)',
      borderRight: '1px solid var(--border-subtle)',
      display: 'flex',
      flexDirection: 'column',
      overflowY: 'auto',
    }}>
      <div style={{ padding: 'var(--sp-4)', borderBottom: '1px solid var(--border-subtle)' }}>
        <div className="section-label">Current State</div>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 'var(--sp-2)' }}>
          {[
            { label: 'x', value: x.toFixed(4), color: 'var(--blue)' },
            { label: 'Λ', value: lambda.toFixed(3), color: 'var(--text-secondary)' },
            { label: 'r_b', value: fmt(state.r_b), color: 'var(--amber)' },
            { label: 'r_c', value: fmt(state.r_c), color: 'var(--teal)' },
          ].map(({ label, value, color }) => (
            <div key={label} style={{ background: 'var(--bg-elevated)', borderRadius: 'var(--radius-sm)', padding: '6px var(--sp-3)' }}>
              <div style={{ fontSize: '0.625rem', textTransform: 'uppercase', letterSpacing: '0.08em', color: 'var(--text-muted)', fontFamily: 'var(--font-mono)' }}>{label}</div>
              <div style={{ fontSize: '0.875rem', fontFamily: 'var(--font-mono)', color, fontWeight: 600 }}>{value}</div>
            </div>
          ))}
        </div>
      </div>

      <div style={{ padding: 'var(--sp-4)', borderBottom: '1px solid var(--border-subtle)', display: 'flex', flexDirection: 'column', gap: 'var(--sp-4)' }}>
        <div className="section-label">Parameters</div>

        <div className="toggle-group">
          {(['x', 'mass', 'delta'] as const).map(m => (
            <button key={m} className={`toggle-btn ${inputMode === m ? 'active' : ''}`} onClick={() => setInputMode(m)}>
              {m === 'x' ? 'x' : m === 'mass' ? 'M' : 'Δ/S'}
            </button>
          ))}
        </div>

        {inputMode === 'x' && (
          <div className="slider-wrap">
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <label style={{ fontSize: '0.8125rem', color: 'var(--text-secondary)' }}>x = r_b / r_c</label>
              <span style={{ fontFamily: 'var(--font-mono)', fontSize: '0.875rem', color: 'var(--blue-text)', fontWeight: 600 }}>{x.toFixed(4)}</span>
            </div>
            <input type="range" className="slider" min="0.005" max="0.995" step="0.001"
              value={x} onChange={e => setX(parseFloat(e.target.value))} />
            <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.6875rem', color: 'var(--text-muted)' }}>
              <span>Pure dS →</span><span>← Nariai</span>
            </div>
          </div>
        )}

        {inputMode === 'mass' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--sp-2)' }}>
            <label style={{ fontSize: '0.8125rem', color: 'var(--text-secondary)' }}>
              Mass M (0 to {fmt(state.M_nariai)})
            </label>
            <div style={{ display: 'flex', gap: 'var(--sp-2)' }}>
              <input className="input" placeholder={fmt(state.M)} value={massInput}
                onChange={e => setMassInput(e.target.value)}
                onKeyDown={e => e.key === 'Enter' && applyMassInput()} />
              <button className="btn btn-sm" onClick={applyMassInput}>Set</button>
            </div>
            {massError && <div style={{ fontSize: '0.75rem', color: 'var(--text-danger)' }}>{massError}</div>}
            <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Current M = {fmt(state.M)}</div>
          </div>
        )}

        {inputMode === 'delta' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--sp-2)' }}>
            <label style={{ fontSize: '0.8125rem', color: 'var(--text-secondary)' }}>
              Δ/S_Λ (0 to 0.333)
            </label>
            <div style={{ display: 'flex', gap: 'var(--sp-2)' }}>
              <input className="input" placeholder={fmt(state.fDelta)} value={deltaInput}
                onChange={e => setDeltaInput(e.target.value)}
                onKeyDown={e => e.key === 'Enter' && applyDeltaInput()} />
              <button className="btn btn-sm" onClick={applyDeltaInput}>Set</button>
            </div>
            {deltaError && <div style={{ fontSize: '0.75rem', color: 'var(--text-danger)' }}>{deltaError}</div>}
            <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Current = {fmt(state.fDelta)}</div>
          </div>
        )}

        <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--sp-2)' }}>
          <label style={{ fontSize: '0.8125rem', color: 'var(--text-secondary)' }}>Λ (0.01 – 10)</label>
          <div style={{ display: 'flex', gap: 'var(--sp-2)', alignItems: 'center' }}>
            <input type="number" className="input" step="0.1" min="0.01" max="10"
              value={lambda} onChange={e => setLambda(parseFloat(e.target.value) || lambda)} />
          </div>
          <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>r_Λ = {fmt(state.r_lambda)} · M_N = {fmt(state.M_nariai)}</div>
        </div>
      </div>

      <div style={{ padding: 'var(--sp-4)', borderBottom: '1px solid var(--border-subtle)', display: 'flex', flexDirection: 'column', gap: 'var(--sp-2)' }}>
        <div className="section-label">Presets</div>
        {Object.values(PRESETS).map(p => (
          <button key={p.label} className="btn btn-ghost" style={{ justifyContent: 'flex-start', fontSize: '0.8125rem' }}
            onClick={() => setX(p.x)} title={p.description}>
            {p.label}
          </button>
        ))}
      </div>

      <div style={{ padding: 'var(--sp-4)', borderBottom: '1px solid var(--border-subtle)', display: 'flex', flexDirection: 'column', gap: 'var(--sp-3)' }}>
        <div className="section-label">Parameter Sweep</div>
        <p style={{ fontSize: '0.75rem', margin: 0 }}>Sweeps x from 0 to 1 — not time evolution.</p>
        <div style={{ display: 'flex', gap: 'var(--sp-2)', alignItems: 'center' }}>
          <button className={`btn ${isSweeping ? 'btn-primary' : ''}`} style={{ flex: 1 }}
            onClick={() => setSweeping(!isSweeping)}>
            {isSweeping ? '⏸ Pause' : '▶ Play'}
          </button>
          <button className="btn btn-ghost btn-sm" onClick={() => setX(Math.max(0.005, x - 0.01))}>‹</button>
          <button className="btn btn-ghost btn-sm" onClick={() => setX(Math.min(0.995, x + 0.01))}>›</button>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 'var(--sp-2)', fontSize: '0.75rem', color: 'var(--text-secondary)' }}>
          <span>Speed</span>
          <input type="range" className="slider" style={{ flex: 1 }} min="1" max="30" value={sweepSpeed}
            onChange={e => setSweepSpeed(parseInt(e.target.value))} />
          <span style={{ fontFamily: 'var(--font-mono)', minWidth: 30 }}>{sweepSpeed}x</span>
        </div>
      </div>

      <div style={{ padding: 'var(--sp-4)', flex: 1, display: 'flex', flexDirection: 'column', gap: 'var(--sp-3)' }}>
        <div className="section-label">Saved States</div>
        <div style={{ display: 'flex', gap: 'var(--sp-2)' }}>
          <input className="input" placeholder="Name this state…" value={saveNameInput}
            onChange={e => setSaveNameInput(e.target.value)}
            onKeyDown={e => { if (e.key === 'Enter' && saveNameInput.trim()) { saveCurrentState(saveNameInput.trim()); setSaveNameInput(''); }}} />
          <button className="btn btn-sm" disabled={!saveNameInput.trim()}
            onClick={() => { if (saveNameInput.trim()) { saveCurrentState(saveNameInput.trim()); setSaveNameInput(''); } }}>
            Save
          </button>
        </div>
        {savedStates.length === 0 && (
          <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', textAlign: 'center', padding: 'var(--sp-4)' }}>
            No saved states. Save a state to recall it later.
          </div>
        )}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--sp-2)', overflowY: 'auto' }}>
          {savedStates.map(s => (
            <div key={s.id} style={{
              background: 'var(--bg-elevated)', borderRadius: 'var(--radius-sm)',
              padding: 'var(--sp-2) var(--sp-3)',
              display: 'flex', alignItems: 'center', gap: 'var(--sp-2)',
            }}>
              <div style={{ flex: 1, cursor: 'pointer' }} onClick={() => loadSavedState(s)}>
                <div style={{ fontSize: '0.8125rem', fontWeight: 500 }}>{s.name}</div>
                <div style={{ fontSize: '0.6875rem', color: 'var(--text-muted)', fontFamily: 'var(--font-mono)' }}>
                  x={s.x.toFixed(3)} Λ={s.lambda.toFixed(2)}
                </div>
              </div>
              <button className="btn btn-ghost btn-sm btn-icon" onClick={() => deleteState(s.id)} title="Delete" style={{ color: 'var(--text-muted)' }}>✕</button>
            </div>
          ))}
        </div>
      </div>
    </aside>
  );
}
