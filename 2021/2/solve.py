from aocd import get_data
from aocd import submit

input = get_data(day=2, year=2021)

a_x = 0
b_x = 0
a_z = 0
b_z = 0
aim = 0

for line in input.splitlines():
    dir, dist = line.split(" ")

    dist = int(dist)

    if dir == "forward":
        a_x += dist
        b_x += dist
        b_z += aim * dist
    elif dir == "down":
        a_z += dist
        aim += dist
    elif dir == "up":
        a_z -= dist
        aim -= dist

submit(a_x * a_z, part="a", day=2, year=2021)
submit(b_x * b_z, part="b", day=2, year=2021)
