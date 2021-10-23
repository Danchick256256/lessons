from flask import Blueprint, jsonify, request
import random

first_game_blueprint = Blueprint('first_game_blueprint', __name__)


@first_game_blueprint.route('/first_game', methods=['POST'])
def first_game():
    user_data = request.get_json()
    value = user_data["value"]
    result = ""
    for i in value:
        if random.randint(0, 1) == 1:
            result += i.lower()
        else:
            result += i.upper()
    return jsonify(value=result)
