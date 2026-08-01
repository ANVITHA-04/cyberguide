import psutil
import platform
import socket
from datetime import datetime

from models.system_log import SystemLog
from extensions import db
from ai.predictor import predict_threat


def get_running_processes():
    processes = []

    for process in psutil.process_iter(
        ['pid', 'name', 'username', 'cpu_percent', 'memory_percent']
    ):
        try:
            processes.append({
                "pid": process.info["pid"],
                "name": process.info["name"],
                "user": process.info["username"],
                "cpu": round(process.info["cpu_percent"], 2),
                "memory": round(process.info["memory_percent"], 2)
            })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            pass

    return processes


def get_system_info():

    boot_time = datetime.fromtimestamp(psutil.boot_time())

    # Running Processes
    processes = get_running_processes()
    process_count = len(processes)

    # System Information
    system_info = {
        "hostname": socket.gethostname(),
        "operating_system": platform.system(),
        "os_version": platform.version(),
        "processor": platform.processor(),
        "cpu_usage": psutil.cpu_percent(interval=1),
        "cpu_cores": psutil.cpu_count(logical=True),
        "memory_usage": psutil.virtual_memory().percent,
        "total_memory_gb": round(
            psutil.virtual_memory().total / (1024 ** 3), 2
        ),
        "disk_usage": psutil.disk_usage('/').percent,
        "boot_time": boot_time.strftime("%Y-%m-%d %H:%M:%S"),
        "process_count": process_count
    }

    # ==========================
    # AI Threat Prediction
    # ==========================
    prediction = predict_threat(
        system_info["cpu_usage"],
        system_info["memory_usage"],
        system_info["disk_usage"],
        system_info["process_count"]
    )

    system_info["threat_prediction"] = prediction["prediction"]
    system_info["confidence"] = prediction["confidence"]
    system_info["severity"] = prediction["severity"]
    system_info["reasons"] = prediction["reasons"]
    system_info["recommendations"] = prediction["recommendations"]

    # ==========================
    # Save to Database
    # ==========================
    log = SystemLog(
        hostname=system_info["hostname"],
        operating_system=system_info["operating_system"],
        cpu_usage=system_info["cpu_usage"],
        memory_usage=system_info["memory_usage"],
        disk_usage=system_info["disk_usage"],
        process_count=system_info["process_count"],
        threat_prediction=system_info["threat_prediction"],
        confidence=system_info["confidence"],
        severity=system_info["severity"]
    )

    db.session.add(log)
    db.session.commit()

    print("\n========== CyberGuardian AI ==========")
    print(system_info)
    print("======================================\n")

    return system_info