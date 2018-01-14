file = open('input.txt', 'r')
stream = file.readline().strip()
file.close()
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
print(score)
print(garbageCharacters)
