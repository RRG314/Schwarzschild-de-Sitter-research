import { create } from 'zustand';
import { SDSState, SavedState, TabId, Mode, InputMode } from '../engine/types';
import { computeState } from '../engine/physics';
import { loadSavedStates, addSavedState, deleteSavedState, renameSavedState } from '../utils/storage';
import { pushUrl, decodeUrl } from '../utils/url';

interface AppStore {
  x: number;
  lambda: number;
  state: SDSState;
  activeTab: TabId;
  mode: Mode;
  inputMode: InputMode;
  sidebarOpen: boolean;
  isSweeping: boolean;
  sweepSpeed: number;
  savedStates: SavedState[];
  compareA: SDSState | null;
  compareB: SDSState | null;
  setX: (x: number) => void;
  setLambda: (lambda: number) => void;
  setTab: (tab: TabId) => void;
  setMode: (mode: Mode) => void;
  setInputMode: (m: InputMode) => void;
  toggleSidebar: () => void;
  setSweeping: (v: boolean) => void;
  setSweepSpeed: (v: number) => void;
  saveCurrentState: (name: string) => void;
  deleteState: (id: string) => void;
  renameState: (id: string, name: string) => void;
  loadSavedState: (s: SavedState) => void;
  setCompareA: (s: SDSState | null) => void;
  setCompareB: (s: SDSState | null) => void;
  pinCurrentAsA: () => void;
  pinCurrentAsB: () => void;
}

function clampX(x: number) { return Math.max(0.005, Math.min(0.995, x)); }
function clampL(l: number) { return Math.max(0.01, Math.min(10, l)); }

const urlState = decodeUrl();

const initX = clampX(urlState.x ?? 0.45);
const initL = clampL(urlState.lambda ?? 1.0);

export const useAppStore = create<AppStore>((set, get) => ({
  x: initX,
  lambda: initL,
  state: computeState(initX, initL),
  activeTab: urlState.tab ?? 'explore',
  mode: urlState.mode ?? 'beginner',
  inputMode: 'x',
  sidebarOpen: true,
  isSweeping: false,
  sweepSpeed: 10,
  savedStates: loadSavedStates(),
  compareA: null,
  compareB: null,

  setX: (x) => {
    const clamped = clampX(x);
    const state = computeState(clamped, get().lambda);
    set({ x: clamped, state });
    pushUrl({ x: clamped, lambda: get().lambda, tab: get().activeTab, mode: get().mode });
  },
  setLambda: (lambda) => {
    const clamped = clampL(lambda);
    const state = computeState(get().x, clamped);
    set({ lambda: clamped, state });
    pushUrl({ x: get().x, lambda: clamped, tab: get().activeTab, mode: get().mode });
  },
  setTab: (tab) => {
    set({ activeTab: tab });
    pushUrl({ x: get().x, lambda: get().lambda, tab, mode: get().mode });
  },
  setMode: (mode) => {
    set({ mode });
    pushUrl({ x: get().x, lambda: get().lambda, tab: get().activeTab, mode });
  },
  setInputMode: (inputMode) => set({ inputMode }),
  toggleSidebar: () => set(s => ({ sidebarOpen: !s.sidebarOpen })),
  setSweeping: (isSweeping) => set({ isSweeping }),
  setSweepSpeed: (sweepSpeed) => set({ sweepSpeed }),
  saveCurrentState: (name) => {
    const { x, lambda, savedStates } = get();
    const updated = addSavedState(savedStates, name, x, lambda);
    set({ savedStates: updated });
  },
  deleteState: (id) => {
    const updated = deleteSavedState(get().savedStates, id);
    set({ savedStates: updated });
  },
  renameState: (id, name) => {
    const updated = renameSavedState(get().savedStates, id, name);
    set({ savedStates: updated });
  },
  loadSavedState: (s) => {
    const clamped = clampX(s.x);
    const clampedL = clampL(s.lambda);
    const state = computeState(clamped, clampedL);
    set({ x: clamped, lambda: clampedL, state });
  },
  setCompareA: (compareA) => set({ compareA }),
  setCompareB: (compareB) => set({ compareB }),
  pinCurrentAsA: () => set(s => ({ compareA: s.state })),
  pinCurrentAsB: () => set(s => ({ compareB: s.state })),
}));
