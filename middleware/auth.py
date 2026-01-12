from flask import request, jsonify
import jwt
from lib.auth import JWT_SECRET

def verify_jwt():
  auth_header = request.headers.get("Authorization")
  if not auth_header or not auth_header.startswith("Bearer "):
    return jsonify(message="Login required"), 401
  
  token = auth_header.split(" ", 1)[1].strip()
  try:
      jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
      return None 
  except jwt.ExpiredSignatureError:
    return jsonify(message="Token has expired, please log in again"), 401
  except jwt.InvalidTokenError:
    return jsonify(message="Invalid or malformed token, please log in again"), 401