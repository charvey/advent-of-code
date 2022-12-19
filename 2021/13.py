from aocd import data, submit

input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

input = data

page = set()
folds = None
for line in input.splitlines():
    if line == "":
        folds = list()
    elif folds is None:
        (x, y) = line.split(",")
        page.add((int(x), int(y)))
    else:
        folds.append(line.split(" ")[2].split("="))
        folds[-1][1] = int(folds[-1][1])


def turn(page, dir, z):
    next_page = set()
    for dot in page:
        if dir == "x":
            next_page.add((z - abs(dot[0] - z), dot[1]))
        elif dir == "y":
            next_page.add((dot[0], (z - abs(dot[1] - z))))
        else:
            raise "N/A"
    return next_page


submit(len(turn(page, folds[0][0], folds[0][1])), part="a")


for fold in folds:
    page = turn(page, fold[0], fold[1])

for y in range(6):
    for x in range(4 * 8 + 7):
        if (x, y) in page:
            print("#", end="")
        else:
            print(".", end="")
    print()

# submit(None, part='b', day=13, year=2021)
