import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import { useAppStore } from '../../store/appStore';
import { encodeUrl } from '../../utils/url';
import { copyToClipboard } from '../../utils/export';
import { useState } from 'react';
export function TopBar() {
    const { mode, setMode, activeTab, x, lambda, toggleSidebar } = useAppStore();
    const [copied, setCopied] = useState(false);
    const handleShare = async () => {
        const url = encodeUrl({ x, lambda, tab: activeTab, mode });
        await copyToClipboard(url);
        setCopied(true);
        setTimeout(() => setCopied(false), 2000);
    };
    return (_jsxs("header", { style: {
            height: 'var(--topbar-height)',
            background: 'var(--bg-surface)',
            borderBottom: '1px solid var(--border-subtle)',
            display: 'flex',
            alignItems: 'center',
            padding: '0 var(--sp-4)',
            gap: 'var(--sp-3)',
            flexShrink: 0,
        }, children: [_jsx("button", { className: "btn btn-ghost btn-icon", onClick: toggleSidebar, title: "Toggle sidebar", style: { fontSize: '1rem' }, children: "\u2630" }), _jsxs("div", { style: { display: 'flex', flexDirection: 'column', lineHeight: 1.2 }, children: [_jsx("span", { style: { fontWeight: 700, fontSize: '0.9375rem', color: 'var(--text-primary)' }, children: "SdS Workbench" }), _jsx("span", { style: { fontSize: '0.6875rem', color: 'var(--text-muted)', letterSpacing: '0.04em' }, children: "4D Schwarzschild\u2013de Sitter \u00B7 Fixed \u039B" })] }), _jsx("div", { style: { flex: 1 } }), _jsxs("div", { className: "toggle-group", style: { width: 180 }, children: [_jsx("button", { className: `toggle-btn ${mode === 'beginner' ? 'active' : ''}`, onClick: () => setMode('beginner'), children: "Beginner" }), _jsx("button", { className: `toggle-btn ${mode === 'technical' ? 'active' : ''}`, onClick: () => setMode('technical'), children: "Technical" })] }), _jsx("button", { className: "btn", onClick: handleShare, title: "Copy shareable link", children: copied ? '✓ Copied' : '⇧ Share' })] }));
}
