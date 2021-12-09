import fileinput
from itertools import filterfalse


def part_one():
    numbers = []
    for line in fileinput.input():
        numbers.append(line)
    gamma = ""
    epsilon = ""
    for i in range(len(numbers[0])-1):
        zeros = 0
        ones = 0
        for j in range(len(numbers)):
            if numbers[j][i]=="0":
                zeros+=1
            if numbers[j][i]=="1":
                ones+=1
        if ones>zeros:
            gamma+="1"
        else:
            gamma+="0"
    
    for i in range(len(gamma)):
        if gamma[i]=="0":
            epsilon+="1"
        else:
            epsilon+="0"
    print (gamma, " ", epsilon)
    print (int(gamma,2)*int(epsilon,2))

def predicate(number, pos, remove_zeros):
    if (number[pos]=="0" and remove_zeros):
        return True
    if (number[pos]=="1" and remove_zeros==False):
        return True
    return False


def part_two():
    numbers = []
    for line in fileinput.input():
        numbers.append(line)
    oxygen_numbers = numbers.copy()
    for i in range(len(numbers[0])):
        zeros = 0
        ones = 0
        remove_zeros = True
        for j in range(len(oxygen_numbers)):
            if oxygen_numbers[j][i]=="0":
                zeros+=1
            if oxygen_numbers[j][i]=="1":
                ones+=1
            if ones<zeros:
                remove_zeros = False
            else:
                remove_zeros = True
                
        oxygen_numbers[:] = [x for x in oxygen_numbers if not predicate(x,i, remove_zeros)]
        if (len(oxygen_numbers)==1):
            break
    print(oxygen_numbers)

    co2_numbers = numbers.copy()

    for i in range(len(numbers[0])):
        zeros = 0
        ones = 0
        remove_zeros = True
        for j in range(len(co2_numbers)):
            if co2_numbers[j][i]=="0":
                zeros+=1
            if co2_numbers[j][i]=="1":
                ones+=1
            if ones<zeros:
                remove_zeros = True
            else:
                remove_zeros = False

        co2_numbers[:] = [x for x in co2_numbers if not predicate(x,i, remove_zeros)]
        if (len(co2_numbers)==1):
            break
    print(co2_numbers)
    print (int(oxygen_numbers[0],2)*int(co2_numbers[0],2))

part_two()
    
