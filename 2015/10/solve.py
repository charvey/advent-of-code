import itertools

start = ''
file = open('input.txt', 'r')
for line in file:
    start = line
file.close()


def getNext(n):
    result = ''
    count = 0
    character = ' '
    for c in (n+' '):
        if(c == character):
            count += 1
        else:
            if count > 0:
                result += str(count)+character
            count = 1
            character = c
    return result


next = start

for i in range(40):
    next = getNext(next)

print(len(next))

for i in range(50-40):
    next = getNext(next)

print(len(next))