import { SDSState } from './types';

export function computeState(x: number, lambda: number): SDSState {
  const PI = Math.PI;
  const denom = x * x + x + 1;
  const r_lambda = Math.sqrt(3 / lambda);
  const r_c = r_lambda / Math.sqrt(denom);
  const r_b = x * r_c;
  const M = (r_b / 2) * (1 - (lambda * r_b * r_b) / 3);
  const M_nariai = 1 / (3 * Math.sqrt(lambda));

  const S_lambda = (3 * PI) / lambda;
  const S_b = PI * r_b * r_b;
  const S_c = PI * r_c * r_c;
  const Delta = PI * r_b * r_c;

  const fb = (x * x) / denom;
  const fc = 1 / denom;
  const fDelta = x / denom;

  const u = x / Math.sqrt(denom);
  const v = 1 / Math.sqrt(denom);

  const T_b = (1 - lambda * r_b * r_b) / (4 * PI * r_b);
  const T_c = (lambda * r_c * r_c - 1) / (4 * PI * r_c);
  const T_ratio = (x * (x + 2)) / (1 + 2 * x);
  const eta_C = (1 - x * x) / (1 + 2 * x);

  const res_eisenstein = r_b * r_b + r_b * r_c + r_c * r_c - 3 / lambda;
  const res_entropy = S_lambda - S_b - S_c - Delta;
  const res_arc = u * u + u * v + v * v - 1;
  const res_Tratio = T_c / T_b - T_ratio;

  return {
    x, lambda, r_lambda, r_c, r_b, M, M_nariai,
    S_lambda, S_b, S_c, Delta,
    fb, fc, fDelta, u, v,
    T_b, T_c, T_ratio, eta_C,
    res_eisenstein, res_entropy, res_arc, res_Tratio,
  };
}

export function computeStateFromMass(lambda: number, M: number): SDSState | null {
  const M_nariai = 1 / (3 * Math.sqrt(lambda));
  if (M <= 0 || M >= M_nariai) return null;
  const r_b_max = 1 / Math.sqrt(lambda);
  let lo = 1e-10, hi = r_b_max * 0.9999;
  for (let i = 0; i < 80; i++) {
    const mid = (lo + hi) / 2;
    const M_mid = (mid / 2) * (1 - lambda * mid * mid / 3);
    if (M_mid < M) lo = mid; else hi = mid;
  }
  const r_b = (lo + hi) / 2;
  const disc = 12 / lambda - 3 * r_b * r_b;
  if (disc < 0) return null;
  const r_c = (-r_b + Math.sqrt(disc)) / 2;
  if (r_c <= r_b) return null;
  const x = r_b / r_c;
  if (x <= 0 || x >= 1) return null;
  return computeState(x, lambda);
}

export function computeStateFromDeltaFrac(lambda: number, deltaFrac: number): SDSState | null {
  const maxDelta = 1 / 3 - 1e-6;
  if (deltaFrac <= 0 || deltaFrac >= maxDelta) return null;
  const d = deltaFrac;
  const disc = 1 - 2 * d - 3 * d * d;
  if (disc < 0) return null;
  const x = (1 - d - Math.sqrt(disc)) / (2 * d);
  if (x <= 0 || x >= 1) return null;
  return computeState(x, lambda);
}

export const PRESETS = {
  pureDeSitter: { x: 0.02, label: 'Near pure de Sitter', description: 'x → 0: tiny black hole, almost pure de Sitter' },
  midpoint: { x: 0.45, label: 'Midpoint', description: 'A balanced demo state' },
  nearNariai: { x: 0.95, label: 'Near Nariai', description: 'x → 1: horizons nearly merged' },
  quarter: { x: 0.25, label: 'x = 0.25', description: 'Small black hole regime' },
};
