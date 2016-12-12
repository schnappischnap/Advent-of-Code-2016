def is_valid_triangle(input):
    sides = [int(side) for side in input.split()]
    sides.sort()
    return sides[0] + sides[1] > sides[2]


def count_valid_triangles(lines):
    valid_triangles = 0

    for line in lines:
        if is_valid_triangle(line):
            valid_triangles += 1

    return valid_triangles


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
    with open("day_03_input.txt") as f:
        input = f.readlines()
        print "Part 1 answer: " + str(count_valid_triangles(input))
        print "Part 1 answer: " + str(count_valid_triangles_vertically(input))