file = open('input.txt', 'r')
basementPosition = None
for line in file:
    floor = 0
    position = 1
    for c in line:
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        else:
            raise Exception("Invalid character")

        if floor < 0 and basementPosition is None:
            basementPosition = position
        position += 1
file.close()
print(floor)
print(basementPosition)
