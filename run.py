from app import create_app
from flask_login import LoginManager
from app.blueprints.auth.models import User

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
