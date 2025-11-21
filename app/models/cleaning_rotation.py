from app.database import db

class CleaningRotation(db.Model):
    __tablename__ = "cleaning_rotation"

    id = db.Column(db.Integer, primary_key=True)
    rotation_index = db.Column(db.Integer, nullable=False)
    stored_week = db.Column(db.String, nullable=False)
