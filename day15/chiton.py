import fileinput, time, sys
from collections import deque
import heapq


risk = []


def read_input():
    for line in fileinput.input():
        gridline = []
        for i in range(len(line.strip())):
            gridline.append(int(line[i]))
        risk.append(gridline)


def printgrid(input):
    for i in range(len(input)):
        line = ""
        for j in range(len(input[i])):
            line += str(input[i][j])
        print(line)
    print()


# solve using BFS
def solve_part_one():
    count = 0
    lowest_risk = [len(risk) * [100000000] for k in range(len(risk[0]))]
    queue = deque()
    queue.append((0, 0, 0))
    while queue:
        x, y, total_risk = queue.popleft()
        count += 1
        for newx, newy in get_adjacent(x, y):
            if lowest_risk[newx][newy] > total_risk + risk[newx][newy]:
                lowest_risk[newx][newy] = total_risk + risk[newx][newy]
                queue.append((newx, newy, lowest_risk[newx][newy]))
    print("count", count)
    return lowest_risk[len(lowest_risk) - 1][len(lowest_risk[0]) - 1]


def get_adjacent(x, y):
    paths = []
    pairs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in pairs:
        if x + dx > -1 and y + dy > -1 and x + dx < len(risk) and y + dy < len(risk[x]):
            paths.append((x + dx, y + dy))
    return paths


# Dijkstra with pq
def solve():
    unvisited_nodes = set()
    for i in range(len(risk)):
        for j in range(len(risk[0])):
            unvisited_nodes.add((i, j))
    # init distances to a high value
    distances = {}
    for node in unvisited_nodes:
        distances[node] = 1000000

    # distances - starting point
    distances[(0, 0)] = 0

    pq = [(0, (0, 0))]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor in get_adjacent(current_vertex[0], current_vertex[1]):
            distance = current_distance + risk[neighbor[0]][neighbor[1]]

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances[(len(risk) - 1, len(risk) - 1)]


def enlarge_grid(grid):
    grid_size = len(grid)
    new_size = grid_size * 5
    new_grid = [new_size * [0] for k in range(new_size)]
    for i in range(len(grid)):
        for j in range(len(grid)):
            for k in range(5):
                for l in range(5):
                    new_val = grid[i][j] + k + l
                    if new_val > 9:
                        new_val = new_val % 9
                    new_grid[k * grid_size + i][l * grid_size + j] = new_val
    return new_grid


def part_one():
    start_time = time.time()

    print("part one:", solve())

    print("--- %s seconds ---" % (time.time() - start_time))


def part_two():
    start_time = time.time()

    global risk
    risk = enlarge_grid(risk)
    print("part one:", solve())
    print("--- %s seconds ---" % (time.time() - start_time))


read_input()
part_one()
part_two()
