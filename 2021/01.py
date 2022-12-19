from aocd import data, submit

depths = [int(x) for x in data.splitlines()]


def Window3(depths):
    result = []
    for i in range(2, len(depths)):
        result.append(depths[i - 2] + depths[i - 1] + depths[i])
    return result


def count_inc(depths):
    increases = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            increases += 1
    return increases


submit(count_inc(depths), part="a")
submit(count_inc(Window3(depths)), part="b")
