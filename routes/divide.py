from flask import Blueprint, jsonify
from lib import utils
from middleware.auth import verify_jwt
from flasgger import swag_from

divide_bp = Blueprint("divide", __name__)

@divide_bp.before_request
def _require_jwt():
  return verify_jwt()

@divide_bp.get("/<int:param1>/<int:param2>")
@swag_from("../docs/divide.yml")
def get_division(param1, param2):
  total = utils.divide(param1, param2)
  return jsonify(message=f"{param1} / {param2} = {total}")