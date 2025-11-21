from app.database import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    role = db.Column(db.String, default="student", nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    created_at = db.Column(db.String, nullable=False)
