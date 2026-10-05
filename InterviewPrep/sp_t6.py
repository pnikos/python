import csv, json

def count_slow_requests(filename, limit):
	count_slow = count_malformed = 0
	try:
		with open(filename, 'r') as f:
			for line in f:
				try:
					timestamp, method, endpoint, duration_ms, status = line.split()
					duration_ms = int(duration_ms)
				except ValueError:
					count_malformed += 1
					continue
				if duration_ms > limit:
					count_slow += 1
	except FileNotFoundError:
		raise

	return count_slow, count_malformed

print(count_slow_requests("f1.dat", 1000))


def count_errors(filename):
	count = 0

	try:
		with open(filename) as csvfile:
			csvreader = csv.DictReader(csvfile)
			for line in csvreader:
				try:
					if int(line["status"]) >= 500:
						count += 1
				except (ValueError, TypeError):
					continue
	except FileNotFoundError:
		raise

	return count


print(count_errors("f2.csv"))

def endpoint_stats(filename):
	stats = {}
	try:
		with open(filename) as csvfile:
			csvreader = csv.DictReader(csvfile)
			for line in csvreader:
				endpoint = line["endpoint"]
				duration = int(line["duration"])
				status = int(line["status"])

				if endpoint not in stats:
					stats[endpoint] = {
						"requests": 0,
						"errors": 0,
						"total_duration": 0,
						"average_duration": 0
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
	except FileNotFoundError:
		raise
	return stats




print(endpoint_stats("f3.csv"))

## malformed csv

def endpoint_stats_mf(filename):
	stats = {}
	malformed_count = 0

	try:
		with open(filename) as csvfile:
			csvreader = csv.DictReader(csvfile)

			for line in csvreader:
				try:
					endpoint = line["endpoint"]
					duration = int(line["duration"])
					status = int(line["status"])
				except (KeyError, ValueError, TypeError):
					malformed_count += 1
					continue

				if endpoint not in stats:
					stats[endpoint] = {
						"requests": 0,
						"errors": 0,
						"total_duration": 0,
						"average_duration": 0
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
	except FileNotFoundError:
		raise

	return stats, malformed_count

print(endpoint_stats_mf("f4.csv"))