import itertools


def solve(letters, instructions):
    password = list(letters)

    for line in instructions:
        split = line.split()

        if split[0] == "swap":
            if split[1] == "position":
                pos1, pos2 = int(split[2]), int(split[5])
                a, b = password[pos1], password[pos2]
                password[pos1] = b
                password[pos2] = a

            else:
                letter1, letter2 = split[2], split[5]
                password = [letter1 if c == letter2 else letter2 if c == letter1 else c for c in password]

        elif split[0] == "rotate":
            if split[1] == "based":
                amount = 1 + password.index(split[6])
                if amount > 4: 
                    amount += 1
            else:
                amount = int(split[2]) * (-1 if split[1] == "left" else 1)

            amount = amount % len(password)
            password = password[-amount:] + password[:-amount]

        elif split[0] == "reverse":
            pos1, pos2 = int(split[2]), int(split[4])
            password[pos1:pos2 + 1] = reversed(password[pos1:pos2 + 1])

        elif split[0] == "move":
            pos1, pos2 = int(split[2]), int(split[5])
            letter = password.pop(pos1)
            password.insert(pos2,letter)

    return "".join(a for a in password)


def part_2(letters, input):
    for permutation in itertools.permutations(letters):
        if solve(permutation, input) == letters:
            return ''.join(permutation)


if __name__ == '__main__':
    with open("day_21_input.txt") as f:
        input = f.readlines()
        print "Part 1 answer: " + str(solve("abcdefgh",input))
        print "Part 2 answer: " + str(part_2("fbgdceah", input))