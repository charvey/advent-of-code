file = open('input.txt', 'r')
steps = file.readline().strip()
file.close()


def findVisited(steps):
    pos = (0, 0)
    visited = {pos}
    for step in steps:
        if step == '^':
            pos = (pos[0], pos[1] + 1)
        elif step == 'v':
            pos = (pos[0], pos[1] - 1)
        elif step == '>':
            pos = (pos[0] + 1, pos[1])
        elif step == '<':
            pos = (pos[0] - 1, pos[1])
        visited.add(pos)
    return visited


print(len(findVisited(steps)))
print(len(findVisited(steps[0::2]).union(findVisited(steps[1::2]))))
