from aocd import data, submit

stream = data.strip()
ignore = False
garbage = False
depth = 0
score = 0
garbageCharacters = 0
for c in stream:
    if ignore:
        ignore = False
    elif garbage:
        if c == '!':
            ignore = True
        elif c == '>':
            garbage = False
        else:
            garbageCharacters += 1
    elif c == '<':
        garbage = True
    elif c == '}':
        depth -= 1
    elif c == '{':
        depth += 1
        score += depth
    elif c == ',':
        pass
    else:
        print(ignore, garbage, depth, c)
        raise SyntaxError()
submit(score, part='a')
submit(garbageCharacters, part='b')
