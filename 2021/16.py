from aocd import data, submit
import math

input = "A0016C880162017C3686B18A3D4780"
# input = "D2FE28"

input = data

codes = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

binary = ""
for c in input:
    binary += codes[c]


def parse(code, i=0):
    version = code[i: i + 3]
    i += 3
    print(version)

    version_sum = int(version, 2)

    type = code[i: i + 3]
    i += 3
    print(type)

    if type == "100":
        literal = ""
        while code[i] == "1":
            i += 1
            literal += code[i: i + 4]
            i += 4
        i += 1
        literal += code[i: i + 4]
        i += 4
        return i, int(literal, 2), version_sum
    else:
        length_type = code[i]
        i += 1
        values = []
        if length_type == "0":
            length = int(code[i: i + 15], 2)
            i += 15
            limit = i + length
            while i < limit:
                (i, val, ver) = parse(code, i)
                values.append(val)
                version_sum += ver
        elif length_type == "1":
            length = int(code[i: i + 11], 2)
            i += 11
            for _ in range(length):
                (i, val, ver) = parse(code, i)
                values.append(val)
                version_sum += ver

        value = None

        if type == "000":
            value = sum(values)
        elif type == "001":  # sum
            value = math.prod(values)
        elif type == "010":
            value = min(values)
        elif type == "011":
            value = max(values)
        elif type == "101":
            value = 1 if values[0] > values[1] else 0
        elif type == "110":
            value = 1 if values[0] < values[1] else 0
        elif type == "111":
            value = 1 if values[0] == values[1] else 0

        return i, value, version_sum


print(binary)

result = parse(binary)

submit(result[2], part="a")
submit(result[1], part="b")
