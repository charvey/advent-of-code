registers = dict()
maxEver = 0
file = open('input.txt', 'r')
for line in file:
    symbols = line.split()
    register = symbols[0]
    operation = symbols[1]
    value = int(symbols[2])
    variable = symbols[4]
    comparison = symbols[5]
    threshold = int(symbols[6])

    if register not in registers:
        registers[register] = 0
    if variable not in registers:
        registers[variable] = 0

    operations = {
        '>': lambda a, b: a > b,
        '<': lambda a, b: a < b,
        '>=': lambda a, b: a >= b,
        '<=': lambda a, b: a <= b,
        '==': lambda a, b: a == b,
        '!=': lambda a, b: a != b,
    }
    evaluates = operations[comparison](registers[variable], threshold)

    if evaluates:
        if operation == 'inc':
            registers[register] += value
        elif operation == 'dec':
            registers[register] -= value

    maxEver = max(maxEver, max(registers.values()))
file.close()
print(max(registers.values()))
print(maxEver)
