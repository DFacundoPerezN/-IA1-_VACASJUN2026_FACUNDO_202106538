import os

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure_database(app):

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        os.getenv("DATABASE_URL")
    )

    app.config[
        "SQLALCHEMY_TRACK_MODIFICATIONS"
    ] = False

    db.init_app(app)