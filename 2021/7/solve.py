from aocd import get_data
from aocd import submit
import statistics

input = get_data(day=7, year=2021)

crabs = [int(x) for x in input.split(",")]

middle = int(statistics.median(crabs))

distance = 0
for crab in crabs:
    distance += abs(crab - middle)

submit(distance, part="a", day=7, year=2021)


def addup(dist):
    return int(dist * (dist + 1) / 2)


middle = int(statistics.mean(crabs))

distance = 0
for crab in crabs:
    distance += addup(abs(crab - middle))

submit(distance, part="b", day=7, year=2021)
