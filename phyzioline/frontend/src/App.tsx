import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainLayout from './layouts/MainLayout';

// Placeholder for modules
const Dashboard = () => <div className="p-4"><h1>Dashboard (React)</h1></div>;
const AI = () => <div className="p-4"><h1>AI Engine (React)</h1></div>;
const CRM = () => <div className="p-4"><h1>CRM (React)</h1></div>;

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<MainLayout />}>
                    <Route index element={<Dashboard />} />
                    <Route path="ai/*" element={<AI />} />
                    <Route path="crm/*" element={<CRM />} />
                </Route>
            </Routes>
        </Router>
    );
}

export default App;
