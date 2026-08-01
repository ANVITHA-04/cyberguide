from flask import Blueprint, jsonify

from models.threat_alert import ThreatAlert


alerts = Blueprint(
    "alerts",
    __name__
)


@alerts.route("/", methods=["GET"])
def get_alerts():


    alerts_data = ThreatAlert.query.order_by(
        ThreatAlert.timestamp.desc()
    ).all()


    result = []


    for alert in alerts_data:

        result.append({

            "id": alert.id,

            "time": str(alert.timestamp),

            "alert_type": alert.alert_type,

            "threat_name": alert.threat_name,

            "severity": alert.severity,

            "confidence": alert.confidence,

            "source": alert.source,

            "status": alert.status

        })


    return jsonify(result), 200