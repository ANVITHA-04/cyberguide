import React, { useEffect, useState } from "react";
import api from "../api/axios";
import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

function Network() {
    const [connections, setConnections] = useState([]);

    useEffect(() => {
        fetchConnections();

        const interval = setInterval(fetchConnections, 5000);

        return () => clearInterval(interval);
    }, []);

    const fetchConnections = async () => {
        try {
            const response = await api.get("/network/connections");

            console.log("Network Data:", response.data);

            setConnections(response.data);
        } catch (error) {
            console.error("Error fetching network connections:", error);
        }
    };

    return (
        <>
            <Sidebar />

            <div className="dashboard-content">
                <Navbar />

                <h1 className="dashboard-title">
                    Network Monitoring
                </h1>

                <div className="network-table">

                    <table>

                        <thead>
                            <tr>
                                <th>Local Address</th>
                                <th>Remote Address</th>
                                <th>Status</th>
                                <th>PID</th>
                            </tr>
                        </thead>

                        <tbody>

                            {connections.length > 0 ? (

                                connections.map((connection, index) => (

                                    <tr key={index}>

                                        <td>{connection.local_address || "-"}</td>

                                        <td>{connection.remote_address || "-"}</td>

                                        <td>{connection.status}</td>

                                        <td>{connection.pid || "-"}</td>

                                    </tr>

                                ))

                            ) : (

                                <tr>

                                    <td colSpan="4">
                                        No Active Connections
                                    </td>

                                </tr>

                            )}

                        </tbody>

                    </table>

                </div>

            </div>
        </>
    );
}

export default Network;