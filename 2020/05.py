from aocd import data, submit
from math import ceil, floor


def seat_id_r(boarding_pass, l, h):
    if l == h:
        return l

    if boarding_pass[0] == "F" or boarding_pass[0] == "L":
        return seat_id_r(boarding_pass[1:], l, floor((h + l) / 2))
    if boarding_pass[0] == "B" or boarding_pass[0] == "R":
        return seat_id_r(boarding_pass[1:], ceil((h + l) / 2), h)

    raise "Invalid character"


def seat_id(boarding_pass):
    return seat_id_r(boarding_pass, 0, 8 * 128 - 1)


passes = set()
for line in data.splitlines():
    passes.add(seat_id(line))
submit(max(passes), part='a')


def my_seat(passes):
    for i in range(min(passes), max(passes)):
        if i not in passes:
            return i


submit(my_seat(passes), part='b')
