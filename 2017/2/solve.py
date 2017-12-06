file = open('input.txt', 'r')
sum1 = 0
sum2 = 0
for line in file:
    numbers = sorted(list(map(int, line.strip().split())))
    sum1 += max(numbers) - min(numbers)
    for a in numbers:
        for b in numbers:
            if a < b and b % a == 0:
                sum2 += int(b / a)
print(sum1)
print(sum2)
file.close()
