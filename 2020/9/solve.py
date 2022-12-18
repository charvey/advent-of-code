from aocd import get_data

input = get_data(day=9, year=2020)

numbers = [int(x) for x in input.splitlines()]


def is_valid(i):
    for x in range(i - 25, i):
        for y in range(x + 1, i):
            if numbers[x] + numbers[y] == numbers[i]:
                return True
    return False


def find_invalid():
    for i in range(25, len(numbers)):
        if not is_valid(i):
            return numbers[i]


def find_range(target):
    for i in range(0, len(numbers)):
        for j in range(i, len(numbers)):
            if sum(numbers[i:j]) == target:
                return numbers[i:j]


invalid = find_invalid()
print(invalid)
invalid_range = find_range(invalid)
print(min(invalid_range) + max(invalid_range))
