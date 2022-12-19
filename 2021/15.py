from aocd import data, submit
from math import inf

input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

input = data

risks = [[int(y) for y in x] for x in input.splitlines()]
min_risk = [[inf for y in x] for x in input.splitlines()]

min_risk[0][0] = 0

for i in range(1, len(risks)):
    min_risk[i][0] = min_risk[i - 1][0] + risks[i][0]

for i in range(1, len(risks[0])):
    min_risk[0][i] = min_risk[0][i - 1] + risks[0][i]

for i in range(1, len(risks)):
    for j in range(1, len(risks[i])):
        min_risk[i][j] = min(min_risk[i - 1][j],
                             min_risk[i][j - 1])+risks[i][j]

print(min_risk)

# submit(None, part="a", day=15, year=2021)
# submit(None, part="b", day=15, year=2021)
