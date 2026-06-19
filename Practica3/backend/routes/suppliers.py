from flask import Blueprint
from flask import request
from flask import jsonify

from database.db import db

from models.supplier import Supplier

suppliers_bp = Blueprint(
    "suppliers",
    __name__,
    url_prefix="/suppliers"
)

@suppliers_bp.route( "", methods=["POST"])
def create_supplier():

    data = request.json

    supplier = Supplier(
        name=data["name"],
        nit=data["nit"],
        email=data.get("email"),
        phone=data.get("phone")
    )

    db.session.add( supplier)

    db.session.commit()

    return jsonify({
        "message":
        "Proveedor creado"
    }), 201

@suppliers_bp.route( "/<int:id>", methods=["GET"])
def get_supplier(id):

    supplier = Supplier.query.get_or_404(
        id
    )

    return jsonify({
        "id": supplier.id,
        "name": supplier.name,
        "nit": supplier.nit,
        "email": supplier.email,
        "phone": supplier.phone
    })

@suppliers_bp.route(
    "",
    methods=["GET"]
)
def get_suppliers():

    suppliers = Supplier.query.all()

    result = []

    for supplier in suppliers:

        result.append({
            "id": supplier.id,
            "name": supplier.name,
            "nit": supplier.nit,
            "email": supplier.email,
            "phone": supplier.phone
        })

    return jsonify(result)

@suppliers_bp.route( "/<int:id>", methods=["DELETE"])
def delete_supplier(id):

    supplier = Supplier.query.get_or_404( id)

    db.session.delete( supplier)

    db.session.commit()

    return jsonify({
        "message":
        "Proveedor eliminado"
    })