events = [
    {"service": "api", "duration_ms": 20},
    {"service": "payments", "duration_ms": 120},
    {"service": "api", "duration_ms": 80},
    {"service": "api", "duration_ms": 30},
    {"service": "payments", "duration_ms": 40},
    {"service": "search", "duration_ms": 200},
]

def highest_duration_services(events):
	services = {}
	service_list = []

	for event in events:
		try:
			service = event["service"]
			duration = event["duration_ms"]
		except (KeyError, TypeError, ValueError):
			continue

		if service not in services:
			services[service] = {
				"total": 0,
				"duration": 0
			}

		services[service]["total"] += 1
		services[service]["duration"] += duration

	for service, value in services.items():
		value["avg_duration"] = round(
			value["duration"] /
			value["total"], 2
		)
		del value["total"]
		service_list.append((service, value["avg_duration"]))

	return [
	    service
	    for service, avg_duration in sorted(
	        service_list, key=lambda x: -x[1]
	    )[:3]
	]

print(highest_duration_services(events))