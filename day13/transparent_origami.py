import fileinput, time


def read_input():
    points = set()
    folds = []
    for line in fileinput.input():
        if "," in line:
            x, y = map(int, line.strip().split(","))
            points.add((x, y))
        elif "=" in line:
            direction = line[11]
            fold_along = int(line.strip().split("=")[1])
            folds.append((direction, fold_along))
    return (points, folds)


def fold(points, direction, fold_along):
    new_points = set()
    right_of_fold = []
    # add all points left of fold
    for point in points:
        x = point[0]
        y = point[1]
        if x < fold_along and direction == "x" or y < fold_along and direction == "y":
            new_points.add(point)
        elif x > fold_along and direction == "x" or y > fold_along and direction == "y":
            right_of_fold.append(point)
    for point in right_of_fold:
        x = point[0]
        y = point[1]
        if direction == "x":
            x = fold_along - (point[0] - fold_along)
        elif direction == "y":
            y = fold_along - (point[1] - fold_along)
        if not (x, y) in new_points:
            new_points.add((x, y))
    return new_points


def part_one():
    start_time = time.time()
    points, fold_along = read_input()
    print(len(fold(points, fold_along[0][0], fold_along[0][1])))
    print("--- %s seconds ---" % (time.time() - start_time))


def printgrid(points):
    max_x = 0
    max_y = 0
    for point in points:
        if point[0] > max_x:
            max_x = point[0]
        if point[1] > max_y:
            max_y = point[1]

    grid = [[0] * (max_x + 1) for i in range(max_y + 1)]
    for point in points:
        x = point[0]
        y = point[1]
        grid[y][x] = 1

    for i in range(max_y + 1):
        line = ""
        for j in range(max_x + 1):
            if grid[i][j] == 1:
                line += "#"
            else:
                line += "."
        print(line)


def part_two():
    start_time = time.time()
    points, fold_along = read_input()
    for fold_data in fold_along:
        points = fold(points, fold_data[0], fold_data[1])

    printgrid(points)
    print("--- %s seconds ---" % (time.time() - start_time))


part_two()