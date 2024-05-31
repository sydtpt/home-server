from flask import Blueprint, request, make_response
from datetime import datetime
from flask_cors import cross_origin
from lib import deviceController


devices_routes = Blueprint(
    'devices', __name__,
    url_prefix='/api/devices')

@devices_routes.route('/')
def devices():
    controller = deviceController.deviceController()
    devices = controller.getDevices()
    
    for column_name, item in devices.iterrows():
        ip = item['domain']
        status = controller.get_device_status(ip)
        devices.at[column_name, 'status'] = status
    response = make_response(devices.to_json(orient='records'), 200)
    response.mimetype = "application/json"
    return response
    
@devices_routes.route('/<name>/on')
def turn_on(name):
    response = make_response({}, 200)
    response.mimetype = "application/json"
    return response

@devices_routes.route('/<name>/off')
def turn_off(name):
    response = make_response({}, 200)
    response.mimetype = "application/json"
    return response

