from flask import Blueprint, jsonify, request
from lib.auth import login
auth_bp = Blueprint("auth", __name__)

@auth_bp.post("/login")
def authenticate():
  data = request.get_json() or {}
  username = data.get("username")
  password = data.get("password")
  
  if not username or not password:
    return jsonify(message="Username and password are required")
  
  user_token = login(username, password)
  if not user_token: return jsonify(message="Incorrect username or password"), 400
  
  return jsonify(message="Successfully logged in", token=user_token)