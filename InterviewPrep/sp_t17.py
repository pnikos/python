import json

log_data = '''
[
    {"service": "api", "status": 200, "duration_ms": 35},
    {"service": "payments", "status": 500, "duration_ms": 120},
    {"service": "api", "status": 503, "duration_ms": 85},
    {"service": "payments", "status": 200, "duration_ms": 40},
    {"service": "api", "status": 200, "duration_ms": 25},
    {"service": "test", "status": 200, "duration_ms": 25}
]
'''

def process_logs(load_data):
	try:
		js_data = json.loads(load_data)
	except json.decoder.JSONDecodeError:
		print("Error parsing JSON")
		return

	services = {}

	for data in js_data:
		#print(data)
		try:
			service = data["service"]
			status = int(data["status"])
		except (TypeError, ValueError, KeyError):
			continue

		if service not in services and status >= 500:
			services[service] = 0

		if status >= 500:
			services[service] += 1

	return services

print(process_logs(log_data))