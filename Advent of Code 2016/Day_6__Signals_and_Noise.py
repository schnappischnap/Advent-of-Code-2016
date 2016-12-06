from collections import Counter

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


# Part 1
def decode(input):
    return "".join(Counter(x).most_common()[0][0] for x in zip(*input))


# Part 2
def decode_again(input):
    return "".join(Counter(x).most_common()[-1][0] for x in zip(*input))
        

if __name__ == '__main__':
    print "Part 1 input:"
    a = get_list_input()   
    print "Puzzle answer: " + str(decode(a))

    print "\nPart 2 input:"
    a = get_list_input()   
    print "Puzzle answer: " + str(decode_again(a))