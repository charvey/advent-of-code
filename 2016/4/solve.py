import itertools

file = open('input.txt', 'r')
for line in file:
    line.rindex('-')
    name = line[:line.rindex('-')]
    sector = int(line[line.rindex('-') + 1:line.rindex('[')])
    checksum = line[line.rindex('[') + 1:line.rindex(']')]
    letters = itertools.groupby([x for x in name if x != '-'])

    print(name)
    print(list(map(lambda x: x[0], letters)))
    lettersA = sorted(list(letters), key=lambda x: x[0])
    print(lettersA)
    print(list(map(lambda x: x[0], lettersA)))
    lettersB = sorted(lettersA, key=lambda x: len(list(x[1])), reverse=True)
    print(list(map(lambda x: x[0], lettersB)))

    print(checksum)
file.close()
