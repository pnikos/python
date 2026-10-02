# Maximum Subarray Sum

def max_subarray_sum(ar):
    sum = 0
    max = 0
    final_list = []
    for i in range(len(ar)):
        sum = 0
        sub_list = []
        for j in range(i, len(ar)):
            sum += ar[j]
            sub_list.append(ar[j])
        if sum > max:
            max = sum
            final_list = sub_list

    print(final_list, max)

arr = [2, 3, -8, 7, -1, 2, 3]
#max_subarray_sum(arr)

def find_the_missing_number_sorted(ar):
    missing = -1
    if len(ar) < 2:
        return
    for i in range(2, len(ar)):
        if ar[i] != ar[i-1] + 1:
            missing = ar[i-1] + 1
    return missing

def
arr = [1, 2, 4, 6, 3, 7, 8]
print(find_the_missing_number(arr))

