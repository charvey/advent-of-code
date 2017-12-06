import math

input = 312051

x = 0
y = 0
n = 1
for d in range(3, 9999999, 2):
    n += 1
    x += 1

    for i in range(n, min(input, n + d - 2)):
        n += 1
        y += 1

    for i in range(n, min(input, n + d - 1)):
        n += 1
        x -= 1

    for i in range(n, min(input, n + d - 1)):
        n += 1
        y -= 1

    for i in range(n, min(input, n + d - 1)):
        n += 1
        x += 1

    if n == input:
        break

print(math.fabs(x) + math.fabs(y))
