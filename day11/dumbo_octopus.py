import fileinput, time

N = 10
grid = [N * [0] for k in range(N)]
flashes = 0
will_flash = []


def read_input():
    for i in range(N):
        line = input().strip()
        print(line)
        for j in range(N):
            grid[i][j] = int(line[j])
    print(grid)


def is_safe_check(x, y):
    return x >= 0 and y >= 0 and x < N and y < N


def flash(x, y):
    print("flash(", x, ",", y, ") called")
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            i = x + dx
            j = y + dy
            print("checking point:", i, j)
            if not (dx == 0 and dy == 0) and is_safe_check(i, j):
                grid[i][j] += 1
                if grid[i][j] > 9:
                    will_flash.append((i, j))


def step():
    # increase energy levelse
    for i in range(N):
        for j in range(N):
            grid[i][j] += 1

    has_flashed = set()
    for i in range(N):
        for j in range(N):
            if grid[i][j] > 9:
                will_flash.append((i, j))
    while will_flash:
        point = will_flash.pop()
        if not point in has_flashed:
            flash(point[0], point[1])
            has_flashed.add(point)
    # reset all octopus that has flashed to zero
    for point in has_flashed:
        grid[point[0]][point[1]] = 0
    return len(has_flashed)


def printgrid():
    for i in range(N):
        line = ""
        for j in range(N):
            line += str(grid[i][j])
        print(line)
    print()


def part_two():
    start_time = time.time()
    read_input()
    steps = 0
    flashes = 0
    while not flashes == N * N:
        flashes = step()
        steps += 1
    print("steps:", steps)
    print("--- %s seconds ---" % (time.time() - start_time))


def part_one():
    flashes = 0
    start_time = time.time()
    read_input()
    print("before any steps")
    printgrid()
    for i in range(100):
        flashes += step()
        print("after ", i + 1, " steps")
        printgrid()
        print("flashes:", flashes)
    print("flashes:", flashes)
    print("--- %s seconds ---" % (time.time() - start_time))


part_two()