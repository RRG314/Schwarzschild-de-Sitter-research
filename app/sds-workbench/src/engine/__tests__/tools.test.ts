import { describe, expect, test } from 'vitest';
import {
  buildSampleTraceCsv,
  buildToolsDecisionsCsv,
  dualReservoirAggressiveBand,
  schedulerOverview,
  SDS_TOOLS_SNAPSHOT,
  toolDecisionEntries,
} from '../tools';

describe('SDS-inspired tools snapshot helpers', () => {
  test('promotion decisions keep recommended tools visible', () => {
    const decisions = toolDecisionEntries();
    expect(decisions.find((entry) => entry.id === 'dual_reservoir_controller')?.decision.status).toBe('recommended');
    expect(decisions.find((entry) => entry.id === 'deficit_driven_scheduler')?.decision.status).toBe('recommended');
    expect(decisions.find((entry) => entry.id === 'state_space_monitor')?.decision.status).toBe('experimental');
  });

  test('aggressive-band dual reservoir summary improves on baseline', () => {
    const rows = dualReservoirAggressiveBand();
    const baseline = rows.find((row) => row.label.startsWith('Adam'));
    const full = rows.find((row) => row.label.startsWith('Full'));
    expect(baseline).toBeDefined();
    expect(full).toBeDefined();
    expect(full!.bestValLoss).toBeLessThan(baseline!.bestValLoss);
  });

  test('scheduler overview includes deficit-driven scheduler and export helpers serialize', () => {
    const scheduler = schedulerOverview();
    expect(scheduler.some((row) => row.label === 'Deficit-driven scheduler')).toBe(true);
    expect(buildToolsDecisionsCsv()).toContain('dual_reservoir_controller');
    expect(buildSampleTraceCsv()).toContain('useful_imbalance');
    expect(SDS_TOOLS_SNAPSHOT.sampleTrace.length).toBeGreaterThan(10);
  });
});
