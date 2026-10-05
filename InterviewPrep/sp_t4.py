records = [
    ("10:00:01", "api", "/login", 120, 200),
    ("10:00:02", "api", "/login", 250, 200),
    ("10:00:03", "api", "/trade", 900, 500),
    ("10:00:02", "api", "/login"),
    ("10:00:04", "api", "/login", 1500, 500),
    ("10:00:05", "db",  "/query", 300, 200),
]


# (timestamp, service, endpoint, duration_ms, status_code)

def endpoint_stats(records):
	result = {}
	avg = {}
	requests = {}
	errors = {}	

	for rec in records:
		avg[rec[2]] = avg.get(rec[2], 0) + rec[3]
		requests[rec[2]] = requests.get(rec[2], 0) + 1
		if rec[4] >= 500:
			errors[rec[2]] = errors.get(rec[2],0) + 1
		
		result[rec[2]] = {
			"average": avg[rec[2]] / requests[rec[2]],
			"requests": requests[rec[2]],
			"errors": errors.get(rec[2], 0)
		}

	return result

def endpoint_stats_alt(records):
	stats = {}

	for timestamp, service, endpoint, duration, status_code in records:

		if endpoint not in stats:
			stats[endpoint] = {
				"total": 0,
				"requests": 0,
				"errors": 0
			}

		stats[endpoint]["total"] += duration
		stats[endpoint]["requests"] += 1
		if status_code >= 500:
			stats[endpoint]["errors"] += 1

	for endpoint in stats:
		stats[endpoint]["average"] = (
			stats[endpoint]["total"] /
			stats[endpoint]["requests"]
		)
		del stats[endpoint]["total"]		 
	return stats


def endpoint_stats_exc(records):
	stats = {}

	for rec in records:

		try:
			endpoint = rec[2]
			duration = rec[3]
			status_code = rec[4]

			if not isinstance(duration, (int, float)):
				continue

			if not isinstance(status_code, int):
				continue

		except IndexError:
			continue

		if endpoint not in stats:
			stats[endpoint] = {
				"total": 0,
				"requests": 0,
				"errors": 0
			}

		stats[endpoint]["total"] += duration
		stats[endpoint]["requests"] += 1
		if status_code >= 500:
			stats[endpoint]["errors"] += 1

	for endpoint in stats:
		stats[endpoint]["average"] = (
			stats[endpoint]["total"]/stats[endpoint]["requests"])
		del stats[endpoint]["total"]

	return stats


#print(endpoint_stats(records))
#print(endpoint_stats_alt(records))
#print(endpoint_stats_exc(records))

values = [4, 7, 2, 7, 9, 4, 1]

def first_duplicate(values):
	cnt = {}

	for v in values:
		cnt[v] = cnt.get(v, 0) + 1
		if cnt[v] > 1:
			return v

def first_duplicate_alt(values):
	seen = set()

	for v in values:
		if v in seen:
			return v
		seen.add(v)
	return None

print(first_duplicate(values))