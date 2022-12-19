from aocd import data, submit

floor = 0
position = 1
basementPosition = None
for line in data.splitlines():
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

submit(floor, part='a')
submit(basementPosition, part='b')
