import rawSnapshot from '../data/sdsToolsSnapshot.json';

export type ToolStatus = 'recommended' | 'experimental' | 'archived';
export type ToolId =
  | 'dual_reservoir_controller'
  | 'deficit_driven_scheduler'
  | 'state_space_monitor'
  | 'equilibrium_early_stopping'
  | 'one_parameter_control_family';

export interface ToolDecision {
  status: ToolStatus;
  why: string;
}

export interface SummaryRow {
  task: string;
  variant: string;
  seed: number;
  final_train_loss: number;
  final_val_loss: number;
  best_val_loss: number;
  final_accuracy: number | null;
  best_accuracy: number | null;
  epochs_run: number;
  diverged: boolean;
  stop_reason: string | null;
}

export interface MonitorSummary {
  metric: string;
  monitor_rho: number;
  raw_loss_slope_rho: number;
  advantage: number;
}

export interface SampleTraceRow {
  epoch: number;
  train_loss: number;
  val_loss: number;
  grad_norm: number;
  step_norm: number;
  hot_reservoir: number;
  cold_reservoir: number;
  deficit: number;
  total_budget: number;
  x: number;
  efficiency: number;
  useful_imbalance: number;
  instability_score: number;
  stall_score: number;
  loss_volatility: number;
  generalization_gap: number;
  regime: 'productive' | 'transition' | 'equilibrium' | 'unstable';
  variant: string;
  task: string;
  seed: number;
  train_accuracy: number | null;
  val_accuracy: number | null;
  batch_loss_mean: number;
  scheduler_scale: number;
  lr_multiplier: number;
  beta1: number;
  weight_decay_multiplier: number;
  effective_lr: number;
}

export interface ControlCurvePoint {
  mode: string;
  x: number;
  lr_scale: number;
  beta1: number;
  weight_decay_scale: number;
  noise_scale: number;
  hot_fraction: number;
  cold_fraction: number;
  deficit_fraction: number;
}

export interface ToolsSnapshot {
  promotionDecisions: Record<ToolId, ToolDecision>;
  schedulerSummary: SummaryRow[];
  dualReservoirSummary: SummaryRow[];
  earlyStoppingSummary: SummaryRow[];
  controlFamilySummary: SummaryRow[];
  monitorSummary: MonitorSummary;
  sampleTrace: SampleTraceRow[];
  controlCurve: ControlCurvePoint[];
}

export interface ToolCopy {
  title: string;
  shortLabel: string;
  sdsBorrowing: string;
  whenToUse: string;
  whenNotToUse: string;
  evidence: string;
}

export interface AggregateRow {
  label: string;
  bestValLoss: number;
  finalValLoss: number;
  bestAccuracy: number | null;
  finalAccuracy: number | null;
  epochsRun: number;
  divergedRate: number;
  count: number;
}

const snapshot = rawSnapshot as ToolsSnapshot;

export const SDS_TOOLS_SNAPSHOT = snapshot;

