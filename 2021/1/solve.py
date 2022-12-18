from re import sub
from aocd import get_data
from aocd import submit

input = get_data(day=1, year=2021)

depths = [int(x) for x in input.splitlines()]


def Window3(depths):
    result = []
    for i in range(2, len(depths)):
        result.append(depths[i - 2] + depths[i - 1] + depths[i])
    return result


def count_inc(depths):
    increases = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            increases += 1
    return increases


submit(count_inc(depths), part="a", day=1, year=2021)
submit(count_inc(Window3(depths)), part="b", day=1, year=2021)
