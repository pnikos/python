events = [
    {"service": "pricing", "status": 200, "duration_ms": 40},
    {"service": "pricing", "status": "500", "duration_ms": "120"},
    {"service": "settlement", "status": 200, "duration_ms": 80},
    {"service": "pricing", "status": 503, "duration_ms": "invalid"},
    {"service": "settlement", "duration_ms": 150},
    {"service": "", "status": 500, "duration_ms": 100},
    None,
    {"service": "pricing", "status": 200, "duration_ms": 60},
]

def analyse_events(events):
	services = {}

	for event in events:
		if not isinstance(event, dict):
			continue

		try:
			service = event["service"]
			status = int(event["status"])
			duration_ms = int(event["duration_ms"])
		except (KeyError, ValueError, TypeError):
			continue

		if not service:
			continue

		if service not in services:
			services[service] = {
				"total": 0,
				"errors": 0,
				"duration_ms": 0
			}

		services[service]["total"] += 1
		services[service]["duration_ms"] += duration_ms
		if status >= 500:
			services[service]["errors"] += 1

	for service in services.values():
		service["avg_duration_ms"] = round(
			service["duration_ms"] /
			service["total"], 2
		)
		del service["duration_ms"]

	return services


print(analyse_events(events))