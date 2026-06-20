from werkzeug.security import (
    generate_password_hash
)

from app import app
from database.db import db

from models.user import User

with app.app_context():

    user = User.query.filter_by(
        username="admin"
    ).first()

    if not user:

        user = User(
            username="admin",
            password=
            generate_password_hash(
                "faxx123"
            ),
            email= "3607834730101@ingenieria.usac.edu.gt"
        )

        db.session.add(user)

        db.session.commit()

        print(
            "Usuario creado"
        )