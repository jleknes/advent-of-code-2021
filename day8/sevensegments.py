import fileinput, time

def process_line_part_one(signal_pattern, digits_values):
    sum = 0
    known_lengths = [2, 3, 4, 7]
    for digits in digits_values:
        if len(digits) in known_lengths:
            sum+=1
    return sum

def part_one():
    start_time = time.time()
    sum = 0
    for line in fileinput.input():
        lists = line.split('|')
        signal_pattern = lists[0].split()
        digits_values = lists[1].split()
        print (signal_pattern, digits_values)
        sum+=process_line_part_one(signal_pattern, digits_values)
        pass
    print (sum)
    print("--- %s seconds ---" % (time.time() - start_time))

def part_two():
    start_time = time.time()
    sum = 0
    for line in fileinput.input():
        lists = line.split('|')
        signal_pattern = lists[0].split()
        digits_values = lists[1].split()
        print (signal_pattern, digits_values)
        sum+=process_line_part_two(signal_pattern, digits_values)
        pass
    print (sum)
    print("--- %s seconds ---" % (time.time() - start_time))

def strings_matching_characters(string1, string2):
    return set(string1)==set(string2)

def lookup_pattern_to_value(dict, string):
    for pattern in dict.keys():
        if strings_matching_characters(pattern, string):
            return dict[pattern]

def process_line_part_two(signal_pattern, digits_values):
    sum = ""
    pattern_to_value = build_dict(signal_pattern)
    print (pattern_to_value)
    for pattern in digits_values:
        digit = lookup_pattern_to_value(pattern_to_value, pattern)
        print (digit)
        sum+=str(digit)
    return int(sum)


def build_dict(signal_pattern):
    length_to_digit = {2: 1, 3:7, 4:4, 7:8}
    pattern_to_value = {}
    value_to_pattern = {}
    # Find segments based on length of pattern: 1, 4, 7 and 8
    for pattern in signal_pattern:
        if len(pattern) in length_to_digit:
            digit = length_to_digit[len(pattern)]
            pattern_to_value[pattern]=digit
            value_to_pattern[digit]=set(pattern)

    for pattern in pattern_to_value.keys():
        signal_pattern.remove(pattern)

    # find segment corresponding to 3: length 5 and includes all elements in 1
    for pattern in signal_pattern:
        chars = set(pattern)
        if len(pattern)==5 and value_to_pattern[1].issubset(chars):
            pattern_to_value[pattern]=3
            value_to_pattern[3]=set(pattern)
            signal_pattern.remove(pattern)

    # find segment corresponding to 9:
    # find segment of length 6 containing all segments in 4
    for pattern in signal_pattern:
        if len(pattern)==6 and value_to_pattern[4].issubset(pattern):            
            pattern_to_value[pattern]=9
            value_to_pattern[9]=set(pattern)
            signal_pattern.remove(pattern)

    # find segment corresponding to 0:
    for pattern in signal_pattern:
        if len(pattern)==6 and value_to_pattern[7].issubset(pattern):            
            pattern_to_value[pattern]=0
            value_to_pattern[0]=set(pattern)
            signal_pattern.remove(pattern)

    # find segment corresponding to 0: 
    for pattern in signal_pattern:
        if len(pattern)==6:
            pattern_to_value[pattern]=6
            value_to_pattern[6]=set(pattern)
            signal_pattern.remove(pattern)
    
    # find segment corresponding to 2
    upper_right_segment = set(value_to_pattern[8])-set(value_to_pattern[6])
    for pattern in signal_pattern:
        if len(pattern)==5 and upper_right_segment.issubset(pattern):
            pattern_to_value[pattern]=2
            value_to_pattern[2]=pattern
            signal_pattern.remove(pattern)

    # find segment corresponding to 5
    print (signal_pattern)
    pattern = signal_pattern[0]
    pattern_to_value[pattern]=5
    value_to_pattern[5]=pattern

    print (value_to_pattern)
    print (pattern_to_value)
    return pattern_to_value    



part_two()