import { describe, expect, test } from 'vitest';
import { buildEvolutionTrajectory } from '../evolution';
import { computeState } from '../physics';

function isMonotone(values: number[], direction: 'nondecreasing' | 'nonincreasing'): boolean {
  for (let i = 1; i < values.length; i++) {
    if (direction === 'nondecreasing' && values[i] < values[i - 1]) return false;
    if (direction === 'nonincreasing' && values[i] > values[i - 1]) return false;
  }
  return true;
}

describe('Evolution engine', () => {
  test('evaporation trajectory is stable and mass decreases monotonically', () => {
    const initial = computeState(0.48, 1.0);
    const run = buildEvolutionTrajectory(initial, {
      direction: 'evaporation',
      k: 0.0006,
      dt: 1,
      steps: 120,
    });

    expect(run.points.length).toBeGreaterThan(10);
    expect(isMonotone(run.points.map((p) => p.M), 'nonincreasing')).toBe(true);
    expect(run.points.every((p) => p.x > 0 && p.x < 1)).toBe(true);
    expect(run.points.every((p) => Number.isFinite(p.eta_C))).toBe(true);
  });

  test('reverse flow increases mass while staying below the Nariai cap', () => {
    const initial = computeState(0.2, 1.0);
    const run = buildEvolutionTrajectory(initial, {
      direction: 'injection',
      k: 0.0006,
      dt: 1,
      steps: 120,
    });

    const masses = run.points.map((p) => p.M);
    expect(isMonotone(masses, 'nondecreasing')).toBe(true);
    expect(Math.max(...masses)).toBeLessThan(initial.M_nariai);
  });
});
