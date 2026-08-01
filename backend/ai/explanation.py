def explain_threat(cpu, memory, disk, process_count):

    reasons = []
    recommendations = []

    # ---------------- CPU ----------------
    if cpu >= 90:
        reasons.append(
            f"CPU usage is critically high ({cpu:.1f}%)."
        )
        recommendations.append(
            "Inspect CPU-intensive processes."
        )

    elif cpu >= 75:
        reasons.append(
            f"CPU usage is higher than normal ({cpu:.1f}%)."
        )

    # ---------------- MEMORY ----------------
    if memory >= 90:
        reasons.append(
            f"Memory usage is critically high ({memory:.1f}%)."
        )
        recommendations.append(
            "Check for memory leaks or malicious applications."
        )

    elif memory >= 75:
        reasons.append(
            f"Memory usage is above the recommended limit ({memory:.1f}%)."
        )

    # ---------------- DISK ----------------
    if disk >= 95:
        reasons.append(
            f"Disk usage is critically high ({disk:.1f}%)."
        )
        recommendations.append(
            "Free disk space and inspect recent file activity."
        )

    elif disk >= 80:
        reasons.append(
            f"Disk utilization is high ({disk:.1f}%)."
        )

    # ---------------- PROCESSES ----------------
    if process_count >= 350:
        reasons.append(
            f"An unusually high number of running processes ({process_count}) was detected."
        )
        recommendations.append(
            "Review unknown background processes."
        )

    elif process_count >= 250:
        reasons.append(
            f"Process count is above the normal range ({process_count})."
        )

    # ---------------- DEFAULT ----------------
    if len(reasons) == 0:

        reasons.append(
            "System resources are operating within normal limits."
        )

        recommendations.append(
            "Continue monitoring the system."
        )

    # ---------------- SEVERITY ----------------
    score = 0

    if cpu >= 90:
        score += 2
    elif cpu >= 75:
        score += 1

    if memory >= 90:
        score += 2
    elif memory >= 75:
        score += 1

    if disk >= 95:
        score += 2
    elif disk >= 80:
        score += 1

    if process_count >= 350:
        score += 2
    elif process_count >= 250:
        score += 1

    if score >= 6:
        severity = "Critical"

    elif score >= 3:
        severity = "High"

    elif score >= 1:
        severity = "Medium"

    else:
        severity = "Low"

    return {

        "severity": severity,

        "reasons": reasons,

        "recommendations": recommendations

    }
def explain_network_threat(
        port=None,
        remote_address=None,
        status=None
):

    reasons = []

    recommendations = []


    # External connection

    if remote_address:

        reasons.append(
            "External network connection detected."
        )

        recommendations.append(
            "Verify whether the remote IP is trusted."
        )


    # Suspicious ports

    suspicious_ports = {

        21: "FTP",

        22: "SSH",

        23: "Telnet",

        445: "SMB",

        3389: "Remote Desktop"

    }


    if port in suspicious_ports:

        reasons.append(
            f"Suspicious port detected: {port} ({suspicious_ports[port]})."
        )

        recommendations.append(
            "Investigate the application using this port."
        )


    # Connection state

    if status == "ESTABLISHED":

        reasons.append(
            "Active communication with another host detected."
        )


    # Default

    if len(reasons) == 0:

        reasons.append(
            "No suspicious network behaviour detected."
        )

        recommendations.append(
            "Continue monitoring network activity."
        )



    # Severity

    if len(reasons) >= 3:

        severity = "High"

    elif len(reasons) == 2:

        severity = "Medium"

    else:

        severity = "Low"



    return {

        "severity": severity,

        "reasons": reasons,

        "recommendations": recommendations

    }