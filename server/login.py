from flask import jsonify, request, Blueprint
import json

login_blueprint = Blueprint('login', __name__)


@login_blueprint.route("/api/auth/login", methods=["POST"])
def login():
    request_body = request.get_json()
    if not request_body:
        return jsonify(
            status=False,
            reason="Missing required body params: 'username' and 'password'",
        )
    u = request_body.get("username", None)
    p = request_body.get("password", None)

    if u is None or p is None:
        return jsonify(
            status=False,
            reason="Missing required body params: 'username' and 'password'",
        )

    with open("users.json") as data_json:
        users = json.load(data_json)

    for i in users:
        if i.get("username") == u:
            if p != i.get("password"):
                break
            return jsonify(status=True)
    return jsonify(status=False, reason="username or password is not correct")
