def init(input):
    discs = []
    for line in input:
        split = line.split()
        discs.append((int(split[11][:-1]), int(split[3])))
    return discs


def is_valid(discs, i):
    for time, disc in enumerate(discs, start = (i + 1)):
        if ((disc[0] + time) % disc[1]) != 0:
            return False
    return True


def solve(input, part = 1):
    discs = init(input)
    if part == 2:
        discs.append((0,11))
    
    i = 0
    while True:
        if is_valid(discs,i):
            return i
        i += 1


if __name__ == "__main__":
    with open("day_15_input.txt") as f:
        input = f.readlines()
        print "Part 1 answer: " + str(solve(input))
        print "Part 2 answer: " + str(solve(input, 2))