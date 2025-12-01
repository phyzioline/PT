import { Menu, Bell, Search } from 'lucide-react';

const Navbar = () => {
    return (
        <div className="navbar bg-base-100 shadow-sm sticky top-0 z-10">
            <div className="flex-none lg:hidden">
                <label htmlFor="my-drawer-2" aria-label="open sidebar" className="btn btn-square btn-ghost">
                    <Menu className="h-6 w-6" />
                </label>
            </div>
            <div className="flex-1">
                <div className="form-control w-full max-w-xs ml-4">
                    <div className="relative">
                        <input type="text" placeholder="Search..." className="input input-bordered w-full pl-10" />
                        <Search className="absolute left-3 top-3 h-5 w-5 text-gray-400" />
                    </div>
                </div>
            </div>
            <div className="flex-none gap-2">
                <button className="btn btn-ghost btn-circle">
                    <div className="indicator">
                        <Bell className="h-5 w-5" />
                        <span className="badge badge-xs badge-primary indicator-item"></span>
                    </div>
                </button>
                <div className="dropdown dropdown-end">
                    <div tabIndex={0} role="button" className="btn btn-ghost btn-circle avatar">
                        <div className="w-10 rounded-full">
                            <img alt="User Avatar" src="https://daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg" />
                        </div>
                    </div>
                    <ul tabIndex={0} className="mt-3 z-[1] p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-52">
                        <li>
                            <a className="justify-between">
                                Profile
                                <span className="badge">New</span>
                            </a>
                        </li>
                        <li><a>Settings</a></li>
                        <li><a>Logout</a></li>
                    </ul>
                </div>
            </div>
        </div>
    );
};

export default Navbar;
