from collections import Counter

def decode(input):
    return "".join(Counter(x).most_common()[0][0] for x in zip(*input))


def decode_again(input):
    return "".join(Counter(x).most_common()[-1][0] for x in zip(*input))
        

if __name__ == '__main__':
    with open("day_06_input.txt") as f:
        input = f.readlines()
        print "Part 1 answer: " + str(decode(input))
        print "Part 1 answer: " + str(decode_again(input))