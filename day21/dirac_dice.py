import fileinput
from os import read


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


def main():
    positions = read_input()
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
        print(
            "player rolling:",
            player_in_turn,
            "last_rolled_after_update:",
            last_rolled,
            "sum: ",
            sum,
            "new position:",
            positions[player_in_turn],
            "score player 1, score player 2:",
            score[0],
            score[1],
        )
        # change turn
        player_in_turn = 1 - player_in_turn

    print(score[player_in_turn] * rolls)


main()