

# time complexity: O(n^2)
# space complexity: O(n)
def first_unique(s):
	
	chars = set()
	i=1
	found=True
	for c in s:
		if c not in s[i:] and c not in chars:
			return c
		else:
			chars.add(c)
			i+=1
	return 'None'

# time complexity O(n)
# space complexity O(n)
def first_unique2(s):
	counts = {}

	for c in s:
		counts[c] = counts.get(c,0) + 1

	for c in s:
		if counts[c] == 1:
			return c
	return 'None'
	

# time complexity O(n)
# space complexity O(n)
def find_duplicates(l:list):
	cnt = {}
	result = []

	for a in l:
		if a in cnt:
			cnt[a] += 1
		else:
			cnt[a] = 1

	for a in cnt:
		if cnt[a] >= 2:
			result.append(a)

	return result

records = [
    ("GetCustomer", 183),
    ("GetOrder", 91),
    ("GetCustomer", 211),
    ("GetOrder", 105),
    ("GetCustomer", "1s75"),
]

# time complexity O(n)
# space complexity O(k) : k number of unique queries
def average_duration(recs):

	avgs = {}
	mlfrmd = 0

	for query, duration in recs:
		if not isinstance(duration, (int, float)):
			mlfrmd+=1
			continue

		if query in avgs:
			avgs[query] = [avgs[query][0] + duration, avgs[query][1] + 1]
		else:
			avgs[query] = [duration, 1]

	for query in avgs:
		avgs[query] = avgs[query][0] / avgs[query][1]

	return(avgs, mlfrmd)



#s = input()
s='sometinh'
print(first_unique(s))
print(first_unique2(s))

print(find_duplicates([4, 7, 2, 7, 4, 9, 2, 5]))

print(average_duration(records))
