instructions = {} #{bot_id : [("bot"|"output", receiver_id), ("bot"|"output", receiver_id)], ...}
bots = {} #{bot_id : [value1, value2], ...}
output = {} #{output_id : value, ...}


def give_value_to_bot(bot_id, value):
    bots[bot_id].append(value)
    values = bots[bot_id]
    if len(values) == 2:
        if 61 in values and 17 in values:
            print bot_id

        low, high = min(values), max(values)
        bots[bot_id] = []

        instruction = instructions[bot_id]
        if(instruction[0][0] == "bot"):
            give_value_to_bot(instruction[0][1], low)
        else:
            give_value_to_output(instruction[0][1], low)

        if(instruction[1][0] == "bot"):
            give_value_to_bot(instruction[1][1], high)
        else:
            give_value_to_output(instruction[1][1], high)


def give_value_to_output(id, value):
    output[id] = value


def solve(input):
    for line in input:
        if line.startswith("bot"):
            split = line.split()
            instructions[int(split[1])] = [(split[5], int(split[6])), (split[10], int(split[11]))]
            bots[int(split[1])] = []

    for line in input:
        if line.startswith("value"):
            split = line.split()
            give_value_to_bot(int(split[5]), int(split[1]))


def part_2():
    return output[0] * output[1] * output[2]


if __name__ == "__main__":
    with open("day_10_input.txt") as f:
        input = f.readlines()
        print "Part 1 answer: "
        solve(input)
        print "Part 2 answer: " + str(part_2())