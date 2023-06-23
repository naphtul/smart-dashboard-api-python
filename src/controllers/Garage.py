from flask import Blueprint, jsonify, Response
from myq.MyQ import MyQ

garage = MyQ()
app = Blueprint('garage', __name__, url_prefix='/garage')


@app.route('/', methods=['GET'])
def get_doors() -> dict:
    return garage.get_garage_doors()


@app.route('/doors/<door_name>', methods=['POST'])
def open_door(door_name: str) -> Response:
    res = garage.open_garage_door(door_name)
    return jsonify(result=res, code=201 if res else 500)


@app.route('/doors/<door_name>', methods=['DELETE'])
def close_door(door_name: str) -> Response:
    res = garage.close_garage_door(door_name)
    return jsonify(result=res, code=200 if res else 500)
