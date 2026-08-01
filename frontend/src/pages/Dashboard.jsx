import React, { useEffect, useState } from "react";
import api from "../api/axios";
import StatCard from "../components/StatCard";
import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import SystemInfo from "../components/SystemInfo";
import ThreatStatus from "../components/ThreatStatus";
import Recommendations from "../components/Recommendations";

function Dashboard() {
    const [system, setSystem] = useState({});

    useEffect(() => {
        fetchSystem();

        const interval = setInterval(fetchSystem, 5000);

        return () => clearInterval(interval);
    }, []);

    const fetchSystem = async () => {
        try {
            const response = await api.get("/system/info");

            console.log("API Response:", response.data);

            setSystem(response.data);
        } catch (error) {
            console.error("Error fetching system info:", error);
        }
    };

    return (
        <>
            <Sidebar />

            <div className="dashboard-content">
                <Navbar />

                <h1 className="dashboard-title">
                    CyberGuardian AI Dashboard
                </h1>

                <div className="cards">
                    <StatCard
                        title="CPU Usage"
                        value={`${system.cpu_usage || 0}%`}
                    />

                    <StatCard
                        title="Memory Usage"
                        value={`${system.memory_usage || 0}%`}
                    />

                    <StatCard
                        title="Disk Usage"
                        value={`${system.disk_usage || 0}%`}
                    />

                    <StatCard
                        title="Processes"
                        value={system.process_count || 0}
                    />
                </div>

                {/* System Information Section */}
                <SystemInfo system={system} />
                <ThreatStatus system={system} />
                <Recommendations system={system} />

            </div>
        </>
    );
}

export default Dashboard;