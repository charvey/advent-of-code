from aocd import data, submit

input = data

contain_count = 0
overlap_count = 0
for pair in input.splitlines():
    (first, second) = pair.split(",")
    (fx, fy) = first.split("-")
    (sx, sy) = second.split("-")

    sx = int(sx)
    sy = int(sy)
    fx = int(fx)
    fy = int(fy)

    if (fx <= sx and sy <= fy) or (sx <= fx and fy <= sy):
        contain_count += 1

    if (
        (fx <= sx and sx <= fy)
        or (fx <= sy and sy <= fy)
        or (sx <= fx and fx <= sy)
        or (sx <= fy and fy <= sy)
    ):
        overlap_count += 1

submit(contain_count, part="a")
submit(overlap_count, part="b")
