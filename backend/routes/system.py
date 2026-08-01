from flask import Blueprint, jsonify

from monitoring.system_monitor import (
    get_system_info,
    get_running_processes
)

from models.system_log import SystemLog


system = Blueprint("system", __name__)


# ==========================
# System Information
# ==========================
@system.route("/info", methods=["GET"])
def system_info():

    data = get_system_info()

    return jsonify(data), 200


# ==========================
# Running Processes
# ==========================
@system.route("/processes", methods=["GET"])
def processes():

    return jsonify(
        get_running_processes()
    ), 200


# ==========================
# Threat History
# ==========================
@system.route("/history", methods=["GET"])
def history():

    logs = SystemLog.query.order_by(
        SystemLog.timestamp.desc()
    ).all()

    history = []

    for log in logs:

        history.append({

            "id": log.id,

            "timestamp": log.timestamp.strftime("%Y-%m-%d %H:%M:%S"),

            "hostname": log.hostname,

            "operating_system": log.operating_system,

            "cpu_usage": log.cpu_usage,

            "memory_usage": log.memory_usage,

            "disk_usage": log.disk_usage,

            "process_count": log.process_count,

            "threat_prediction": log.threat_prediction,

            "confidence": log.confidence,

            "severity": log.severity

        })

    return jsonify(history), 200