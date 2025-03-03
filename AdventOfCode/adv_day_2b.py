def check_list(ar):
    trd=okl=0
    prev = ar[0]
    for i in range(1, len(ar)):
        if trd == 0:
            if ar[i] > ar[i - 1]:
                trd = 1
            elif ar[i] < ar[i - 1]:
                trd = -1

        if trd == 1 and ar[i] - ar[i-1] <= 3 and ar[i] - ar[i-1] >= 1:
            okl=True
        elif trd == -1 and ar[i-1] - ar[i] <= 3 and ar[i-1] - ar[i] >= 1:
            okl=True
        else:
            okl=False
            break
    return okl

cnt = 0
with open("data/adv_day_2.dat", 'r') as file:
    for line in file.readlines():
 #       print(line)
        trd=okl=rm=0
        tmplist = []
        lnums = [int(x) for x in line.split()]
        sz = len(lnums)
        i=1
        while i < sz:
            if trd == 0:
                if lnums[i] > lnums[i-1]:
                    trd = 1
                elif lnums[i] < lnums[i-1]:
                    trd = -1

            if trd == 1 and lnums[i] - lnums[i-1] <= 3 and lnums[i] - lnums[i-1] >= 1:
                okl=True
            elif trd == -1 and lnums[i-1] - lnums[i] <= 3 and lnums[i-1] - lnums[i] >= 1:
                okl=True
            elif rm==0:
                tmplist = lnums.copy()
                del tmplist[i-1]
                if check_list(tmplist):
                    okl=True
                    lnums = tmplist.copy()
                    rm += 1
                    sz -= 1
                    if i < 2:
                        trd = 0

                else:
                    tmplist = lnums.copy()
                    del tmplist[i]
                    if check_list(tmplist):
                        okl=True
                        lnums = tmplist.copy()
                        rm+=1
                        sz -= 1
                        if i < 2:
                            trd = 0
                    else:
                        if i >= 2:
                            tmplist = lnums.copy()
                            del tmplist[i-2]
                            if check_list(tmplist):
                                okl=True
                                lnums = tmplist.copy()
                              #  trd = -trd
                                if i < 2:
                                    trd = 0
                                rm += 1
                                sz -= 1
                            else:
                                okl=False
                                break
                        else:
                            okl=False
                            break
            else:
                okl=False
                break
            i+=1
        if okl == True and rm == 1:
            print(line)
        #    print(rm)
            print(okl)
        if okl:
            cnt+=1
print(cnt)
