from aocd import data, submit

nodes = dict()


def add(n, a, b):
    if a not in n:
        n[a] = set()
    n[a].add(b)
    if b not in n:
        n[b] = set()
    n[b].add(a)


for line in data.splitlines():
    lhs, rhs = line.split(' <-> ')
    l = int(lhs)
    for r in [int(x.strip()) for x in rhs.split(',')]:
        add(nodes, l, r)


def connected(n, e):
    counted = set()
    unvisited = set()
    unvisited.add(e)
    while len(unvisited) > 0:
        x = unvisited.pop()
        counted.add(x)
        for y in nodes[x]:
            if y not in counted:
                unvisited.add(y)
    return counted


submit(len(connected(nodes, 0)), part='a')

minimums = set()
for x in nodes:
    minimums.add(min(connected(nodes, x)))
submit(len(minimums), part='b')
