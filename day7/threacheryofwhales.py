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
        step_costs[i]=int((i*(i+1))/2)
    return

def total_cost_position(positions, i):
    cost = 0
    for j in range (len(positions)):
        distance = abs(positions[j]-i)
        cost+=step_costs[distance]
    return cost

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
        cost = total_cost_position(positions, i)
        if (cost<lowest_cost):            
            lowest_cost=cost
        print(i, cost)
    print(lowest_cost)
    print("--- %s seconds ---" % (time.time() - start_time))

# binary search for lowest value
def iter_search(positions):
    l = 0
    r = len(positions)
    while (l <= r) :
        m = int(l + (r - l) / 2) # m = (l + r) / 2
        cost_l = total_cost_position(positions, l)
        cost_r = total_cost_position(positions, l)
        if ((r == l + 1) and cost_l <= cost_r):
            return cost_l
        
        if ((r == l + 1) and cost_l > cost_r):
            return cost_r

        cost_m = total_cost_position(positions, m)
        cost_m_plus_one = total_cost_position(positions, m+1)
        cost_m_minus_one = total_cost_position(positions, m-1)

        if (cost_m < cost_m_plus_one and cost_m < cost_m_minus_one):
            return cost_m

        if (cost_m < cost_m_plus_one and cost_m > cost_m_minus_one):
            r = m - 1
        else :
            l = m + 1
    return -1

def part_two_binary_search():
    start_time = time.time()
    for line in fileinput.input():
        positions = list(map(int, line.split(',')))
        pass
    positions.sort()
    generate_step_costs(positions[len(positions)-1]+1)

    lowest_cost = iter_search(positions)
    print(lowest_cost)
    print("--- %s seconds ---" % (time.time() - start_time))

part_two_binary_search()
