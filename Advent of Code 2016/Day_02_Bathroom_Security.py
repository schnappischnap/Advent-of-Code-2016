def solve_9_keypad(steps):
    code = []
    position = 5

    for step in steps:
        for c in step:
            if c.upper() == "L":
                if ((position - 1) % 3) != 0:
                    position -= 1
            elif c.upper() == "R":
                if(position % 3) != 0:
                    position += 1
            elif c.upper() == "U":
                if (position - 3) > 0:
                    position -= 3
            elif c.upper() == "D":
                if (position + 3) < 10:
                    position += 3 

        code.append(position)

    return code


def solve_fancy_keypad(steps):
    keypad = [["*", "*", "1", "*", "*"],
              ["*", "2", "3", "4", "*"],
              ["5", "6", "7", "8", "9"],
              ["*", "A", "B", "C", "*"],
              ["*", "*", "D", "*", "*"]]
    code = []
    position = [2,0]

    for step in steps:
        for c in step:
            if c.upper() == "L":
                if position[1] > 0 and keypad[position[0]][position[1] - 1] != "*":
                    position[1] -= 1
            if c.upper() == "R":
                if position[1] < 4 and keypad[position[0]][position[1] + 1] != "*":
                    position[1] += 1
            if c.upper() == "U":
                if position[0] > 0 and keypad[position[0] - 1][position[1]] != "*":
                    position[0] -= 1
            if c.upper() == "D":
                if position[0] < 4 and keypad[position[0] + 1][position[1]] != "*":
                    position[0] += 1

        code.append(keypad[position[0]][position[1]])

    return code


if __name__ == "__main__":    
    with open("day_02_input.txt") as f:
        input = f.readlines()
        print "Part 1 answer: " + str(solve_9_keypad(input))
        print "Part 2 answer: " + str(solve_fancy_keypad(input))