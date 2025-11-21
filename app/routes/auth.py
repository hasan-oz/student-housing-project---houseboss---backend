from flask import Blueprint, request
from app.database import db
from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.post("/register")
def register():
    data = request.json
    user = User(
        username=data["username"],
        first_name=data["first_name"],
        last_name=data["last_name"],
        password_hash=generate_password_hash(data["password"]),
        role="student",
        created_at="now"
    )
    db.session.add(user)
    db.session.commit()
    return {"message": "User registered"}

@auth_bp.post("/login")
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()

    if not user or not check_password_hash(user.password_hash, data["password"]):
        return {"error": "Invalid credentials"}, 401

    token = create_access_token(identity=str(user.id))
    return {"token": token, "role": user.role, "username": user.username}
