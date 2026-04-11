import { SavedState } from '../engine/types';

const KEY = 'sds-saved-states';

export function loadSavedStates(): SavedState[] {
  try {
    const raw = localStorage.getItem(KEY);
    if (!raw) return [];
    return JSON.parse(raw) as SavedState[];
  } catch { return []; }
}

export function saveSavedStates(states: SavedState[]): void {
  try { localStorage.setItem(KEY, JSON.stringify(states)); } catch {}
}

export function addSavedState(states: SavedState[], name: string, x: number, lambda: number): SavedState[] {
  const next: SavedState = {
    id: crypto.randomUUID(),
    name,
    x,
    lambda,
    createdAt: Date.now(),
  };
  const updated = [next, ...states].slice(0, 20);
  saveSavedStates(updated);
  return updated;
}

export function deleteSavedState(states: SavedState[], id: string): SavedState[] {
  const updated = states.filter(s => s.id !== id);
  saveSavedStates(updated);
  return updated;
}

export function renameSavedState(states: SavedState[], id: string, name: string): SavedState[] {
  const updated = states.map(s => s.id === id ? { ...s, name } : s);
  saveSavedStates(updated);
  return updated;
}
