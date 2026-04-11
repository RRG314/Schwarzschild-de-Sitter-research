import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import { useAppStore } from '../../store/appStore';
import { computeStateFromMass, computeStateFromDeltaFrac, PRESETS } from '../../engine/physics';
import { fmt } from '../../engine/format';
import { useState, useRef, useEffect } from 'react';
export function Sidebar() {
    const { x, lambda, state, inputMode, setInputMode, sidebarOpen, setX, setLambda, savedStates, saveCurrentState, deleteState, loadSavedState, isSweeping, sweepSpeed, setSweeping, setSweepSpeed, } = useAppStore();
    const [massInput, setMassInput] = useState('');
    const [deltaInput, setDeltaInput] = useState('');
    const [saveNameInput, setSaveNameInput] = useState('');
    const [massError, setMassError] = useState('');
    const [deltaError, setDeltaError] = useState('');
    const sweepRef = useRef(null);
    useEffect(() => {
        if (isSweeping) {
            const step = 0.005;
            let dir = 1;
            let cur = x;
            sweepRef.current = window.setInterval(() => {
                cur += step * dir;
                if (cur >= 0.995) {
                    cur = 0.995;
                    dir = -1;
                }
                if (cur <= 0.005) {
                    cur = 0.005;
                    dir = 1;
                }
                setX(cur);
            }, 1000 / sweepSpeed);
        }
        else {
            if (sweepRef.current)
                clearInterval(sweepRef.current);
        }
        return () => { if (sweepRef.current)
            clearInterval(sweepRef.current); };
    }, [isSweeping, sweepSpeed]);
    const applyMassInput = () => {
        const M = parseFloat(massInput);
        const s = computeStateFromMass(lambda, M);
        if (s) {
            setX(s.x);
            setMassError('');
        }
        else
            setMassError(`M must be in (0, ${fmt(state.M_nariai)})`);
    };
    const applyDeltaInput = () => {
        const d = parseFloat(deltaInput);
        const s = computeStateFromDeltaFrac(lambda, d);
        if (s) {
            setX(s.x);
            setDeltaError('');
        }
        else
            setDeltaError('Δ/S_Λ must be in (0, 0.333)');
    };
    if (!sidebarOpen)
        return null;
    return (_jsxs("aside", { style: {
            width: 'var(--sidebar-width)',
            flexShrink: 0,
            background: 'var(--bg-surface)',
            borderRight: '1px solid var(--border-subtle)',
            display: 'flex',
            flexDirection: 'column',
            overflowY: 'auto',
        }, children: [_jsxs("div", { style: { padding: 'var(--sp-4)', borderBottom: '1px solid var(--border-subtle)' }, children: [_jsx("div", { className: "section-label", children: "Current State" }), _jsx("div", { style: { display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 'var(--sp-2)' }, children: [
                            { label: 'x', value: x.toFixed(4), color: 'var(--blue)' },
                            { label: 'Λ', value: lambda.toFixed(3), color: 'var(--text-secondary)' },
                            { label: 'r_b', value: fmt(state.r_b), color: 'var(--amber)' },
                            { label: 'r_c', value: fmt(state.r_c), color: 'var(--teal)' },
                        ].map(({ label, value, color }) => (_jsxs("div", { style: { background: 'var(--bg-elevated)', borderRadius: 'var(--radius-sm)', padding: '6px var(--sp-3)' }, children: [_jsx("div", { style: { fontSize: '0.625rem', textTransform: 'uppercase', letterSpacing: '0.08em', color: 'var(--text-muted)', fontFamily: 'var(--font-mono)' }, children: label }), _jsx("div", { style: { fontSize: '0.875rem', fontFamily: 'var(--font-mono)', color, fontWeight: 600 }, children: value })] }, label))) })] }), _jsxs("div", { style: { padding: 'var(--sp-4)', borderBottom: '1px solid var(--border-subtle)', display: 'flex', flexDirection: 'column', gap: 'var(--sp-4)' }, children: [_jsx("div", { className: "section-label", children: "Parameters" }), _jsx("div", { className: "toggle-group", children: ['x', 'mass', 'delta'].map(m => (_jsx("button", { className: `toggle-btn ${inputMode === m ? 'active' : ''}`, onClick: () => setInputMode(m), children: m === 'x' ? 'x' : m === 'mass' ? 'M' : 'Δ/S' }, m))) }), inputMode === 'x' && (_jsxs("div", { className: "slider-wrap", children: [_jsxs("div", { style: { display: 'flex', justifyContent: 'space-between', alignItems: 'center' }, children: [_jsx("label", { style: { fontSize: '0.8125rem', color: 'var(--text-secondary)' }, children: "x = r_b / r_c" }), _jsx("span", { style: { fontFamily: 'var(--font-mono)', fontSize: '0.875rem', color: 'var(--blue-text)', fontWeight: 600 }, children: x.toFixed(4) })] }), _jsx("input", { type: "range", className: "slider", min: "0.005", max: "0.995", step: "0.001", value: x, onChange: e => setX(parseFloat(e.target.value)) }), _jsxs("div", { style: { display: 'flex', justifyContent: 'space-between', fontSize: '0.6875rem', color: 'var(--text-muted)' }, children: [_jsx("span", { children: "Pure dS \u2192" }), _jsx("span", { children: "\u2190 Nariai" })] })] })), inputMode === 'mass' && (_jsxs("div", { style: { display: 'flex', flexDirection: 'column', gap: 'var(--sp-2)' }, children: [_jsxs("label", { style: { fontSize: '0.8125rem', color: 'var(--text-secondary)' }, children: ["Mass M (0 to ", fmt(state.M_nariai), ")"] }), _jsxs("div", { style: { display: 'flex', gap: 'var(--sp-2)' }, children: [_jsx("input", { className: "input", placeholder: fmt(state.M), value: massInput, onChange: e => setMassInput(e.target.value), onKeyDown: e => e.key === 'Enter' && applyMassInput() }), _jsx("button", { className: "btn btn-sm", onClick: applyMassInput, children: "Set" })] }), massError && _jsx("div", { style: { fontSize: '0.75rem', color: 'var(--text-danger)' }, children: massError }), _jsxs("div", { style: { fontSize: '0.75rem', color: 'var(--text-muted)' }, children: ["Current M = ", fmt(state.M)] })] })), inputMode === 'delta' && (_jsxs("div", { style: { display: 'flex', flexDirection: 'column', gap: 'var(--sp-2)' }, children: [_jsx("label", { style: { fontSize: '0.8125rem', color: 'var(--text-secondary)' }, children: "\u0394/S_\u039B (0 to 0.333)" }), _jsxs("div", { style: { display: 'flex', gap: 'var(--sp-2)' }, children: [_jsx("input", { className: "input", placeholder: fmt(state.fDelta), value: deltaInput, onChange: e => setDeltaInput(e.target.value), onKeyDown: e => e.key === 'Enter' && applyDeltaInput() }), _jsx("button", { className: "btn btn-sm", onClick: applyDeltaInput, children: "Set" })] }), deltaError && _jsx("div", { style: { fontSize: '0.75rem', color: 'var(--text-danger)' }, children: deltaError }), _jsxs("div", { style: { fontSize: '0.75rem', color: 'var(--text-muted)' }, children: ["Current = ", fmt(state.fDelta)] })] })), _jsxs("div", { style: { display: 'flex', flexDirection: 'column', gap: 'var(--sp-2)' }, children: [_jsx("label", { style: { fontSize: '0.8125rem', color: 'var(--text-secondary)' }, children: "\u039B (0.01 \u2013 10)" }), _jsx("div", { style: { display: 'flex', gap: 'var(--sp-2)', alignItems: 'center' }, children: _jsx("input", { type: "number", className: "input", step: "0.1", min: "0.01", max: "10", value: lambda, onChange: e => setLambda(parseFloat(e.target.value) || lambda) }) }), _jsxs("div", { style: { fontSize: '0.75rem', color: 'var(--text-muted)' }, children: ["r_\u039B = ", fmt(state.r_lambda), " \u00B7 M_N = ", fmt(state.M_nariai)] })] })] }), _jsxs("div", { style: { padding: 'var(--sp-4)', borderBottom: '1px solid var(--border-subtle)', display: 'flex', flexDirection: 'column', gap: 'var(--sp-2)' }, children: [_jsx("div", { className: "section-label", children: "Presets" }), Object.values(PRESETS).map(p => (_jsx("button", { className: "btn btn-ghost", style: { justifyContent: 'flex-start', fontSize: '0.8125rem' }, onClick: () => setX(p.x), title: p.description, children: p.label }, p.label)))] }), _jsxs("div", { style: { padding: 'var(--sp-4)', borderBottom: '1px solid var(--border-subtle)', display: 'flex', flexDirection: 'column', gap: 'var(--sp-3)' }, children: [_jsx("div", { className: "section-label", children: "Parameter Sweep" }), _jsx("p", { style: { fontSize: '0.75rem', margin: 0 }, children: "Sweeps x from 0 to 1 \u2014 not time evolution." }), _jsxs("div", { style: { display: 'flex', gap: 'var(--sp-2)', alignItems: 'center' }, children: [_jsx("button", { className: `btn ${isSweeping ? 'btn-primary' : ''}`, style: { flex: 1 }, onClick: () => setSweeping(!isSweeping), children: isSweeping ? '⏸ Pause' : '▶ Play' }), _jsx("button", { className: "btn btn-ghost btn-sm", onClick: () => setX(Math.max(0.005, x - 0.01)), children: "\u2039" }), _jsx("button", { className: "btn btn-ghost btn-sm", onClick: () => setX(Math.min(0.995, x + 0.01)), children: "\u203A" })] }), _jsxs("div", { style: { display: 'flex', alignItems: 'center', gap: 'var(--sp-2)', fontSize: '0.75rem', color: 'var(--text-secondary)' }, children: [_jsx("span", { children: "Speed" }), _jsx("input", { type: "range", className: "slider", style: { flex: 1 }, min: "1", max: "30", value: sweepSpeed, onChange: e => setSweepSpeed(parseInt(e.target.value)) }), _jsxs("span", { style: { fontFamily: 'var(--font-mono)', minWidth: 30 }, children: [sweepSpeed, "x"] })] })] }), _jsxs("div", { style: { padding: 'var(--sp-4)', flex: 1, display: 'flex', flexDirection: 'column', gap: 'var(--sp-3)' }, children: [_jsx("div", { className: "section-label", children: "Saved States" }), _jsxs("div", { style: { display: 'flex', gap: 'var(--sp-2)' }, children: [_jsx("input", { className: "input", placeholder: "Name this state\u2026", value: saveNameInput, onChange: e => setSaveNameInput(e.target.value), onKeyDown: e => { if (e.key === 'Enter' && saveNameInput.trim()) {
                                    saveCurrentState(saveNameInput.trim());
                                    setSaveNameInput('');
                                } } }), _jsx("button", { className: "btn btn-sm", disabled: !saveNameInput.trim(), onClick: () => { if (saveNameInput.trim()) {
                                    saveCurrentState(saveNameInput.trim());
                                    setSaveNameInput('');
                                } }, children: "Save" })] }), savedStates.length === 0 && (_jsx("div", { style: { fontSize: '0.75rem', color: 'var(--text-muted)', textAlign: 'center', padding: 'var(--sp-4)' }, children: "No saved states. Save a state to recall it later." })), _jsx("div", { style: { display: 'flex', flexDirection: 'column', gap: 'var(--sp-2)', overflowY: 'auto' }, children: savedStates.map(s => (_jsxs("div", { style: {
                                background: 'var(--bg-elevated)', borderRadius: 'var(--radius-sm)',
                                padding: 'var(--sp-2) var(--sp-3)',
                                display: 'flex', alignItems: 'center', gap: 'var(--sp-2)',
                            }, children: [_jsxs("div", { style: { flex: 1, cursor: 'pointer' }, onClick: () => loadSavedState(s), children: [_jsx("div", { style: { fontSize: '0.8125rem', fontWeight: 500 }, children: s.name }), _jsxs("div", { style: { fontSize: '0.6875rem', color: 'var(--text-muted)', fontFamily: 'var(--font-mono)' }, children: ["x=", s.x.toFixed(3), " \u039B=", s.lambda.toFixed(2)] })] }), _jsx("button", { className: "btn btn-ghost btn-sm btn-icon", onClick: () => deleteState(s.id), title: "Delete", style: { color: 'var(--text-muted)' }, children: "\u2715" })] }, s.id))) })] })] }));
}
