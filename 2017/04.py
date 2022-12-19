from aocd import data, submit

wordCount = 0
anagramCount = 0
for line in data.splitlines():
    isWordValid = True
    isAnagramValid = True
    words = set()
    anagrams = set()
    for word in line.split():
        if word in words:
            isWordValid = False
        if ''.join(sorted(word)) in anagrams:
            isAnagramValid = False
        words.add(word)
        anagrams.add(''.join(sorted(word)))
    if isWordValid:
        wordCount += 1
    if isAnagramValid:
        anagramCount += 1

submit(wordCount, part='a')
submit(anagramCount, part='b')
