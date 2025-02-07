from app import create_app
from flask_login import LoginManager
from app.blueprints.auth.models import User

app = create_app()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

if __name__ == "__main__":
    app.run(debug=True)
