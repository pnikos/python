class ServiceCounter:
    def __init__(self, service):
        self.service = service
        self.requests = 0

    def record_request(self):
    	self.requests += 1

    def get_count(self):
        return self.requests

api = ServiceCounter("api")
payments = ServiceCounter("payments")

api.record_request()
api.record_request()
payments.record_request()

print(api.get_count())       # 2
print(payments.get_count())  # 1
print(api.service)           # api
print("-"*80)

class KeyValueStore:
	def __init__(self):
		self.store = {}

	def insert(self, key, value):
		if key not in self.store:
			self.store[key] = value

	def update(self, key, value):
		if key in self.store:
			self.store[key] = value

	def remove(self, key):
		if key in self.store:
			del self.store[key]

	def get(self, key):
		return self.store.get(key, None)

store = KeyValueStore()

store.insert("api", 10)
store.insert("api", 20)    # Ignored: key already exists
store.update("api", 30)
store.update("web", 40)    # Ignored: key doesn't exist

print(store.get("api"))    # 30
print(store.get("web"))    # None

store.remove("api")
print(store.get("api"))    # None
print("-"*80)

events = [
    {"service": "api", "status": 200},
    {"service": "payments", "status": 503},
    {"service": "api", "status": 500},
    {"service": "api", "status": 404},
    {"service": "payments", "status": 200},
    {"service": "payments", "status": 502},
]

def count_errors(events):
	services = {}

	for event in events:
		try:
			service = event["service"]
			status = int(event["status"])
		except (KeyError, ValueError, TypeError):
			continue

		if service not in services:
			services[service] = 0

		if status >= 500 and status <= 599:
			services[service] += 1

	return services

print(count_errors(events))
