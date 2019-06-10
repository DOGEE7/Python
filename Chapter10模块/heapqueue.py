from heapq import *
from random import shuffle

data = list(range(10))
shuffle(data)
heap = []
for d in data:
    heappush(heap, d)

print(heap)
for h in heap:
    print(heappop(heap))
print(nlargest(2, heap))
print(nsmallest(3,heap))
print(heap)
