def get_list_input():
    l = []
    i = 0
    while True:
        input = raw_input(str(i) + ": ")
        if input == "":
            break
        l.append(input)
        i += 1

    return l


def is_valid_triangle(input):
    sides = [int(side) for side in input.split()]
    sides.sort()
    return sides[0] + sides[1] > sides[2]


# Part 1
def count_valid_triangles(lines):
    valid_triangles = 0

    for line in lines:
        if is_valid_triangle(line):
            valid_triangles += 1

    return valid_triangles


# Part 2
def count_valid_triangles_vertically(lines):
    steps = [x.split() for x in lines]

    args = []
    for i in range(len(steps)/3):
        for j in range(3):
            arg = [steps[i*3][j], steps[i*3 + 1][j], steps[i*3 + 2][j]]
            args.append(" ".join(arg))

    valid_triangles = 0
    for arg in args:
        if is_valid_triangle(arg):
            valid_triangles += 1

    return valid_triangles


if __name__ == '__main__':
    print "Part 1 input:"
    a = get_list_input()   
    print "Puzzle answer: " + str(count_valid_triangles(a))

    print "\nPart 2 input:"
    a = get_list_input()
    print "Puzzle answer: " + str(count_valid_triangles_vertically(a))