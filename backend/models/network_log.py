from extensions import db
from datetime import datetime


class NetworkLog(db.Model):

    __tablename__ = "network_logs"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    timestamp = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    process_name = db.Column(
        db.String(100)
    )


    local_address = db.Column(
        db.String(100)
    )


    remote_address = db.Column(
        db.String(100)
    )


    status = db.Column(
        db.String(50)
    )


    pid = db.Column(
        db.Integer
    )