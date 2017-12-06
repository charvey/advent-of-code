import math

firstRevisit = None
file = open('input.txt', 'r')
for line in file:
    x = 0
    y = 0
    visited = {(x, y)}
    theta = math.radians(90)
    for step in line.split(','):
        step = step.strip()
        direction = step[0]
        if direction == 'R':
            theta -= math.radians(90)
        elif direction == 'L':
            theta += math.radians(90)
        else:
            raise Exception("Invalid direction")
        distance = int(step[1:])
        for _ in range(distance):
            x += round(math.cos(theta))
            y += round(math.sin(theta))
            if (x, y) in visited and firstRevisit is None:
                firstRevisit = (x, y)
            visited.add((x, y))
    print(int(math.fabs(x) + math.fabs(y)))
    print(int(math.fabs(firstRevisit[0]) + math.fabs(firstRevisit[1])))
file.close()
