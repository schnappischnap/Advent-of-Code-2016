from itertools import combinations
import re
import copy


seen = []
elements = []


def get_pairs(distribution):
    pairs = []

    for element in elements:
        pair = sorted([distribution.index(floor) for floor in distribution if any(element in item for item in floor)])
        if len(pair) == 1:
            pair.append(pair[0])
        pairs.append(pair)

    return sorted(pairs)


def get_combinations(input):
    output = [[a] for a in input]
    for b in combinations(input, 2):
        output.append([c for c in b])
    return output


def is_valid_distribution(distribution):
    for floor in distribution:
        generators, microchips = [], []
        for x in floor:
            if x.startswith("generator"):
                generators.append(x[10:])
            else:
                microchips.append(x[10:])

        for microchip in microchips:
            if generators and microchip not in generators:
                return False

    return True


def get_adjacents(state):
    cur_floor, cur_distance, cur_distribution = state

    adjacents = []

    item_combinations = get_combinations(cur_distribution[cur_floor])
    new_floors = [(cur_floor + x) for x in [-1,1] if 0 <= (cur_floor + x) <= 3]

    for new_floor in new_floors:
        for item_combination in item_combinations:
            new_distribution = copy.deepcopy(cur_distribution)

            for item in item_combination:
                new_distribution[cur_floor].remove(item)
                new_distribution[new_floor].append(item)

            if not is_valid_distribution(new_distribution):
                continue

            pairs = get_pairs(new_distribution)

            if (new_floor, pairs) in seen:
                continue

            seen.append((new_floor,pairs))

            adjacents.append((new_floor,cur_distance + 1,new_distribution))

    return adjacents


def init(input):
    distribution = [[],[],[],[]]
    item_count = 0

    for floor_number in range(4):
        split = re.split(" ", input[floor_number])
        for i in range(len(split)):
            if split[i] == "a":
                item_count += 1

                if split[i + 1].endswith("compatible"):
                    name = "microchip_" + split[i + 1][:-11]
                else:
                    name = "generator_" + split[i + 1]
                    if split[i + 1] not in elements:
                        elements.append(split[i + 1])

                distribution[floor_number].append(name)

    return distribution, item_count


def init_2(input):
    distribution, item_count = init(input)

    distribution[0].extend(["microchip_elerium", "generator_elerium", "generator_dilithium", "microchip_dilithium"])
    item_count += 4
    elements.extend(["elerium","dilithium"])

    return distribution, item_count


def solve(input, part = 1):
    if part == 1:
        initial_distribution, item_count = init(input)
    else:
        initial_distribution, item_count = init_2(input)

    # (floor, distance, distribution)
    current_state = (0, 0, initial_distribution)
    adjacents = get_adjacents(current_state)

    while adjacents:
        current_state = adjacents.pop(0)

        if len(current_state[2][3]) == item_count:
            return current_state[1]
            
        adjacents.extend(get_adjacents(current_state))


if __name__ == "__main__":
    with open("day_11_input.txt") as f:
        input = f.readlines()
        print "Part 1 answer: " + str(solve(input))
        print "Part 2 answer: " + str(solve(input, 2))