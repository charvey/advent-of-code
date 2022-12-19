from aocd import data, submit

input = data


def find(str, n):
    for i in range(n, len(str)):
        if len(set(str[i - n: i])) == n:
            return i


submit(find(input, 4), part="a")
submit(find(input, 14), part="b")
