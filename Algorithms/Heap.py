# Heap
import heapq

class HeapN:
    def __init__(self):
        self.heap = []

    def heappush(self, h, element):
        self.heap.append(element)

    def heapprint(self):
        for d in self.heap:
            print(d)

org_ls = [1, 3, 4, 8, 9, 11]
hq = []
for i in org_ls:
    heapq.heappush(hq, i)
heapq.heappush(hq, 2)
print(hq)

ls = []
a = 5
hp = HeapN()
HeapN.heappush(hp, ls, a)
HeapN.heapprint(hp)
hp.heappush(ls, 3)
hp.heapprint()