import datetime
from datetime import datetime
from datetime import timedelta


def running_pace_calculator(running_time, running_distance, running_pace):
	"""Convert Running Total Time and Miles Run to Running Pace"""
	time_format = "%H:%M:%S"
	pace_format = "%M:%S"
	try:
		if running_time and running_distance != "":
			try:
				formatted = datetime.strptime(str(running_time), time_format)
				total_seconds = (formatted.hour * 3600) + (
						formatted.minute * 60) + formatted.second
				pace = total_seconds / float(running_distance)
				m, s = divmod(int(pace), 60)
				return f"{m:2d}:{s:02d}" + " " + "per mile"
			except ValueError:
				running_time = "00:" + running_time
				formatted = datetime.strptime(str(running_time), time_format)
				total_seconds = (formatted.hour * 3600) + (
						formatted.minute * 60) + formatted.second
				pace = total_seconds / float(running_distance)
				m, s = divmod(int(pace), 60)
				return f"{m:2d}:{s:02d}" + " " + "per mile"
		elif running_distance and running_pace != "":
			formatted = datetime.strptime(str(running_pace), pace_format)
			minutes = (float(formatted.minute) * float(running_distance)) * 60
			seconds = float(formatted.second) * float(running_distance)
			total_seconds = round((minutes + seconds))
			return str(timedelta(seconds=total_seconds))
		elif running_time and running_pace != "":
			try:
				formatted = datetime.strptime(str(running_time), time_format)
				time_seconds = formatted.hour * 3600 + formatted.minute * 60 + formatted.second
				for_pace = datetime.strptime(running_pace, pace_format)
				pace_seconds = for_pace.minute * 60 + for_pace.second
				return str(round(
					(time_seconds / pace_seconds), 2)) + " " + "miles"
			except ValueError:
				running_time = "00:" + running_time
				formatted = datetime.strptime(str(running_time), time_format)
				time_seconds = formatted.hour * 3600 + formatted.minute * 60 + formatted.second
				for_pace = datetime.strptime(running_pace, pace_format)
				pace_seconds = for_pace.minute * 60 + for_pace.second
				return str(round(
					(time_seconds / pace_seconds), 2)) + " " + "miles"
	except ValueError:
		return "invalid input"
