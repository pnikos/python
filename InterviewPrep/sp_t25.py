import re

log = '''2026-10-11 10:00:01 service=api status=200 duration_ms=35
2026-10-11 10:00:02 service=payments status=503 duration_ms=120
2026-10-11 10:00:03 service=api status=500 duration_ms=85
2026-10-11 10:00:04 service=api status=200 duration_ms=40
2026-10-11 10:00:05 service=payments status=200 duration_ms=60'''

def parse_logs(log_text):
    pattern = re.compile(
        r"service=(?P<service>[\w.-]+) "
        r"status=(?P<status>\d+)"
    )

    for line in log_text.splitlines():
        match = pattern.search(line)

        if match:
            yield {
                "service": match.group("service"),
                "status": int(match.group("status"))
            }

def error_rates(log_text):
    services = {}

    for event in parse_logs(log_text):
        service = event["service"]
        status = event["status"]

        if service not in services:
            services[service] = {"total": 0, "errors": 0}

        services[service]["total"] += 1

        if 500 <= status <= 599:
            services[service]["errors"] += 1

    return {
        service: round(data["errors"] / data["total"] * 100, 2)
        for service, data in services.items()
    }

print(error_rates(log))