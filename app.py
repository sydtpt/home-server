from flask import Flask
from routes.air import air_routes
from routes.soil import soil_routes
from routes.feeding import feeding_routes
from routes.devices import devices_routes
from routes.scheduler import schedule_routes
from lib.scheduleController import scheduleController

app = Flask(__name__)
app.register_blueprint(air_routes)
app.register_blueprint(soil_routes)
app.register_blueprint(feeding_routes)
app.register_blueprint(devices_routes)
app.register_blueprint(schedule_routes)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

