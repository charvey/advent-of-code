from aocd import data, submit

input = data.splitlines()


def mkdir(pwd, dir):
    if dir not in pwd:
        pwd[dir] = dict()


def total_size(dir):
    size = 0

    for x in dir:
        if type(dir[x]) is dict:
            size += total_size(dir[x])
        else:
            size += dir[x]

    return size


root = dict()
path = [root]
for line in input:
    tokens = line.split()
    if tokens[0] == '$':
        if tokens[1] == 'cd':
            if tokens[2] == '/':
                path = [root]
            elif tokens[2] == '..':
                path.pop()
            else:
                mkdir(path[-1], tokens[2])
                path.append(path[-1][tokens[2]])
        elif tokens[1] == 'ls':
            pass
    else:
        if tokens[0] == 'dir':
            mkdir(path[-1], tokens[1])
        else:
            path[-1][tokens[1]] = int(tokens[0])


def dir_sizes(dir):
    sizes = [total_size(dir)]

    for x in dir:
        if type(dir[x]) is dict:
            sizes += dir_sizes(dir[x])

    return sizes


sizes = dir_sizes(root)
part_a = sum([v for v in sizes if v <= 100000])
need = 30000000-(70000000-total_size(root))
part_b = min([v for v in sizes if v >= need])

submit(part_a, part="a")
submit(part_b, part="b")
