# csv, exceptions, sorting

import csv

def slow_endpoints(filename, limit, top_n):
	stats = {}
	slow_endpoints = []

	with open(filename) as csvfile:
		csvreader = csv.DictReader(csvfile)

		for line in csvreader:

			try:
				endpoint = line["endpoint"]
				duration = int(line["duration"])
				status = int(line["status"])
			except (ValueError, TypeError):
				continue

			if endpoint not in stats:
				stats[endpoint] = {
					"requests": 0,
					"errors": 0,
					"total_duration": 0
				}

			stats[endpoint]["requests"] += 1
			stats[endpoint]["total_duration"] += duration

			if status >= 500:
				stats[endpoint]["errors"] += 1

		for endpoint in stats:
			stats[endpoint]["average_duration"] = (
				stats[endpoint]["total_duration"] / 
				stats[endpoint]["requests"]
			)

			if stats[endpoint]["average_duration"] > limit and stats[endpoint]["requests"] >= 2:
				sendp = (endpoint, stats[endpoint]["average_duration"])
				slow_endpoints.append(sendp)

		return sorted(slow_endpoints, key = lambda x: x[1], reverse = True)[:top_n]


def slow_endpoints_alt(filename, limit, top_n):
    stats = {}
    slow_endpoints = []

    with open(filename) as csvfile:
        csvreader = csv.DictReader(csvfile)

        for line in csvreader:
            try:
                endpoint = line["endpoint"]
                duration = int(line["duration"])
                status = int(line["status"])
            except (ValueError, TypeError, KeyError):
                continue

            if endpoint not in stats:
                stats[endpoint] = {
                    "requests": 0,
                    "errors": 0,
                    "total_duration": 0
                }

            stats[endpoint]["requests"] += 1
            stats[endpoint]["total_duration"] += duration

            if status >= 500:
                stats[endpoint]["errors"] += 1

    for endpoint in stats:
        if stats[endpoint]["requests"] >= 2:
            average = (
                stats[endpoint]["total_duration"] /
                stats[endpoint]["requests"]
            )

            if average > limit:
                slow_endpoints.append((endpoint, average))

    return sorted(
        slow_endpoints,
        key=lambda x: x[1],
        reverse=True
    )[:top_n]


print(slow_endpoints("f5.csv", 100, 6))