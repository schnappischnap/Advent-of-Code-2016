values = {"a": 0, "b" : 0, "c" : 0, "d" : 0}


def get_value(input):
    try: 
        return int(input)
    except ValueError:
        return values[input]


def solve(input, part = 1):
    if part == 2:
        values["c"] = 1

    i = 0
    while i < len(input):
        split = input[i].split()

        if split[0] == "jnz":
            if get_value(split[1]) != 0:
                i += get_value(split[2]) - 1

        elif split[0] == "cpy":
            values[split[2]] = get_value(split[1])

        elif split[0] == "inc":
            values[split[1]] += 1

        elif split[0] == "dec":
            values[split[1]] -= 1

        i += 1

    return values["a"]




if __name__ == "__main__":
    with open("day_12_input.txt") as f:
        input = f.readlines()
        print "Part 1 answer: " + str(solve(input))
        print "Part 2 answer: " + str(solve(input, 2))