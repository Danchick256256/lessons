from flask import Blueprint, jsonify, request

third_game_blueprint = Blueprint('third_game_blueprint', __name__)


@third_game_blueprint.route('/third_game', methods=['POST'])
def third_game():
    value = int(request.get_json()["value"])
    fib1 = fib2 = 1
    i = 2
    if value == 1 or value == 0:
        fib_sum = 1
    elif value < 0:
        return jsonify(status=False, reason="Negative number")
    else:
        for i in range(value):
            fib_sum = fib2 + fib1
            fib1, fib2 = fib2, fib_sum
    return jsonify(status=True, value=fib_sum)
