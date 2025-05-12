from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config
from dotenv import load_dotenv
load_dotenv()
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    jwt.init_app(app)
    CORS(app)

    from app.routes.auth import auth_bp
    from app.routes.devices import devices_bp
    from app.routes.locations import locations_bp
    from app.routes.calls import calls_bp
    from app.routes.sms import sms_bp
    from app.routes.apps import apps_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(devices_bp, url_prefix='/api/devices')
    app.register_blueprint(locations_bp, url_prefix='/api/locations')
    app.register_blueprint(calls_bp, url_prefix='/api/calls')
    app.register_blueprint(sms_bp, url_prefix='/api/sms')
    app.register_blueprint(apps_bp, url_prefix='/api/apps')

    with app.app_context():
        db.create_all()

    return app
