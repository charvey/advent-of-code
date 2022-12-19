from aocd import data, submit

adapters = sorted([int(x) for x in data.splitlines()])

final_adapter = max(adapters) + 3

differences = {1: 0, 2: 0, 3: 0}
voltage = 0
for adapter in adapters:
    differences[adapter - voltage] += 1
    voltage = adapter
differences[final_adapter - voltage] += 1
voltage = final_adapter

submit(differences[1] * differences[3], part='a')

arrangement_cache = dict()


def get_arrangements(i=-1, current=0):
    if i in arrangement_cache:
        return arrangement_cache[i]

    arrangements = 0
    j = i + 1
    while j < len(adapters) and adapters[j] - current <= 3:
        arrangements += get_arrangements(j, adapters[j])
        j += 1
    if final_adapter - current <= 3:
        arrangements += 1
    arrangement_cache[i] = arrangements
    return arrangements


submit(get_arrangements(), part='b')
