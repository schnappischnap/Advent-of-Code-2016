def dragon_curve(s):
    b = "".join("0" if c == "1" else "1" for c in s[::-1])
    return s + "0" + b


def checksum(s):
    output = ""
    for i in range(0, len(s), 2):
        output += "1" if s[i] == s[i+1] else "0"
    if len(output) % 2 == 1:
        return output
    else:
        return checksum(output)


def solve(input, length):
    while len(input) < length:
        input = dragon_curve(input)
    input = input[:length]

    return checksum(input)


if __name__ == '__main__':
    with open("day_16_input.txt") as f:
        input = f.read()
        print "Part 1 answer: " + str(solve(input, 272))
        print "Part 2 answer: " + str(solve(input,35651584))