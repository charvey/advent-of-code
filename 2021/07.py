from aocd import data, submit
import statistics

input = data

crabs = [int(x) for x in input.split(",")]

middle = int(statistics.median(crabs))

distance = 0
for crab in crabs:
    distance += abs(crab - middle)

submit(distance, part="a")


def addup(dist):
    return int(dist * (dist + 1) / 2)


middle = int(statistics.mean(crabs))

distance = 0
for crab in crabs:
    distance += addup(abs(crab - middle))

submit(distance, part="b")
