import os

from dotenv import load_dotenv

from flask import Flask

from models.user import User

from database.db import (
    configure_database,
    db
)

from routes.auth import auth_bp

load_dotenv()

app = Flask(__name__)

configure_database(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():

    return {
        "message":
        "Invoice System API"
    }

@app.route("/health")
def health():

    return {
        "message":
        "Todo OK"
    }

app.register_blueprint(
    auth_bp
)

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )