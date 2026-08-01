from extensions import db
from datetime import datetime


class ThreatAlert(db.Model):

    __tablename__ = "threat_alerts"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    timestamp = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    alert_type = db.Column(
        db.String(50)
    )


    threat_name = db.Column(
        db.String(100)
    )


    severity = db.Column(
        db.String(20)
    )


    confidence = db.Column(
        db.Float
    )


    source = db.Column(
        db.String(50)
    )


    status = db.Column(
        db.String(20),
        default="New"
    )


    # AI Explanation Details

    reasons = db.Column(
        db.Text
    )


    recommendations = db.Column(
        db.Text
    )