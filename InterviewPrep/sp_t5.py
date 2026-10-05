values = [3, 2, 4]
target = 6

def two_sum(values, target):

	for i, a in enumerate(values):
		for j, x in enumerate(values[i+1:]):
			print(i,a,j,x, a+x)
			if a+x == target:
				return i, i+j+1
	return None

def two_sum_alt(values, target):
	for a in range(len(values)):
		for b in range(a+1, len(values)):
			if values[a]+values[b] == target:
				return a,b

def two_sum_alt2(values, target):
	seen = {}

	for i, value in enumerate(values):
		complement = target - value

		if complement in seen:
			return seen[complement], i

		seen[value] = i

#print(two_sum_alt(values,target))
print(two_sum_alt2(values,target))

## File handling


def decorator(func):
	def wrapper(*args, **kwargs):
		print("====before")
		func(*args,**kwargs)
		print("after====")
	return wrapper


@decorator
def process(line):
	print(line, end="")

with open("sp_t1.py", 'r') as f:
	for line in f:
		if line:
			process(line)

def timer(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

@timer
def hello():
    print("hello")

hello()
