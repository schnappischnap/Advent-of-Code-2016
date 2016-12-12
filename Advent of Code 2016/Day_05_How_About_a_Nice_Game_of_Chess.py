import hashlib

def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


# Part 1
def get_password(input):
    code = []

    i = 0
    while len(code) < 8:
        hash = hashlib.md5(input + str(i)).hexdigest()
        if hash.startswith("00000"):
            code.append(hash[5])
            print code
        i += 1

    return "".join(code)


# Part 2
def get_second_password(input):
    code = ["X","X","X","X","X","X","X","X"]

    i = 0
    while "X" in code:
        hash = hashlib.md5(input + str(i)).hexdigest()
        if hash.startswith("00000"):
            position = hash[5]
            if is_int(position) and int(position) < 8 and code[int(position)] == "X":
                code[int(position)] = hash[6]
                print code
        i += 1

    return "".join(code)


if __name__ == "__main__":
    with open("day_05_input.txt") as f:
        input = f.readlines()[0]
        print "Part 1 answer: " + str(get_password(input))
        print "Part 2 answer: " + str(get_second_password(input))