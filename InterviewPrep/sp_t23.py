import re

log = '''2026-10-11 10:00:01 service=api status=200 duration_ms=35
2026-10-11 10:00:02 service=payments status=503 duration_ms=120
2026-10-11 10:00:03 service=api status=500 duration_ms=85
2026-10-11 10:00:04 service=api status=200 duration_ms=40
2026-10-11 10:00:05 service=payments status=200 duration_ms=60'''


def error_rates(log_text):
	services = {}

	pattern = (
		r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "
		r"service=(?P<service>\w+) "
		r"status=(?P<status>[0-9]+) "
		r"duration_ms=(?P<duration_ms>[0-9]+)"
	)

	for line in log_text.splitlines():
		match = re.fullmatch(pattern, line.strip())
		if match:
			
			service = match.group("service")
			status = int(match.group("status"))

			if service not in services:
				services[service] = {
					"total": 0,
					"errors": 0
				}

			services[service]["total"] += 1
			if status >= 500 and status <= 599:
				services[service]["errors"] += 1

	for key, value in services.items():
		services[key] = round(
			value["errors"] / value["total"] * 100, 2)

	return services

print(error_rates(log))
