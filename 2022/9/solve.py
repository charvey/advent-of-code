from aocd import get_data
from aocd import submit
import math

input = get_data(day=9, year=2022)

knots = 10

kx = [0]*knots
ky = [0]*knots
visited = [set() for _ in range(knots)]

for line in input.splitlines():
    dir, count = line.split(' ')

    for x in range(int(count)):
        if dir == 'D':
            ky[0] -= 1
        elif dir == 'U':
            ky[0] += 1
        elif dir == 'L':
            kx[0] -= 1
        elif dir == 'R':
            kx[0] += 1

        for k in range(1, knots):
            dx = kx[k-1]-kx[k]
            dy = ky[k-1]-ky[k]

            if math.sqrt(math.pow(dx, 2)+math.pow(dy, 2)) >= 2:
                if dx != 0:
                    kx[k] += int(math.copysign(1, dx))
                if dy != 0:
                    ky[k] += int(math.copysign(1, dy))

            visited[k].add((kx[k], ky[k]))

submit(len(visited[1]), part="a", day=9, year=2022)
submit(len(visited[-1]), part="b", day=9, year=2022)
