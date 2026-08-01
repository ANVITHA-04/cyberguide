import {
    LayoutDashboard,
    Cpu,
    Network,
    ShieldAlert,
    Settings
} from "lucide-react";

import { Link, useLocation } from "react-router-dom";

function Sidebar() {

    const location = useLocation();

    return (

        <div className="sidebar">

            <h2 className="logo">
                CyberGuardian
            </h2>

            <ul>

                <li className={location.pathname === "/" ? "active" : ""}>
                    <Link to="/">
                        <LayoutDashboard size={20} />
                        <span>Dashboard</span>
                    </Link>
                </li>

                <li className={location.pathname === "/network" ? "active" : ""}>
                    <Link to="/network">
                        <Network size={20} />
                        <span>Network</span>
                    </Link>
                </li>

                <li className={location.pathname === "/threats" ? "active" : ""}>
                    <Link to="/threats">
                        <ShieldAlert size={20} />
                        <span>Threats</span>
                    </Link>
                </li>

                <li className={location.pathname === "/system" ? "active" : ""}>
                    <Link to="/system">
                        <Cpu size={20} />
                        <span>System</span>
                    </Link>
                </li>

                <li className={location.pathname === "/settings" ? "active" : ""}>
                    <Link to="/settings">
                        <Settings size={20} />
                        <span>Settings</span>
                    </Link>
                </li>

            </ul>

        </div>

    );
}

export default Sidebar;