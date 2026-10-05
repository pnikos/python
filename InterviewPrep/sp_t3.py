
def word_counts(words):
	counts = {}
	for word in words:
		counts[word] = counts.get(word,0) + 1

	return counts

def first_non_repeated(words):
	counts = {}

	for word in words:
		counts[word] = counts.get(word,0) + 1

	for word, count in counts.items():
		if count == 1:
			return word

	return None 

# for x in d:             # keys
# for x in d.keys():      # keys
# for x in d.values():    # values
# for x in d.items():     # (key, value) pairs

def first_unique_char_old(s):
	k = 1
	old_chars = []
	for c in s:
		found = True

		for c_rest in s[k:]:
			if c == c_rest:
				old_chars.append(c)
				found = False
				continue
		k+=1
		if found and c not in old_chars:
			return c

	return None

def first_unique_char(s):
	counts = {}

	for c in s:
		counts[c] = counts.get(c, 0) + 1
	for c in s:
		if counts[c] == 1:
			return c
	return None

def has_duplicate(values):
	counts = {}
	for v in values:
		counts[v] = counts.get(v,0) + 1
	for v in values:
		if counts[v] > 1:
			return True
	return False

def has_duplicate_alt(values):
	old_values = set()

	for v in values:
		if v in old_values:
			return True
		else:
			old_values.add(v)
	return False


# First loop: O(n)
# Second loop: O(n)
# Overall: O(n)
# Space: O(n)
def find_missing_number(values, n):
	seen = set()

	for v in values:
		if v not in seen:
			seen.add(v)

	for v in range(0, n+1):
		print(f"{v}")
		if v not in seen:
			return v


# same but with O(1) extra space complexity
def find_missing_number_xor(values, n):
	result = 0

	for v in range(n+1):
		result ^= v

	for v in values:
		result ^= v

	return result

def sort_by_duration(records):
	return sorted(records, key = lambda x: (-x[1], x[0]))

# return the query names whose duration is greater than 100:
def long_queries(records):
	result = []
	for rec in records:
		if rec[1] > 100:
			result.append(rec[0])
	return result

#return the query names whose duration is greater than 100 using comprehension
def long_queries_alt(records):
	return [rec[0] for rec in records if rec[1] > 100]

# we want to find the position of the first duration over 100.
def first_long_query(records):
	for i, rec in enumerate(records):		
		if rec[1] > 100:
			return i

	return None


#sorted(items, key=lambda x: (primary_key, secondary_key))

# zip
print(first_unique_char("aafbbcc"))
print(has_duplicate_alt([1, 2, 3, 4]))
print(has_duplicate_alt([1, 2, 3, 2]))
print(find_missing_number_xor([3, 0, 1], 3))
print(find_missing_number([0, 1], 2))
#print(find_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1], n=9))

recs = [
    ("queryA", 300),
    ("queryD", 100),
    ("queryC", 200),
    ("queryB", 100)
]

print(sort_by_duration(recs))
print(long_queries(recs))
print(first_long_query(recs))

# --------------

# zip pairs elements positionally, It stops at the shorter input

def make_records(names, durations):
	return list(zip(names, durations))


names = ["Alice", "Bob", "Charlie"]
durations = [100, 250, 150]

print(make_records(names, durations))

# Mutability

def add_item(items):
    items.append("X")

values = ["A", "B"]
add_item(values)

print(values)

# what does this print and why?

# Python passes object references by assignment. 
# The parameter items refers to the same list object as values, so append() mutates that shared list.

# Lists implement += as an in-place mutation.

