from aocd import data, submit

trees = data.splitlines()


def Trees(r, d):
    y, x = 0, 0
    treesHit = 0
    while y < len(trees):
        if trees[y][x % len(trees[y])] == "#":
            treesHit += 1

        y += d
        x += r
    return treesHit


submit(Trees(3, 1), part='a')
submit(Trees(1, 1)
       * Trees(3, 1)
       * Trees(5, 1)
       * Trees(7, 1)
       * Trees(1, 2), part='b')
