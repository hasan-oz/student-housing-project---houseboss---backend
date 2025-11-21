from app.database import db

class Contact(db.Model):
    __tablename__ = "contacts"

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String, nullable=False)
    phone = db.Column(db.String)
    email = db.Column(db.String)
