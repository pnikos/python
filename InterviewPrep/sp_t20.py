events = [
    {"service": "api", "duration_ms": 20},
    {"service": "payments", "duration_ms": 100},
    {"service": "api", "duration_ms": 40},
    {"service": "payments", "duration_ms": 200},
    {"service": "api", "duration_ms": 30},
]

def average_duration(events):
	services = {}

	for event in events:
		try:
			service = event["service"]
			duration_ms = int(event["duration_ms"])
		except (KeyError, TypeError, ValueError):
			continue

		if service not in services:
			services[service] = {
				"total_duration": 0,
				"total_count": 0
			}

		services[service]["total_duration"] += duration_ms
		services[service]["total_count"] += 1

	for key, value in services.items():
		services[key] = round(
			value["total_duration"] /
			value["total_count"], 2
		)
	return services

print(average_duration(events))
