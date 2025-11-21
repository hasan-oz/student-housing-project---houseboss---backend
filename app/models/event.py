from app.database import db

class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    date = db.Column(db.String, nullable=False)
    time = db.Column(db.String)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"))
