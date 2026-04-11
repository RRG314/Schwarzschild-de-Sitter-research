const KEY = 'sds-saved-states';
export function loadSavedStates() {
    try {
        const raw = localStorage.getItem(KEY);
        if (!raw)
            return [];
        return JSON.parse(raw);
    }
    catch {
        return [];
    }
}
export function saveSavedStates(states) {
    try {
        localStorage.setItem(KEY, JSON.stringify(states));
    }
    catch { }
}
export function addSavedState(states, name, x, lambda) {
    const next = {
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
export function deleteSavedState(states, id) {
    const updated = states.filter(s => s.id !== id);
    saveSavedStates(updated);
    return updated;
}
export function renameSavedState(states, id, name) {
    const updated = states.map(s => s.id === id ? { ...s, name } : s);
    saveSavedStates(updated);
    return updated;
}
