from aocd import data, submit

lines = data.splitlines()

length = len(lines[0])


def get_counts(lines):
    counts = {"0": [0] * length, "1": [0] * length}

    for line in lines:
        for i in range(len(line)):
            counts[line[i]][i] += 1

    return counts


counts = get_counts(lines)

gamma = ""
epsilon = ""
for i in range(length):
    if counts["0"][i] < counts["1"][i]:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

submit(gamma * epsilon, part="a")


def oxygen():
    remainders = lines
    for i in range(length):
        counts = get_counts(remainders)
        next = []
        for line in remainders:
            c = line[i]
            if (c == "1" and counts["1"][i] >= counts["0"][i]) or (
                c == "0" and counts["0"][i] > counts["1"][i]
            ):
                next.append(line)
        remainders = next
        if len(remainders) == 1:
            return int(remainders[0], 2)


def c02():
    remainders = lines
    for i in range(length):
        counts = get_counts(remainders)
        next = []
        for line in remainders:
            c = line[i]
            if (c == "1" and counts["1"][i] < counts["0"][i]) or (
                c == "0" and counts["0"][i] <= counts["1"][i]
            ):
                next.append(line)
        remainders = next
        if len(remainders) == 1:
            return int(remainders[0], 2)


submit(oxygen() * c02(), part="b")
