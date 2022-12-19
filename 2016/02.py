from aocd import data, submit

firstKeypad = [
    "     ",
    " 123 ",
    " 456 ",
    " 789 ",
    "     "
]
secondKeypad = [
    "       ",
    "   1   ",
    "  234  ",
    " 56789 ",
    "  ABC  ",
    "   D   ",
    "       "
]

keypads = {'a': firstKeypad, 'b': secondKeypad}

for part, keypad in keypads.items():
    code = ""
    for line in data.splitlines():
        pos = (2, 2)
        for step in line.strip():
            if step == 'U':
                newPos = (pos[0], pos[1] - 1)
            elif step == 'D':
                newPos = (pos[0], pos[1] + 1)
            elif step == 'R':
                newPos = (pos[0] + 1, pos[1])
            elif step == 'L':
                newPos = (pos[0] - 1, pos[1])
            else:
                raise Exception('Invalid direction')
            if keypad[newPos[1]][newPos[0]] != ' ':
                pos = newPos

        code += keypad[pos[1]][pos[0]]

    submit(code, part=part)
