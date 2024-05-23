from flask import Blueprint, request, make_response
from datetime import datetime
from flask_cors import cross_origin
import csv

air_routes = Blueprint(
    'air', __name__,
    url_prefix='/api/air')

cross_origin()
@air_routes.route('/')
def air():
    response = make_response({'temperature': 20.1, 'humidity': 60}, 200)
    response.mimetype = "application/json"
    return response
          
cross_origin()
@air_routes.route('/summary')
def summary():
    response = make_response(
        {
            'max_temperature': 20.1,
            'avg_temperature': 16.2,
            'max_humidity': 70,
            'avg_humidity': 44
        }, 200)
    response.mimetype = "application/json"
    return response

cross_origin()
@air_routes.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        content = request.get_json()
        with open("./data/air.csv", 'a') as f:
            writer = csv.writer(f)
            writer.writerow([content['temperature'], content['humidity'], datetime.now()])
            f.close()
        response = make_response({}, 201)
        return response
    else:
        print("get")
        response = make_response([], 200)
        response.mimetype = "application/json"
        return response            
    
    
