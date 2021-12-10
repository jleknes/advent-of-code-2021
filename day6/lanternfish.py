import fileinput

lanternfish = []

for line in fileinput.input():
    lanternfish = list(map(int, line.split(",")))
    pass


def part_one():
    for i in range(80):
        for j in range(len(lanternfish)):
            if lanternfish[j] == 0:
                lanternfish.append(8)
                lanternfish[j] = 6
            else:
                lanternfish[j] -= 1
    print(len(lanternfish))


def calculate(initial_state, days):
    fish_states = [0] * 9
    fish_states[initial_state] = 1
    for i in range(days):
        fish_states_mod = [0] * 9
        for j in reversed(range(len(fish_states))):
            num_fish = fish_states[j]
            if j != 0:
                fish_states_mod[j - 1] = num_fish
            else:
                fish_states_mod[8] = num_fish
                fish_states_mod[6] += num_fish
        fish_states = fish_states_mod
        print(i, fish_states)

    return sum(fish_states)


spawns = [0] * 6
for i in range(6):
    spawns[i] = calculate(i, 256)


def part_two():
    sum = 0
    for i in range(len(lanternfish)):
        sum += spawns[lanternfish[i]]
    print(sum)


part_two()