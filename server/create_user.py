from typing import Dict, List
from flask import jsonify, request, Blueprint
import json

create_user_blueprint = Blueprint('create_user', __name__)


@create_user_blueprint.route("/api/create_user", methods=["POST"])
def create_user():
    req = request.get_json()
    if not req:
        return jsonify(
            status=False,
            reason="Missing required body params: 'username' and 'password'",
        )
    u = req.get("username", None)
    p = req.get("password", None)

    if u is None or p is None:
        return jsonify(
            status=False,
            reason="Missing required body params: 'username' and 'password'",
        )
    with open("users.json", mode="r") as file:
        users: List[Dict[str, str]] = json.load(file)
    with open("users.json", mode="w") as file:
        users.append({"username": u, "password": p})
        json.dump(users, file)
    return jsonify(status=True)
