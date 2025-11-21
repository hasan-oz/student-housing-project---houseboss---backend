from flask import Flask
from app.config import Config
from app.database import db
from flask_jwt_extended import JWTManager
from app.routes.students import students_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    JWTManager(app)

    # Import routes
    from app.routes.auth import auth_bp
    from app.routes.complaints import complaints_bp
    from app.routes.events import events_bp
    from app.routes.rules import rules_bp
    from app.routes.contacts import contacts_bp

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(complaints_bp, url_prefix="/complaints")
    app.register_blueprint(events_bp, url_prefix="/events")
    app.register_blueprint(rules_bp, url_prefix="/rules")
    app.register_blueprint(contacts_bp, url_prefix="/contacts")
    app.register_blueprint(students_bp, url_prefix="/students")

    return app
