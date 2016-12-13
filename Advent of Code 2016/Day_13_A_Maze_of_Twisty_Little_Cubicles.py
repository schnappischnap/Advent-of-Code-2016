def is_wall(point, input):
    x, y = point
    if x < 0 or y < 0:
        return True
    i = x*x + 3*x + 2*x*y + y + y*y + int(input)
    return bin(i).count("1") % 2 == 1


def get_neighbours(point, input):
    return [(point[0] + x, point[1] + y) for x in range(-1,2) 
                                         for y in range(-1,2) 
                                         if ((x == 0) ^ (y == 0)) 
                                         and not is_wall((point[0] + x, point[1] + y), input)]


def solve(input):
    seen = [(1,1)]
    current_state = ((1,1), 0)
    end = (31,39)
    neighbours = ([(n, 1) for n in get_neighbours(current_state[0], input)])

    part_1 = 0
    part_2 = 1

    while neighbours:
        current_state = neighbours.pop(0)
        current_point, current_steps = current_state

        if current_point in seen:
            continue
        else:
            seen.append(current_point)

        if current_point == end:
            part_1 = current_steps
        if current_steps <= 50:
            part_2 += 1
        elif part_1 != 0:
            return part_1, part_2
            
        neighbours.extend([(n, current_steps + 1) for n in get_neighbours(current_state[0], input)])


if __name__ == "__main__":
    with open("day_13_input.txt") as f:
        input = f.read()
        part_1, part_2 = solve(input)
        print "Part 1 answer: " + str(part_1)
        print "Part 2 answer: " + str(part_2)