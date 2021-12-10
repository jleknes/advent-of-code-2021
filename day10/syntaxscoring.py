import fileinput, time, math
from collections import deque

corr_separators = {"]": "[", "}": "{", ")": "(", ">": "<"}
part_one_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
part_two_points = {"(": 1, "[": 2, "{": 3, "<": 4}


def part_one():
    start_time = time.time()
    illegal_chars = []
    for line in fileinput.input():
        stack = deque()
        for char in line.strip():
            if char in corr_separators:
                print(stack)
                if stack[len(stack) - 1] == corr_separators[char]:
                    stack.pop()
                else:
                    illegal_chars.append(char)
                    break
            else:
                stack.append(char)
        print(illegal_chars)
        pass
    sum = 0
    for char in illegal_chars:
        sum += part_one_points[char]
    print(sum)
    print("--- %s seconds ---" % (time.time() - start_time))


def part_two():
    start_time = time.time()
    scores = []
    for line in fileinput.input():
        stack = deque()
        illegal = False
        for char in line.strip():
            if char in corr_separators:
                if stack[len(stack) - 1] == corr_separators[char]:
                    stack.pop()
                else:
                    illegal = True
                    break
            else:
                stack.append(char)
        if not illegal:
            score = 0
            for i in range(len(stack)):
                score *= 5
                points = part_two_points[stack.pop()]
                score += points
            scores.append(score)
        pass
    # print middle element of scores
    scores.sort()
    print(scores[math.floor(len(scores) / 2)])
    print("--- %s seconds ---" % (time.time() - start_time))


# part_one()
part_two()