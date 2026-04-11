import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import { useAppStore } from './store/appStore';
import { TopBar } from './components/layout/TopBar';
import { Sidebar } from './components/layout/Sidebar';
import { ExploreTab } from './components/tabs/ExploreTab';
import { GeometryTab } from './components/tabs/GeometryTab';
import { ThermodynamicsTab } from './components/tabs/ThermodynamicsTab';
import { CompareTab } from './components/tabs/CompareTab';
import { ExportTab } from './components/tabs/ExportTab';
import './styles/globals.css';
const TABS = [
    { id: 'explore', label: 'Explore' },
    { id: 'geometry', label: 'Geometry' },
    { id: 'thermo', label: 'Thermodynamics' },
    { id: 'compare', label: 'Compare' },
    { id: 'export', label: 'Export' },
];
export default function App() {
    const { activeTab, setTab, isSweeping } = useAppStore();
    return (_jsxs("div", { className: "app", children: [_jsx(TopBar, {}), _jsxs("div", { className: "app-body", children: [_jsx(Sidebar, {}), _jsxs("main", { style: { flex: 1, display: 'flex', flexDirection: 'column', overflow: 'hidden', background: 'var(--bg-base)' }, children: [_jsx("div", { className: "tab-bar", children: TABS.map(tab => (_jsxs("button", { className: `tab-btn ${activeTab === tab.id ? 'active' : ''}`, onClick: () => setTab(tab.id), children: [tab.label, tab.id === 'explore' && isSweeping && (_jsx("span", { style: { marginLeft: 6, fontSize: '0.6875rem', color: 'var(--amber-text)' }, children: "\u25B6" }))] }, tab.id))) }), activeTab === 'explore' && _jsx(ExploreTab, {}), activeTab === 'geometry' && _jsx(GeometryTab, {}), activeTab === 'thermo' && _jsx(ThermodynamicsTab, {}), activeTab === 'compare' && _jsx(CompareTab, {}), activeTab === 'export' && _jsx(ExportTab, {})] })] })] }));
}
