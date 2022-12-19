from aocd import data, submit

steps = data.strip()


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


submit(len(findVisited(steps)), part='a')
submit(len(findVisited(steps[0::2]).union(findVisited(steps[1::2]))), part='b')
