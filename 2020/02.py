from aocd import data, submit

firstPolicyCount = 0
secondPolicyCount = 0
for line in data.splitlines():
    policy, pwd = line.split(":")
    pwd = pwd.strip()
    limits, letter = policy.split(" ")
    lower, upper = limits.split("-")
    lower = int(lower)
    upper = int(upper)

    occurences = pwd.count(letter)

    if lower <= occurences and occurences <= upper:
        firstPolicyCount += 1

    first = pwd[lower - 1]
    second = pwd[upper - 1]
    if first != second and (first == letter or second == letter):
        secondPolicyCount += 1

submit(firstPolicyCount, part='a')
submit(secondPolicyCount, part='b')
