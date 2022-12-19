from aocd import data, submit

input = data

cals = [sum([int(c) for c in elf.splitlines()]) for elf in input.split("\n\n")]

cals.sort()

submit(max(cals), part="a")
submit(sum(cals[-3:]), part="b")
