start = ''
with open('input.txt', 'r') as file:
    start = file.readline()


def HasSequence(chars):
    for i in range(len(chars)-2):
        if chars[i]+1 == chars[i+1] and chars[i+1]+1 == chars[i+2]:
            return True
    return False


def NoConfusingLetters(chars):
    for c in chars:
        if c == ord('i') or c == ord('o') or c == ord('l'):
            return False
    return True


def HasNonOverlappingPairs(chars):
    i = 0
    pairsFound = 0
    while i < len(chars)-1:
        if chars[i] == chars[i+1]:
            pairsFound += 1
            i += 2
        else:
            i += 1

    return pairsFound >= 2


def MeetsRequirements(chars):
    return HasSequence(chars) and NoConfusingLetters(chars) and HasNonOverlappingPairs(chars)


def Increment(chars):
    for i in range(len(chars)):
        j = len(chars)-(i+1)
        if chars[j] == ord('z'):
            chars[j] = ord('a')
        else:
            chars[j] += 1
            break


def FindNextPassword(start):
    current = list(map(ord, start))
    Increment(current)
    while not MeetsRequirements(current):
        Increment(current)
    return ''.join(list(map(chr, current)))


startingPassword = start
nextPassword = FindNextPassword(startingPassword)
followingPassword = FindNextPassword(nextPassword)

print(nextPassword)
print(followingPassword)
