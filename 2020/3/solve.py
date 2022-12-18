from aocd import get_data

input = get_data(day=3, year=2020)

trees = input.splitlines()


def Trees(r, d):
    y, x = 0, 0
    treesHit = 0
    while y < len(trees):
        if trees[y][x % len(trees[y])] == "#":
            treesHit += 1

        y += d
        x += r
    return treesHit


print(Trees(3, 1))
print(Trees(1, 1) * Trees(3, 1) * Trees(5, 1) * Trees(7, 1) * Trees(1, 2))
