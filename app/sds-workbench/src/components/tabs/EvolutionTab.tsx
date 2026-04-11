import { useCallback, useEffect, useMemo, useState } from 'react';
import { buildEvolutionTrajectory } from '../../engine/evolution';
import { fmt, fmtPct, fmtTemp } from '../../engine/format';
import { computeState } from '../../engine/physics';
import { EvolutionDirection, SavedState } from '../../engine/types';
import { useAppStore } from '../../store/appStore';
import { downloadFile, exportTrajectoryAsCsv, exportTrajectoryAsJson } from '../../utils/export';
import { CopyButton } from '../ui/CopyButton';

type StartMode = 'current' | 'saved';

const DEFAULT_K = 0.0006;
const DEFAULT_DT = 1;
const DEFAULT_STEPS = 220;

function getSavedStateById(saved: SavedState[], id: string): SavedState | null {
  return saved.find((item) => item.id === id) ?? null;
}

function polyline(points: number[], width: number, height: number): string {
  if (!points.length) return '';
  const min = Math.min(...points);
  const max = Math.max(...points);
  const span = Math.max(max - min, 1e-12);

  return points
    .map((value, idx) => {
      const x = points.length === 1 ? width / 2 : (idx / (points.length - 1)) * width;
      const y = height - ((value - min) / span) * height;
      return `${x.toFixed(2)},${y.toFixed(2)}`;
    })
    .join(' ');
}

