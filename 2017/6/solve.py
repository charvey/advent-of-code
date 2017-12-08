file = open('input.txt', 'r')
line = file.readline().strip()
file.close()

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
print(len(visited))
print(len(visited) - visited[tuple(banks)])
