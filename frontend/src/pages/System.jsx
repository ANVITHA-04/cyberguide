import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

function System() {
    return (
        <>
            <Sidebar />

            <div className="dashboard-content">
                <Navbar />

                <h1 className="dashboard-title">
                    System Monitoring
                </h1>

                <p>System monitoring information will be displayed here.</p>
            </div>
        </>
    );
}

export default System;