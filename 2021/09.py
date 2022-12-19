from aocd import data, submit

input = """2199943210
3987894921
9856789892
8767896789
9899965678"""

input = data

depths = dict()
basin = dict()

for i, row in enumerate(input.splitlines()):
    for j, c in enumerate(row):
        depths[(i, j)] = int(c)
        basin[(i, j)] = 0 if depths[(i, j)] == 9 else 1

risk = 0
for cur in depths.keys():

    neighbors = [
        (cur[0] + 0, cur[1] - 1),
        (cur[0] + 0, cur[1] + 1),
        (cur[0] - 1, cur[1] + 0),
        (cur[0] + 1, cur[1] + 0),
    ]

    min = cur
    for neighbor in neighbors:
        if neighbor in depths and depths[neighbor] <= depths[min]:
            min = neighbor

    if min == cur:
        risk += depths[cur] + 1

submit(risk, part="a")

for d in range(8, 0, -1):
    for c in depths:
        if depths[c] == d:
            neighbors = [
                (c[0] + 0, c[1] - 1),
                (c[0] + 0, c[1] + 1),
                (c[0] - 1, c[1] + 0),
                (c[0] + 1, c[1] + 0),
            ]

            nxt = c
            for neighbor in neighbors:
                if neighbor in depths and depths[neighbor] < depths[nxt]:
                    nxt = neighbor

            if nxt != c:
                basin[nxt] += basin[c]
                basin[c] = 0


biggest = sorted(basin.values())[-3:]

submit(biggest[0] * biggest[1] * biggest[2], part="b")
