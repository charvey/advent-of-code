from aocd import get_data
from aocd import submit

input = "3,4,3,1,2"

input = get_data(day=6, year=2021)

school = [0] * 9

for x in input.split(","):
    school[int(x)] += 1


def next(school):
    new_school = [0] * 9
    for i in range(8):
        if i == 0:
            new_school[8] += school[i]
            new_school[6] += school[i]

        new_school[i] += school[i + 1]
    return new_school


for day in range(80):
    school = next(school)

submit(sum(school), part="a", day=6, year=2021)

for day in range(80, 256):
    school = next(school)

submit(sum(school), part="b", day=6, year=2021)
