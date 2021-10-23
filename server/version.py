from flask import jsonify, Blueprint

version_blueprint = Blueprint('version_blueprint', __name__)


@version_blueprint.route("/", methods=["GET"])
def index_api():
    return jsonify(version="1.0.1")
