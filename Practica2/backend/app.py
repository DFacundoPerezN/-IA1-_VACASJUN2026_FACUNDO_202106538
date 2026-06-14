# py -3.10 -m venv venv
# .\venv\Scripts\Activate.ps1
from flask import Flask
from flask_cors import CORS

from routes.auth import auth_bp
from routes.categories import categories_bp
from routes.questions import questions_bp
from routes.telegram import telegram_bp
from services.telegram_listener import (
    start_listener
)
from threading import Thread

app = Flask(__name__)

CORS(app)

app.register_blueprint(auth_bp)
app.register_blueprint(categories_bp)
app.register_blueprint(questions_bp)
app.register_blueprint(telegram_bp)

if __name__ == "__main__":

    telegram_thread = Thread(
        target=start_listener,
        daemon=True
    )

    telegram_thread.start()

    app.run(
    host="0.0.0.0",
    port=5000,
    debug=False
    )