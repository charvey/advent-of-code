from aocd import get_data
from aocd import submit
import statistics

input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

input = get_data(day=10, year=2021)


def find_error(line):
    stack = []
    for i, c in enumerate(line):
        if c in "<[{(":
            stack.append(c)
        elif c == ">" and stack[-1] == "<":
            stack.pop()
        elif c == ")" and stack[-1] == "(":
            stack.pop()
        elif c == "]" and stack[-1] == "[":
            stack.pop()
        elif c == "}" and stack[-1] == "{":
            stack.pop()
        else:
            return (i, stack)
    return (-1, stack)


corrupt_scores = []
incomplete_scores = []
corrupt_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
incomplete_points = {"(": 1, "[": 2, "{": 3, "<": 4}
for line in input.splitlines():
    err, stack = find_error(line)
    if err != -1:
        corrupt_scores.append(corrupt_points[line[err]])
    elif len(stack) > 0:
        score = 0
        for c in reversed(stack):
            score *= 5
            score += incomplete_points[c]
        incomplete_scores.append(score)

submit(sum(corrupt_scores), part="a", day=10, year=2021)

submit(statistics.median(incomplete_scores), part="b", day=10, year=2021)
