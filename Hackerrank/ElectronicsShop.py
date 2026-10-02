def getMoneySpent(keyboards, drives, b):
    max = -1
    for k in keyboards:
        for d in drives:
            if (k+d) > max and (k+d) < b:
                max = k+d
    return max



if __name__ == '__main__':
    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(moneySpent)
