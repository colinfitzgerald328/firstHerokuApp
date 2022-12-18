from flask import Flask, request
from flask_cors import CORS, cross_origin
from utilities import running_pace_calculator

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
@cross_origin()
def index():
	return "Hello World!"


@app.route("/convert", methods=["POST"])
@cross_origin()
def convert_input():
	params = request.json
	running_time = str(params.get("running_time", "")).strip()
	running_distance = str(params.get("running_distance", "")).strip()
	running_pace = str(params.get("running_pace")).strip()
	if running_time and running_distance != "":
		final_output = running_pace_calculator(running_time, running_distance, running_pace)
	elif running_distance and running_pace != "":
		final_output = running_pace_calculator(running_time, running_distance, running_pace)
	elif running_time and running_pace != "":
		final_output = running_pace_calculator(running_time, running_distance, running_pace)
	else:
		final_output = ""
	return {
		"operation": "success",
		"converted_result": final_output
	}
