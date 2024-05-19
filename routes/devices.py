from flask import Blueprint, request, make_response
from datetime import datetime
from flask_cors import cross_origin


devices_routes = Blueprint(
    'devices', __name__,
    url_prefix='/api/devices')

cross_origin()
@devices_routes.route('/')
def list_cities():
    response = make_response([], 200)
    response.mimetype = "application/json"
    return response
    
    
