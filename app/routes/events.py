from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.database import db
from app.models.event import Event
from app.models.event_registration import EventRegistration
from datetime import datetime

events_bp = Blueprint("events", __name__)

@events_bp.post("/")
@jwt_required()
def create_event():
    user_id = int(get_jwt_identity())
    data = request.json

    event = Event(
        title=data["title"],
        description=data.get("description"),
        date=data["date"],
        time=data.get("time"),
        created_by=user_id
    )
    db.session.add(event)
    db.session.commit()
    return {"message": "Event created"}

@events_bp.post("/register/<int:event_id>")
@jwt_required()
def join_event(event_id):
    user_id = int(get_jwt_identity())

    registration = EventRegistration(
        event_id=event_id,
        user_id=user_id,
        registered_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    db.session.add(registration)
    db.session.commit()

    return {"message": "Registered for event"}

@events_bp.get("/")
@jwt_required()
def list_events():
    events = Event.query.all()
    return [
        {
            "id": e.id,
            "title": e.title,
            "description": e.description,
            "date": e.date,
            "time": e.time,
            "created_by": e.created_by
        } for e in events
    ]
