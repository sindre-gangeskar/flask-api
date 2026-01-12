from flask import Blueprint, jsonify
from lib import utils
from middleware.auth import verify_jwt
from flasgger import swag_from

multiply_bp = Blueprint("multiply", __name__)

@multiply_bp.before_request
def _require_jwt():
  return verify_jwt()

@multiply_bp.get("/<int:param1>/<int:param2>")
@swag_from("../docs/multiply.yml")
def get_multiplication(param1, param2):
  total = utils.multiply(param1, param2)
  return jsonify(message=f"{param1} * {param2} = {total}")