from flask import Flask
from create_user import create_user_blueprint
from login import login_blueprint
from version import version_blueprint
from games.second_game import second_game_blueprint
from games.first_game import first_game_blueprint
from games.third_game import third_game_blueprint
from games.fourth_game import fourth_game_blueprint


app = Flask(__name__)
app.register_blueprint(create_user_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(version_blueprint)
app.register_blueprint(first_game_blueprint)
app.register_blueprint(second_game_blueprint)
app.register_blueprint(third_game_blueprint)
app.register_blueprint(fourth_game_blueprint)


if __name__ == "__main__":
    app.run()