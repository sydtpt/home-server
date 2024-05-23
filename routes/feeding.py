from flask import Blueprint, request, make_response, jsonify
from datetime import datetime, timedelta
from flask_cors import cross_origin
import csv
import pandas as pd

feeding_routes = Blueprint(
    'feeding', __name__,
    url_prefix='/api/feeding')

cross_origin()
@feeding_routes.route('/', methods=['GET'], strict_slashes=False)
def summary():

    air_history = pd.read_csv('./data/air.csv')
    # Convert the 'timestamp' column to datetime format
    air_history['timestamp'] = pd.to_datetime(df['timestamp'])

    # Get the current time
    now = datetime.now()

    # Calculate the time 48 hours ago
    time_48_hours_ago = now - timedelta(hours=48)

    # Filter rows where the timestamp is within the last 48 hours
    filtered_df = air_history[air_history['timestamp'] >= time_48_hours_ago]

    max_temperature = filtered_df['temperature'].max()
    avg_temperature = round(filtered_df['temperature'].mean(),1)
    max_humidity = filtered_df['humidity'].max()
    avg_humidity = round(filtered_df['humidity'].mean(), 1)
    


    feeding_data = {
        'watter': '05d',
        'leaf': '10d',
        'soil': '20d',
        'max_temperature': int(max_temperature),
        'avg_temperature': float(avg_temperature),
        'max_humidity': int(max_humidity),
        'avg_humidity': float(avg_humidity)
    }
    print("####")
    print(feeding_data)
    print("####")
    print(jsonify(feeding_data))
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
    
