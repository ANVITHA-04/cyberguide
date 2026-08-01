import React, { useEffect, useState } from "react";
import axios from "axios";
import "./index.css";

import {
  FaMicrochip,
  FaMemory,
  FaHdd,
  FaCogs,
  FaShieldAlt,
  FaDesktop,
  FaServer,
  FaExclamationTriangle
} from "react-icons/fa";

import {
  CircularProgressbar,
  buildStyles,
} from "react-circular-progressbar";

import "react-circular-progressbar/dist/styles.css";

function Gauge({ title, value, icon }) {
  return (
    <div className="card">

      <div className="cardIcon">
        {icon}
      </div>

      <div className="gauge">

        <CircularProgressbar
          value={value}
          text={`${value}%`}
          styles={buildStyles({
            textColor: "#ffffff",
            pathColor: "#00ff99",
            trailColor: "#23324d",
            textSize: "16px"
          })}
        />

      </div>

      <h3>{title}</h3>

    </div>
  );
}

function App() {

  const [data, setData] = useState(null);

  useEffect(() => {

    fetchData();

    const timer = setInterval(fetchData, 5000);

    return () => clearInterval(timer);

  }, []);

  const fetchData = async () => {

    try {

      const response = await axios.get(
        "http://127.0.0.1:5000/api/system/info"
      );

      setData(response.data);

    } catch (err) {

      console.log(err);

    }

  };

  if (!data) {

    return (
      <div className="loading">

        <h1>Loading CyberGuardian AI...</h1>

      </div>
    );

  }

  return (

<div className="container">

<header>

<h1>🛡 CyberGuardian AI</h1>

<p>

Real-Time AI Powered Cyber Security Monitoring Dashboard

</p>

</header>

<div className="cards">

<Gauge
title="CPU"
value={data.cpu_usage}
icon={<FaMicrochip />}
/>

<Gauge
title="Memory"
value={data.memory_usage}
icon={<FaMemory />}
/>

<Gauge
title="Disk"
value={data.disk_usage}
icon={<FaHdd />}
/>

<div className="card">

<div className="cardIcon">
<FaCogs />
</div>

<h2 className="processCount">

{data.process_count}

</h2>

<h3>Running Processes</h3>

</div>

</div>

<div
className={
data.threat_prediction === "Normal"
?
"threat safe"
:
"threat danger"
}
>

<h2>

<FaShieldAlt />

&nbsp;

Threat Detection

</h2>

<h1>

{data.threat_prediction}

</h1>

<h3>

Confidence : {data.confidence}%

</h3>

{
data.threat_prediction === "Normal"
?

<p>

✔ No suspicious behaviour detected.

</p>

:

<p>

⚠ High resource usage detected.
AI recommends immediate investigation.

</p>

}

</div>

<div className="systemCard">

<h2>

<FaDesktop />

&nbsp;

System Information

</h2>

<table>

<tbody>

<tr>

<td>

Hostname

</td>

<td>

{data.hostname}

</td>

</tr>

<tr>

<td>

Operating System

</td>

<td>

{data.operating_system}

</td>

</tr>

<tr>

<td>

Processor

</td>

<td>

{data.processor}

</td>

</tr>

<tr>

<td>

CPU Cores

</td>

<td>

{data.cpu_cores}

</td>

</tr>

<tr>

<td>

RAM

</td>

<td>

{data.total_memory_gb} GB

</td>

</tr>

<tr>

<td>

Boot Time

</td>

<td>

{data.boot_time}

</td>

</tr>

</tbody>

</table>

</div>

<div className="footer">

<FaServer />

&nbsp;

CyberGuardian AI © 2026

</div>

</div>

  );

}

export default App;