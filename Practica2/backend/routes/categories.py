from flask import Blueprint, jsonify, request
from database.mongodb import db
from bson import ObjectId

categories_bp = Blueprint(
    "categories",
    __name__,
    url_prefix="/categories"
)

@categories_bp.route("", methods=["GET"])
def get_categories():

    categories = []

    for category in db.categories.find():

        categories.append({
            "id": str(category["_id"]),
            "name": category["name"]
        })

    return jsonify(categories)

@categories_bp.route("", methods=["POST"])
def create_category():

    data = request.json

    result = db.categories.insert_one({
        "name": data["name"]
    })

    return jsonify({
        "message": "Categoría creada",
        "id": str(result.inserted_id)
    }), 201


@categories_bp.route("/<id>", methods=["PUT"])
def update_category(id):

    data = request.json

    result = db.categories.update_one(
        {"_id": ObjectId(id)},
        {
            "$set": {
                "name": data["name"]
            }
        }
    )

    if result.matched_count == 0:
        return jsonify({
            "message": "Categoría no encontrada"
        }), 404

    return jsonify({
        "message": "Categoría actualizada"
    })

@categories_bp.route("/<id>", methods=["DELETE"])
def delete_category(id):

    result = db.categories.delete_one({
        "_id": ObjectId(id)
    })

    if result.deleted_count == 0:
        return jsonify({
            "message": "Categoría no encontrada"
        }), 404

    return jsonify({
        "message": "Categoría eliminada"
    })