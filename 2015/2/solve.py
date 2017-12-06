file = open('input.txt', 'r')
area = 0
length = 0
for line in file:
    sides = sorted([int(x) for x in line.split('x')])
    area += sides[0] * sides[1] \
        + 2 * sides[0] * sides[1] \
        + 2 * sides[0] * sides[2] \
        + 2 * sides[1] * sides[2]
    length += 2 * (sides[0] + sides[1])\
        + sides[0] * sides[1] * sides[2]
file.close()
print(area)
print(length)
