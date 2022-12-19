from aocd import data, submit

rules = dict()
for line in data.splitlines():
    key, value = line.split(" bags contain ")

    rules[key] = dict()
    if value == "no other bags.":
        continue

    for item in value[:-1].split(","):
        words = item.strip().split(" ")
        rules[key][f"{words[1]} {words[2]}"] = int(words[0])


def contains_gold(color):
    for c in rules[color].keys():
        if c == "shiny gold":
            return True
        if contains_gold(c):
            return True
    return False


count = 0
for rule in rules.keys():
    if rule != "shiny gold" and contains_gold(rule):
        count += 1
submit(count, part='a')


def count_bags(color):
    count = 0
    for c in rules[color]:
        count += rules[color][c] * (1 + count_bags(c))
    return count


submit(count_bags("shiny gold"), part='b')
