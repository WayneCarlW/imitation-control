from flask import Flask
from dotenv import load_dotenv
import os
from config.config import config
from app.extensions import mongo
from app.blueprints.auth.routes import auth
from app.blueprints.dashboard.routes import dashboard
from app.routes import test
def create_app(config_name="development"):
    load_dotenv("./env")
    app = Flask(__name__, template_folder="../templates")
    app.config.from_object(config[config_name])

    mongo.init_app(app)


    #Registration of blueprints
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(dashboard, url_prefix="/dashboard")
    app.register_blueprint(test, url_prefix="/")

    return app
