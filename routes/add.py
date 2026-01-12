from flask import Blueprint, jsonify
from lib import utils
from middleware.auth import verify_jwt
from flasgger import swag_from
add_bp = Blueprint("add", __name__)

@add_bp.before_request
def _require_jwt():
  return verify_jwt()

@add_bp.get("/<int:param1>/<int:param2>")
@swag_from("../docs/add.yml")
def get_addition(param1, param2):
  total = utils.add(param1, param2)
  return jsonify(message=f"{param1} + {param2} = {total}")