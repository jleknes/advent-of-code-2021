import fileinput

SIDE = 1000
grid = [SIDE * [0] for k in range(SIDE)]

def isDiagonal(p1, p2):
    x1=p1[0] 
    y1=p1[1]
    x2=p2[0]
    y2=p2[1]
    if (x1!=x2 and y1!=y2):
        return True
    return False

def part_one():
    segments = [
        [tuple(map(int, seg.split(','))) for seg in line.split(' -> ')]
        for line in fileinput.input()
    ]

    for (x1,y1), (x2, y2) in segments:
        if not isDiagonal((x1,y1),(x2,y2)):
            x1,x2 = min(x1,x2), max(x1,x2)
            y1,y2 = min(y1,y2), max(y1,y2)
            if (x2>x1):
                x2+=1
            if (y2>y1):
                y2+=1
            if (y1==y2):
                y2+=1
            if (x1==x2):
                x2+=1
            for y in range(y1,y2):
                for x in range(x1,x2):
                    print (x, y)
                    grid[y][x]+=1


    sum = 0

    for y in range(len(grid[0])):
        for x in range(len(grid)):        
            if grid[y][x]>1:
                sum+=1
    print (sum)

def part_two():
    segments = [
        [tuple(map(int, seg.split(','))) for seg in line.split(' -> ')]
        for line in fileinput.input()
    ]

    for (x1,y1), (x2, y2) in segments:
        print (x1, y1, x2, y2)
        if (not isDiagonal((x1,y1),(x2,y2))):
            x1,x2 = min(x1,x2), max(x1,x2)
            y1,y2 = min(y1,y2), max(y1,y2)
            if (x2>x1):
                x2+=1
            if (y2>y1):
                y2+=1
            if (y1==y2):
                y2+=1
            if (x1==x2):
                x2+=1
            for y in range(y1,y2):
                for x in range(x1,x2):
                    grid[y][x]+=1
        else:
            line_length = abs(x2-x1)
            dx = int((x2-x1)/abs(x2-x1))
            dy = int((y2-y1)/abs(y2-y1))
            
            print (dx, dy,line_length)
            x,y = x1, y1
            while True:
                grid[y][x]+=1
                if (x,y) == (x2,y2):
                    break
                x+=dx; y+=dy

    for i in range(len(grid)):
        print(grid[i])

    sum = 0

    for y in range(len(grid[0])):
        for x in range(len(grid)):        
            if grid[y][x]>1:
                sum+=1
    print (sum)

#part_one()

part_two()