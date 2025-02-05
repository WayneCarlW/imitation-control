from flask import Flask
from config import Config
from app.blueprints.auth import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)


    #Registration of blueprints
    app.register_blueprint(auth_bp)

    return app
