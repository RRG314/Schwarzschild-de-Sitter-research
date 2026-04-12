import { useMemo } from 'react';
import {
  buildSampleTraceCsv,
  buildToolsDecisionsCsv,
  buildToolsSnapshotJson,
  controlFamilyOverview,
  dualReservoirAggressiveBand,
  dualReservoirOverview,
  earlyStoppingOverview,
  SDS_TOOLS_SNAPSHOT,
  schedulerOverview,
  toolDecisionEntries,
  type AggregateRow,
  type ControlCurvePoint,
  type SampleTraceRow,
  type ToolStatus,
} from '../../engine/tools';
import { downloadFile } from '../../utils/export';
import { CopyButton } from '../ui/CopyButton';

const TRACE_WIDTH = 620;
const TRACE_HEIGHT = 240;

function formatNumber(value: number, digits = 3): string {
  return Number.isFinite(value) ? value.toFixed(digits) : '—';
}

function formatAccuracy(value: number | null): string {
  return typeof value === 'number' ? `${(value * 100).toFixed(1)}%` : '—';
}

function formatPercent(value: number, digits = 1): string {
  return `${(value * 100).toFixed(digits)}%`;
}

function statusClass(status: ToolStatus): string {
  if (status === 'recommended') return 'badge-teal';
  if (status === 'archived') return 'badge-amber';
  return 'badge-blue';
}

function regimeColor(regime: SampleTraceRow['regime']): string {
  switch (regime) {
    case 'productive':
      return 'var(--teal)';
    case 'transition':
      return 'var(--blue)';
    case 'equilibrium':
      return 'var(--amber)';
    case 'unstable':
      return 'var(--text-danger)';
  }
}

function polylineFromValues(values: number[], width: number, height: number): string {
  if (!values.length) return '';
  const min = Math.min(...values);
  const max = Math.max(...values);
  const span = Math.max(max - min, 1e-12);
  return values
    .map((value, index) => {
      const x = values.length === 1 ? width / 2 : (index / (values.length - 1)) * width;
      const y = height - ((value - min) / span) * height;
      return `${x.toFixed(2)},${y.toFixed(2)}`;
    })
    .join(' ');
}

function stateSpacePoints(trace: SampleTraceRow[], width: number, height: number): string {
  if (!trace.length) return '';
  return trace
    .map((row) => {
      const x = row.x * width;
      const y = height - row.useful_imbalance * height;
      return `${x.toFixed(2)},${y.toFixed(2)}`;
    })
    .join(' ');
}

function stateSpacePosition(row: SampleTraceRow, width: number, height: number): { x: number; y: number } {
  return {
    x: row.x * width,
    y: height - row.useful_imbalance * height,
  };
}

