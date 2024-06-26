from flask import Blueprint, request, make_response
from datetime import datetime
from flask_cors import cross_origin
import csv

soil_routes = Blueprint(
    'soil', __name__,
    url_prefix='/api/soil')

cross_origin()
@soil_routes.route('/')
def soil():
    response = make_response({'temperature': 20.1, 'humidity': 60}, 200)
    response.mimetype = "application/json"
    return response
   
cross_origin()
@soil_routes.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        content = request.get_json()
        with open("./data/soil.csv", 'a') as f:
            writer = csv.writer(f)
            writer.writerow([content['humidity_soil'],'sensor_1' ,datetime.now()])
            f.close()
        response = make_response({}, 201)
        return response
    else:
        response = make_response([], 200)
        response.mimetype = "application/json"
        return response            
    
    
