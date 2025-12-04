from flask import Blueprint, request
from app.database import db
from app.models.user import User
from flask_jwt_extended import create_access_token

import hashlib
import base64
import uuid
import hmac

auth_bp = Blueprint("auth", __name__)


def hash_password(password: str, salt_b64: str | None = None) -> tuple[str, str]:
    if salt_b64 is None:
        salt = uuid.uuid4().bytes
        salt_b64 = base64.urlsafe_b64encode(salt).decode("ascii")
    else:
        salt = base64.urlsafe_b64decode(salt_b64.encode("ascii"))

    sha = hashlib.sha512()
    sha.update(password.encode("utf-8") + salt)
    hashed_password_b64 = base64.urlsafe_b64encode(sha.digest()).decode("ascii")

    return hashed_password_b64, salt_b64


def verify_password(password: str, stored_hash_b64: str, stored_salt_b64: str) -> bool:
    candidate_hash_b64, _ = hash_password(password, stored_salt_b64)
    return hmac.compare_digest(stored_hash_b64, candidate_hash_b64)


@auth_bp.post("/register")
def register():
    data = request.json

    password_hash, salt_b64 = hash_password(data["password"])

    user = User(
        username=data["username"],
        first_name=data["first_name"],
        last_name=data["last_name"],
        password_hash=password_hash,  
        salt=salt_b64,                
        role="student",
        created_at="now",             
    )
    db.session.add(user)
    db.session.commit()
    return {"message": "User registered"}


@auth_bp.post("/login")
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()


    if not user or not verify_password(data["password"], user.password_hash, user.salt):
        return {"error": "Invalid credentials"}, 401

    token = create_access_token(identity=str(user.id))
    return {"token": token, "role": user.role, "username": user.username}
