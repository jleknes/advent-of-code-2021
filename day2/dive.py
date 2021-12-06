import fileinput

def part_one():    
    depth = 0
    hor_pos = 0
    for line in fileinput.input():
        [command, X] = line.split()
        if command=='forward':
            hor_pos+=int(X)
        if command=='down':            
            depth+=int(X)
        if command=='up':                        
            depth-=int(X)
    print(depth*hor_pos)

def part_two():    
    depth = 0
    aim = 0
    hor_pos = 0
    for line in fileinput.input():
        [command, X] = line.split()
        if command=='forward':
            hor_pos+=int(X)
            depth+=aim*int(X)
        if command=='down':            
            aim+=int(X)
        if command=='up':                        
            aim-=int(X)
    print(depth*hor_pos)

part_two()
