from apscheduler.schedulers.background import BackgroundScheduler

from monitoring.system_monitor import get_system_info
from monitoring.network_monitor import get_network_connections

from models.system_log import SystemLog
from models.network_log import NetworkLog
from models.threat_alert import ThreatAlert

from ai.predictor import (
    predict_threat,
    predict_network_threat
)

from ai.alert_generator import generate_alert

from ai.explanation import (
    explain_threat,
    explain_network_threat
)

from extensions import db



def start_scheduler(app):

    scheduler = BackgroundScheduler()


    def monitor():

        with app.app_context():


            print("🔄 Collecting system information...")


            # ==========================
            # SYSTEM MONITORING
            # ==========================


            system_data = get_system_info()



            # AI SYSTEM PREDICTION

            threat_result = predict_threat(

                system_data["cpu_usage"],

                system_data["memory_usage"],

                system_data["disk_usage"],

                system_data["process_count"]

            )



            # SYSTEM EXPLANATION

            system_explanation = explain_threat(

                system_data["cpu_usage"],

                system_data["memory_usage"],

                system_data["disk_usage"],

                system_data["process_count"]

            )



            # CREATE SYSTEM ALERT

            system_alert = generate_alert(

                threat_result["prediction"],

                threat_result["confidence"],

                "System",

                system_explanation

            )



            if system_alert:


                alert = ThreatAlert(

                    alert_type=system_alert["alert_type"],

                    threat_name=system_alert["threat_name"],

                    severity=system_alert["severity"],

                    confidence=system_alert["confidence"],

                    source=system_alert["source"],

                    reasons=str(system_alert["reasons"]),

                    recommendations=str(system_alert["recommendations"])

                )


                db.session.add(alert)



            # STORE SYSTEM LOG


            system_log = SystemLog(

                hostname=system_data["hostname"],

                operating_system=system_data["operating_system"],

                cpu_usage=system_data["cpu_usage"],

                memory_usage=system_data["memory_usage"],

                disk_usage=system_data["disk_usage"],

                process_count=system_data["process_count"],

                threat_prediction=threat_result["prediction"],

                confidence=threat_result["confidence"]

            )


            db.session.add(system_log)



            # ==========================
            # NETWORK MONITORING
            # ==========================


            print("🌐 Collecting network information...")


            connections = get_network_connections()



            for conn in connections:



                # AI NETWORK PREDICTION

                network_threat = predict_network_threat(conn)



                # NETWORK EXPLANATION

                network_explanation = explain_network_threat(

                    remote_address=conn["remote_address"],

                    status=conn["status"]

                )



                # CREATE NETWORK ALERT


                network_alert = generate_alert(

                    network_threat["prediction"],

                    network_threat["confidence"],

                    "Network",

                    network_explanation

                )



                if network_alert:


                    alert = ThreatAlert(

                        alert_type=network_alert["alert_type"],

                        threat_name=network_alert["threat_name"],

                        severity=network_alert["severity"],

                        confidence=network_alert["confidence"],

                        source=network_alert["source"],

                        reasons=str(network_alert["reasons"]),

                        recommendations=str(network_alert["recommendations"])

                    )


                    db.session.add(alert)



                # STORE NETWORK LOG


                network_log = NetworkLog(

                    local_address=conn["local_address"],

                    remote_address=conn["remote_address"],

                    status=conn["status"],

                    pid=conn["pid"],

                    threat_prediction=network_threat["prediction"],

                    confidence=network_threat["confidence"]

                )


                db.session.add(network_log)



            db.session.commit()


            print("✅ Monitoring data stored")



    scheduler.add_job(

        monitor,

        trigger="interval",

        seconds=5

    )


    scheduler.start()


    print("✅ Background Monitoring Started")