function SectionTable({ rows }: { rows: AggregateRow[] }) {
  return (
    <div style={{ overflowX: 'auto' }}>
      <table className="data-table">
        <thead>
          <tr>
            <th>Variant</th>
            <th>Best val. loss</th>
            <th>Final val. loss</th>
            <th>Best accuracy</th>
            <th>Epochs</th>
            <th>Diverged</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((row) => (
            <tr key={row.label}>
              <td>{row.label}</td>
              <td className="mono">{formatNumber(row.bestValLoss, 4)}</td>
              <td className="mono">{formatNumber(row.finalValLoss, 4)}</td>
              <td className="mono">{formatAccuracy(row.bestAccuracy)}</td>
              <td className="mono">{formatNumber(row.epochsRun, 1)}</td>
              <td className="mono">{formatPercent(row.divergedRate, 0)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function CurveChart({
  points,
  field,
  title,
  color,
  formatter,
}: {
  points: ControlCurvePoint[];
  field: 'lr_scale' | 'beta1' | 'weight_decay_scale' | 'noise_scale';
  title: string;
  color: string;
  formatter: (value: number) => string;
}) {
  const values = points.map((point) => point[field]);
  const path = polylineFromValues(values, 280, 120);
  const first = values[0];
  const last = values[values.length - 1];

  return (
    <div className="card card-sm" style={{ display: 'flex', flexDirection: 'column', gap: 'var(--sp-3)' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', gap: 'var(--sp-3)' }}>
        <div>
          <div className="section-label" style={{ marginBottom: 2 }}>{title}</div>
          <div style={{ fontSize: '0.8125rem', color: 'var(--text-secondary)' }}>
            x from 0.05 to 0.95
          </div>
        </div>
        <div className="mono" style={{ color }}>{formatter(last)}</div>
      </div>
      <svg viewBox="0 0 280 120" style={{ width: '100%', height: 120, background: 'var(--bg-base)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
        <polyline fill="none" stroke={color} strokeWidth="2.5" points={path} />
      </svg>
      <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.75rem', color: 'var(--text-muted)' }}>
        <span>{formatter(first)}</span>
        <span>{formatter(last)}</span>
      </div>
    </div>
  );
}

export function ToolsTab() {
  const decisions = useMemo(() => toolDecisionEntries(), []);
  const recommended = decisions.filter((item) => item.decision.status === 'recommended');
  const experimental = decisions.filter((item) => item.decision.status === 'experimental');

  const dualRows = useMemo(() => dualReservoirOverview(), []);
  const dualAggressiveRows = useMemo(() => dualReservoirAggressiveBand(), []);
  const schedulerRows = useMemo(() => schedulerOverview(), []);
  const earlyRows = useMemo(() => earlyStoppingOverview(), []);
  const controlOverview = useMemo(() => controlFamilyOverview(), []);

  const aggressiveGain = useMemo(() => {
    const baseline = dualAggressiveRows.find((row) => row.label.startsWith('Adam'));
    const full = dualAggressiveRows.find((row) => row.label.startsWith('Full'));
    if (!baseline || !full || !Number.isFinite(baseline.bestValLoss) || !Number.isFinite(full.bestValLoss)) return null;
    return (baseline.bestValLoss - full.bestValLoss) / baseline.bestValLoss;
  }, [dualAggressiveRows]);

  const controlGap = useMemo(() => {
    const bestPreset = controlOverview.presets[0];
    const bestGrid = controlOverview.bestGrid;
    return (bestPreset.bestValLoss - bestGrid.bestValLoss) / bestGrid.bestValLoss;
  }, [controlOverview]);

  const trace = SDS_TOOLS_SNAPSHOT.sampleTrace;
  const statePath = stateSpacePoints(trace, TRACE_WIDTH, TRACE_HEIGHT);
  const startPoint = trace[0];
  const endPoint = trace[trace.length - 1];
  const usefulImbalanceSeries = polylineFromValues(trace.map((row) => row.useful_imbalance), 620, 140);

  return (
    <div className="tab-content">
      <div className="callout">
        <strong>SDS-inspired practical tools.</strong> This tab sits on the applied side of the repository. The exact Schwarzschild-de Sitter formulas remain in the theory tabs and papers; the tools here borrow structural ideas like coupled reservoirs, deficit, reduced state, and near-equilibrium collapse to build practical controllers and diagnostics.
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: 'var(--sp-4)' }}>
        <div className="stat-box stat-teal">
          <div className="stat-label">Promoted Tools</div>
          <div className="stat-value">{recommended.length} / {decisions.length}</div>
          <div className="stat-sub">Supported and benchmarked for real use</div>
        </div>
        <div className="stat-box stat-blue">
          <div className="stat-label">Experimental Tools</div>
          <div className="stat-value">{experimental.length}</div>
          <div className="stat-sub">Kept visible, but not the default path</div>
        </div>
        <div className="stat-box stat-violet">
          <div className="stat-label">Aggressive-Band Gain</div>
          <div className="stat-value">{aggressiveGain === null ? '—' : formatPercent(aggressiveGain, 1)}</div>
          <div className="stat-sub">Mean best validation-loss improvement for the full controller over Adam at LR 0.30-0.60</div>
        </div>
        <div className="stat-box stat-amber">
          <div className="stat-label">Monitor Advantage</div>
          <div className="stat-value">{formatNumber(SDS_TOOLS_SNAPSHOT.monitorSummary.advantage, 3)}</div>
          <div className="stat-sub">Spearman advantage over raw loss slope on the current prediction benchmark</div>
        </div>
      </div>

      <div className="card">
        <div style={{ display: 'flex', justifyContent: 'space-between', gap: 'var(--sp-3)', flexWrap: 'wrap', marginBottom: 'var(--sp-4)' }}>
          <div>
            <h2 style={{ marginBottom: 'var(--sp-2)' }}>Promotion Decisions</h2>
            <p>Only the tools that survived honest baseline comparison are treated as recommended. The rest stay available, but they are not presented as default practice.</p>
          </div>
        </div>

        <div className="tools-grid">
          {decisions.map(({ id, decision, copy }) => (
            <article key={id} className="tool-card">
              <div style={{ display: 'flex', justifyContent: 'space-between', gap: 'var(--sp-3)', alignItems: 'flex-start', marginBottom: 'var(--sp-3)' }}>
                <div>
                  <h3 style={{ marginBottom: 4 }}>{copy.title}</h3>
                  <p style={{ fontSize: '0.8125rem' }}>{copy.shortLabel}</p>
                </div>
                <span className={`badge ${statusClass(decision.status)}`}>{decision.status}</span>
              </div>
              <div className="divider" style={{ margin: '0 0 var(--sp-3)' }} />
              <p style={{ marginBottom: 'var(--sp-3)' }}><strong>Why it survived or stalled:</strong> {decision.why}</p>
              <p style={{ marginBottom: 'var(--sp-2)' }}><strong>SDS borrowing:</strong> {copy.sdsBorrowing}</p>
              <p style={{ marginBottom: 'var(--sp-2)' }}><strong>When to use:</strong> {copy.whenToUse}</p>
              <p style={{ marginBottom: 'var(--sp-2)' }}><strong>When not to use:</strong> {copy.whenNotToUse}</p>
              <p style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>{copy.evidence}</p>
            </article>
          ))}
        </div>
      </div>

      <div className="card">
        <h2 style={{ marginBottom: 'var(--sp-2)' }}>Dual-Reservoir Controller</h2>
        <p style={{ marginBottom: 'var(--sp-4)' }}>
          The full controller is strongest in the aggressive learning-rate band, where a plain Adam baseline becomes more brittle. That is the use case that justified promotion.
        </p>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: 'var(--sp-4)' }}>
          <div>
            <div className="section-label">All tested rates</div>
            <SectionTable rows={dualRows} />
            <div className="section-label" style={{ marginTop: 'var(--sp-4)' }}>Aggressive band focus</div>
            <SectionTable rows={dualAggressiveRows} />
          </div>
          <div className="card card-sm" style={{ display: 'flex', flexDirection: 'column', gap: 'var(--sp-3)' }}>
            <div>
              <div className="section-label" style={{ marginBottom: 2 }}>Sample trace</div>
              <p>
                One representative run is shown in SDS state space using the promoted controller at a tuning-sensitive learning rate.
              </p>
            </div>
            <svg viewBox={`0 0 ${TRACE_WIDTH} ${TRACE_HEIGHT}`} style={{ width: '100%', height: 260, background: 'var(--bg-base)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
              <line x1="0" y1={TRACE_HEIGHT} x2={TRACE_WIDTH} y2={TRACE_HEIGHT} stroke="var(--border-default)" />
              <line x1="0" y1="0" x2="0" y2={TRACE_HEIGHT} stroke="var(--border-default)" />
              <polyline fill="none" stroke="var(--blue)" strokeWidth="2" points={statePath} />
              {trace.map((row, index) => {
                const point = stateSpacePosition(row, TRACE_WIDTH, TRACE_HEIGHT);
                const radius = index === 0 || index === trace.length - 1 ? 4.5 : 3;
                return <circle key={`${row.epoch}-${row.regime}`} cx={point.x} cy={point.y} r={radius} fill={regimeColor(row.regime)} opacity={0.95} />;
              })}
            </svg>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: 'var(--sp-3)' }}>
              <div className="stat-box stat-blue">
                <div className="stat-label">Start → End</div>
                <div className="stat-value" style={{ fontSize: '0.9375rem' }}>{startPoint.regime} → {endPoint.regime}</div>
                <div className="stat-sub">x from {formatNumber(startPoint.x, 3)} to {formatNumber(endPoint.x, 3)}</div>
              </div>
              <div className="stat-box stat-teal">
                <div className="stat-label">Peak Efficiency</div>
                <div className="stat-value">{formatNumber(Math.max(...trace.map((row) => row.efficiency)), 3)}</div>
                <div className="stat-sub">Useful imbalance peak {formatNumber(Math.max(...trace.map((row) => row.useful_imbalance)), 3)}</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="card">
        <h2 style={{ marginBottom: 'var(--sp-2)' }}>Deficit-Driven Scheduler</h2>
        <p style={{ marginBottom: 'var(--sp-4)' }}>
          This scheduler earned promotion because it stayed competitive with plateau scheduling while being easier to interpret in SDS terms: a falling useful imbalance means the process is losing productive separation between pressure and reserve.
        </p>
        <SectionTable rows={schedulerRows} />
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: 'var(--sp-4)' }}>
        <div className="card">
          <h2 style={{ marginBottom: 'var(--sp-2)' }}>State-Space Monitor</h2>
          <p style={{ marginBottom: 'var(--sp-4)' }}>
            The monitor remains useful as an interpretation layer, but it is still experimental because the current benchmark shows raw loss slope predicting short-horizon validation improvement more strongly.
          </p>
          <div className="stat-grid" style={{ marginBottom: 'var(--sp-4)' }}>
            <div className="stat-box stat-blue">
              <div className="stat-label">Monitor ρ</div>
              <div className="stat-value">{formatNumber(SDS_TOOLS_SNAPSHOT.monitorSummary.monitor_rho, 3)}</div>
              <div className="stat-sub">Spearman correlation to 5-epoch future gain</div>
            </div>
            <div className="stat-box stat-amber">
              <div className="stat-label">Loss-slope ρ</div>
              <div className="stat-value">{formatNumber(SDS_TOOLS_SNAPSHOT.monitorSummary.raw_loss_slope_rho, 3)}</div>
              <div className="stat-sub">Current baseline diagnostic</div>
            </div>
          </div>
          <div className="section-label">Useful imbalance over time</div>
          <svg viewBox="0 0 620 140" style={{ width: '100%', height: 160, background: 'var(--bg-base)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
            <polyline fill="none" stroke="var(--teal)" strokeWidth="2.25" points={usefulImbalanceSeries} />
          </svg>
          <p style={{ marginTop: 'var(--sp-3)' }}>
            Practical reading: high useful imbalance tends to mean the run is still exploiting a productive asymmetry; low useful imbalance with rising stall score suggests the process is settling into an endpoint-like regime.
          </p>
        </div>

        <div className="card">
          <h2 style={{ marginBottom: 'var(--sp-2)' }}>Equilibrium Early Stopping</h2>
          <p style={{ marginBottom: 'var(--sp-4)' }}>
            The stopping logic works and is explainable, but it did not save enough compute without tradeoff to displace simpler baselines yet.
          </p>
          <SectionTable rows={earlyRows} />
        </div>
      </div>

      <div className="card">
        <h2 style={{ marginBottom: 'var(--sp-2)' }}>One-Parameter Control Family</h2>
        <p style={{ marginBottom: 'var(--sp-4)' }}>
          This is the cleanest educational translation of the one-parameter SDS state idea: one control variable x drives several optimizer knobs at once. It remains experimental because its best preset is still {formatPercent(controlGap, 1)} above the best manual three-knob grid point on the current regression benchmark.
        </p>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: 'var(--sp-4)', marginBottom: 'var(--sp-4)' }}>
          <CurveChart
            points={SDS_TOOLS_SNAPSHOT.controlCurve}
            field="lr_scale"
            title="Learning-rate scale"
            color="var(--blue)"
            formatter={(value) => value.toFixed(3)}
          />
          <CurveChart
            points={SDS_TOOLS_SNAPSHOT.controlCurve}
            field="beta1"
            title="Momentum / beta1"
            color="var(--teal)"
            formatter={(value) => value.toFixed(3)}
          />
          <CurveChart
            points={SDS_TOOLS_SNAPSHOT.controlCurve}
            field="weight_decay_scale"
            title="Weight-decay scale"
            color="var(--amber)"
            formatter={(value) => value.toFixed(3)}
          />
          <CurveChart
            points={SDS_TOOLS_SNAPSHOT.controlCurve}
            field="noise_scale"
            title="Noise scale"
            color="var(--violet)"
            formatter={(value) => value.toFixed(4)}
          />
        </div>
        <div className="section-label">Preset comparison</div>
        <SectionTable rows={[...controlOverview.presets, controlOverview.bestGrid]} />
      </div>

      <div className="card">
        <h2 style={{ marginBottom: 'var(--sp-2)' }}>Exports</h2>
        <p style={{ marginBottom: 'var(--sp-4)' }}>
          Export the benchmark decisions and one representative controller trace directly from the workbench. These exports are generated from the current benchmark snapshot checked into the repository.
        </p>
        <div style={{ display: 'flex', gap: 'var(--sp-2)', flexWrap: 'wrap', marginBottom: 'var(--sp-4)' }}>
          <button className="btn btn-primary" onClick={() => downloadFile(buildToolsSnapshotJson(), 'sds-tools-snapshot.json', 'application/json')}>
            Download Snapshot JSON
          </button>
          <button className="btn" onClick={() => downloadFile(buildToolsDecisionsCsv(), 'sds-tools-decisions.csv', 'text/csv')}>
            Download Decisions CSV
          </button>
          <button className="btn" onClick={() => downloadFile(buildSampleTraceCsv(), 'sds-tools-sample-trace.csv', 'text/csv')}>
            Download Sample Trace CSV
          </button>
          <CopyButton text={buildToolsSnapshotJson()} label="Copy Snapshot JSON" />
          <CopyButton text={buildToolsDecisionsCsv()} label="Copy Decisions CSV" />
        </div>
        <p>
          Recommended path: start with the dual-reservoir controller or deficit-driven scheduler, then use the monitor and one-parameter family as interpretive or exploratory layers rather than default replacements for simpler baselines.
        </p>
      </div>
    </div>
  );
}
