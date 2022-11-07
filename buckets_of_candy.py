from queue import PriorityQueue
from sys import stdin
from itertools import islice

import time

t1 = time.perf_counter()

line1 = input()
B = int(line1.split()[0])
N = int(line1.split()[1])

num_empty_buckets = B - N
candies = PriorityQueue()
for x in stdin.readlines():
    candies.put(-int(x.strip()))

t2 = time.perf_counter()

while num_empty_buckets > 0:
    m = -candies.get()
    candies.put(-(m // 2))
    candies.put(-(m - (m // 2)))
    num_empty_buckets -= 1

t3 = time.perf_counter()

print(-candies.get())

print(t2 - t1, t3 - t2)