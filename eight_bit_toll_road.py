from sys import stdin, setrecursionlimit
from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict
N = int(input())

setrecursionlimit(1000000)

@dataclass
class Road:
    end: int
    length: int

@dataclass
class City:
    roads: List[Road] = field(default_factory=list)
    min_length_for_cost: Dict[int, int] = field(default_factory=dict)

cities: Dict[int, City] = defaultdict(City)

for line in stdin.readlines():
    S, T, L = [int(x) for x in line.split()]
    cities[S].roads.append(Road(T, L))

def dfs(start, length, cost):
    city = cities[start]
    if cost in city.min_length_for_cost:
        if length < city.min_length_for_cost[cost]:
            city.min_length_for_cost[cost] = length
        else:
            return
    else:
        city.min_length_for_cost[cost] = length
    for road in city.roads:
        dfs(road.end, length+road.length, (cost+road.length)%256)

dfs(1, 0, 0)
print(*min(cities[2].min_length_for_cost.items()))