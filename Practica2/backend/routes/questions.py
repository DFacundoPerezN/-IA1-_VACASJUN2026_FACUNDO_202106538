from flask import Blueprint, jsonify
from database.mongodb import db

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