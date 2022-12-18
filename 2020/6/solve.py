from aocd import get_data

input = get_data(day=6, year=2020)

groups = list()
group = list()
for line in input.splitlines():
    if line == "":
        groups.append(group)
        group = list()
        continue

    person = set(line)
    group.append(person)

groups.append(group)


anyTotalCount = 0
allTotalCount = 0
for group in groups:
    anySet = set()
    allSet = set("abcdefghijklmnopqrstuvwxyz")
    for person in group:
        anySet = anySet.union(person)
        allSet = allSet.intersection(person)
    anyTotalCount += len(anySet)
    allTotalCount += len(allSet)

print(anyTotalCount)
print(allTotalCount)