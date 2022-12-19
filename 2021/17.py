from aocd import data, submit

input = """target area: x=20..30, y=-10..-5"""

input = data

(x, y) = input.split(": ")[1].split(", ")
tx = [int(z) for z in x.split("=")[1].split("..")]
ty = [int(z) for z in y.split("=")[1].split("..")]

print(tx)
print(ty)


def sign(n):
    if n == 0:
        return 0
    elif n < 0:
        return -1
    else:
        return 1


def step(x, y, vx, vy):
    x += vx
    y += vy
    vx -= sign(vx)
    vy -= 1
    return (x, y, vx, vy)


possible_vx0 = []
for vx0 in range(1, tx[1] + 1):
    x = 0
    y = 0
    vx = vx0
    vy = 0
    while True:
        (x, y, vx, vy) = step(x, y, vx, vy)
        if x > tx[1]:
            break
        elif x >= tx[0]:
            possible_vx0.append(vx0)
            print(f"Add {vx0}")

        if vx == 0:
            break
    print(f"Done {vx0}")

print(possible_vx0)
# submit(None, part="a", day=15, year=2021)
# submit(None, part="b", day=15, year=2021)
