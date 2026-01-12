from flask import Blueprint, jsonify
from lib import utils
from middleware.auth import verify_jwt
add_bp = Blueprint("add", __name__)

# Middleware that is run for this specific blueprint endpoint - protected and requires a valid Bearer jwt token to be included in the request
# via the Authorization header
@add_bp.before_request
def _require_jwt():
  return verify_jwt()

@add_bp.get("/<int:param1>/<int:param2>")
def get_addition(param1, param2):
  total = utils.add(param1, param2)
  return jsonify(message=f"{param1} + {param2} = {total}")