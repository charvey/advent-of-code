from aocd import get_data

input = get_data(day=20, year=2015)

target_house = int(int(input) / 10)


def build(target_house):
    houses = [0] * (target_house + 1)
    for i in range(1, target_house):
        for j in range(i, target_house, i):
            houses[j] += i

    return houses


def find():
    for i, house in enumerate(build(target_house)):
        if house >= target_house:
            return i


print(find())


def build2(target_house):
    houses = dict()
    for i in range(1, target_house):
        for j in range(i, 51 * i, i):
            if j not in houses:
                houses[j] = 0
            houses[j] += i

    return houses


def find2():
    houses = build2(target_house)
    for house in sorted(houses):
        if houses[house] * 11 >= target_house * 10:
            return house


print(find2())