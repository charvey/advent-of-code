from logging import disable
from aocd import get_data
import sys

input = """e => H
e => O
H => HO
H => OH
O => HH

HOHOHO
"""

input = get_data(day=19, year=2015)

lines = input.splitlines()

rules = dict()
rev_rules = list()

for line in lines[:-2]:
    before, after = [x.strip() for x in line.split("=>")]

    if before not in rules:
        rules[before] = set()

    rules[before].add(after)

    rev_rules.append({"x": after, "y": before})

medicine = lines[-1]


def split(code):
    m = list()
    cur = code[0]
    for c in code[1:]:
        if c.isupper():
            m.append(cur)
            cur = ""
        cur += c
    m.append(cur)
    return m


def neighbors(code):
    molecules = set()
    medicine_molecule = split(code)

    for i, m in enumerate(medicine_molecule):
        if m in rules:
            for rule in rules[m]:
                new_molecule = medicine_molecule.copy()
                new_molecule[i] = rule
                molecules.add("".join(new_molecule))
    return molecules


def rev_neighbors(code):
    molecules = list()

    for rule in rev_rules:
        i = 0
        while i >= 0 and i < len(code):
            i = code.find(rule["x"], i)

            if i != -1:
                new_molecule = code[:i] + rule["y"] + code[i + len(rule["x"]) :]
                molecules.append(new_molecule)
                i += 1

    return molecules


print(len(neighbors(medicine)))


def dfs(code):
    if code == "e":
        return 0

    ns = rev_neighbors(code)

    if len(ns) == 0:
        return None

    for n in ns:
        next = dfs(n)
        if next is None:
            continue
        return next + 1


print(dfs(medicine))