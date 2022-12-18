from aocd import get_data
from aocd import submit

input = get_data(day=6, year=2022)


def find(str, n):
    for i in range(n, len(str)):
        if len(set(str[i - n : i])) == n:
            return i


submit(find(input, 4), part="a", day=6, year=2022)
submit(find(input, 14), part="b", day=6, year=2022)
