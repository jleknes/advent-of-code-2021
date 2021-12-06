import fileinput

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

part_one()
    
