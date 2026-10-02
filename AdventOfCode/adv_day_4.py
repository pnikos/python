import re

def count_xmas_hor(ar):
    total = 0
    for d in ar:
        cnt = len(re.findall("XMAS", d))
        total += cnt
        cnt = len(re.findall("XMAS", ''.join(reversed(d))))
        total += cnt

    return total

def count_xmas_ver(ar):
    total =0
    for i in range(0, len(ar[0])):
        line = ""
        for j in range(0, len(ar)):
            #print(f"{i}{j}")
            line += ar[j][i]
        cnt = len(re.findall("XMAS", line))
        total += cnt
        cnt = len(re.findall("XMAS", ''.join(reversed(line))))
        total += cnt
    return total

def count_xmas_diag(ar):
    total = 0

    for i in range(0, len(ar)):
        line = ""
        for j in range(i, -1, -1):
            print(f"{i-j}{j}", end=" ")
            line += ar[i-j][j]
        print(line)
        cnt = len(re.findall("XMAS", line))
        total += cnt
        cnt = len(re.findall("XMAS", ''.join(reversed(line))))
        total += cnt

    for i in range(len(ar)):
        line = ""
        for j in range(i, -1, -1):
            print(f"{i-j}{j}", end=" ")
            line += ar[i-j][j]
        print(line)

    return total


with open("data/tmp.dat", 'r') as file:
    arr = file.read()
    tb = arr.split()
   # print(tb)

    for i in range(0, 10):
        for j in range(0, 10):
            print(f"{i}{j}", end=" ")
        print()

    print()

    total = 0
    total += count_xmas_hor(tb)
    total += count_xmas_ver(tb)
    count_xmas_diag(tb)

    print(total)