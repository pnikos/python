import json


def unhealthy_services(filename):
	u_services = []

	with open(filename) as jsonfile:
		services = json.load(jsonfile)

	for service in services["services"]:

		if not service["healthy"]:
			u_services.append((service["name"], service["host"], service["port"]))

	return u_services

print(unhealthy_services("services.json"))

def get_cpu_usage(filename):
	with open(filename) as jsonfile:
		metrics = json.load(jsonfile)

	for metric in metrics["metrics"]:
		if metric["name"] == "cpu":
			return metric["values"]
	return None

print(get_cpu_usage("metrics.json"))
print("-"*40)

# defensive parsing

# Returns a list of (name, host, cpu) only for those that cpu is higher than the threshold
def high_cpu_services(filename, threshold):
	result = []

	with open(filename) as jsonfile:
		services = json.load(jsonfile)

	for service in services["services"]:

		try:
			if int(service["metrics"]["cpu"]) >= threshold:
				try:
					result.append((service["name"], service["host"], service["metrics"]["cpu"]))
				except (KeyError):
					continue
		
		except (KeyError, ValueError, TypeError):
			continue

	return result


def high_cpu_services_alt(filename, threshold):
    result = []

    with open(filename) as jsonfile:
        services = json.load(jsonfile)

    for service in services["services"]:
        try:
            name = service["name"]
            host = service["host"]
            cpu = int(service["metrics"]["cpu"])
        except (KeyError, ValueError, TypeError):
            continue

        if cpu >= threshold:
            result.append((name, host, cpu))

    return result

print(high_cpu_services("metrics2.json", 80))
print("="*40)

# Use line reading and json.loads to read from a file with separate json lines

def count_errors_jsonl(filename):
	count_errors = 0
	with open(filename) as f:

		for line in f:
			try:
				jsonline = json.loads(line)
			except json.JSONDecodeError:
				continue

			try:				
				if int(jsonline["status"]) >= 500:
					count_errors += 1
			except (KeyError):
				continue

	return count_errors

def count_errors_jsonl_alt(filename):
    count_errors = 0

    with open(filename) as f:
        for line in f:
            try:
                record = json.loads(line)
                status = int(record["status"])
            except (json.JSONDecodeError, KeyError, ValueError, TypeError):
                continue

            if status >= 500:
                count_errors += 1

    return count_errors

print(count_errors_jsonl("requests.jsonl"))
print("="*40)

def endpoints_stats_jsonl(filename):
	stats = {}

	with open(filename) as f:
		for line in f:

			try:
				record = json.loads(line)
				endpoint = record["endpoint"]
				duration = int(record["duration"])
				status = int(record["status"])
			except (json.JSONDecodeError, KeyError, ValueError, TypeError):
				continue

			if endpoint not in stats:
				stats[endpoint] = {
					"requests": 0,
					"errors": 0,
					"total_duration": 0
				}

			stats[endpoint]["requests"] += 1
			if status >= 500:
				stats[endpoint]["errors"] += 1

			stats[endpoint]["total_duration"] += duration

	return stats

print(endpoints_stats_jsonl("requests3.jsonl"))
print("-"*40)


def high_cpu_services_new(filename, threshold):
	result = []

	with open(filename) as jsonfile:
		hosts = json.load(jsonfile)

	for host in hosts["hosts"]:
		for service in host["services"]:
			if service["cpu"] >= threshold:
				result.append((host["name"], service["name"], service["cpu"]))

	return sorted(result, key=lambda x: -x[2])


print(high_cpu_services_new("metrics4.json", 80))