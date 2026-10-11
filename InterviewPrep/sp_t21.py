events = [
    {"timestamp": 100, "duration_ms": 20},
    {"timestamp": 120, "duration_ms": 40},
    {"timestamp": 150, "duration_ms": 30},
    {"timestamp": 170, "duration_ms": 50},
]

from collections import deque

def rolling_average(events):
	sum = count = 0
	dq = deque()
	result = []

	for event in events:	
		try:
			timestamp = int(event["timestamp"])
			duration = int(event["duration_ms"])
		except (KeyError, TypeError, ValueError):
			continue

		dq.append(event)
		sum += duration
		count += 1

		while dq and int(dq[0]["timestamp"]) < timestamp - 60:
			count -= 1
			sum -= int(dq[0]["duration_ms"])
			dq.popleft()

		result.append(round(sum/count, 2))

	return result



print(rolling_average(events))