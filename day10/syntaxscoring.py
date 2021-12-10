import fileinput, time
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
                if not stack.pop() == corr_separators[char]:
                    illegal_chars.append(char)
                    break
            else:
                stack.append(char)
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
        corrupted = False
        for char in line.strip():
            if char in corr_separators:
                if not stack.pop() == corr_separators[char]:
                    corrupted = True
                    break
            else:
                stack.append(char)
        if not corrupted:
            score = 0
            for i in range(len(stack)):
                score = score * 5 + part_two_points[stack.pop()]
            scores.append(score)
        pass
    # print middle element of scores
    scores.sort()
    print(scores[len(scores) // 2])
    print("--- %s seconds ---" % (time.time() - start_time))


# part_one()
part_two()
