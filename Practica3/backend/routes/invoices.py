import os
import uuid

from flask import Blueprint
from flask import request
from flask import jsonify

from models.invoice import Invoice
from database.db import db

import tempfile
import os
from services.ocr_service import (extract_text_from_image, extract_text_from_pdf)

from services.invoice_parser import (extract_invoice_data)
from services.validation_service import (validate_invoice)

invoices_bp = Blueprint("invoices", __name__, url_prefix="/invoices")

ALLOWED_EXTENSIONS = {
    "pdf",
    "jpg",
    "jpeg",
    "png"
}

def allowed_file(filename):

    if  "." in filename: # si hay punto
        extension = filename.rsplit( ".",1)[1].lower()
        # si tiene extension permitida
        if extension in ALLOWED_EXTENSIONS:
            return True
        
    return False

@invoices_bp.route("/upload", methods=["POST"])
def upload_invoice():

    if "file" not in request.files:

        return jsonify({ "message": "Archivo requerido"}), 400

    file = request.files["file"]

    if file.filename == "":

        return jsonify({
            "message":
            "Archivo inválido, falta nombre"
        }), 400

    if not allowed_file(file.filename):

        return jsonify({
            "message":
            "Formato no permitido"
        }), 400

    extension = file.filename.split(".")[-1]

    filename = f"{uuid.uuid4()}.{extension}"

    invoice = Invoice(
        original_filename=filename,
        status="UPLOADED"
    )

    db.session.add(
        invoice
    )

    db.session.commit()

    return jsonify({
        "id": invoice.id,
        "original_filename": filename,
        "status": "UPLOADED"
    })

@invoices_bp.route("",methods=["GET"])
def get_invoices():

    invoices = Invoice.query.all()

    result = []

    for invoice in invoices:

        result.append({
            "id": invoice.id,
            "invoice_number":
                invoice.invoice_number,
            "status":
                invoice.status,
            "original_filename":
                invoice.original_filename
        })

    return jsonify(result)

@invoices_bp.route("/process", methods=["POST"])
def process_invoice():


    if "file" not in request.files:

        return {
            "message":
            "Archivo requerido"
        }, 400

    file = request.files["file"]

    if not allowed_file(file.filename):

        return {
            "message":
            "Formato inválido"
        }, 400
    
    extension = file.filename.split(".")[-1].lower()

    with tempfile.NamedTemporaryFile(suffix=f".{extension}",delete=False) as temp:

        file.save( temp.name)

        temp_path = temp.name

    try:

        if extension == "pdf":

            text = extract_text_from_pdf(temp_path) 

        else:

            text = extract_text_from_image(temp_path)
        print("OCR RESULT:", flush=True)
        print(text, flush=True)

        data =  extract_invoice_data(text)
        
        errors = validate_invoice(data)

        if errors:

            return {
                "status":"ERROR",
                "errors":  errors,
                "data":data
            }, 400
       
        invoice = Invoice(

            original_filename= file.filename,

            invoice_number= data["invoice_number"],

            nit= data["nit"],

            subtotal= data["subtotal"],

            tax= data["tax"],

            total= data["total"],

            status="PROCESSED"
        )

        db.session.add(invoice)

        db.session.commit()

        return {
                "status": "SUCCESS",
                "invoice_id": invoice.id,
                "data": data
            }
    

    except Exception as e:          
        return {
            "status":"ERROR",
            "message":  "Algo ocurrio mientras se haceia ocr",
            "error":str(e)
        }, 400

    finally:

        if os.path.exists(temp_path):
            os.remove(temp_path)