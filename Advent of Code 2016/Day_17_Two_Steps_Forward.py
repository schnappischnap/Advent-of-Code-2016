import hashlib


def get_open_rooms(state, input):
    point, path = state
    hash = hashlib.md5(input + path).hexdigest()
    rooms = []

    if point[1] - 1 >= 0 and hash[0] in "bcdef":
        rooms.append(((point[0], point[1] - 1), path + "U"))
    if point[1] + 1 < 4 and hash[1] in "bcdef":
        rooms.append(((point[0], point[1] + 1), path + "D"))
    if point[0] - 1 >= 0 and hash[2] in "bcdef":
        rooms.append(((point[0] - 1, point[1]), path + "L"))
    if point[0] + 1 < 4 and hash[3] in "bcdef":
        rooms.append(((point[0] + 1, point[1]), path + "R"))

    return rooms


def get_path(input):
    shortest_path = ""
    paths_count = 0

    current_state = ((0,0), "")
    end = (3,3)
    neighbours = get_open_rooms(current_state, input)

    while neighbours:
        current_state = neighbours.pop(0)
        current_point, current_path = current_state

        if current_point == end:
            if shortest_path == "":
                shortest_path = current_path
            paths_count = len(current_path)
        else:
            neighbours.extend(get_open_rooms(current_state, input))

    return shortest_path, paths_count


if __name__ == "__main__":
    with open("day_17_input.txt") as f:
        input = f.read()
        part_1, part_2 = get_path(input)
        print "Part 1 answer: " + str(part_1)
        print "Part 2 answer: " + str(part_2)