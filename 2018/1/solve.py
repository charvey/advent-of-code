from aocd import get_data

input = get_data(day=1, year=2018)

steps = list(map(int, input.splitlines()))

print(sum(steps))

freqs = set()
freq = 0
current = 0

while freq not in freqs:
    freqs.add(freq)
    freq += steps[current]
    current = (current+1) % len(steps)

print(freq)
