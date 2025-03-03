from flask import Flask
from dotenv import load_dotenv
import os
from config.config import config
from app.extensions import init_extensions, login_manager
from app.blueprints.auth.routes import auth
from app.blueprints.dashboard.routes import dashboard
from app.blueprints.auth.models import User
from app.routes import test

def create_app(config_name="development"):
    load_dotenv("./env")
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config.from_object(config[config_name])

    init_extensions(app)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)
        
    #Registration of blueprints
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(dashboard, url_prefix="/dashboard")
    app.register_blueprint(test, url_prefix="/")

    return app