export const TOOL_COPY: Record<ToolId, ToolCopy> = {
  dual_reservoir_controller: {
    title: 'Dual-Reservoir Controller',
    shortLabel: 'Optimizer control for brittle learning-rate bands',
    sdsBorrowing: 'Two coupled reservoirs, a deficit term, and an efficiency-like imbalance score drive optimizer damping.',
    whenToUse: 'Use it when training becomes tuning-sensitive or starts oscillating under more aggressive update scales.',
    whenNotToUse: 'Skip it when a simple baseline already trains stably at your chosen learning rate.',
    evidence: 'Empirical engineering tool. The SDS structure is borrowed; the benchmark result is practical rather than theorem-level.',
  },
  deficit_driven_scheduler: {
    title: 'Deficit-Driven Scheduler',
    shortLabel: 'Drop-in scheduler for plateau and instability handling',
    sdsBorrowing: 'A useful-imbalance deficit signal replaces epoch-count heuristics as the scheduling trigger.',
    whenToUse: 'Use it when you want a scheduler that reacts to coupled progress/stability signals instead of just elapsed time.',
    whenNotToUse: 'Skip it when cosine or plateau decay already behaves well enough for the task and no extra interpretability is needed.',
    evidence: 'Empirical engineering tool benchmarked against constant, cosine, step, and plateau schedules.',
  },
  state_space_monitor: {
    title: 'State-Space Monitor',
    shortLabel: 'Low-dimensional diagnostic view of iterative behavior',
    sdsBorrowing: 'Training traces are mapped into a reduced state via reservoir balance, deficit, and efficiency coordinates.',
    whenToUse: 'Use it when you want a readable diagnostic story that goes beyond raw loss plots.',
    whenNotToUse: 'Do not treat it as a default predictor of future improvement yet; the current benchmark does not support that promotion.',
    evidence: 'Empirical diagnostic. Helpful for interpretation, not yet strong enough to replace simpler signals.',
  },
  equilibrium_early_stopping: {
    title: 'Equilibrium Early Stopping',
    shortLabel: 'Stop when useful imbalance collapses',
    sdsBorrowing: 'Stopping is tied to loss of productive imbalance rather than only patience or flat validation loss.',
    whenToUse: 'Use it as an alternate stopper when you want a physically motivated explanation of why the run is no longer productive.',
    whenNotToUse: 'Do not make it the default stopper yet; compute savings were not strong enough in the current benchmark.',
    evidence: 'Empirical callback benchmarked against fixed epochs, patience, and loss-change stopping.',
  },
  one_parameter_control_family: {
    title: 'One-Parameter Control Family',
    shortLabel: 'Collapse multiple knobs onto one master SDS-style state',
    sdsBorrowing: 'A single reduced parameter x controls learning rate, momentum, decay, and noise through coupled budget fractions.',
    whenToUse: 'Use it when you want a compact control surface for quick experiments or educational inspection.',
    whenNotToUse: 'Do not use it as the main tuned path when you can afford a richer manual search.',
    evidence: 'Empirical convenience layer. It reduces tuning burden, but it did not yet match the best manual grid closely enough.',
  },
};

function mean(values: number[]): number {
  if (!values.length) return Number.NaN;
  return values.reduce((acc, value) => acc + value, 0) / values.length;
}

function meanNullable(values: Array<number | null>): number | null {
  const filtered = values.filter((value): value is number => typeof value === 'number');
  return filtered.length ? mean(filtered) : null;
}

function aggregateRows(rows: SummaryRow[]): AggregateRow {
  return {
    label: '',
    bestValLoss: mean(rows.map((row) => row.best_val_loss)),
    finalValLoss: mean(rows.map((row) => row.final_val_loss)),
    bestAccuracy: meanNullable(rows.map((row) => row.best_accuracy)),
    finalAccuracy: meanNullable(rows.map((row) => row.final_accuracy)),
    epochsRun: mean(rows.map((row) => row.epochs_run)),
    divergedRate: mean(rows.map((row) => (row.diverged ? 1 : 0))),
    count: rows.length,
  };
}

function withLabel(label: string, rows: SummaryRow[]): AggregateRow {
  return { ...aggregateRows(rows), label };
}

function rowsWithPrefix(rows: SummaryRow[], prefix: string): SummaryRow[] {
  return rows.filter((row) => row.variant.startsWith(prefix));
}

function rowsWithVariant(rows: SummaryRow[], variant: string): SummaryRow[] {
  return rows.filter((row) => row.variant === variant);
}

export function toolDecisionEntries(): Array<{ id: ToolId; decision: ToolDecision; copy: ToolCopy }> {
  const rank: Record<ToolStatus, number> = { recommended: 0, experimental: 1, archived: 2 };
  return (Object.entries(snapshot.promotionDecisions) as Array<[ToolId, ToolDecision]>)
    .map(([id, decision]) => ({ id, decision, copy: TOOL_COPY[id] }))
    .sort((a, b) => rank[a.decision.status] - rank[b.decision.status] || a.copy.title.localeCompare(b.copy.title));
}

export function dualReservoirOverview(): AggregateRow[] {
  const rows = snapshot.dualReservoirSummary;
  return [
    withLabel('Adam baseline', rowsWithPrefix(rows, 'adam@')),
    withLabel('Efficiency-only ablation', rowsWithPrefix(rows, 'efficiency_only@')),
    withLabel('Full dual-reservoir controller', rowsWithPrefix(rows, 'dual_reservoir@')),
  ];
}

