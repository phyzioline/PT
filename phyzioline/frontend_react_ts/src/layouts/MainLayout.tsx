import { Outlet } from 'react-router-dom';
import Navbar from '../components/Navbar';
import Sidebar from '../components/Sidebar';
import Footer from '../components/Footer';

const MainLayout = () => {
    return (
        <div className="drawer lg:drawer-open">
            <input id="my-drawer-2" type="checkbox" className="drawer-toggle" />
            <div className="drawer-content flex flex-col min-h-screen bg-base-200">
                {/* Navbar */}
                <Navbar />

                {/* Page Content */}
                <main className="flex-1 p-6">
                    <Outlet />
                </main>

                {/* Footer */}
                <Footer />
            </div>

            {/* Sidebar */}
            <div className="drawer-side z-20">
                <label htmlFor="my-drawer-2" aria-label="close sidebar" className="drawer-overlay"></label>
                <Sidebar />
            </div>
        </div>
    );
};

export default MainLayout;
