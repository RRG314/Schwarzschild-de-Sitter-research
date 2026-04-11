import { useAppStore } from '../../store/appStore';
import { exportStateAsJson, exportStateAsCsv, exportSweepAsCsv, exportComparisonAsCsv, downloadFile } from '../../utils/export';
import { encodeUrl } from '../../utils/url';
import { CopyButton } from '../ui/CopyButton';
import { fmt } from '../../engine/format';

export function ExportTab() {
  const { state, compareA, compareB, x, lambda, activeTab, mode } = useAppStore();

  const shareUrl = encodeUrl({ x, lambda, tab: activeTab, mode });
  const jsonStr = exportStateAsJson(state);
  const csvStr = exportStateAsCsv(state);

  return (
    <div className="tab-content">
      <div className="card">
        <h2 style={{ marginBottom: 'var(--sp-2)' }}>Shareable Link</h2>
        <p style={{ marginBottom: 'var(--sp-4)' }}>
          This URL encodes the current state (x, Λ, active tab, mode). Anyone opening it will see exactly this state.
        </p>
        <div style={{ display: 'flex', gap: 'var(--sp-2)', flexWrap: 'wrap' }}>
          <input className="input" readOnly value={shareUrl} style={{ flex: 1, fontSize: '0.75rem', fontFamily: 'var(--font-mono)' }} />
          <CopyButton text={shareUrl} label="Copy URL" />
        </div>
      </div>

      <div className="card">
        <h2 style={{ marginBottom: 'var(--sp-4)' }}>Export Current State</h2>
        <div style={{ display: 'flex', gap: 'var(--sp-3)', flexWrap: 'wrap', marginBottom: 'var(--sp-4)' }}>
          <CopyButton text={jsonStr} label="Copy JSON" />
          <button className="btn" onClick={() => downloadFile(jsonStr, `sds-state-x${x.toFixed(3)}.json`, 'application/json')}>Download JSON</button>
          <CopyButton text={csvStr} label="Copy CSV" />
          <button className="btn" onClick={() => downloadFile(csvStr, `sds-state-x${x.toFixed(3)}.csv`, 'text/csv')}>Download CSV</button>
        </div>
        <pre style={{ background: 'var(--bg-base)', borderRadius: 'var(--radius-sm)', padding: 'var(--sp-4)', fontSize: '0.75rem', fontFamily: 'var(--font-mono)', color: 'var(--teal-text)', overflowX: 'auto', maxHeight: 200, overflowY: 'auto', border: '1px solid var(--border-subtle)' }}>
          {jsonStr}
        </pre>
      </div>

      <div className="card">
        <h2 style={{ marginBottom: 'var(--sp-2)' }}>Parameter Sweep Export</h2>
        <p style={{ marginBottom: 'var(--sp-4)' }}>
          Exports all derived quantities for 100 evenly-spaced values of x from 0.01 to 0.99 at the current Λ = {fmt(lambda)}.
        </p>
        <div style={{ display: 'flex', gap: 'var(--sp-3)' }}>
          <button className="btn btn-primary" onClick={() => {
            const csv = exportSweepAsCsv(lambda, 100);
            downloadFile(csv, `sds-sweep-lambda${lambda.toFixed(2)}.csv`, 'text/csv');
          }}>Download Sweep CSV</button>
          <CopyButton text={exportSweepAsCsv(lambda, 20)} label="Copy (20 pts)" />
        </div>
      </div>

      {compareA && compareB ? (
        <div className="card">
          <h2 style={{ marginBottom: 'var(--sp-4)' }}>Export Comparison (A vs B)</h2>
          <div style={{ display: 'flex', gap: 'var(--sp-3)' }}>
            <button className="btn" onClick={() => {
              const csv = exportComparisonAsCsv(compareA, compareB);
              downloadFile(csv, 'sds-comparison.csv', 'text/csv');
            }}>Download Comparison CSV</button>
            <CopyButton text={exportComparisonAsCsv(compareA, compareB)} label="Copy Comparison" />
          </div>
        </div>
      ) : (
        <div className="card">
          <h2 style={{ marginBottom: 'var(--sp-2)' }}>Comparison Export</h2>
          <p>Pin two states in the Compare tab, then return here to export the comparison table.</p>
        </div>
      )}
    </div>
  );
}
