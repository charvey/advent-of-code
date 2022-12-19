from aocd import data, submit

line = data.strip()

banks = [int(x) for x in line.split()]

visited = dict()

while tuple(banks) not in visited:
    visited[tuple(banks)] = len(visited)

    maxBank = 0
    for bank, blocks in enumerate(banks):
        if blocks > banks[maxBank]:
            maxBank = bank
    blocks = banks[maxBank]
    banks[maxBank] = 0
    for block in range(0, blocks):
        banks[(maxBank + 1 + block) % len(banks)] += 1

submit(len(visited), part='a')
submit(len(visited) - visited[tuple(banks)], part='b')
