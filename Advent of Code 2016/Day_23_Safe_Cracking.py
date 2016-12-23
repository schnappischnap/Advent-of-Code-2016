values = {"a": 0, "b" : 0, "c" : 0, "d" : 0}


def get_value(input):
    try: 
        return int(input)
    except ValueError:
        return values[input]


def solve(input, part = 1):
    values["a"] = 7 if part == 1 else 12

    instructions = []

    for line in input:
        instructions.append(tuple(line.split()))

    i = 0
    while i < len(instructions):
        instruction = instructions[i]

        if i == 4:
            values["a"] = (values["b"] * values["d"])
            values["d"] = 0
            values["c"] = 0
            i += 5
            continue

        if instruction[0] == "jnz":
            if get_value(instruction[1]) != 0:
                i += get_value(instruction[2])
                continue

        if instruction[0] == "cpy":
            values[instruction[2]] = get_value(instruction[1])

        elif instruction[0] == "inc":
            values[instruction[1]] += 1

        elif instruction[0] == "dec":
            values[instruction[1]] -= 1

        elif instruction[0] == "tgl":
            index = i + get_value(instruction[1])
            if index >= len(instructions) or index < 0:
                pass
            elif(len(instructions[index]) == 2):
                if instructions[index][0] == "inc":
                    instructions[index] = ("dec", instructions[index][1])
                else:
                    instructions[index] = ("inc", instructions[index][1])
            else:
                if instructions[index][0] == "jnz":
                    instructions[index] = ("cpy", instructions[index][1], instructions[index][2])
                else:
                    instructions[index] = ("jnz", instructions[index][1], instructions[index][2])

        i += 1

    return values["a"]


if __name__ == "__main__":
    with open("day_23_input.txt") as f:
        input = f.readlines()
        print "Part 1 answer: " + str(solve(input))
        print "Part 2 answer: " + str(solve(input, 2))