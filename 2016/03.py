from aocd import data, submit


def countTriangles(triangles):
    count = 0
    for triangle in triangles:
        sides = sorted(triangle)
        if sides[0] + sides[1] > sides[2]:
            count += 1
    return count


numbers = []
for line in data.splitlines():
    numbers.append([int(x.strip()) for x in line.split()])


horizontalTriangles = numbers
verticalTriangles = []

for i in range(0, len(numbers), 3):
    for j in range(len(numbers[i])):
        verticalTriangles.append([
            numbers[i + 0][j],
            numbers[i + 1][j],
            numbers[i + 2][j]
        ])

submit(countTriangles(horizontalTriangles), part='a')
submit(countTriangles(verticalTriangles), part='b')
