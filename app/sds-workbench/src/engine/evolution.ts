import { computeStateFromMass } from './physics';
import { EvolutionConfig, EvolutionDirection, EvolutionPoint, EvolutionRun, SDSState } from './types';

const MIN_MASS_RATIO = 1e-6;
const MAX_MASS_RATIO = 0.999999;
const MIN_K = 1e-12;
const MIN_DT = 1e-6;

function clamp(value: number, min: number, max: number): number {
  return Math.max(min, Math.min(max, value));
}

function nextMassByCubicStep(mass: number, dt: number, k: number, direction: EvolutionDirection): number {
  const signed = direction === 'evaporation' ? -1 : 1;
  const nextCubic = mass * mass * mass + signed * 3 * k * dt;
  return nextCubic > 0 ? Math.cbrt(nextCubic) : 0;
}

function asPoint(index: number, t: number, state: SDSState): EvolutionPoint {
  return {
    index,
    t,
    M: state.M,
    x: state.x,
    r_b: state.r_b,
    r_c: state.r_c,
    S_b: state.S_b,
    S_c: state.S_c,
    Delta: state.Delta,
    T_b: state.T_b,
    T_c: state.T_c,
    eta_C: state.eta_C,
  };
}

export function buildEvolutionTrajectory(initialState: SDSState, config: EvolutionConfig): EvolutionRun {
  const lambda = initialState.lambda;
  const safeK = Math.max(config.k, MIN_K);
  const safeDt = Math.max(config.dt, MIN_DT);
  const maxSteps = Math.max(1, Math.floor(config.steps));

  const minMass = Math.max(initialState.M_nariai * MIN_MASS_RATIO, MIN_MASS_RATIO);
  const maxMass = initialState.M_nariai * MAX_MASS_RATIO;

  let mass = clamp(initialState.M, minMass, maxMass);
  let terminatedEarly = false;
  let terminationReason: string | null = null;

  const points: EvolutionPoint[] = [];

  for (let i = 0; i <= maxSteps; i++) {
    const state = i === 0 ? initialState : computeStateFromMass(lambda, mass);
    if (!state) {
      terminatedEarly = true;
      terminationReason = 'Failed to reconstruct a physical SdS state from evolved mass.';
      break;
    }

    points.push(asPoint(i, i * safeDt, state));
    if (i === maxSteps) break;

    const nextMass = clamp(nextMassByCubicStep(mass, safeDt, safeK, config.direction), minMass, maxMass);

    if (config.direction === 'evaporation' && nextMass <= minMass * 1.001) {
      mass = nextMass;
      terminatedEarly = true;
      terminationReason = 'Evaporation reached the configured minimum mass floor.';
      continue;
    }

    if (config.direction === 'injection' && nextMass >= maxMass * 0.999) {
      mass = nextMass;
      terminatedEarly = true;
      terminationReason = 'Injection reached the Nariai safety cap.';
      continue;
    }

    mass = nextMass;
  }

  return {
    lambda,
    initialMass: initialState.M,
    initialX: initialState.x,
    config: {
      k: safeK,
      dt: safeDt,
      steps: maxSteps,
      direction: config.direction,
    },
    points,
    terminatedEarly,
    terminationReason,
  };
}
