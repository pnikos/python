import random

# Linear search O(n)


# Binary search (O(log(n)))
def binary_search():
    pass



# Insertion sort (best case: O(n), worst case: O(n^2))
def insertion_sort(ar):
    for i in range(1, len(ar)):
        key = ar[i]
        j = i - 1
        while j>=0 and key < ar[j]:
            ar[j+1] = ar[j]
            j -= 1
        ar[j+1] = key

# Merge sort (O(log(n)) - space complexity: O(n)
def merge_sort():
    pass

# Quick sort (best case: O(nlog(n)), worst case: O(n^2)) - space complexity: O(log(n))
def quick_sort():
    pass

# Travelling salesman solution
def greedy_algorithm():
    pass

initial_array = random.sample(range(1, 101), 20)
print(initial_array)
insertion_sort(initial_array)

print(initial_array)