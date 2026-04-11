import { useAppStore } from './store/appStore';
import { TopBar } from './components/layout/TopBar';
import { Sidebar } from './components/layout/Sidebar';
import { ExploreTab } from './components/tabs/ExploreTab';
import { GeometryTab } from './components/tabs/GeometryTab';
import { ThermodynamicsTab } from './components/tabs/ThermodynamicsTab';
import { EvolutionTab } from './components/tabs/EvolutionTab';
import { CompareTab } from './components/tabs/CompareTab';
import { ExportTab } from './components/tabs/ExportTab';
import './styles/globals.css';

const TABS = [
  { id: 'explore', label: 'Explore' },
  { id: 'geometry', label: 'Geometry' },
  { id: 'thermo', label: 'Thermodynamics' },
  { id: 'evolution', label: 'Evolution' },
  { id: 'compare', label: 'Compare' },
  { id: 'export', label: 'Export' },
] as const;

export default function App() {
  const { activeTab, setTab, isSweeping } = useAppStore();

  return (
    <div className="app">
      <TopBar />
      <div className="app-body">
        <Sidebar />
        <main style={{ flex: 1, display: 'flex', flexDirection: 'column', overflow: 'hidden', background: 'var(--bg-base)' }}>
          <div className="tab-bar">
            {TABS.map(tab => (
              <button key={tab.id} className={`tab-btn ${activeTab === tab.id ? 'active' : ''}`}
                onClick={() => setTab(tab.id)}>
                {tab.label}
                {tab.id === 'explore' && isSweeping && (
                  <span style={{ marginLeft: 6, fontSize: '0.6875rem', color: 'var(--amber-text)' }}>▶</span>
                )}
              </button>
            ))}
          </div>

          {activeTab === 'explore' && <ExploreTab />}
          {activeTab === 'geometry' && <GeometryTab />}
          {activeTab === 'thermo' && <ThermodynamicsTab />}
          {activeTab === 'evolution' && <EvolutionTab />}
          {activeTab === 'compare' && <CompareTab />}
          {activeTab === 'export' && <ExportTab />}
        </main>
      </div>
    </div>
  );
}
