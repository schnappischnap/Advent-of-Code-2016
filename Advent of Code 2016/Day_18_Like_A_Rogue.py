def count_traps(input, part = 1):
    room = [[x for x in input]]
    rows = 400000 if part == 2 else 40

    for i in range(1, rows):
        room.append([])

        for j in range(len(input)):
            a = room[i - 1][j - 1] if j > 0 else "."
            b = room[i - 1][j]
            c = room[i - 1][j + 1] if j < 99 else "."

            if a == c:
                room[i].append(".")
            else:
                room[i].append("^")

    return sum(x.count(".") for x in room)


if __name__ == "__main__":
    with open("day_18_input.txt") as f:
        input = f.read()
        print "Part 1 answer: " + str(count_traps(input))
        print "Part 2 answer: " + str(count_traps(input, 2))