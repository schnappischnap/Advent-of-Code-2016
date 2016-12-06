# Part 1
def rectilinear_distance(input):
    direction = 0
    position = [0,0]

    for step in input.split(", "):
        if step[0].upper() == "L":
            direction -= 1
        else:
            direction += 1
        direction = direction % 4

        if direction == 0:
            position[1] += int(step[1:])
        elif direction == 1:
            position[0] += int(step[1:])
        elif direction == 2:
            position[1] -= int(step[1:])
        elif direction == 3:
            position[0] -= int(step[1:])

    return abs(position[0]) + abs(position[1])


# Part 2
def first_visited_twice_distance(input):
    direction = 0
    position = [0,0]
    visited = [[0,0]]

    for step in input.split(", "):
        if step[0].upper() == "L":
            direction -= 1
        else:
            direction += 1
        direction = direction % 4

        for i in range(0, int(step[1:])):
            if direction == 0:
                position[1] += 1
            elif direction == 1:
                position[0] += 1
            elif direction == 2:
                position[1] -= 1
            elif direction == 3:
                position[0] -= 1

            if position in visited:
                return abs(position[0]) + abs(position[1])
            visited.append(list(position))

    return -1


if __name__ == '__main__':
    input = raw_input("Part 1 input: ")
    print("Puzzle answer: " + str(rectilinear_distance(input)))

    input = raw_input("\nPart 2 input: ")
    print("Puzzle answer: " + str(first_visited_twice_distance(input)))