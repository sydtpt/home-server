from flask import Blueprint, request, make_response
from datetime import datetime
from flask_cors import cross_origin

feeding_routes = Blueprint(
    'feeding', __name__,
    url_prefix='/api/feeding')

cross_origin()
@feeding_routes.route('/')
def summary():
    feeding_data = {
        'watter': '5d',
        'leaf': '10d',
        'soil': '20d'      
    }
    response = make_response(jsonify(feeding_data), 200)
    response.mimetype = "application/json"
    return response
            
cross_origin()
@feeding_routes.route('/leaf', methods=['POST'])
def leaf():
    print("POST")
    response = make_response([], 200)
    response.mimetype = "application/json"
    return response

cross_origin()
@feeding_routes.route('/water', methods=['POST'])
def water():
    print("POST")
    response = make_response([], 200)
    response.mimetype = "application/json"
    return response

cross_origin()
@feeding_routes.route('/soil', methods=['POST'])
def soil():
    print("POST")
    response = make_response([], 200)
    response.mimetype = "application/json"
    return response
    
