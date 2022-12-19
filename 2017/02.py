from aocd import data, submit

sum1 = 0
sum2 = 0
for line in data.splitlines():
    numbers = sorted(list(map(int, line.strip().split())))
    sum1 += max(numbers) - min(numbers)
    for a in numbers:
        for b in numbers:
            if a < b and b % a == 0:
                sum2 += int(b / a)
submit(sum1, part='a')
submit(sum2, part='b')
