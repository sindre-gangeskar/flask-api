from flask import Blueprint, jsonify
from flasgger import swag_from
index_bp = Blueprint("index", __name__)

@index_bp.get("/")
@swag_from("../docs/index.yml")
def index():
    return (jsonify(message="Welcome to Sindre Gangeskar's simple Flask API - documentation can be reached at /apidocs"), 200)
