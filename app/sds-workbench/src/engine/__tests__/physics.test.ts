import { describe, expect, test } from 'vitest';
import { computeState, computeStateFromMass } from '../physics';

const EPS = 1e-10;

describe('SdS exact engine identities', () => {
  test('x parametrization and entropy identity hold', () => {
    const state = computeState(0.37, 1.25);
    expect(state.r_b / state.r_c).toBeCloseTo(state.x, 12);
    expect(state.S_lambda - state.S_b - state.S_c - state.Delta).toBeCloseTo(0, 10);
    expect(Math.abs(state.res_eisenstein)).toBeLessThan(EPS);
    expect(Math.abs(state.res_entropy)).toBeLessThan(EPS);
  });

  test('temperature ratio and Carnot efficiency formulas are consistent', () => {
    const state = computeState(0.61, 0.8);
    const ratioFormula = (state.x * (state.x + 2)) / (1 + 2 * state.x);
    const etaFormula = (1 - state.x * state.x) / (1 + 2 * state.x);

    expect(state.T_ratio).toBeCloseTo(ratioFormula, 12);
    expect(state.eta_C).toBeCloseTo(etaFormula, 12);
    expect(state.T_c / state.T_b).toBeCloseTo(state.T_ratio, 10);
  });

  test('mass inversion returns original state family point', () => {
    const original = computeState(0.42, 1.7);
    const reconstructed = computeStateFromMass(original.lambda, original.M);

    expect(reconstructed).not.toBeNull();
    expect(reconstructed?.x).toBeCloseTo(original.x, 9);
    expect(reconstructed?.r_b).toBeCloseTo(original.r_b, 9);
    expect(reconstructed?.r_c).toBeCloseTo(original.r_c, 9);
  });
});
