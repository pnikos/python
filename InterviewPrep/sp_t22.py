import re


def analyse_logs_alt(log_text):
	services = {}

	pattern = (
		r"service=(?P<service>\w+) "
		r"status=(?P<status>[0-9]+) "
		r"duration_ms=(?P<duration_ms>[0-9]+)"
	)

	with open(log_text) as f:

		for line in f:
			match = re.search(pattern, line)

			if match:
				service = match.group("service")
				status = int(match.group("status"))
				duration_ms = int(match.group("duration_ms"))

				if service not in services:
					services[service] = {
						"total_duration": 0,
						"requests": 0,
						"errors": 0
					}

				services[service]["total_duration"] += duration_ms
				services[service]["requests"] += 1
				if status >= 500 and status <= 599:
					services[service]["errors"] += 1

		for service in services.values():
			service["avg_duration_ms"] = round(
				service["total_duration"] /
				service["requests"], 2
			)
			del service["total_duration"]

		return services


def analyse_logs(log_text):
	services = {}

	pattern = re.compile(
	    r"(?P<timestamp>\d{4}-\d{2}-\d{2} "
	    r"\d{2}:\d{2}:\d{2}) "
	    r"service=(?P<service>[\w\.\-]+) "
	    r"status=(?P<status>\d+) "
	    r"duration_ms=(?P<duration_ms>\d+)"
	)

	with open(log_text) as f:

		for line in f:
			match = re.fullmatch(pattern, line.strip())

			if match:
				service = match.group("service")
				status = int(match.group("status"))
				duration_ms = int(match.group("duration_ms"))

				if service not in services:
					services[service] = {
						"total_duration": 0,
						"requests": 0,
						"errors": 0
					}

				services[service]["total_duration"] += duration_ms
				services[service]["requests"] += 1
				if status >= 500 and status <= 599:
					services[service]["errors"] += 1
				print(services)

		for service in services.values():
			service["avg_duration_ms"] = round(
				service["total_duration"] /
				service["requests"], 2
			)
			del service["total_duration"]

		return services




print(analyse_logs("errors_re.dat"))
