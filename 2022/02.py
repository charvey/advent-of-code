from aocd import data, submit

input = data

beats = {"R": "S", "P": "R", "S": "P"}
loses = {"R": "P", "P": "S", "S": "R"}
them = {"A": "R", "B": "P", "C": "S"}
me = {"X": "R", "Y": "P", "Z": "S"}
scores = {"R": 1, "P": 2, "S": 3}


def get_score(opp, you):
    score = scores[you]

    if opp == you:
        score += 3
    elif beats[you] == opp:
        score += 6
    else:
        pass

    return score


aScore = 0
bScore = 0
for match in input.splitlines():
    (t, m) = match.split(" ")

    opp = them[t]
    aYou = me[m]

    bYou = None
    if m == "X":
        bYou = beats[opp]
    elif m == "Y":
        bYou = opp
    elif m == "Z":
        bYou = loses[opp]

    aScore += get_score(opp, aYou)
    bScore += get_score(opp, bYou)

submit(aScore, part="a")
submit(bScore, part="b")
