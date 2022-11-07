import random

N = random.randint(0, 2000)
print(N)

for _ in range(N):
    S, T = random.randint(1, 5), random.randint(1, 5)
    L = random.randint(1, 1000000)

    print(S, T, L)