from flask import Blueprint, request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.json

    username = data.get("username")
    password = data.get("password")

    if (username == "IA1-User"
        and
        password == "IA1-password@_new"):

        return jsonify({
            "message": "Login exitoso"
        }), 200

    return jsonify({
        "message": "Credenciales inválidas"
    }), 401