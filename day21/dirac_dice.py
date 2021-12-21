import fileinput
import numpy as np
from os import read
from functools import cache
import copy


def read_input():
    positions = [0, 0]
    count = 0
    for line in fileinput.input():
        positions[count] = int(line.strip().split(": ")[1])
        count += 1
    return positions


def roll_dice(last_rolled):
    sum = 0
    count = 0
    while count < 3:
        sum += last_rolled + 1
        count += 1
        last_rolled += 1
        if last_rolled == 100:
            last_rolled = 0
    return sum, last_rolled


def part_one(positions):
    score = [0, 0]
    rolls = 0
    player_in_turn = 0
    last_rolled = 0
    while score[player_in_turn] < 1000 and score[1 - player_in_turn] < 1000:

        rolls += 3
        sum, last_rolled = roll_dice(last_rolled)
        positions[player_in_turn] += sum
        positions[player_in_turn] -= 1
        positions[player_in_turn] %= 10
        positions[player_in_turn] += 1
        score[player_in_turn] += positions[player_in_turn]
        # change turn
        player_in_turn = 1 - player_in_turn

    return score[player_in_turn] * rolls


def roll_dirac():
    sums = []
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                sums.append(i + j + k)
    sums.sort()
    return sums


@cache
def score(score, pos, sum):
    score += newpos(pos, sum)
    return score


@cache
def newpos(pos, sum):
    pos += sum
    pos -= 1
    pos %= 10
    pos += 1
    return pos


@cache
def victories(p1, p2, score1, score2):

    num_vict = 0

    num_losses = 0

    for sum in roll_dirac():
        pos1 = newpos(p1, sum)
        roll1_score = score(score1, p1, sum)
        if roll1_score > 20:
            num_vict += 1
        else:
            ls, vt = victories(p2, pos1, score2, roll1_score)
            num_losses += ls
            num_vict += vt
    return (num_vict, num_losses)


def part_two(positions):
    print(positions[0], positions[1])
    print(victories(positions[0], positions[1], 0, 0))


def main():
    positions = read_input()
    print(part_one(copy.deepcopy(positions)))
    part_two(positions)


main()