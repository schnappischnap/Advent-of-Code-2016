def decompressed_length(input, part):
    total = 0
    i = 0
    while i < len(input):
        if input[i] == '(':
            i += 1
            marker = ""
            while input[i] != ')':
                marker += input[i]
                i += 1
            character_count, repeat_amount = [int(x) for x in marker.split('x')]
            if part == 1:
                total += repeat_amount * character_count
            else:
                total += repeat_amount * decompressed_length(input[(i + 1) : (i + character_count + 1)], 2)
            i += character_count
        else:
            total += 1
        i += 1
    return total


if __name__ == "__main__":
    with open("day_09_input.txt") as f:
        input = f.read()
        print "Part 1 answer: " + str(decompressed_length(input, 1))
        print "Part 2 answer: " + str(decompressed_length(input, 2))