import collections


def part_1(input):
    elves = collections.deque([x + 1 for x in range(int(input))])
        
    while len(elves) > 1:
        a = elves.popleft()
        b = elves.popleft()
        elves.appendleft(a)
        elves.rotate(-1)

    return elves


def part_2(input):
    left_elves = collections.deque()
    right_elves = collections.deque()

    elf_count = int(input)
    for i in range(elf_count):
        if i + 1 < (elf_count / 2) + 1:
            left_elves.append(i + 1)
        else:
            right_elves.appendleft(i + 1)

    while left_elves and right_elves:
        if len(left_elves) > len(right_elves):
            left_elves.pop()
        else:
            right_elves.pop()

        right_elves.appendleft(left_elves.popleft())
        left_elves.append(right_elves.pop())

    return left_elves if left_elves else right_elves


if __name__ == "__main__":
    with open("day_19_input.txt") as f:
        input = f.read()
        print "Part 1 answer: " + str(part_1(input))
        print "Part 2 answer: " + str(part_2(input))