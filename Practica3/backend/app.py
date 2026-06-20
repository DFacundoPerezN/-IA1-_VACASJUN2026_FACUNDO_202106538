import os

from dotenv import load_dotenv

from flask import Flask

#Modelos qeu usamos para la base de datos en postgreSQL
from models.user import User
from models.supplier import Supplier
from models.invoice import Invoice
from models.processing_log import ProcessingLog

from database.db import (
    configure_database,
    db
)

# Rutas de los endpoints
from routes.auth import auth_bp
from routes.suppliers import suppliers_bp
from routes.invoices import invoices_bp
from routes.processing_log import logs_bp

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

# Agregar blueprints o hulleas de los endpoints
app.register_blueprint( auth_bp)
app.register_blueprint( suppliers_bp)
app.register_blueprint( invoices_bp)
app.register_blueprint( logs_bp)

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )