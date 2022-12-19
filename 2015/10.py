from aocd import data, submit


def getNext(n):
    result = ''
    count = 0
    character = ' '
    for c in (n+' '):
        if (c == character):
            count += 1
        else:
            if count > 0:
                result += str(count)+character
            count = 1
            character = c
    return result


next = data

for i in range(40):
    next = getNext(next)

submit(len(next), part='a')

for i in range(50-40):
    next = getNext(next)

submit(len(next), part='b')
