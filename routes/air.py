from flask import Blueprint, request, make_response
from datetime import datetime
from flask_cors import cross_origin
from lib.airController import airController

air_routes = Blueprint(
    'air', __name__,
    url_prefix='/api/air')

cross_origin()
@air_routes.route('/')
def air():
    air = airController()
    temperature = air.temperature()
    humidity = air.humidity()
    response = make_response({'temperature': temperature, 'humidity': humidity}, 200)
    response.mimetype = "application/json"
    return response
          
cross_origin()
@air_routes.route('/log', methods=['GET', 'POST'])
def log():
    air = airController()
    if request.method == 'POST':
        content = request.get_json()
        air.log(content['temperature'], content['humidity'])
        response = make_response({}, 201)
        return response
    else:
        print("get")
        response = make_response([], 200)
        response.mimetype = "application/json"
        return response            
    
    
