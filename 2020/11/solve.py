from aocd import get_data

input = get_data(day=11, year=2020)

layout = [list(s) for s in input.splitlines()]


def solve(get_neighbors, limit):
    current = layout
    occupied = 0
    while True:
        changes = 0
        next_layout = list()
        for i in range(len(current)):
            next_row = list()
            for j in range(len(current[i])):
                next_seat = current[i][j]

                if next_seat == ".":
                    pass
                else:
                    neighbors = get_neighbors(current, i, j)

                    if next_seat == "L" and neighbors == 0:
                        next_seat = "#"
                        changes += 1
                        occupied += 1
                    elif next_seat == "#" and neighbors >= limit:
                        next_seat = "L"
                        changes += 1
                        occupied -= 1

                next_row.append(next_seat)
            next_layout.append(next_row)
        current = next_layout

        # print(occupied)
        # for l in current:
        #    print("".join(l))

        if changes == 0:
            return occupied


def adjacent_neighbors(current, i, j):
    neighbors = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue
            elif (
                i + x >= 0
                and i + x < len(current)
                and j + y >= 0
                and j + y < len(current[i])
            ):
                if current[x + i][y + j] == "#":
                    neighbors += 1
    return neighbors


def seen_neighbors(current, i, j):
    neighbors = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue
            a = i + x
            b = j + y
            while a >= 0 and a < len(current) and b >= 0 and b < len(current[a]):
                if current[a][b] == "#":
                    neighbors += 1
                    break
                elif current[a][b] == "L":
                    break
                else:
                    a += x
                    b += y

    return neighbors


print(solve(adjacent_neighbors, 4))
print(solve(seen_neighbors, 5))