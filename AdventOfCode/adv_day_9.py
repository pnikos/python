
lst = []
with open("data/adv_day_9.dat", "r") as file:
    for line in file.readlines():
        t=1
        k=0
        for d in line:
            if d.isnumeric():
                for i in range(int(d)):
                    if t==1:
                        lst.append(k)
                    else:
                        lst.append('.')
                t=-t
                if t==1:
                    k += 1
        print(lst)
        for i in range(len(lst)):
            if lst[i] == '.':
                k=len(lst)-1
                while lst[k] == '.':
                    k-=1
                if k<=i:
                    break
                lst[i] = lst[k]
                lst[k] = '.'
        print(lst)
        k=checksum=0
        for d in lst:
            if d != '.':
                checksum += d * k
                k+=1

        print(checksum)