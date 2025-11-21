# admin feature, user list
from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.models.user import User

students_bp = Blueprint("students", __name__)

@students_bp.get("/")
@jwt_required()
def list_students():
    users = User.query.all()
    return [{
        "id": u.id,
        "username": u.username,
        "role": u.role
    } for u in users]
