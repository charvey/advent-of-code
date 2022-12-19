from aocd import data, submit

for line in data.splitlines():
    line = line.strip()
    sum1 = 0
    sum2 = 0
    for i in range(len(line)):
        if line[i] == line[(i + 1) % len(line)]:
            sum1 += int(line[i])
        if line[i] == line[(i + int(len(line) / 2)) % len(line)]:
            sum2 += int(line[i])
    submit(sum1, part='a')
    submit(sum2, part='b')
