
import fileinput, time

connections = {}

paths = set()

part_two = False

def single_cave_visited_twice(path):
    visited = set()
    for edge in path.split(','):
        if edge.islower() and edge in visited:
            return True
        visited.add(edge)
    return False

def dfs(path, last_edge):
    connected_edges = connections[last_edge]
    for edge in connected_edges:
        if edge=='end':
            paths.add(path+','+edge)
            pass
        elif edge=='start':
            pass
        elif edge.islower():
            # edge is a small cave
            if not edge in path:
                dfs(path+','+edge, edge)
            elif part_two and not single_cave_visited_twice(path):
                dfs(path+','+edge, edge)
            else:
                # path already contains this small cave
                pass
        else:
            dfs(path+','+edge, edge)

def read_input():
    for line in fileinput.input():
        e1, e2 = line.strip().split("-")
        if (not e1 in connections):
            connections[e1]=set()
        if (not e2 in connections):
            connections[e2]=set()
        connections[e1].add(e2)
        connections[e2].add(e1)
    print (connections)


def part_one():
    start_time = time.time()
    read_input()
    dfs('start','start')
    print(paths)
    print(len(paths))

def part_two():
    part_two = True
    start_time = time.time()
    read_input()
    dfs('start','start')
    print(paths)
    print(len(paths))

part_two()