export function dualReservoirAggressiveBand(): AggregateRow[] {
  const rows = snapshot.dualReservoirSummary.filter((row) => row.variant.endsWith('@0.30') || row.variant.endsWith('@0.60'));
  return [
    withLabel('Adam baseline (0.30-0.60)', rowsWithPrefix(rows, 'adam@')),
    withLabel('Efficiency-only (0.30-0.60)', rowsWithPrefix(rows, 'efficiency_only@')),
    withLabel('Full controller (0.30-0.60)', rowsWithPrefix(rows, 'dual_reservoir@')),
  ];
}

export function schedulerOverview(): AggregateRow[] {
  const rows = snapshot.schedulerSummary;
  return [
    withLabel('Constant LR', rowsWithVariant(rows, 'constant')),
    withLabel('Cosine decay', rowsWithVariant(rows, 'cosine')),
    withLabel('Step decay', rowsWithVariant(rows, 'step')),
    withLabel('Reduce on plateau', rowsWithVariant(rows, 'plateau')),
    withLabel('Deficit-driven scheduler', rowsWithVariant(rows, 'deficit')),
  ].sort((a, b) => a.bestValLoss - b.bestValLoss);
}

export function earlyStoppingOverview(): AggregateRow[] {
  const rows = snapshot.earlyStoppingSummary;
  return [
    withLabel('Fixed epochs', rowsWithVariant(rows, 'fixed_epochs')),
    withLabel('Patience', rowsWithVariant(rows, 'patience')),
    withLabel('Loss-change threshold', rowsWithVariant(rows, 'loss_change')),
    withLabel('Equilibrium threshold', rowsWithVariant(rows, 'equilibrium_threshold')),
    withLabel('Equilibrium relative peak', rowsWithVariant(rows, 'equilibrium_relative_peak')),
    withLabel('Equilibrium smoothed', rowsWithVariant(rows, 'equilibrium_smoothed')),
  ].sort((a, b) => a.bestValLoss - b.bestValLoss);
}

export function controlFamilyOverview(): { presets: AggregateRow[]; bestGrid: AggregateRow } {
  const rows = snapshot.controlFamilySummary;
  const presets = [
    withLabel('Conservative preset', rowsWithVariant(rows, 'control_conservative')),
    withLabel('Balanced preset', rowsWithVariant(rows, 'control_balanced')),
    withLabel('Aggressive preset', rowsWithVariant(rows, 'control_aggressive')),
  ].sort((a, b) => a.bestValLoss - b.bestValLoss);

  const gridRows = rows.filter((row) => row.variant.startsWith('grid_'));
  const bestGridValue = Math.min(...gridRows.map((row) => row.best_val_loss));
  const bestGridRows = gridRows.filter((row) => row.best_val_loss === bestGridValue);

  return {
    presets,
    bestGrid: withLabel('Best manual three-knob grid point', bestGridRows),
  };
}

function recordsToCsv(records: Array<Record<string, string>>): string {
  if (!records.length) return '';
  const headers = Object.keys(records[0]);
  const lines = records.map((record) => headers.map((header) => record[header]).join(','));
  return [headers.join(','), ...lines].join('\n');
}

export function buildToolsDecisionsCsv(): string {
  return recordsToCsv(
    toolDecisionEntries().map(({ id, decision, copy }) => ({
      tool_id: id,
      title: copy.title,
      status: decision.status,
      reason: decision.why,
      sds_borrowing: copy.sdsBorrowing,
      when_to_use: copy.whenToUse,
      when_not_to_use: copy.whenNotToUse,
      evidence: copy.evidence,
    }))
  );
}

export function buildToolsSnapshotJson(): string {
  return JSON.stringify(snapshot, null, 2);
}

export function buildSampleTraceCsv(): string {
  return recordsToCsv(
    snapshot.sampleTrace.map((row) => {
      const record: Record<string, string> = {};
      for (const [key, value] of Object.entries(row)) {
        record[key] = typeof value === 'number' ? value.toString() : String(value);
      }
      return record;
    })
  );
}
