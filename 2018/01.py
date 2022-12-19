from aocd import data, submit

steps = list(map(int, data.splitlines()))

submit(sum(steps), part='a')

freqs = set()
freq = 0
current = 0

while freq not in freqs:
    freqs.add(freq)
    freq += steps[current]
    current = (current+1) % len(steps)

submit(freq, part='b')
