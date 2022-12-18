from aocd import get_data
from aocd import submit

input = get_data(day=8, year=2022).splitlines()

height = len(input)
width = len(input[0])

heights = dict()
visible = dict()
for r in range(len(input)):
    for c in range(len(input[r])):
        heights[(r, c)] = int(input[r][c])
        visible[(r, c)] = False

max_height = [-1]*len(input[0])
for r in range(len(input)):
    for c in range(len(input[r])):
        if heights[(r, c)] > max_height[c]:
            visible[(r, c)] = True
            max_height[c] = heights[(r, c)]

max_height = [-1]*len(input[0])
for r in reversed(range(len(input))):
    for c in range(len(input[r])):
        if heights[(r, c)] > max_height[c]:
            visible[(r, c)] = True
            max_height[c] = heights[(r, c)]

max_height = [-1]*len(input)
for c in range(len(input[0])):
    for r in range(len(input)):
        if heights[(r, c)] > max_height[r]:
            visible[(r, c)] = True
            max_height[r] = heights[(r, c)]

max_height = [-1]*len(input)
for c in reversed(range(len(input[0]))):
    for r in range(len(input)):
        if heights[(r, c)] > max_height[r]:
            visible[(r, c)] = True
            max_height[r] = heights[(r, c)]


part_a = len([v for v in visible.values() if v])


def scenic_score(heights, r, c):
    d1 = 0
    for x in range(r+1, height):
        d1 += 1
        if heights[(x, c)] >= heights[(r, c)]:
            break
    d2 = 0
    for x in range(r-1, -1, -1):
        d2 += 1
        if heights[(x, c)] >= heights[(r, c)]:
            break

    d3 = 0
    for x in range(c+1, width):
        d3 += 1
        if heights[(r, x)] >= heights[(r, c)]:
            break

    d4 = 0
    for x in range(c-1, -1, -1):
        d4 += 1
        if heights[(r, x)] >= heights[(r, c)]:
            break

    return d1*d2*d3*d4


max_scenic_score = 0
for r in range(height):
    for c in range(width):
        max_scenic_score = max(max_scenic_score, scenic_score(heights, r, c))

submit(part_a, part="a", day=8, year=2022)
submit(max_scenic_score, part="b", day=8, year=2022)
