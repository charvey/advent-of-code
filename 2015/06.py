from aocd import data, submit
import itertools

operations = []
for line in data.splitlines():
    parts = line.split()
    if parts[0] == 'toggle':
        op = 'toggle'
    else:
        op = parts[1]
    lx, ly = [int(x) for x in parts[-3].split(',')]
    rx, ry = [int(x) for x in parts[-1].split(',')]
    operations.append((op, min(lx, rx), min(ly, ry), max(lx, rx), max(ly, ry)))


def isLightOn(x, y):
    on = False
    brightness = 0
    for op in operations:
        if op[1] <= x and x <= op[3] and op[2] <= y and y <= op[4]:
            if op[0] == 'toggle':
                on = not on
                brightness += 2
            elif op[0] == 'on':
                on = True
                brightness += 1
            elif op[0] == 'off':
                on = False
                brightness = max(0, brightness - 1)
    return on, brightness


count = 0
brightness = 0
for p in itertools.product(range(0, 1000), repeat=2):
    light = isLightOn(p[0], p[1])
    if light[0]:
        count += 1
    brightness += light[1]

submit(count, part='a')
submit(brightness, part='b')
