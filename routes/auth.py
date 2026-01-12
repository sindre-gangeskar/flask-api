from flask import Blueprint, jsonify, request
from lib.auth import login
from flasgger import swag_from
auth_bp = Blueprint("auth", __name__)

@auth_bp.post("/login")
@swag_from("../docs/auth.yml")
def authenticate():
  data = request.get_json(force=True, silent=True) or {}
  print(data)
  username = data.get("username")
  password = data.get("password")
  
  if not username or not password:
    return jsonify(message="Username and password are required"), 400
  
  user_token = login(username, password)
  if not user_token: return jsonify(message="Incorrect username or password"), 401
  
  return jsonify(message="Successfully logged in", token=user_token)