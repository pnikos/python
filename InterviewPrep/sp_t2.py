from collections import deque
import tracemalloc

class SlidingAverage:
	def __init__(self, window_seconds):
		self.dq = deque()
		self.window = window_seconds
		self.aggregates = {}

	def add(self, timestamp, query, duration):
		self.dq.append([timestamp, query, duration])

		if self.aggregates.get(query) != None:
			self.aggregates[query][0] = self.aggregates[query][0] + duration
			self.aggregates[query][1] = self.aggregates[query][1] + 1
		else:
			self.aggregates[query] = [duration, 1]
		k=0

		print(self.aggregates)
		while self.dq and self.dq[k][0] < timestamp - self.window:
			old_timestamp, old_query, old_duration = self.dq.popleft()
			self.aggregates[old_query][0] -= old_duration
			self.aggregates[old_query][1] -= 1

			if self.aggregates[old_query][1] == 0:
				del self.aggregates[old_query]

		snapshot = tracemalloc.take_snapshot()
		stats = snapshot.statistics("lineno")	

		for stat in stats[:10]:
			print(stat)
		print(self.dq)

	def average(self, query):
		if query in self.aggregates.keys():
			return self.aggregates[query][0] / self.aggregates[query][1]

tracemalloc.start()
s = SlidingAverage(60)
s.add(1000, "GetCustomer", 100)
s.add(1010, "GetCustomer", 200)
s.add(1020, "GetCustomer", 300)

print(s.average("GetCustomer"))
s.add(1061, "GetCustomer", 400)

print(s.average("GetCustomer"))