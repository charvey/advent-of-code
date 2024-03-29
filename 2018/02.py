from aocd import data, submit


def contains_n(str, n):
    counts = dict()
    for c in str:
        if c not in counts:
            counts[c] = 0
        counts[c] += 1

    for entry in counts:
        if counts[entry] == n:
            return True
    return False


contains_2 = 0
contains_3 = 0

for line in data.splitlines():
    if contains_n(line, 2):
        contains_2 += 1
    if contains_n(line, 3):
        contains_3 += 1

submit(contains_2 * contains_3, part='a')
