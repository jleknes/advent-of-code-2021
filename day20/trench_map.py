import fileinput, time

algorithm = ""
enhance_mask = [(1, 1), (0, 1), (-1, 1), (1, 0), (0, 0), (-1, 0), (1, -1), (0, -1), (-1, -1)]


def printgrid(input):
    for i in range(len(input)):
        line = ""
        for j in range(len(input[i])):
            line += str(input[i][j])
        print(line)
    print()


def read_input():
    global algorithm
    input_image = []
    for line in fileinput.input():
        if fileinput.isfirstline():
            algorithm = line

        # skip empty line between algorithm and image
        elif line.strip() != "":
            gridline = []
            for i in range(len(line.strip())):
                if line[i] == "#":
                    gridline.append(1)
                else:
                    gridline.append(0)
            input_image.append(gridline)
    return input_image


def enhance_pixel(x, y, input_image):
    algorithm_index = 0
    for i in range(len(enhance_mask)):
        bit_mask = 0
        dx = enhance_mask[i][0]
        dy = enhance_mask[i][1]
        bit_mask = input_image[y + dy][x + dx]
        algorithm_index |= bit_mask << i
    return int(algorithm[algorithm_index] == "#")


def enhance(input_image, pass_number):
    output_size = len(input_image) + 2
    enhanced_image = [output_size * [0] for k in range(output_size)]
    fill = 0
    if pass_number % 2 == 0 and algorithm[0] == "#":
        fill = 1

    expanded_input = expand_image(input_image, fill)
    for y in range(len(enhanced_image)):
        for x in range(len(enhanced_image)):
            enhanced_image[y][x] = enhance_pixel(x + 1, y + 1, expanded_input)
    return enhanced_image


def expand_image(input_image, fill):
    output_size = len(input_image) + 4
    output_image = [output_size * [0] for k in range(output_size)]
    for y in range(output_size):
        for x in range(output_size):
            if y < 2 or x < 2 or x > output_size - 3 or y > output_size - 3:
                output_image[y][x] = fill
            else:
                output_image[y][x] = input_image[y - 2][x - 2]
    return output_image


def solve(input_image):

    final = enhance(input_image, 1)
    for i in range(2, 51):
        final = enhance(final, i)

    sum = 0
    for y in range(len(final)):
        for x in range(len(final)):
            sum += final[y][x]
    return sum


def main():
    input_image = read_input()
    sum = solve(input_image)
    print(sum)


main()