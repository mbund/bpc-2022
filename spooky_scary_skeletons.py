from collections import Counter

N, K, Q = [int(x) for x in input().split()]
skeletons = [int(x) for x in input().split()]

for _ in range(Q):
    l, r = [int(x) for x in input().split()]

    line = skeletons[l - 1 : r]
    count = Counter(line)

    remaining = {x for x in line if count[x] % 2 != 0}

    if len(remaining) == 1:
        x ,= remaining
        print(x)
    else:
        print(0)
