from aocd import get_data
from aocd import submit

input = get_data(day=1, year=2022)

cals = [sum([int(c) for c in elf.splitlines()]) for elf in input.split("\n\n")]

cals.sort()

submit(max(cals), part="a", day=1, year=2022)
submit(sum(cals[-3:]), part="b", day=1, year=2022)