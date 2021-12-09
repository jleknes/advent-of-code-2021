import fileinput, time

heightmap = []

def is_lower(x,y, diffx, diffy):
    if (x+diffx<0 or y+diffy<0 or x+diffx>=len(heightmap[0]) or y+diffy>=len(heightmap)):
        return True
    else:
        return heightmap[y][x]<heightmap[y+diffy][x+diffx]
    

# Edge safe function
def is_lowpoint(x,y):
    return is_lower(x,y, -1, 0) and is_lower(x,y, 0, -1) and is_lower(x,y, +1, 0) and is_lower(x,y, 0, +1)


def part_one():
    start_time = time.time()
    sum = 0
    for line in fileinput.input():
        pointline = []
        for char in line.strip():            
            pointline.append(int(char))
        pass
        heightmap.append(pointline)
    lowpoints = []
    for i in range(len(heightmap)):
        for j in range (len(heightmap[i])):
            if is_lowpoint(j,i):
                lowpoints.append(heightmap[i][j])
    sum = 0
    for points in lowpoints:
        sum+=points+1
    print (sum)
    print("--- %s seconds ---" % (time.time() - start_time))



def is_part_of_basin(x,y, diffx, diffy):
    if (x+diffx<0 or y+diffy<0 or x+diffx>=len(heightmap[0]) or y+diffy>=len(heightmap)):
        return False
    if heightmap[y+diffy][x+diffx]==9:
        return False
    return True

# BFS

def bfs(x,y, points_in_basin):
    diffx=-1
    diffy=0
    if is_part_of_basin(x,y,diffx,diffy) and (x+diffx,y+diffy) not in points_in_basin:
        points_in_basin.add((x+diffx,y+diffy))
        points_in_basin = points_in_basin | bfs(x+diffx,y+diffy, points_in_basin)
    diffx=0
    diffy=-1

    if is_part_of_basin(x,y,diffx,diffy) and (x+diffx,y+diffy) not in points_in_basin:
        points_in_basin.add((x+diffx,y+diffy))
        points_in_basin = points_in_basin | bfs(x+diffx,y+diffy, points_in_basin)
    diffx=1
    diffy=0

    if is_part_of_basin(x,y,diffx,diffy) and (x+diffx,y+diffy) not in points_in_basin:
        points_in_basin.add((x+diffx,y+diffy))
        points_in_basin = points_in_basin | bfs(x+diffx,y+diffy, points_in_basin)
    diffx=0
    diffy=1

    if is_part_of_basin(x,y,diffx,diffy) and (x+diffx,y+diffy) not in points_in_basin:
        points_in_basin.add((x+diffx,y+diffy))
        points_in_basin = points_in_basin | bfs(x+diffx,y+diffy, points_in_basin)

    return points_in_basin


def part_two():
    start_time = time.time()
    sum = 0
    for line in fileinput.input():
        pointline = []
        for char in line.strip():            
            pointline.append(int(char))
        pass
        heightmap.append(pointline)
    lowpoints = []
    for i in range(len(heightmap)):
        for j in range (len(heightmap[i])):
            if is_lowpoint(j,i):
                lowpoints.append((i,j))

    basins = []
    for point in lowpoints:
        print (point[0],point[1])
        basins.append(bfs(point[1],point[0], set()))
    
    basin_sizes = []
    for basin in basins:
        basin_sizes.append(len(basin))
    basin_sizes.sort(reverse = True)
    print (basin_sizes[0]*basin_sizes[1]*basin_sizes[2])

    print("--- %s seconds ---" % (time.time() - start_time))

part_one()
part_two()