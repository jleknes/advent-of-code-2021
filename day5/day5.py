import fileinput

lines = []

for line in fileinput.input():
    [p1,p2] = tup[(line.split(' -> ').split(','))
    print (p1)
    print (p2)
    #lines.append()
    pass

print (lines)