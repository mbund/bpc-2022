from sys import stdin

N = int(input())

layers = []

# Read in layers
layer = []
c = N
for line in stdin.readlines():
    if c == 0:
        N -= 1
        c = N
        layers.append(layer.copy())
        layer = []
    layer.append([int(x) for x in line.split()])
    c -= 1
layers.append(layer)

# Solve

def surrounding_costs(l, a, b):
    v = layers[l][a][b]
    

print(layers)
for l in layers:
    for a in l:
        for b in a:
            print(b, end=" ")
        print()
    print()
