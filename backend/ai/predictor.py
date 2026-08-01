import joblib
import os
import numpy as np

from ai.explanation import explain_threat

# ---------------- Load Trained Model ----------------

current_dir = os.path.dirname(__file__)

model_path = os.path.join(
    current_dir,
    "..",
    "ml",
    "models",
    "threat_model.pkl"
)

model = joblib.load(model_path)


# ---------------- Threat Prediction ----------------

def predict_threat(cpu, memory, disk, processes):

    # Prepare input for ML model
    data = np.array([[cpu, memory, disk, processes]])

    # Predict
    prediction = model.predict(data)[0]

    # Prediction confidence
    probabilities = model.predict_proba(data)[0]

    confidence = round(max(probabilities) * 100, 2)

    # Generate AI explanation
    explanation = explain_threat(
        cpu,
        memory,
        disk,
        processes
    )

    # Return complete result
    return {

        "prediction": prediction,

        "confidence": confidence,

        "severity": explanation["severity"],

        "reasons": explanation["reasons"],

        "recommendations": explanation["recommendations"]

    }
# ---------------- Network Threat Prediction ----------------

def predict_network_threat(connection):

    score = 0
    reasons = []

    # Check external connection

    if connection["remote_address"]:

        score += 20

        reasons.append(
            "External network connection detected"
        )


    # Check suspicious ports

    suspicious_ports = [
        21,     # FTP
        22,     # SSH
        23,     # Telnet
        445,    # SMB
        3389    # RDP
    ]


    if connection["local_address"]:

        port = int(
            connection["local_address"].split(":")[-1]
        )


        if port in suspicious_ports:

            score += 50

            reasons.append(
                f"Suspicious port detected: {port}"
            )


    # Prediction

    if score >= 50:

        prediction = "Suspicious"

    else:

        prediction = "Normal"



    confidence = min(score + 50, 100)


    return {

        "prediction": prediction,

        "confidence": confidence,

        "reasons": reasons

    }