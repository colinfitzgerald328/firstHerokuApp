from flask import Flask, request
from utilities import running_pace_calculator

app = Flask(__name__)


@app.route("/")
def index():
	return "Hello World!"


@app.route("/convert")
def convert_input():
	running_time = str(request.args.get("running_time", "")).strip()
	running_distance = str(request.args.get("running_distance", "")).strip()
	running_pace = str(request.args.get("running_pace")).strip()
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
