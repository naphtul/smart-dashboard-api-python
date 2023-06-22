from hydrawise_irrigation.Hydrawise import Hydrawise
from flask import Blueprint, request, send_from_directory

irrigation = Hydrawise()
app = Blueprint('irrigation', __name__, url_prefix='/irrigation')


@app.route('/controllers', methods=['GET'])
def get_controllers_schedules() -> dict:
    return irrigation.get_schedules()


@app.route('/zones/<zone_id>', methods=['POST'])
def run_zone(zone_id: str) -> dict:
    run_time = request.args.get('run_time', 0)
    return irrigation.run_zone(zone_id, run_time)


@app.route('/zones/<zone_id>', methods=['DELETE'])
def stop_zone(zone_id: str) -> dict:
    return irrigation.stop_zone(zone_id)
