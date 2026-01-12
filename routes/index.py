from flask import Blueprint, jsonify

index_bp = Blueprint("index", __name__)

@index_bp.get("/")
def index():
    return (jsonify(message="Welcome to the index of this simple Flask API"), 200)
