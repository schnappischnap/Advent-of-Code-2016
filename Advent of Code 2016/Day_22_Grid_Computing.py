from __future__ import print_function


def get_nodes(input):
    nodes = []

    for line in input:
        if line.startswith("/"):
            split = line.split()
            pos_split = split[0].split("-")
            position = (int(pos_split[1][1:]), int(pos_split[2][1:]))
            size = int(split[1][:-1])
            used = int(split[2][:-1])
            avail = int(split[3][:-1])
            use_percentage = int(split[4][:-1])
            nodes.append((position, size, used, avail, use_percentage))

    return nodes


def viable_pairs(input):
    nodes = get_nodes(input)
    pairs = 0

    for a in nodes:
        for b in nodes:
            if a == b:
                continue
            if a[2] == 0:
                continue
            if a[2] > b[3]:
                continue
            pairs += 1

    return pairs


def print_grid(input):
    nodes = sorted(get_nodes(input) , key=lambda k: [k[0][1], k[0][0]])

    for a in nodes:
        if a[0][0] == 0:
            print("\n")

        if a[2] == 0:
            print("_", end = "")
        elif a[1] > 100:
            print("#", end = "")
        else:
            print(".", end = "")


if __name__ == "__main__":    
    with open("day_22_input.txt") as f:
        input = f.readlines()
        print ("Part 1 answer: " + str(viable_pairs(input)))
        print ("Part 2 answer: ") 
        print_grid(input)
        # Solve part 2 by hand