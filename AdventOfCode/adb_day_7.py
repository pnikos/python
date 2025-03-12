def solve_line(total, ar):
    p=(lambda x,y:x+y,lambda x,y:x*y)
    #ep=bin(len(ar)-1**2)

    for i in range( 2**(len(ar)-1)):
        res = ar[0]
        ep=bin(i).replace("0b","").zfill(len(ar)-1)
        print(ep)
        for j in range(1, len(ar)):
            #print(ep[j-1])
            res = p[int(ep[j-1])](res, ar[j])
            #print(res)
        if res == total:
            print(ar)
            return res
    return 0

sum=fr=0
with open("data/adv_day_7.dat", 'r') as file:
    for line in file.readlines():
        tb=list(map(int, line.replace(":","").split()))
        arr=tb[1:]
 #       print(tb)
   #     print(arr)
        fr=solve_line(tb[0], arr)
        sum+=fr
        print(f"===> {fr} - {sum}")

print(f"Total: {sum}")

lst = list(map(int, "5 8 3 2 8 44 2 8 9 80 81 3".split()))
#print(solve_line(372902,lst))
lst = list(lst)

