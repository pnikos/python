import csv
import io

csv_data = """timestamp,service,status,duration_ms
1000,api,200,35
1010,payments,500,120
1020,api,503,85
1030,payments,200,40
1040,api,200,25
"""

def service_duration(csv_data):
	services = {}

	data = csv.DictReader(io.StringIO(csv_data))

	for line in data:
		
		try:
			service = line["service"]
			duration_ms = float(line["duration_ms"])
		except (TypeError, ValueError, KeyError):
			continue

		if service not in services:
			services[service] = {
				"duration_sum" : 0,
				"count" : 0
			}

		services[service]["duration_sum"] += duration_ms
		services[service]["count"] += 1

	for service, value in services.items():
		services[service] = round(
			value["duration_sum"] /
			value["count"]
		, 2)
		del value["duration_sum"]
		del value["count"]

	return services

print(service_duration(csv_data))
