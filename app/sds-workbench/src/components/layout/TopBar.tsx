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

  return (
    <header style={{
      height: 'var(--topbar-height)',
      background: 'var(--bg-surface)',
      borderBottom: '1px solid var(--border-subtle)',
      display: 'flex',
      alignItems: 'center',
      padding: '0 var(--sp-4)',
      gap: 'var(--sp-3)',
      flexShrink: 0,
    }}>
      <button className="btn btn-ghost btn-icon" onClick={toggleSidebar} title="Toggle sidebar" style={{ fontSize: '1rem' }}>
        ☰
      </button>

      <div style={{ display: 'flex', flexDirection: 'column', lineHeight: 1.2 }}>
        <span style={{ fontWeight: 700, fontSize: '0.9375rem', color: 'var(--text-primary)' }}>
          SdS Workbench
        </span>
        <span style={{ fontSize: '0.6875rem', color: 'var(--text-muted)', letterSpacing: '0.04em' }}>
          4D Schwarzschild–de Sitter · Fixed Λ
        </span>
      </div>

      <div style={{ flex: 1 }} />

      <div className="toggle-group" style={{ width: 180 }}>
        <button className={`toggle-btn ${mode === 'beginner' ? 'active' : ''}`} onClick={() => setMode('beginner')}>Beginner</button>
        <button className={`toggle-btn ${mode === 'technical' ? 'active' : ''}`} onClick={() => setMode('technical')}>Technical</button>
      </div>

      <button className="btn" onClick={handleShare} title="Copy shareable link">
        {copied ? '✓ Copied' : '⇧ Share'}
      </button>
    </header>
  );
}
