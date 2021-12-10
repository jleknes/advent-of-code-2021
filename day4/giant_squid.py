import fileinput
import numpy as np

input = fileinput.input()

numbers = list(map(int, input.readline().split(",")))

boards = []


def checkboard(n, called_numbers):
    winning = False
    for i in range(5):
        if all(elem in called_numbers for elem in boards[n][:, i]):
            return True
        if all(elem in called_numbers for elem in boards[n][i, :]):
            return True
    return False


def score(n, called_numbers):
    sum_unmarked = np.sum(np.setdiff1d(boards[n], called_numbers))
    return sum_unmarked * called_numbers[len(called_numbers) - 1]


num_boards = 0
for line in input:
    board = []
    for i in range(5):
        board.append(list(map(int, input.readline().split())))
    boards.append(np.array(board))
    num_boards += 1
    pass

print(numbers)

print(boards[0])

marked_won = set()

for i in range(len(numbers)):
    for j in range(num_boards):
        if checkboard(j, numbers[0:i]):
            marked_won.add(j)
            if len(marked_won) == num_boards:
                print(j, score(j, numbers[0:i]))
                break
