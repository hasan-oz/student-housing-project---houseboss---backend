from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.database import db
from app.models.complaint import Complaint
from datetime import datetime

complaints_bp = Blueprint("complaints", __name__)

@complaints_bp.post("/")
@jwt_required()
def create_complaint():
    user_id = int(get_jwt_identity())
    data = request.json
    complaint = Complaint(
        user_id=user_id,
        description=data["description"],
        created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    db.session.add(complaint)
    db.session.commit()
    return {"message": "Complaint created"}

@complaints_bp.get("/")
@jwt_required()
def list_complaints():
    complaints = Complaint.query.all()
    return [
        {
            "id": c.id,
            "user_id": c.user_id,
            "description": c.description,
            "created_at": c.created_at
        } for c in complaints
    ]
