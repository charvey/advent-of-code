import itertools
import math

file = open('input.txt', 'r')
inputValue = int(file.readline())
file.close()


def spiral():
    x = -1
    y = 0
    n = 0
    for d in range(1, 9999999, 2):
        n += 1
        x += 1

        yield (x, y, n)

        for i in range(n, min(inputValue, n + d - 2)):
            n += 1
            y += 1
            yield (x, y, n)

        for i in range(n, min(inputValue, n + d - 1)):
            n += 1
            x -= 1
            yield (x, y, n)

        for i in range(n, min(inputValue, n + d - 1)):
            n += 1
            y -= 1
            yield (x, y, n)

        for i in range(n, min(inputValue, n + d - 1)):
            n += 1
            x += 1
            yield (x, y, n)


for n in spiral():
    if n[2] == inputValue:
        print(int(math.fabs(n[0]) + math.fabs(n[1])))
        break

squares = {(0, 0): 1}
for n in itertools.islice(spiral(), 1, None):
    sum = 0
    for p in itertools.product([-1, 0, 1], repeat=2):
        s = (n[0] + p[0], n[1] + p[1])
        if s in squares:
            sum += squares[s]
    squares[(n[0], n[1])] = sum

    if squares[(n[0], n[1])] > inputValue:
        print(squares[(n[0], n[1])])
        break
