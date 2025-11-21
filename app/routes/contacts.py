from flask import Blueprint
from app.models.contacts import Contact

contacts_bp = Blueprint("contacts", __name__)

@contacts_bp.get("/")
def get_contacts():
    contacts = Contact.query.all()
    return [
        {"id": c.id, "label": c.label, "phone": c.phone, "email": c.email}
        for c in contacts
    ]
