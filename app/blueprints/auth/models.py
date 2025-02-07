from flask_login import UserMixin
from app import mongo

class User(UserMixin):
    def __init__(self, user_id, firstname, lastname, password, email):
        self.id = user_id  # Required by Flask-Login
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.email = email

    @staticmethod
    def get(user_id):
        """Retrieve a user by ID from MongoDB"""
        user = mongo.db.users.find_one({"_id": user_id})
        if not user:
            return None
        return User(str(user["_id"]), user["firstname"], user["lastname"], user["email"], user["password"])

    @staticmethod
    def get_by_email(email):
        """Retrieve a user by email from MongoDB"""
        user = mongo.db.users.find_one({"email": email})
        if not user:
            return None
        return User(str(user["_id"]), user["firstname"], user["lastname"], user["email"], user["password"])