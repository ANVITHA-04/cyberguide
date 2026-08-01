import { Bell, ShieldCheck } from "lucide-react";

function Navbar() {
    const today = new Date();

    return (
        <div className="navbar">

            <div>
                <h2>System Monitoring Dashboard</h2>
                <p>{today.toLocaleString()}</p>
            </div>

            <div className="navbar-right">

                <div className="status">
                    <ShieldCheck size={20} />
                    <span>Protected</span>
                </div>

                <Bell size={24} className="icon" />

                <div className="profile">
                    <img
                        src="https://ui-avatars.com/api/?name=Admin&background=00ff99&color=000"
                        alt="profile"
                    />
                </div>

            </div>

        </div>
    );
}

export default Navbar;