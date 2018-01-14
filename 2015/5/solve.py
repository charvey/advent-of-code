
def containsThreeVowels(s):
    return s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u') >= 3


def containsARepeat(s):
    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False


def doesNotContainFromBlacklist(s):
    return all(x not in s for x in ['ab', 'cd', 'pq', 'xy'])


def containsRepeatingPair(s):
    pairs = [s[i] + s[i + 1] for i in range(0, len(s) - 1)]
    for pair in pairs:
        if s.rindex(pair) - s.index(pair) > 1:
            return True
    return False


def containsSplitRepeatingLetter(s):
    for i in range(0, len(s) - 2):
        if s[i] == s[i + 2]:
            return True
    return False


def partOneNice(s):
    return containsThreeVowels(s) and containsARepeat(s) and doesNotContainFromBlacklist(s)


def partTwoNice(s):
    return containsRepeatingPair(s) and containsSplitRepeatingLetter(s)


file = open('input.txt', 'r')
partOneCount = 0
partTwoCount = 0
for line in file:
    if partOneNice(line):
        partOneCount += 1
    if partTwoNice(line):
        partTwoCount += 1
file.close()
print(partOneCount)
print(partTwoCount)
