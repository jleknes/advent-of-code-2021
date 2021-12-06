import fileinput


def part_one():
    num_increased = 0
    prev_num = -1
    for line in fileinput.input():
        depth = int(line)
        if(depth>prev_num and prev_num!=-1):
            num_increased+=1
        prev_num = depth
    print(num_increased)

def part_two():
    depths = []
    for line in fileinput.input():
        depths.append(int(line))
    prev_sum = -1
    num_increased = 0
    for i in range(len(depths)-2):
        sum_depths = sum(depths[i:i+3])
        if(sum_depths>prev_sum and prev_sum!=-1):
            num_increased+=1
        prev_sum = sum_depths
        print (prev_sum, sum_depths)
    print(num_increased)



part_two()