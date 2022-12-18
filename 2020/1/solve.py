from aocd import get_data

input = get_data(day=1, year=2020)

expenses = [int(x) for x in input.splitlines()]


def FindTwo(expenses):
    for a in expenses:
        for b in expenses:
            if a + b == 2020:
                return a * b


def FindThree(expenses):
    for a in expenses:
        for b in expenses:
            for c in expenses:
                if a + b + c == 2020:
                    return a * b * c


print(FindTwo(expenses))
print(FindThree(expenses))