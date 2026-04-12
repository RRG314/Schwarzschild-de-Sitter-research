import { TabId, Mode } from '../engine/types';

export interface UrlState {
  x: number;
  lambda: number;
  tab: TabId;
  mode: Mode;
}

export function encodeUrl(state: UrlState): string {
  const params = new URLSearchParams({
    x: state.x.toFixed(4),
    l: state.lambda.toFixed(4),
    t: state.tab,
    m: state.mode,
  });
  const url = new URL(window.location.href);
  url.search = params.toString();
  return url.toString();
}

export function decodeUrl(): Partial<UrlState> {
  const params = new URLSearchParams(window.location.search);
  const result: Partial<UrlState> = {};
  const x = parseFloat(params.get('x') || '');
  if (isFinite(x) && x > 0 && x < 1) result.x = x;
  const l = parseFloat(params.get('l') || '');
  if (isFinite(l) && l > 0) result.lambda = l;
  const t = params.get('t') as TabId;
  if (['explore','geometry','thermo','evolution','tools','compare','export'].includes(t)) result.tab = t;
  const m = params.get('m') as Mode;
  if (['beginner','technical'].includes(m)) result.mode = m;
  return result;
}

export function pushUrl(state: UrlState): void {
  const url = encodeUrl(state);
  window.history.replaceState({}, '', url);
}
