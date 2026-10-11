events = [
    {"service": "api", "duration_ms": 120},
    {"service": "payments", "duration_ms": 80},
    {"service": "api", "duration_ms": 40},
    {"service": "search", "duration_ms": 200},
    {"service": "payments", "duration_ms": 100},
    {"service": "api", "duration_ms": 90},
    {"service": "search", "duration_ms": 100},
]

def top_services(events, n):
    services = {}

    for event in events:
        try:
            service = event["service"]
            duration_ms = int(event["duration_ms"])
        except (ValueError, KeyError, TypeError):
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
            value["total_duration"] / value["total_count"], 2
        )

    return [service for service, _ in sorted(services.items(), key=lambda x: -x[1])[:n]]

print(top_services(events, 2))