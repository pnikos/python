
def Solution(N):
    b = bin(N)
    max = 0
    tx = b.split('1')
    del tx[0]
    if b[len(b)-1] == '0':
        del tx[len(tx)-1]
    for d in tx:
        if len(d) > max:
            max = len(d)
    return max



x=32
print(Solution(x))
print(bin(x))