import re, collections

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


def split_input(input):
    sections = [x for x in re.split('-|\[|\]', input) if x]

    words = sections[:-2]
    sector_id = sections[-2]
    checksum = sections[-1]

    return list(words), int(sector_id), str(checksum)


# Part 1
def get_real_sector_id_sum(rooms):
    sector_id_sum = 0

    for room in rooms:
        words, sector_id, checksum = split_input(room)

        counter = collections.Counter("".join(words))
        c = counter.keys()
        c = sorted(c)
        c = sorted(c, key = lambda x:counter[x], reverse=True)
        valid_checksum = "".join(c[:5])

        if checksum == valid_checksum:
            sector_id_sum += sector_id

    return sector_id_sum


# Part 2
def get_shifted_sector_id(rooms):
    for room in rooms:
        words, sector_id, checksum = split_input(room)

        shift_amount = int(sector_id) % 26

        output = ""
        for word in words:
            output += "".join(chr(((ord(c) - ord('a') + shift_amount) % 26) + ord('a')) for c in word) + " "

        if output.startswith("northpole"):
            return sector_id

    return -1


if __name__ == "__main__":
    print "Part 1 input:"
    a = get_list_input()   
    print "Puzzle answer: " + str(get_real_sector_id_sum(a))

    print "\nPart 2 input:"
    a = get_list_input()  
    print "Puzzle answer: " + str(get_shifted_sector_id(a))