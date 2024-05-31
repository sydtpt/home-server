from flask import Flask
from routes.air import air_routes
from routes.soil import soil_routes
from routes.feeding import feeding_routes
from routes.devices import devices_routes
from routes.scheduler import schedule_routes
from lib.scheduleController import scheduleController
from flask_cors import CORS

app = Flask(__name__)



app.register_blueprint(devices_routes)
app.register_blueprint(air_routes)
app.register_blueprint(soil_routes)
app.register_blueprint(feeding_routes)
app.register_blueprint(schedule_routes)

cors = CORS(app)


@app.route("/")
def home():
    return app.send_static_file('index.html')

@app.route("/devices")
def devices():
    return app.send_static_file('website/devices.html')

@app.route("/schedule")
def schedule():
    return app.send_static_file('website/schedule.html')