screen = [[" " for x in range(50)] for y in range(6)]


def solve_screen(input):
    for line in input:
        if line.startswith("rect"):
            size = line.split(" ")[1].split("x")
            for x in range(int(size[0])):
                for y in range(int(size[1])):
                    screen[y][x] = "#"

        elif line.startswith("rotate column"):
            sections = line.split(" ")
            column_index = int(sections[2][2:])
            shift = int(sections[4])
            column = [row[column_index] for row in screen]
            for y in range(6):
                screen[y][column_index] = column[(y - shift) % 6]

        elif line.startswith("rotate row"):
            sections = line.split(" ")
            row_index = int(sections[2][2:])
            shift = int(sections[4])
            row = [x for x in screen[row_index]]
            for x in range(50):
                screen[row_index][x] = row[(x - shift) % 50]


# Part 1
def count_pixels():
    return len([item for sublist in screen for item in sublist if item == "#"])


# Part 2
def print_screen():
    for item in screen:
        print "".join(item)


if __name__ == "__main__": 
    with open("day_8_input.txt") as f:
        input = f.readlines()
        solve_screen(input)
        print "Part 1 answer: " + str(count_pixels())
        print "Part 2 answer: "
        print_screen()    