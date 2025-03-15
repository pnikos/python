
antennas = dict()
k=0
with open("data/adv_day_8.dat", "r") as file:
    for line in file.readlines():
        ncols = len(line)-1
        for i in range(len(line)-1):
            if line[i] != '.':
                antennas.setdefault(line[i],[]).append((k,i))
        k+=1
    print(antennas)
    solution = []
    nrows = k

    for key, value in antennas.items():
        print(f"{key}:{value}")
        for v in value:
            for v2 in value:
                if v != v2:
                    x1 = (v[0]-(v2[0]-v[0]),v[1]-(v2[1]-v[1]))
                    x2 = (v2[0]+(v2[0]-v[0]),v2[1]+(v2[1]-v[1]))
                    if x1[0] >= 0 and x1[1] >= 0 and x1[0] < nrows and x1[1] < nrows:
                        if x1 not in solution:
                            solution.append(x1)
                    if x2[0] >= 0 and x2[1] >= 0 and x2[0] < ncols and x2[1] < ncols:
                        if x2 not in solution:
                            solution.append(x2)
    print(solution)
    print(len(solution))

