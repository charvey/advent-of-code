from aocd import data, submit

expenses = [int(x) for x in data.splitlines()]


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


submit(FindTwo(expenses), part='a')
submit(FindThree(expenses), part='b')
