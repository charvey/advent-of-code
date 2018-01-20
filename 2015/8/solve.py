strings = []
file = open('input.txt', 'r')
for line in file:
    strings.append(line)
file.close()


def string_value(str):
    str = str[1:-1]
    result = ''
    i = 0
    while i < len(str):
        if str[i] == '\\':
            if str[i + 1] == '\\' or str[i + 1] == '"':
                result += str[i + 1]
                i += 2
            elif str[i + 1] == 'x':
                result += chr(int(str[i + 2:i + 3 + 1], 16))
                i += 4
            else:
                raise 'Invalid character escaped'
        else:
            result += str[i]
            i += 1
    return result


def encode(str):
    result = '"'
    i = 0
    while i < len(str):
        if str[i] == '"':
            result += '\\"'
            i += 1
        elif str[i] == '\\':
            result += '\\\\'
            i += 1
        else:
            result += str[i]
            i += 1
    result += '"'
    return result


assert string_value('""') == ''
assert string_value('"abc"') == 'abc'
assert string_value('"aaa\\"aaa"') == 'aaa"aaa'
assert string_value('"\\x27"') == '\''

assert encode('""') == '"\\"\\""'
assert encode('"abc"') == '"\\"abc\\""'
assert encode('"aaa\\"aaa"') == '"\\"aaa\\\\\\"aaa\\""'
assert encode('"\\x27"') == '"\\"\\\\x27\\""'

shorter = 0
longer = 0
for string in strings:
    shorter += len(string) - len(string_value(string))
    longer += len(encode(string)) - len(string)
print(shorter)
print(longer)
