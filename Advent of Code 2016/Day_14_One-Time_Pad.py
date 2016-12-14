import hashlib


def is_repeated_character(s):
    return s == s[0] * len(s)


def get_index_of_64th_key(input, part = 1):
    code = []
    triplets = {}

    i = 0
    while len(code) < 64:
        hash = hashlib.md5(input + str(i)).hexdigest()
        if part == 2:
            for _ in xrange(2016):
                hash = hashlib.md5(hash).hexdigest()

        for j in range(len(hash) - 4):
            quintuplet = hash[j:j+5]
            if is_repeated_character(quintuplet):
                key = quintuplet[0]
                if key in triplets:
                    indices_to_delete = []
                    for k in range(len(triplets[key])):
                        triplet_index = triplets[key][k]
                        if i - triplet_index <= 1000:
                            code.append(key)
                            if len(code) == 64:
                                return triplet_index
                        indices_to_delete.append(k)

                    indices_to_delete.sort(reverse=True)
                    for index in indices_to_delete:
                        del triplets[key][index]

        for j in range(len(hash) - 2):
            triplet = hash[j:j+3]
            if is_repeated_character(triplet):
                key = triplet[0]
                if key in triplets:
                    triplets[key].append(i)
                else:
                    triplets[key] = [i]
                break

        i += 1


if __name__ == "__main__":
    with open("day_14_input.txt") as f:
        input = f.read()
        print "Part 1 answer: " + str(get_index_of_64th_key(input))
        print "Part 2 answer: " + str(get_index_of_64th_key(input, 2))