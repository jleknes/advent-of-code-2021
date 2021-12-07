import fileinput, time

def part_one():
    start_time = time.time()
    positions = []
    for line in fileinput.input():
        positions = list(map(int, line.split(',')))
        pass
    positions.sort()
    middle_element = round(len(positions)/2)
    median = positions[middle_element]
    sum = 0
    for i in range(len(positions)):
        sum+=abs(positions[i]-median)
    print(sum)
    print("--- %s seconds ---" % (time.time() - start_time))

step_costs = {}

def generate_step_costs(max_val):
    for i in range(max_val):
        step_costs[i]=step_cost(i)
    return

def step_cost(x):
    sum = 0
    for i in range(1,x+1):
        sum+=i
    return sum

def part_two():
    start_time = time.time()
    positions = []
    for line in fileinput.input():
        positions = list(map(int, line.split(',')))
        pass
    positions.sort()
    generate_step_costs(positions[len(positions)-1]+1)

    lowest_cost = 9223372036854775807
    for i in range(positions[len(positions)-1]):
        cost = 0
        for j in range (len(positions)):
            distance = abs(positions[j]-i)
            cost+=step_costs[distance]
        if (cost<lowest_cost):
            lowest_cost=cost
    print(lowest_cost)
    print("--- %s seconds ---" % (time.time() - start_time))


part_one()
