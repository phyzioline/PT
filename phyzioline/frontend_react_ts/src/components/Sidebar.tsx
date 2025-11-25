import { Link, useLocation } from 'react-router-dom';
import {
    LayoutDashboard,
    BrainCircuit,
    Users,
    ShoppingBag,
    Briefcase,
    GraduationCap,
    Activity,
    Globe2
} from 'lucide-react';

const Sidebar = () => {
    const location = useLocation();

    const isActive = (path: string) => {
        return location.pathname === path ? 'active' : '';
    };

    return (
        <ul className="menu p-4 w-80 min-h-full bg-base-100 text-base-content border-r border-base-300">
            {/* Brand */}
            <div className="mb-6 px-4">
                <h1 className="text-2xl font-bold text-primary flex items-center gap-2">
                    <Activity className="h-8 w-8" />
                    Phyzioline
                </h1>
                <p className="text-sm text-gray-500 mt-1">Super Platform</p>
            </div>

            {/* Menu Items */}
            <li className="mb-1">
                <Link to="/" className={isActive('/')}>
                    <LayoutDashboard className="h-5 w-5" />
                    Dashboard
                </Link>
            </li>

            <div className="divider my-2 text-xs font-bold text-gray-400 uppercase">Modules</div>

            <li className="mb-1">
                <Link to="/ai" className={isActive('/ai')}>
                    <BrainCircuit className="h-5 w-5" />
                    AI Engine
                </Link>
            </li>
            <li className="mb-1">
                <Link to="/crm" className={isActive('/crm')}>
                    <Users className="h-5 w-5" />
                    CRM
                </Link>
            </li>
            <li className="mb-1">
                <Link to="/marketplace" className={isActive('/marketplace')}>
                    <ShoppingBag className="h-5 w-5" />
                    Marketplace
                </Link>
            </li>
            <li className="mb-1">
                <Link to="/jobs" className={isActive('/jobs')}>
                    <Briefcase className="h-5 w-5" />
                    Jobs
                </Link>
            </li>
            <li className="mb-1">
                <Link to="/courses" className={isActive('/courses')}>
                    <GraduationCap className="h-5 w-5" />
                    Courses
                </Link>
            </li>
            <li className="mb-1">
                <Link to="/global-stats" className={isActive('/global-stats')}>
                    <Globe2 className="h-5 w-5" />
                    Global Stats
                </Link>
            </li>
        </ul>
    );
};

export default Sidebar;
