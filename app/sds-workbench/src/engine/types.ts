export interface SDSState {
  x: number;
  lambda: number;
  r_lambda: number;
  r_c: number;
  r_b: number;
  M: number;
  M_nariai: number;
  S_lambda: number;
  S_b: number;
  S_c: number;
  Delta: number;
  fb: number;
  fc: number;
  fDelta: number;
  u: number;
  v: number;
  T_b: number;
  T_c: number;
  T_ratio: number;
  eta_C: number;
  res_eisenstein: number;
  res_entropy: number;
  res_arc: number;
  res_Tratio: number;
}

export interface SavedState {
  id: string;
  name: string;
  x: number;
  lambda: number;
  createdAt: number;
}

export type TabId = 'explore' | 'geometry' | 'thermo' | 'evolution' | 'compare' | 'export';
export type Mode = 'beginner' | 'technical';
export type InputMode = 'x' | 'mass' | 'delta';

export type EvolutionDirection = 'evaporation' | 'injection';

export interface EvolutionConfig {
  k: number;
  dt: number;
  steps: number;
  direction: EvolutionDirection;
}

export interface EvolutionPoint {
  index: number;
  t: number;
  M: number;
  x: number;
  r_b: number;
  r_c: number;
  S_b: number;
  S_c: number;
  Delta: number;
  T_b: number;
  T_c: number;
  eta_C: number;
}

export interface EvolutionRun {
  lambda: number;
  initialMass: number;
  initialX: number;
  config: EvolutionConfig;
  points: EvolutionPoint[];
  terminatedEarly: boolean;
  terminationReason: string | null;
}
