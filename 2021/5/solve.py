from aocd import get_data
from aocd import submit

input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


input = get_data(day=5, year=2021)


def count(grid):
    count = 0
    for row in grid:
        for cell in row:
            # print(cell, end="")
            if cell >= 2:
                count += 1
        # print()
    return count


vert_grid = []
diag_grid = []

SIZE = 1000

for i in range(0, SIZE):
    vert_grid.append([0] * SIZE)
    diag_grid.append([0] * SIZE)

for line in input.splitlines():
    (one, two) = line.split(" -> ")
    x1, y1 = [int(x) for x in one.split(",")]
    x2, y2 = [int(x) for x in two.split(",")]

    if x1 == x2:
        x = x1
        for y in range(min(y1, y2), max(y1, y2) + 1):
            vert_grid[x][y] += 1
            diag_grid[x][y] += 1
    elif y1 == y2:
        y = y1
        for x in range(min(x1, x2), max(x1, x2) + 1):
            vert_grid[x][y] += 1
            diag_grid[x][y] += 1
    else:
        for i in range(abs(x1 - x2) + 1):
            x = x1 + (i if x2 > x1 else -i)
            y = y1 + (i if y2 > y1 else -i)

            diag_grid[x][y] += 1

    # print(grid)

    # count(vert_grid)
    # print()
    # count(diag_grid)
    # system("pause")


vert_count = count(vert_grid)
diag_count = count(diag_grid)

print(vert_count)
print(diag_count)

submit(vert_count, part="a", day=5, year=2021)
submit(diag_count, part="b", day=5, year=2021)
