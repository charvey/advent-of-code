from aocd import get_data
from aocd import submit

input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

input = get_data(day=14, year=2021)

template = input.splitlines()[0]

rules = dict()
for rule in input.splitlines()[2:]:
    l, r = rule.split(" -> ")
    rules[l] = r

cache = {1: dict()}
for (k, v) in rules.items():
    cache[1][k] = dict()
    for c in k + v:
        if c not in cache[1][k]:
            cache[1][k][c] = 0
        cache[1][k][c] += 1


def combine(x, y):
    z = dict()
    for k, v in x.items():
        if k not in z:
            z[k] = 0
        z[k] += v
    for k, v in y.items():
        if k not in z:
            z[k] = 0
        z[k] += v
    return z


def find(template, depth):
    if depth < 0:
        raise "Too deep"

    if depth not in cache:
        cache[depth] = dict()

    if len(template) == 2:
        if template in cache[depth]:
            return cache[depth][template]

        result = combine(
            find(template[0] + rules[template], depth - 1),
            find(rules[template] + template[1], depth - 1),
        )
        result[rules[template]] -= 1
        cache[depth][template] = result
        return result
    else:
        result = find(template[0:2], depth - 1)
        for i in range(1, len(template) - 1):
            result = combine(result, find(template[i : i + 2], depth - 1))
            result[template[i]] -= 1
        return result


at_10 = find(template, 10 + 1)

submit(max(at_10.values()) - min(at_10.values()), part="a", day=14, year=2021)

at_40 = find(template, 40 + 1)

submit(max(at_40.values()) - min(at_40.values()), part="b", day=14, year=2021)