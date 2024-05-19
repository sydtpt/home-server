from flask import Flask
from routes.air import air_routes
from routes.feeding import feeding_routes
from routes.devices import devices_routes

app = Flask(__name__)
app.register_blueprint(air_routes)
app.register_blueprint(feeding_routes)
app.register_blueprint(devices_routes)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

