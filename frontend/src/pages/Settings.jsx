import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

function Settings() {
    return (
        <>
            <Sidebar />

            <div className="dashboard-content">
                <Navbar />

                <h1 className="dashboard-title">
                    Settings
                </h1>

                <p>Application settings will be available here.</p>
            </div>
        </>
    );
}

export default Settings;