from flask import Blueprint, request, make_response
from flask_cors import cross_origin
from lib.scheduleController import scheduleController

schedule_routes = Blueprint(
    'schedule', __name__,
    url_prefix='/api/schedule')

cross_origin()
@schedule_routes.route('/', methods=['GET', 'POST'])
def log():
    scheduler = scheduleController();
    if request.method == 'POST':
        content = request.get_json()
        scheduler.add(content['value'], content['device'], content['time'])
        response = scheduler.getSchedule().to_json(orient='records')
        response = make_response(response, 201)
        return response
    else:
        response = scheduler.getSchedule().to_json(orient='records')
        response = make_response(response, 200)
        response.mimetype = "application/json"
        return response            
    
cross_origin()
@schedule_routes.route('/<id>', methods=['DELETE'])
def delete_schedule():
    scheduler = scheduleController();
    response = scheduler.delete(id)
    response = make_response({}, 204)
    return response

cross_origin()
@schedule_routes.route('/start', methods=['POST'])
def start_schedule_job():
    scheduler = scheduleController();
    response = scheduler.start_scheduler()
    response = make_response({}, 201)
    return response
