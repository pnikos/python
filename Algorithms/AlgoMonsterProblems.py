# Given a sorted list of numbers, remove duplicates and return the new length. You must do this in-place and without using extra memory.
# Input: [0, 0, 1, 1, 1, 2, 2].
# Output: 3.

def remove_duplicate(ar):
    i=0
    ln=len(ar)
    for i in range(ln):
        j=i
        while j<ln and ar[j] == ar[i]:
            ar.pop(j)
            j+=1
            ln-=1

    return len(ar)

lst = [0, 0, 1, 1, 1, 2, 2]
print(remove_duplicate(lst))

# Given an array of integers, move all the 0s to the back of the array while maintaining the relative order of the non-zero elements. Do this in-place using constant auxiliary space.
# Input:
# [1, 0, 2, 0, 0, 7]
# Output:
# [1, 2, 7, 0, 0, 0]
def move_zeros(ar):
    i=0
    while i < len(ar):
        if ar[i] == 0:
            ch=False
            for j in range(i+1, len(ar)):
                if ar[j] != 0:
                    ar[j-1],ar[j]=ar[j],ar[j-1]
                    ch=True
            if ch==False:
                break
        else:
            i+=1
    return(ar)

lst = [1, 0, 2, 0, 0, 7]
(print(move_zeros(lst)))

