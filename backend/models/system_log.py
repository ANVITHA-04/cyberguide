from extensions import db
from datetime import datetime


class SystemLog(db.Model):
    __tablename__ = "system_logs"

    id = db.Column(db.Integer, primary_key=True)

    timestamp = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    hostname = db.Column(
        db.String(100)
    )

    operating_system = db.Column(
        db.String(50)
    )

    cpu_usage = db.Column(
        db.Float
    )

    memory_usage = db.Column(
        db.Float
    )

    disk_usage = db.Column(
        db.Float
    )

    process_count = db.Column(
        db.Integer
    )

    threat_prediction = db.Column(
        db.String(50)
    )

    confidence = db.Column(
        db.Float
    )

    severity = db.Column(
        db.String(20)
    )