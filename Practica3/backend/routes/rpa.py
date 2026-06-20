from flask import Blueprint
from flask import render_template
from flask import request
from flask import jsonify

from database.db import db
from models.invoice import Invoice
from models.rpa_record import RPARecord

from services.rpa_service import execute_rpa

rpa_bp = Blueprint(
    "rpa",
    __name__
)

@rpa_bp.route("/rpa-demo")
def rpa_demo():

    return render_template(
        "rpa_form.html"
    )

@rpa_bp.route("/rpa/records")
def get_rpa_records():

    records = RPARecord.query.all()

    result = []

    for record in records:

        result.append({
            "id": record.id,
            "invoice_number": record.invoice_number,
            "supplier": record.supplier,
            "nit": record.nit,
            "subtotal": float(record.subtotal)
                if record.subtotal else None,
            "tax": float(record.tax)
                if record.tax else None,
            "total": float(record.total)
                if record.total else None
        })

    return jsonify(result), 200


@rpa_bp.route("/rpa/process/<int:invoice_id>",methods=["POST"])
def process_rpa(invoice_id):

    invoice = Invoice.query.get(invoice_id)

    if not invoice:

        return {
            "message":
            "Factura no encontrada"
        }, 404

    execute_rpa(invoice)

    return {
        "message": "RPA ejecutado"
    }

@rpa_bp.route("/rpa/save",methods=["POST"])
def save_rpa():

    data = request.json

    record = RPARecord(
        invoice_number=data["invoice_number"],
        supplier=data["supplier"],
        nit=data["nit"],
        total=data["total"]
    )

    db.session.add(record)
    db.session.commit()

    return {
        "message": "Guardado"
    }