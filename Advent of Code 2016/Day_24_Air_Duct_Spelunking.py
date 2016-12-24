import itertools, sys


def get_neighbours(point, walls):
    return [(point[0] + x, point[1] + y) for x in range(-1,2) 
                                         for y in range(-1,2) 
                                         if ((x == 0) ^ (y == 0)) 
                                         and (point[0] + x, point[1] + y) not in walls]


def fewest_steps(start, end, walls):
    seen = [start]
    current_state = (start, 0)
    neighbours = ([(n, 1) for n in get_neighbours(current_state[0], walls)])

    while neighbours:
        current_state = neighbours.pop(0)
        current_point, current_steps = current_state

        if current_point in seen:
            continue
        else:
            seen.append(current_point)

        if current_point == end:
            return current_steps

        neighbours.extend([(n, current_steps + 1) for n in get_neighbours(current_state[0], walls)])


def solve(input):
    walls = set()
    checkpoints = []

    for y, line in enumerate(input):
        for x, c in enumerate(line):
            if c == "#":
                walls.add((x,y))
            elif c in "123456789":
                checkpoints.append((x,y))
            elif c == "0":
                start = (x,y)

    zero_distances = {}
    for point in checkpoints:
        zero_distances[point] = fewest_steps(start,point, walls)

    pair_distances = {}
    for point_1, point_2 in itertools.combinations(checkpoints, 2):
        steps = fewest_steps(point_1, point_2, walls)
        pair_distances[(point_1, point_2)] = steps
        pair_distances[(point_2, point_1)] = steps

    part_1 = sys.maxint
    part_2 = sys.maxint
    for path in itertools.permutations(checkpoints, len(checkpoints)):
        current_distance = zero_distances[path[0]]

        for i in range(len(path) - 1):
            current_distance += pair_distances[(path[i], path[i+1])]
        part_1 = min(part_1, current_distance)
        part_2 = min(part_2, current_distance + zero_distances[path[-1]])

    return part_1,part_2


if __name__ == "__main__":
    with open("day_24_input.txt") as f:
        input = f.readlines()
        part_1, part_2 = solve(input)
        print "Part 1 answer: " + str(part_1)
        print "Part 2 answer: " + str(part_2)