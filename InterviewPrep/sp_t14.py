events = [
    {"service": "api", "status": 200, "duration_ms": 20},
    {"service": "payments", "status": 500, "duration_ms": 120},
    {"service": "api", "status": 500, "duration_ms": 80},
    {"service": "api", "status": 200, "duration_ms": 30},
    {"service": "payments", "status": 200, "duration_ms": 40},
]

def check_requests(events):
	services = {}

	for event in events:
		try:
			service = event["service"]
			status = int(event["status"])
		except (ValueError, KeyError, TypeError):
			continue

		if service not in services:
			services[service] = {
				"number_of_requests": 0,
				"errors": 0
			}

		services[service]["number_of_requests"] += 1
		if status >= 500:
			services[service]["errors"] += 1

	for service in services.values():
		service["error_rate"] = round(
			(service["errors"] /
			service["number_of_requests"]) * 100, 2)
		del service["errors"]

	return services


print(check_requests(events))