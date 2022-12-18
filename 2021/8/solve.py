from aocd import get_data
from aocd import submit
from itertools import permutations

input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

input = get_data(day=8, year=2021)

allowed = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


def possible(segments, mapping):
    for segment in segments:
        lit = ""
        for signal in segment:
            lit += mapping[signal]
        lit = "".join(sorted(lit))
        if lit not in allowed:
            return False
    return True


def solve(signal, output):
    segments = []
    for segment in signal + output:
        lookups = []
        for char in segment:
            lookups.append(ord(char) - ord("a"))
        segments.append(lookups)

    for perm in permutations("abcdefg"):
        if possible(segments, perm):
            result = ""
            for segment in output:
                signals = ""
                for signal in segment:
                    signals += perm[ord(signal) - ord("a")]
                signals = "".join(sorted(signals))
                result += str(allowed[signals])
            return int(result)


count = 0
sum = 0
for entry in input.splitlines():
    (signal, output) = entry.split("|")
    signal = signal.strip().split()
    output = output.strip().split()

    result = solve(signal, output)

    for digit in str(result):
        if digit in "1478":
            count += 1

    sum += result

print(count)
print(sum)

submit(count, part="a", day=8, year=2021)
submit(sum, part="b", day=8, year=2021)
