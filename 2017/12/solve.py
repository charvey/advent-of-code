nodes = dict()


def add(n, a, b):
    if a not in n:
        n[a] = set()
    n[a].add(b)
    if b not in n:
        n[b] = set()
    n[b].add(a)


file = open('input.txt', 'r')
for line in file:
    lhs, rhs = line.split(' <-> ')
    l = int(lhs)
    for r in [int(x.strip()) for x in rhs.split(',')]:
        add(nodes, l, r)
file.close()


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


print(len(connected(nodes, 0)))

minimums = set()
for x in nodes:
    minimums.add(min(connected(nodes, x)))
print(len(minimums))
