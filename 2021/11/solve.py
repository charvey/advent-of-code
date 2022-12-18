from aocd import get_data
from aocd import submit

input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

input = get_data(day=11, year=2021)

cavern = [[int(y) for y in x] for x in input.splitlines()]


def process():
    flashes_toprocess = set()

    for i in range(10):
        for j in range(10):
            print(cavern[i][j], end="")
            cavern[i][j] += 1
            if cavern[i][j] > 9:
                flashes_toprocess.add((i, j))
        print()
    print()

    flashed = set()
    while len(flashes_toprocess) > 0:
        next = flashes_toprocess.pop()

        i = next[0]
        j = next[1]

        flashed.add((i, j))

        for k in [i - 1, i, i + 1]:
            if k < 0 or k > 9:
                continue
            for l in [j - 1, j, j + 1]:
                if l < 0 or l > 9:
                    continue

                if k == i and l == j:
                    continue

                cavern[k][l] += 1

                if cavern[k][l] > 9 and (k, l) not in flashed:
                    flashes_toprocess.add((k, l))

    for flash in flashed:
        cavern[flash[0]][flash[1]] = 0

    return len(flashed)


flashes = 0
for step in range(100):
    flashes += process()

steps = 101
while process() < 100:
    steps += 1

print(flashes)
print(steps)

submit(flashes, part="a", day=11, year=2021)
submit(steps, part="b", day=11, year=2021)
