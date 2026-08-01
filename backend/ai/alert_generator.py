from ai.explanation import (
    explain_threat,
    explain_network_threat
)



def calculate_severity(confidence):

    if confidence >= 90:
        return "Critical"

    elif confidence >= 70:
        return "High"

    elif confidence >= 40:
        return "Medium"

    else:
        return "Low"



def generate_alert(
        prediction,
        confidence,
        source,
        explanation
):

    if prediction != "Suspicious":

        return None


    severity = explanation["severity"]


    return {

        "alert_type": "Threat Detected",

        "threat_name":
            "Suspicious Activity",

        "severity": severity,

        "confidence": confidence,

        "source": source,

        "reasons":
            explanation["reasons"],

        "recommendations":
            explanation["recommendations"]

    }