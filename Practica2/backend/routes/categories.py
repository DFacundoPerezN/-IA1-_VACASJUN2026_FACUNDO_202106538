from flask import Blueprint, jsonify
from database.mongodb import db

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