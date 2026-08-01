from flask import Flask
from flask_cors import CORS

from config import Config
from extensions import db, bcrypt, jwt

from models.user import User
from models.system_log import SystemLog
from models.network_log import NetworkLog

from routes.auth import auth
from routes.system import system
from routes.network import network
from routes.alerts import alerts
from models.threat_alert import ThreatAlert

from monitoring.scheduler import start_scheduler


app = Flask(__name__)

app.config.from_object(Config)


CORS(app)


db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)


# Register routes

app.register_blueprint(
    auth,
    url_prefix="/api/auth"
)


app.register_blueprint(
    system,
    url_prefix="/api/system"
)


app.register_blueprint(
    network,
    url_prefix="/api/network"
)
app.register_blueprint(
    alerts,
    url_prefix="/api/alerts"
)


@app.route("/")
def home():

    return {
        "Project": "CyberGuardian AI",
        "Status": "Backend Running"
    }



# Create database tables

with app.app_context():

    db.create_all()



# Start monitoring

if __name__ == "__main__":

    start_scheduler(app)

    app.run(debug=True)



