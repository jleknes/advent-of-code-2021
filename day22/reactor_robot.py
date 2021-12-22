import fileinput, time
from functools import cache


def read_input():
    cubes = []
    for line in fileinput.input():
        cube = {}
        setting, rest = line.strip().split(" ")
        cube["setting"] = setting
        for pair in rest.split(","):
            index = pair[0:1]
            n1, n2 = pair[2:].split("..")
            cube[index] = (int(n1), int(n2))
        cubes.append(cube)
    return cubes
    # print(cubes)


def limit_range(i1, i2):
    if i1 < -50:
        i1 = -50
    if i2 > 50:
        i2 = 50
    return range(i1, i2 + 1)


def part_one(cubes):
    cuboids = set()
    for cube in cubes:
        for x in limit_range(cube["x"][0], cube["x"][1]):
            for y in limit_range(cube["y"][0], cube["y"][1]):
                for z in limit_range(cube["z"][0], cube["z"][1]):
                    cuboid = (x, y, z)
                    if cube["setting"] == "on":
                        cuboids.add(cuboid)
                    elif cuboid in cuboids:
                        cuboids.remove(cuboid)
    # print(cuboids)
    return cuboids


def main():
    start_time = time.time()
    cubes = read_input()

    print(len(part_one(cubes)))
    # print("part one:", part_one(copy.deepcopy(positions)))
    # part_two(positions)
    print("--- %s seconds ---" % (time.time() - start_time))


main()