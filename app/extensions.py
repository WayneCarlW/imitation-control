from flask_pymongo import PyMongo
from flask_login import LoginManager

mongo = PyMongo()
login_manager = LoginManager()

def init_extensions(app):
    app.config["MONGO_URI"] = "mongodb://localhost:27017/imitation-control-app"
    mongo.init_app(app)
    login_manager.login_view = "auth.login"