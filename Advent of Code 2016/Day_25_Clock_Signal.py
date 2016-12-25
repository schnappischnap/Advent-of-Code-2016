values = {"a": 0, "b" : 0, "c" : 0, "d" : 0}


def get_value(input):
    try: 
        return int(input)
    except ValueError:
        return values[input]


def solve(instructions, a_value):
    values["a"] = a_value
    output = []

    i = 0
    while i < len(instructions):
        instruction = instructions[i]

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
                    instructions[index] = ("dec", instructions[index][Day_25_Clock_Signal.py1])
                else:
                    instructions[index] = ("inc", instructions[index][1])
            else:
                if instructions[index][0] == "jnz":
                    instructions[index] = ("cpy", instructions[index][1], instructions[index][2])
                else:
                    instructions[index] = ("jnz", instructions[index][1], instructions[index][2])

        elif instruction[0] == "out":
            value = get_value(instruction[1])
            if value != 0 and value != 1:
                return False
            if len(output) > 1 and output[-1] == value:
                return False

            output.append(get_value(instruction[1]))
            if len(output) > 50:
                return True

        i += 1

    return False


def lowest_a_value(input):
    instructions = []
    for line in input:
        instructions.append(tuple(line.split()))

    for i in xrange(1000000):
        if solve(instructions, i) == True:
            return i


if __name__ == "__main__":
    with open("day_25_input.txt") as f:
        input = f.readlines()
        print "Final answer: " + str(lowest_a_value(input))