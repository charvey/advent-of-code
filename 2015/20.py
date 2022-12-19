from aocd import data, submit

input = data

target_house = int(int(input) / 10)


def build_a(target_house):
    houses = [0] * (target_house + 1)
    for i in range(1, target_house):
        for j in range(i, target_house, i):
            houses[j] += i

    return houses


def find_a():
    for i, house in enumerate(build_a(target_house)):
        if house >= target_house:
            return i


submit(find_a(), part='a')


def build_b(target_house):
    houses = dict()
    for i in range(1, target_house):
        for j in range(i, 51 * i, i):
            if j not in houses:
                houses[j] = 0
            houses[j] += i

    return houses


def find_b():
    houses = build_b(target_house)
    for house in sorted(houses):
        if houses[house] * 11 >= target_house * 10:
            return house


submit(find_b(), part='b')
