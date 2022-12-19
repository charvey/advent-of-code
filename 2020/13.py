from aocd import data, submit

input = data

start = int(input.splitlines()[0])

buses = set()
for bus in input.splitlines()[1].split(","):
    if bus == "x":
        continue
    elif bus.isnumeric():
        buses.add((int(bus)))
    else:
        raise "Unknown bus"


def find_bus():
    time = start
    while True:
        for bus in buses:
            if time % bus == 0:
                return (time, bus)
        time += 1


x = find_bus()
submit((x[0] - start) * x[1], part='a')
