import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "CyberGuardianSecret123"
    )

    JWT_SECRET_KEY = os.getenv(
        "JWT_SECRET_KEY",
        "CyberGuardianJWT123"
    )

    # Use PostgreSQL on Render
    database_url = os.getenv("DATABASE_URL")

    if database_url:
        if database_url.startswith("postgres://"):
            database_url = database_url.replace(
                "postgres://",
                "postgresql://",
                1
            )

        SQLALCHEMY_DATABASE_URI = database_url

    else:
        # Local development → SQLite
        SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
            BASE_DIR,
            "instance",
            "cyberguardian.db"
        )

    SQLALCHEMY_TRACK_MODIFICATIONS = False