export function EvolutionTab() {
  const { state, savedStates, setLambda, setX } = useAppStore();
  const [startMode, setStartMode] = useState<StartMode>('current');
  const [savedStartId, setSavedStartId] = useState<string>(savedStates[0]?.id ?? '');
  const [direction, setDirection] = useState<EvolutionDirection>('evaporation');
  const [k, setK] = useState<number>(DEFAULT_K);
  const [dt, setDt] = useState<number>(DEFAULT_DT);
  const [steps, setSteps] = useState<number>(DEFAULT_STEPS);
  const [speed, setSpeed] = useState<number>(1);
  const [isPlaying, setIsPlaying] = useState<boolean>(false);

  const [run, setRun] = useState(() =>
    buildEvolutionTrajectory(state, { direction: 'evaporation', k: DEFAULT_K, dt: DEFAULT_DT, steps: DEFAULT_STEPS })
  );
  const [index, setIndex] = useState(0);

  useEffect(() => {
    if (savedStates.length && !getSavedStateById(savedStates, savedStartId)) {
      setSavedStartId(savedStates[0].id);
    }
  }, [savedStates, savedStartId]);

  const startState = useMemo(() => {
    if (startMode === 'saved') {
      const selected = getSavedStateById(savedStates, savedStartId);
      if (selected) return computeState(selected.x, selected.lambda);
    }
    return state;
  }, [savedStartId, savedStates, startMode, state]);

  const rebuildRun = useCallback(() => {
    const nextRun = buildEvolutionTrajectory(startState, { direction, k, dt, steps });
    setRun(nextRun);
    setIndex(0);
    setIsPlaying(false);
  }, [startState, direction, k, dt, steps]);

  useEffect(() => {
    if (!isPlaying) return;
    const delayMs = Math.max(40, Math.floor(280 / speed));
    const timer = window.setInterval(() => {
      setIndex((prev) => {
        if (prev >= run.points.length - 1) {
          setIsPlaying(false);
          return prev;
        }
        return prev + 1;
      });
    }, delayMs);
    return () => window.clearInterval(timer);
  }, [isPlaying, run.points.length, speed]);

  const currentPoint = run.points[Math.min(index, run.points.length - 1)] ?? run.points[0];
  const lastPoint = run.points[run.points.length - 1] ?? currentPoint;
  const firstPoint = run.points[0] ?? currentPoint;

  const massTrend = lastPoint && firstPoint ? lastPoint.M - firstPoint.M : 0;
  const xTrend = lastPoint && firstPoint ? lastPoint.x - firstPoint.x : 0;

  const massCurve = useMemo(
    () => polyline(run.points.map((point) => point.M), 600, 180),
    [run.points]
  );
  const xCurve = useMemo(
    () => polyline(run.points.map((point) => point.x), 600, 180),
    [run.points]
  );

  const trajectoryCsv = useMemo(() => exportTrajectoryAsCsv(run), [run]);
  const trajectoryJson = useMemo(() => exportTrajectoryAsJson(run), [run]);
  const trajectoryFilename = `sds-evolution-${direction}-x${run.initialX.toFixed(3)}-lambda${run.lambda.toFixed(2)}`;

  return (
    <div className="tab-content">
      <div className="callout" style={{ borderColor: 'rgba(245, 158, 11, 0.28)', background: 'var(--amber-dim)' }}>
        <strong>Simplified semiclassical evolution model.</strong> This mode evolves parameters with
        <code> dM/dt = ±k/M² </code>. It is a parameter evolution tool, not a full GR simulation.
      </div>

      <div className="card">
        <h2 style={{ marginBottom: 'var(--sp-4)' }}>Evolution Setup</h2>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(230px, 1fr))', gap: 'var(--sp-4)' }}>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--sp-2)' }}>
            <label className="section-label" style={{ marginBottom: 0 }}>Initial State</label>
            <div className="toggle-group">
              <button className={`toggle-btn ${startMode === 'current' ? 'active' : ''}`} onClick={() => setStartMode('current')}>
                Current
              </button>
              <button
                className={`toggle-btn ${startMode === 'saved' ? 'active' : ''}`}
                onClick={() => setStartMode('saved')}
                disabled={!savedStates.length}
              >
                Saved
              </button>
            </div>
            {startMode === 'saved' && (
              <select
                className="input"
                value={savedStartId}
                onChange={(event) => setSavedStartId(event.target.value)}
                disabled={!savedStates.length}
              >
                {savedStates.length === 0 && <option value="">No saved states</option>}
                {savedStates.map((saved) => (
                  <option key={saved.id} value={saved.id}>
                    {saved.name} (x={saved.x.toFixed(3)}, Λ={saved.lambda.toFixed(2)})
                  </option>
                ))}
              </select>
            )}
            <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
              Start x={startState.x.toFixed(4)}, Λ={startState.lambda.toFixed(4)}, M={fmt(startState.M)}
            </div>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--sp-2)' }}>
            <label className="section-label" style={{ marginBottom: 0 }}>Model Direction</label>
            <div className="toggle-group">
              <button
                className={`toggle-btn ${direction === 'evaporation' ? 'active' : ''}`}
                onClick={() => setDirection('evaporation')}
              >
                Evaporation
              </button>
              <button
                className={`toggle-btn ${direction === 'injection' ? 'active' : ''}`}
                onClick={() => setDirection('injection')}
              >
                Reverse Flow
              </button>
            </div>
            <label style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>k = {k.toExponential(2)}</label>
            <input
              className="slider"
              type="range"
              min="0.0001"
              max="0.005"
              step="0.0001"
              value={k}
              onChange={(event) => setK(parseFloat(event.target.value))}
            />
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--sp-2)' }}>
            <label className="section-label" style={{ marginBottom: 0 }}>Time Grid</label>
            <label style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Δt = {dt.toFixed(2)}</label>
            <input className="slider" type="range" min="0.25" max="4" step="0.25" value={dt}
              onChange={(event) => setDt(parseFloat(event.target.value))} />
            <label style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Steps = {steps}</label>
            <input className="slider" type="range" min="40" max="800" step="20" value={steps}
              onChange={(event) => setSteps(parseInt(event.target.value, 10))} />
          </div>
        </div>

        <div style={{ marginTop: 'var(--sp-4)', display: 'flex', gap: 'var(--sp-2)', flexWrap: 'wrap' }}>
          <button className="btn btn-primary" onClick={rebuildRun}>Initialize Trajectory</button>
          <button className="btn" onClick={() => {
            if (!currentPoint) return;
            setLambda(run.lambda);
            setX(currentPoint.x);
          }}>
            Load Current Evolution Step
          </button>
        </div>
      </div>

      <div className="card">
        <h2 style={{ marginBottom: 'var(--sp-3)' }}>Evolution Controls</h2>
        <div style={{ display: 'flex', gap: 'var(--sp-2)', flexWrap: 'wrap', marginBottom: 'var(--sp-4)' }}>
          <button className={`btn ${isPlaying ? 'btn-primary' : ''}`} onClick={() => setIsPlaying((prev) => !prev)}>
            {isPlaying ? 'Pause' : 'Play'}
          </button>
          <button className="btn btn-ghost" onClick={() => setIndex((prev) => Math.max(0, prev - 1))}>
            Step Back
          </button>
          <button className="btn btn-ghost" onClick={() => setIndex((prev) => Math.min(run.points.length - 1, prev + 1))}>
            Step Forward
          </button>
          <button className="btn btn-ghost" onClick={() => { setIndex(0); setIsPlaying(false); }}>
            Reset
          </button>
          <label style={{ marginLeft: 'auto', fontSize: '0.75rem', color: 'var(--text-secondary)', display: 'flex', alignItems: 'center', gap: 'var(--sp-2)' }}>
            Speed
            <input className="slider" type="range" min="1" max="12" step="1" value={speed}
              onChange={(event) => setSpeed(parseInt(event.target.value, 10))} style={{ width: 120 }} />
            <span className="mono">{speed}x</span>
          </label>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: 'var(--sp-3)', marginBottom: 'var(--sp-3)' }}>
          <span className="mono">t = {currentPoint ? currentPoint.t.toFixed(3) : '0.000'}</span>
          <span style={{ color: 'var(--text-muted)', fontSize: '0.75rem' }}>
            Step {currentPoint ? currentPoint.index : 0} / {Math.max(run.points.length - 1, 0)}
          </span>
          {run.terminatedEarly && (
            <span className="badge badge-amber" title={run.terminationReason ?? undefined}>
              terminated early
            </span>
          )}
        </div>

        <input
          className="slider"
          type="range"
          min="0"
          max={Math.max(run.points.length - 1, 0)}
          step="1"
          value={Math.min(index, Math.max(run.points.length - 1, 0))}
          onChange={(event) => {
            setIsPlaying(false);
            setIndex(parseInt(event.target.value, 10));
          }}
        />
      </div>

      <div className="card">
        <h2 style={{ marginBottom: 'var(--sp-4)' }}>Current Evolution State</h2>
        <div className="stat-grid">
          <div className="stat-box stat-amber">
            <div className="stat-label">M(t)</div>
            <div className="stat-value" style={{ color: 'var(--amber-text)' }}>{fmt(currentPoint?.M ?? 0)}</div>
            <div className="stat-sub">ΔM total: {massTrend >= 0 ? '+' : ''}{fmt(massTrend)}</div>
          </div>
          <div className="stat-box stat-blue">
            <div className="stat-label">x(t)</div>
            <div className="stat-value" style={{ color: 'var(--blue-text)' }}>{(currentPoint?.x ?? 0).toFixed(5)}</div>
            <div className="stat-sub">Δx total: {xTrend >= 0 ? '+' : ''}{xTrend.toFixed(5)}</div>
          </div>
          <div className="stat-box stat-teal">
            <div className="stat-label">Temperatures</div>
            <div className="stat-value" style={{ color: 'var(--teal-text)' }}>
              {fmtTemp(currentPoint?.T_b ?? 0)} / {fmtTemp(currentPoint?.T_c ?? 0)}
            </div>
            <div className="stat-sub">T_b / T_c</div>
          </div>
          <div className="stat-box stat-violet">
            <div className="stat-label">Carnot Efficiency</div>
            <div className="stat-value" style={{ color: 'var(--violet-text)' }}>{fmtPct(currentPoint?.eta_C ?? 0, 2)}</div>
            <div className="stat-sub">η_C(t)</div>
          </div>
        </div>
      </div>

      <div className="card">
        <h2 style={{ marginBottom: 'var(--sp-3)' }}>Trajectory Overview</h2>
        <p style={{ marginBottom: 'var(--sp-4)' }}>
          Amber: M(t), Blue: x(t). Curves are computed from the simplified semiclassical rule and mapped back into
          exact SdS quantities at each step.
        </p>
        <svg viewBox="0 0 620 190" style={{ width: '100%', border: '1px solid var(--border-subtle)', borderRadius: 'var(--radius-sm)', background: 'var(--bg-base)' }}>
          <polyline fill="none" stroke="var(--amber)" strokeWidth="2" points={massCurve} />
          <polyline fill="none" stroke="var(--blue)" strokeWidth="2" points={xCurve} />
        </svg>
      </div>

      <div className="card">
        <h2 style={{ marginBottom: 'var(--sp-3)' }}>Export Trajectory Data</h2>
        <div style={{ display: 'flex', gap: 'var(--sp-2)', flexWrap: 'wrap', marginBottom: 'var(--sp-3)' }}>
          <button className="btn" onClick={() => downloadFile(trajectoryCsv, `${trajectoryFilename}.csv`, 'text/csv')}>
            Download CSV
          </button>
          <button className="btn" onClick={() => downloadFile(trajectoryJson, `${trajectoryFilename}.json`, 'application/json')}>
            Download JSON
          </button>
          <CopyButton text={trajectoryCsv} label="Copy CSV" />
          <CopyButton text={trajectoryJson} label="Copy JSON" />
        </div>
      </div>
    </div>
  );
}
