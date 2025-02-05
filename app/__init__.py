from flask import Flask
from dotenv import load_dotenv
import os
from config.config import config
from app.extensions import mongo
from app.blueprints.auth import auth_bp

def create_app(config_name="development"):
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    mongo.init_app(app)


    #Registration of blueprints
    app.register_blueprint(auth_bp)

    return app
