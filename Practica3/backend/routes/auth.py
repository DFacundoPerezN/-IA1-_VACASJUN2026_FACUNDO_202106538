import os
import jwt
import datetime

from flask import Blueprint
from flask import request
from flask import jsonify

from werkzeug.security import (
    check_password_hash
)

from models.user import User

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)

@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.json

    username = data.get(
        "username"
    )

    password = data.get(
        "password"
    )

    user = User.query.filter_by(
        username=username
    ).first()

    if not user:

        return jsonify({
            "message":
            "Credenciales inválidas"
        }), 401

    if not check_password_hash(
        user.password,
        password
    ):

        return jsonify({
            "message":
            "Credenciales inválidas"
        }), 401

    token = jwt.encode(
        {
            "user_id": user.id,
            "username": user.username,
            "exp":
            datetime.datetime.now(
                datetime.timezone.utc
            ) + datetime.timedelta(
                hours=12
            )
        },
        os.getenv(
            "JWT_SECRET"
        ),
        algorithm="HS256"
    )

    return jsonify({
        "token": token
    })