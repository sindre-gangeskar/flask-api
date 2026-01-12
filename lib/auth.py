import json
import os
import jwt

from dotenv import load_dotenv
import os

load_dotenv()
_secret = os.getenv("JWT_SECRET")
if _secret is None:
    raise RuntimeError("JWT_SECRET environment variable is not set")

JWT_SECRET: str = _secret

def login(username: str, password: str):
    with open(os.path.join(os.path.dirname(__file__), "..", "data", "users.json")) as file:
        data = json.load(file)
        users = data["users"]

        matching_user = next((user for user in users if user["username"] == username), None)
        if not matching_user or matching_user["password"] != password:
            return None

        payload = {"username": username}
        token = jwt.encode(payload, JWT_SECRET)
        return token
