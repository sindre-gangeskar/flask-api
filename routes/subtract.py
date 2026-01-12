from flask import Blueprint, jsonify
from lib import utils
from middleware.auth import verify_jwt
from flasgger import swag_from

subtract_bp = Blueprint("subtract", __name__)

@subtract_bp.before_request
def _require_jwt():
  return verify_jwt()

@subtract_bp.get("/<int:param1>/<int:param2>")
@swag_from("../docs/subtract.yml")
def get_subtraction(param1, param2):
  total = utils.subtract(param1, param2)
  return jsonify(message=f"{param1} - {param2} = {total}")