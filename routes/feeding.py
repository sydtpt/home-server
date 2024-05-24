from flask import Blueprint, request, make_response, jsonify
from datetime import datetime, timedelta
from flask_cors import cross_origin
import csv
import pandas as pd
from lib import airController, feedingController

feeding_routes = Blueprint(
    'feeding', __name__,
    url_prefix='/api/feeding')

cross_origin()
@feeding_routes.route('/', methods=['GET'], strict_slashes=False)
def summary():
    feeding = feedingController.feedingController()
    air = airController.airController()
    feeding_data = {
        'watter': feeding.lastSoilWatter('monstera'),
        'leaf': feeding.lastLeafFeeding('monstera'),
        'soil': feeding.lastSoilFeeding('monstera'),
        'max_temperature': air.max_temperature(48),
        'avg_temperature':  air.avg_temperature(48),
        'max_humidity':  air.max_humidity(48),
        'avg_humidity':  air.avg_humidity(48)
    }
    response = make_response(jsonify(feeding_data), 200)
    response.mimetype = "application/json"
    return response
            
cross_origin()
@feeding_routes.route('/leaf', methods=['POST'])
def leaf():
    if request.method == 'POST':
        content = request.get_json()
        with open("./data/leaf-fert.csv", 'a') as f:
            writer = csv.writer(f)
            writer.writerow([content['plant'] ,datetime.now()])
            f.close()
        response = make_response({}, 201)
        return response
    else:
        response = make_response([], 200)
        response.mimetype = "application/json"
        return response
    

cross_origin()
@feeding_routes.route('/water', methods=['POST'])
def water():
    if request.method == 'POST':
        content = request.get_json()
        with open("./data/watering.csv", 'a') as f:
            writer = csv.writer(f)
            writer.writerow([content['plant'] ,datetime.now()])
            f.close()
        response = make_response({}, 201)
        return response
    else:
        response = make_response([], 200)
        response.mimetype = "application/json"
        return response

cross_origin()
@feeding_routes.route('/soil', methods=['POST'])
def soil():
    if request.method == 'POST':
        content = request.get_json()
        with open("./data/soil-fert.csv", 'a') as f:
            writer = csv.writer(f)
            writer.writerow([content['plant'] ,datetime.now()])
            f.close()
        response = make_response({}, 201)
        return response
    else:
        response = make_response([], 200)
        response.mimetype = "application/json"
        return response
    
