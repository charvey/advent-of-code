file = open('input.txt', 'r')
originalJumps = [int(x) for x in file]
file.close()

jumps = list(originalJumps)
current = 0
steps = 0
while 0 <= current and current < len(jumps):
    jump = jumps[current]
    jumps[current] += 1
    current = current + jump
    steps += 1
print(steps)

jumps = list(originalJumps)
current = 0
steps = 0
while 0 <= current and current < len(jumps):
    jump = jumps[current]
    if jump >= 3:
        jumps[current] -= 1
    else:
        jumps[current] += 1
    current = current + jump
    steps += 1
print(steps)
