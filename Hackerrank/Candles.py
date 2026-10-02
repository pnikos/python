#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candlesCounting' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY candles
#

def candlesCounting(k, candles):
    # Write your code here
    print(candles)
    lst = []
    f = True
    i = 0
    while f:
        ls = candles[0]
        f=False
        for i in range(len(candles)):
            if candles[i][0] > ls[len(ls) - 1][0] and candles[i]:
                ls.append(candles[i])
                f=True
            print(ls)
        lst.append(ls)
    print(lst)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #fptr = open("out.dat", 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    candles = []

    for _ in range(n):
        candles.append(list(map(int, input().rstrip().split())))

    result = candlesCounting(k, candles)

    #fptr.write(str(result) + '\n')

    #fptr.close()
