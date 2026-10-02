

def read_file():
    t = []
    with open("data/adv_day_10.dat", "r") as file:
        for line in file.readlines():
            tl = []
            for d in line:
                try:
                    tl.append(int(d))
                except ValueError:
                    continue
            t.append(tl)
    return t

def scan_starts(t):
    for 

def follow_path():


t = read_file()
