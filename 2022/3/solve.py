from aocd import get_data
from aocd import submit

input = get_data(day=3, year=2022)


def priority(c):
    if c.isupper():
        return ord(c) - (ord("A") - 1) + 26
    elif c.islower():
        return ord(c) - (ord("a") - 1)


rucksacks = input.splitlines()

priorities = 0
for rucksack in rucksacks:
    split = int(len(rucksack) / 2)

    first = set(rucksack[:split])
    second = set(rucksack[split:])

    common = first.intersection(second)

    for c in common:
        priorities += priority(c)

grouped = [rucksacks[i : i + 3] for i in range(0, len(rucksacks), 3)]

badge_priorities = 0
for group in grouped:
    badge = set(group[0]).intersection(group[1]).intersection(group[2])

    for b in badge:
        badge_priorities += priority(b)

submit(priorities, part="a", day=3, year=2022)
submit(badge_priorities, part="b", day=3, year=2022)
