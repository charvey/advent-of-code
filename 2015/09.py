from aocd import data, submit
import itertools
import sys

cities = set()
distances = dict()
for line in data.splitlines():
    frm, _, to, _, dist = line.split()
    cities.add(frm)
    cities.add(to)
    if frm not in distances:
        distances[frm] = dict()
    if to not in distances:
        distances[to] = dict()
    distances[frm][to] = int(dist)
    distances[to][frm] = int(dist)

perms = itertools.permutations(cities)

shortestDistance = sys.maxsize
longestDistance = 0
for perm in perms:
    dist = 0
    current = perm[0]
    otherCities = iter(perm)
    next(otherCities)
    for city in otherCities:
        dist += distances[current][city]
        current = city
    shortestDistance = min(shortestDistance, dist)
    longestDistance = max(longestDistance, dist)

submit(shortestDistance, part='a')
submit(longestDistance, part='b')
