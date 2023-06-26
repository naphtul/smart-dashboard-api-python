from flask import Blueprint, jsonify, Response
from kasa_sdk_python.Kasa import Kasa

in_walls = Kasa()
app = Blueprint('in_walls', __name__, url_prefix='/in_walls')


@app.route('/', methods=['GET'])
def get_devices() -> Response:
    return jsonify(in_walls.discover())


@app.route('/<device_name>', methods=['POST'])
def toggle(device_name: str) -> Response:
    in_walls.toggle(device_name)
    return jsonify(code=201)
