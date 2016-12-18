def count_safe(input, part = 1):
    previous_row = list(input)
    safe_count = previous_row.count(".")
    rows = 400000 if part == 2 else 40

    for i in range(1, rows):
        current_row = []

        for j in range(len(input)):
            l = previous_row[j - 1] if j > 0 else "."
            c = previous_row[j]
            r = previous_row[j + 1] if j < 99 else "."

            if l == r:
                current_row.append(".")
            else:
                current_row.append("^")

        safe_count += current_row.count(".")
        previous_row = current_row[:]

    return safe_count


if __name__ == "__main__":
    with open("day_18_input.txt") as f:
        input = f.read()
        print "Part 1 answer: " + str(count_safe(input))
        print "Part 2 answer: " + str(count_safe(input, 2))