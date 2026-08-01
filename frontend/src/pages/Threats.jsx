import React, { useEffect, useState } from "react";
import api from "../api/axios";
import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

function Threats() {

    const [history, setHistory] = useState([]);

    useEffect(() => {

        fetchHistory();

    }, []);

    const fetchHistory = async () => {

        try {

            const response = await api.get("/system/history");

            console.log(response.data);

            setHistory(response.data);

        }

        catch(error){

            console.error(error);

        }

    };

    return (

        <>

            <Sidebar />

            <div className="dashboard-content">

                <Navbar />

                <h1 className="dashboard-title">
                    Threat History
                </h1>

                <div className="network-table">

                    <table>

                        <thead>

                            <tr>

                                <th>Time</th>

                                <th>CPU</th>

                                <th>Memory</th>

                                <th>Prediction</th>

                                <th>Severity</th>

                                <th>Confidence</th>

                            </tr>

                        </thead>

                        <tbody>

                            {history.length > 0 ? (

                                history.map((item) => (

                                    <tr key={item.id}>

                                        <td>{item.timestamp}</td>

                                        <td>{item.cpu_usage}%</td>

                                        <td>{item.memory_usage}%</td>

                                        <td>{item.threat_prediction}</td>

                                        <td>{item.severity}</td>

                                        <td>{item.confidence}%</td>

                                    </tr>

                                ))

                            ) : (

                                <tr>

                                    <td colSpan="6">

                                        No Threat History

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

export default Threats;