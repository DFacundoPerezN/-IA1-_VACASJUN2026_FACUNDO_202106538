from flask import Blueprint, jsonify, request
from database.mongodb import db
from bson import ObjectId

questions_bp = Blueprint(
    "questions",
    __name__,
    url_prefix="/questions"
)

@questions_bp.route("", methods=["GET"])
def get_questions():

    questions = []

    for question in db.questions.find():

        questions.append({
            "id": str(question["_id"]),
            "question": question["question"],
            "answer": question["answer"],
            "category_id": str(question["category_id"])
        })

    return jsonify(questions)

@questions_bp.route("", methods=["POST"])
def create_question():

    data = request.json

    result = db.questions.insert_one({
        "question": data["question"],
        "answer": data["answer"],
        "category_id": ObjectId(data["category_id"])
    })

    return jsonify({
        "message": "Pregunta creada",
        "id": str(result.inserted_id)
    }), 201

@questions_bp.route("/<id>", methods=["PUT"])
def update_question(id):

    data = request.json

    result = db.questions.update_one(
        {"_id": ObjectId(id)},
        {
            "$set": {
                "question": data["question"],
                "answer": data["answer"],
                "category_id": ObjectId(data["category_id"])
            }
        }
    )

    if result.matched_count == 0:
        return jsonify({
            "message": "Pregunta no encontrada"
        }), 404

    return jsonify({
        "message": "Pregunta actualizada"
    })

@questions_bp.route("/<id>", methods=["DELETE"])
def delete_question(id):

    result = db.questions.delete_one({
        "_id": ObjectId(id)
    })

    if result.deleted_count == 0:
        return jsonify({
            "message": "Pregunta no encontrada"
        }), 404

    return jsonify({
        "message": "Pregunta eliminada"
    })

@questions_bp.route("/with-category", methods=["GET"])
def get_questions_with_category():

    questions = []

    for question in db.questions.find():

        category = db.categories.find_one({
            "_id": question["category_id"]
        })

        questions.append({
            "id": str(question["_id"]),
            "question": question["question"],
            "answer": question["answer"],
            "category": category["name"] if category else ""
        })

    return jsonify(questions)

@questions_bp.route("/search", methods=["POST"])
@questions_bp.route("/answer", methods=["POST"])
def search_question():

    data = request.json

    question_text = data.get("question", "").strip()

    question = db.questions.find_one({
        "question": {
            "$regex": f"^{question_text}$",
            "$options": "i"
        }
    })

    if not question:
        return jsonify({
            "found": False,
            "answer": "Lo siento, no encontré una respuesta para tu consulta."
        })

    return jsonify({
        "found": True,
        "answer": question["answer"]
    })

@questions_bp.route("/category-name/<name>", methods=["GET"])
def get_questions_by_category_name(name):

    category = db.categories.find_one({
        "name": name
    })

    if not category:
        return jsonify({
            "message": "Categoría no encontrada"
        }), 404

    questions = []

    for question in db.questions.find({
        "category_id": category["_id"]
    }):

        questions.append({
            "id": str(question["_id"]),
            "question": question["question"],
            "answer": question["answer"]
        })

    return jsonify(questions)
