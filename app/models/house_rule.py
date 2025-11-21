from app.database import db

class HouseRule(db.Model):
    __tablename__ = "house_rules"

    id = db.Column(db.Integer, primary_key=True)
    rule_text = db.Column(db.String, nullable=False)
    sort_order = db.Column(db.Integer, nullable=False)
