from aocd import data, submit

input = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

input = data

neighbors = dict()

for edge in input.splitlines():
    a, b = edge.split("-")

    if a not in neighbors:
        neighbors[a] = set()
    if b not in neighbors:
        neighbors[b] = set()

    if b != "start" and a != "end":
        neighbors[a].add(b)

    if a != "start" and b != "end":
        neighbors[b].add(a)


def explore(current, path, extra_visit, paths):
    if current == "end":
        paths.add(",".join(path))
        return

    for neighbor in neighbors[current]:
        if neighbor.isupper() or neighbor == "end" or neighbor not in path:
            explore(neighbor, path + [neighbor], extra_visit, paths)
        elif extra_visit:
            print(neighbor)
            explore(neighbor, path + [neighbor], False, paths)


print(neighbors)

paths_a = set()
explore("start", ["start"], False, paths_a)
# print("\n".join(paths_a))
print(len(paths_a))

submit(len(paths_a), part="a")

paths_b = set()
explore("start", ["start"], True, paths_b)
# print("\n".join(paths_b))
print(len(paths_b))

submit(len(paths_b), part="b")
