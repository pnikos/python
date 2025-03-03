import re

total = 0
with open("data/adv_day_3.dat", 'r') as file:
    for line in file.readlines():
        muls = re.findall("mul\([0-9]+\,[0-9]+\)",line)
        for d in muls:
            op1, op2 = map(int, re.findall("[0-9]+", d))
            print(f"{op1} = {op2}")
            res = op1 * op2
            total += res
    print(total)