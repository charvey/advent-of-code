from aocd import data, submit

wires = dict()
for line in data.splitlines():
    lhs, rhs = line.split(' -> ')
    wires[rhs.strip()] = lhs.strip()

signals = dict()


def evaluate(expr):
    if 'NOT' in expr:
        _, v = expr.split()
        # print('~', v, lookup(v), ~lookup(v) + 65535 + 1)
        return ~lookup(v) + 65535 + 1
    elif 'AND' in expr:
        a, _, b = expr.split()
        # print(a, '&', b)
        return lookup(a) & lookup(b)
    elif 'OR' in expr:
        a, _, b = expr.split()
        # print(a, '|', b)
        return lookup(a) | lookup(b)
    elif 'LSHIFT' in expr:
        a, _, b = expr.split()
        # print(a, '<<', b)
        return lookup(a) << lookup(b)
    elif 'RSHIFT' in expr:
        a, _, b = expr.split()
        # print(a, '>>', b)
        return lookup(a) >> lookup(b)
    else:
        v = expr
        return lookup(v)


def lookup(wire):
    # print('lookup', wire)
    if wire not in wires:
        # print('signal', wire, int(wire))
        return int(wire)
    if wire not in signals:
        evaluation = evaluate(wires[wire])
        signals[wire] = max(min(evaluation, pow(2, 16) - 1), 0)
    # print('result', wire, wires[wire], signals[wire])
    return signals[wire]


submit(lookup('a'), part='a')
wires['b'] = str(lookup('a'))
signals = dict()
submit(lookup('a'), part='b')
