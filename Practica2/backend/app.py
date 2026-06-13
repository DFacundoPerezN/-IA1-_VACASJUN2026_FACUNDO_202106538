# py -3.10 -m venv venv
# .\venv\Scripts\Activate.ps1
from flask import Flask
from flask_cors import CORS

from routes.auth import auth_bp
from routes.categories import categories_bp
from routes.questions import questions_bp
from routes.telegram import telegram_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(auth_bp)
app.register_blueprint(categories_bp)
app.register_blueprint(questions_bp)
app.register_blueprint(telegram_bp)

if __name__ == "__main__":
    app.run(debug=True)