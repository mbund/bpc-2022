nhouses, nsides, ndice, ntunnels = [int(x) for x in input().split()]

for _ in range(ntunnels):
    start, *endings = [int(x) for x in input().split()]



print(1 / (ndice * nsides) / nhouses)