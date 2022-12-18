from aocd import get_data

input = get_data(day=2, year=2020)

firstPolicyCount = 0
secondPolicyCount = 0
for line in input.splitlines():
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

print(firstPolicyCount)
print(secondPolicyCount)