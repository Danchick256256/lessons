import math
import random

from flask import Blueprint, jsonify, request

fourth_game_blueprint = Blueprint('fourth_game_blueprint', __name__)


@fourth_game_blueprint.route('/fourth_game', methods=['POST'])
def fourth_game():
    if request.get_json():
        circle = 10 ** 2 + 10 ** 2
        sqrt = round(math.sqrt(circle))
        counter = 0
        for i in range(10):
            x, y = random.randint(0, sqrt * 2), random.randint(0, sqrt * 2)
            score = (x + y) * 2
            if x <= sqrt and y <= sqrt:
                counter += 1
        return jsonify(status=True, value=counter, score=score)