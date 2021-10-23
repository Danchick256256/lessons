from flask import Blueprint, jsonify, request
import json

second_game_blueprint = Blueprint('second_game_blueprint', __name__)


@second_game_blueprint.route('/second_game', methods=['POST'])
def second_game():
    user_data = request.get_json()
    try:
        value = int(user_data['value'])
        with open("client.json", mode="w") as file:
            data = {"value": value, "counter": "0", "left": "0", "right": str(value // 2), "current": str(value // 2)}
            json.dump(data, file)
        return jsonify(status=False, value=value)
    except ValueError:
        if user_data['value'] == 'равно':
            with open("client.json", mode="r") as file:
                data = json.load(file)
            return jsonify(status=True, value=data["current"])
        elif user_data['value'] == 'меньше':
            with open("client.json", mode="r") as file:
                data = json.load(file)

            with open("client.json", mode="w") as file:
                data["right"] = data["current"]
                data["counter"] = int(data["counter"]) + 1
                data["current"] = (int(data["left"]) + int(data["right"])) // 2
                data = {"value": data["value"], "counter": data["counter"], "left": data["left"],
                        "right": data["right"], "current": data["current"]}
                json.dump(data, file)

            return jsonify(status=False, value=data["current"])
        elif user_data['value'] == 'больше':
            with open("client.json", mode="r") as file:
                data = json.load(file)

            with open("client.json", mode="w") as file:
                data["left"] = data["current"]
                data["counter"] = int(data["counter"]) + 1
                data["current"] = (int(data["left"]) + int(data["right"])) // 2
                data = {"value": data["value"], "counter": data["counter"], "left": data["left"],
                        "right": data["right"], "current": data["current"]}
                json.dump(data, file)

            return jsonify(status=False, value=data["current"])
