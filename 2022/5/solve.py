from aocd import get_data
from aocd import submit

input = get_data(day=5, year=2022)

input = input.splitlines()


def msg(ship):
    msg = ""
    for stack in sorted(ship.keys()):
        msg += ship[stack][-1]
    return msg


l = 0

while input[l][1] != "1":
    l += 1

a_ship = {}
b_ship = {}

for stack in input[l].strip().split("   "):
    a_ship[stack] = []
    b_ship[stack] = []

for y in range(l):
    for x in range(1, len(input[y]), 4):
        c = input[y][x]
        if c != " ":
            a_ship[input[l][x]].insert(0, c)
            b_ship[input[l][x]].insert(0, c)

for move in input[l + 2:]:
    tokens = move.split(" ")
    m = int(tokens[1])
    a = tokens[3]
    b = tokens[5]

    b_ship[b].extend(b_ship[a][-m:])

    for _ in range(m):
        a_ship[b].append(a_ship[a].pop())
        b_ship[a].pop()

submit(msg(a_ship), part="a", day=5, year=2022)
submit(msg(b_ship), part="b", day=5, year=2022)
