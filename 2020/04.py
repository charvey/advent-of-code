from aocd import data, submit

passports = list()
passport = dict()
for line in data.splitlines():
    if line == "":
        passports.append(passport)
        passport = dict()
        continue

    for field in line.split(" "):
        key, value = field.split(":")
        passport[key] = value
passports.append(passport)


def isPresent(passport):
    if (
        "byr" in passport
        and "iyr" in passport
        and "eyr" in passport
        and "hgt" in passport
        and "hcl" in passport
        and "ecl" in passport
        and "pid" in passport
    ):
        return True
    return False


def isValid(passport):
    if not isPresent(passport):
        return False

    byr = passport["byr"]
    if not byr.isnumeric() or len(byr) != 4 or int(byr) < 1920 or int(byr) > 2002:
        return False

    iyr = passport["iyr"]
    if not iyr.isnumeric() or len(iyr) != 4 or int(iyr) < 2010 or int(iyr) > 2020:
        return False

    eyr = passport["eyr"]
    if not eyr.isnumeric() or len(eyr) != 4 or int(eyr) < 2020 or int(eyr) > 2030:
        return False

    hgt = passport["hgt"]
    if not hgt[-2:] in ["cm", "in"]:
        return False
    if hgt[-2:] == "cm" and (int(hgt[:-2]) < 150 or int(hgt[:-2]) > 193):
        return False
    if hgt[-2:] == "in" and (int(hgt[:-2]) < 59 or int(hgt[:-2]) > 76):
        return False

    hcl = passport["hcl"]
    if (
        hcl[0] != "#"
        or len(hcl) != 7
        or not all(c in "0123456789abcdef" for c in hcl[1:])
    ):
        return False

    ecl = passport["ecl"]
    if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    pid = passport["pid"]
    if len(pid) != 9 or not pid.isnumeric():
        return False

    return True


presentCount = 0
validCount = 0
for passport in passports:
    if isPresent(passport):
        presentCount += 1
    if isValid(passport):
        validCount += 1

submit(presentCount, part='a')
submit(validCount, part='b')
