from aocd import data, submit

input = "3,4,3,1,2"

input = data

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

submit(sum(school), part="a")

for day in range(80, 256):
    school = next(school)

submit(sum(school), part="b")
