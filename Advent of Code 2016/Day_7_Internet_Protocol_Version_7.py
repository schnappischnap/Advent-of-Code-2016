import re

def count_valid(input, method):
    count = 0
    for line in input:
        if method(line):
            count += 1
    return count


def contains_ABBA(input):
    for i in range(len(input) - 3):
        test = input[i:i+4]
        if test[0] == test[3] and test[1] == test[2] and test[0] != test[1]:
            return True
    return False


def get_ABAs(input):
    a = []
    for i in range(len(input) - 2):
        test = input[i:i+3]
        if test[0] == test[2] and test[0] != test[1]:
            a.append(test)
    return a


# Part 1
def support_TLS(input):
    i = 0
    valid = False
    for section in re.split("\[|\]", input):
        if contains_ABBA(section):
            if i % 2 == 0:
                valid = True
            else:
                return False
        i += 1
    return valid


# Part 2
def support_SSL(input):
    sections = [x for x in re.split("\[|\]", input)]
    ABAs = [get_ABAs(x) for x in sections]
    outside_ABAs = [x for y in ABAs[::2] for x in y]
    inside_ABAs = [x for y in ABAs[1::2] for x in y]

    for ABA in outside_ABAs:
        BAB = ABA[1] + ABA[0] + ABA[1]
        if BAB in inside_ABAs:
            return True
    return False


if __name__ == "__main__":
    with open("day_7_input.txt") as f:
        input = f.readlines()
        print "Part 1 answer: " + str(count_valid(input, support_TLS))
        print "Part 2 answer: " + str(count_valid(input, support_SSL))