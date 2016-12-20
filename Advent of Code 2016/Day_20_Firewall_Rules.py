def solve(input):
    ranges = sorted([tuple(map(int, line.split("-"))) for line in input])

    lowest_ip = 0
    unblocked_count = 0

    i = 0
    for _range in ranges:
        if i < _range[0]:
            if lowest_ip == 0:
                lowest_ip = i
            unblocked_count += _range[0] - i
        if _range[1] + 1 > i:
            i = _range[1] + 1

    return lowest_ip, unblocked_count
        

if __name__ == "__main__":
    with open("day_20_input.txt") as f:
        input = f.readlines()
        part_1, part_2 = solve(input)
        print "Part 1 answer: " + str(part_1)
        print "Part 2 answer: " + str(part_2)