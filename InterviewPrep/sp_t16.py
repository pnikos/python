from collections import deque

metrics_dq = deque()
sum_duration = 0

def metrics_avg(event):
	global sum_duration

	metrics_dq.append(event)
	sum_duration += float(event["duration_ms"])

	while metrics_dq and metrics_dq[0]["timestamp"] < event["timestamp"] - 60:
		sum_duration -= float(metrics_dq[0]["duration_ms"])
		metrics_dq.popleft()

	if metrics_dq:
		return sum_duration / len(metrics_dq)

	return 0

events = [
    {"timestamp": 1000, "duration_ms": 20},
    {"timestamp": 1020, "duration_ms": 40},
    {"timestamp": 1040, "duration_ms": 60},
    {"timestamp": 1070, "duration_ms": 80},
]

print(metrics_avg(events[0]))
print(metrics_avg(events[1]))
print(metrics_avg(events[2]))
print(metrics_avg(events[3]))


