from flask import Blueprint, jsonify
from app.extensions import mongo

test = Blueprint("test", __name__)

@test.route("/test_mongo")
def test_mongo():
    try:
        collections = mongo.db.list_collection_names()  # Fetch collections
        return jsonify({"status": "success", "collections": collections})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    
@test.route("/")
def test_home():
    return "Test home"
