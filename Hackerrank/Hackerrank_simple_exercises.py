def swap_case(s):
    str = ""
    for i in range(0, len(s)):
        if s[i].isupper():
            str += s[i].lower()
        elif s[i].islower():
            str += s[i].upper()
        else:
            str += s[i]
    return str


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

exit(1)

# Hackerrank Basic Data Types
if __name__ == '__main__':
    lst = []
    N = int(input())

    for _ in range(int(N)):
        cmd = input()
        args = cmd.split()
        if args[0] == "append":
            lst.append(int(args[1]))
        elif args[0] == "insert":
            lst.insert(int(args[1]), int(args[2]))
        elif args[0] == "sort":
            lst.sort()
        elif args[0] == "reverse":
            lst.reverse()
        elif args[0] == "pop":
            lst.pop()
        elif args[0] == "print":
            print(lst)
        elif args[0] == "remove":
            lst.remove(int(args[1]))

exit(1)

# not working
import builtins

N = int(input())
lst = []

mp = map(int, input().split())
tp = tuple(mp)
print(hash(tp))
#for _ in range(0, N):


# Hackerrank Basic Data Types
if __name__ == '__main__':
    grades=[]
    scores=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grade = [name, score]
        grades.append(grade)
        scores.append(score)

scores.sort()
max=scores[0]
for d in scores:
    if d != max:
        runner_up=d
        break

names=[]
for st,sc in grades:
    if sc==runner_up:
        names.append(st)
names.sort()
print(grades)
print(names)


exit(1)
# Hackerrank Basic Data Types
n = int(input())
arr = map(int, input().split())

max=-1

lst = list(arr)
lst.sort(reverse=True)
for d in lst:
    if max == -1:
        max = d
    if max != -1 and d != max:
        print(d)
        break

print(lst)

exit(1)

def mutate_string(string, position, character):
    lst = list(string)
    lst[position] = character
    string2 = ''.join(lst)
    return string2

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

exit(1)

def count_substring(string, sub_string):
    f=0

    for i in range(0, len(string)):
        k=j=0
        while j < len(sub_string) and i+j < len(string):
            if string[i+j] == sub_string[j]:
                k+=1
            else:
                break
            j+=1
        if k == len(sub_string):
            f+=1
    return f



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

exit(1)

if __name__ == '__main__':
    s = input()

    q = [0 for _ in range(0,5)]

    for c in s:
        if c.isalnum():
            q[0]+=1
        if c.isalpha():
            q[1]+=1
        if c.isdigit():
            q[2]+=1
        if c.islower():
            q[3]+=1
        if c.isupper():
            q[4]+=1

    for d in q:
        if d>0:
            print(True)
        else:
            print(False)

exit(1)

import textwrap

def wrap_manual(string, max_width):
    lst = list(string)
    k=1
    i=0
    ln = len(lst)
    while i < ln:
        if k==max_width+1:
            lst.insert(i, '\n')
            k=0
            ln+=1
        k+=1
        i+=1
    return ''.join(lst)

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(max_width)
    str = wrapper.fill(text=string)
    return str

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

exit(1)

N, M = map(int, input().split())
for i in range(0, int(N / 2)):
    #for j in range(M/3):
    print('-'*int((N-1)/2-i)*3, end="")
    print('.|.'*int((i*2)+1), end="")
    print('-'*int((N-1)/2-i)*3)

print('-'*int((M-7)/2), end="")
print('WELCOME', end="")
print('-'*int((M-7)/2))
for i in range(int(N/2) - 1, -1, -1):
    print('-'*int((N-1)/2-i)*3, end="")
    print('.|.'*int((i*2)+1), end="")
    print('-'*int((N-1)/2-i)*3)
exit(1)

def average(array):
    # your code goes here
    s = set(array)
    lst = list(s)

    return sum(lst)/len(lst)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

exit(1)

import re


def fun(s):
    # return True if s is a valid email, else return False
    if re.match("^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\\.[a-zA-Z]{1,3}$", s) != None:
        return True
    else:
        return False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

exit(1)

s="hello   world  lol"


def solve(s):
    #lst = [x.capitalize() for x in list(s.split())]
    lst = []
    prev=" "
    for d in s:
        if d != " ":
            if prev == " ":
                lst.append(d.capitalize())
            else:
                lst.append(d)
        else:
            lst.append(d)
        prev = d
    return ''.join(lst)

print(solve(s))

exit(1)

# not optimal - half cases time out
def cnt(s, ss):
    i=j=0
    f=0
    while i+len(ss)<=len(s):
        if s[i:i+len(ss)] == ss:
            f+=1
        i+=1
    return f

def minion_game(string):
    k=t1=t2=0
    visited=[]
    for d in string:
        print(d, end=" ")
        if d not in ['A', 'E', 'I', 'O', 'U']:
            for i in range(k, len(string)):
                st = string[k:i+1]
                if st not in visited:
                    print(st, end=" ")
                    print(cnt(string,st))
                    t1+=cnt(string,st)
                    visited.append(st)
        else:
            for i in range(k, len(string)):
                st = string[k:i+1]
                if st not in visited:
                    print(st, end=" ")
                    print(cnt(string,st))
                    t2+=cnt(string,st)
                    visited.append(st)
        k+=1
    if t1 > t2:
        print("Stuart", t1)
    elif t1 < t2:
        print("Kevin", t2)
    else:
        print("Draw")

if __name__ == '__main__':
   # s = input()
    s="BANANA"
    minion_game(s)
exit(1)