import sys, time, math

ID_LENGTH_IN_BITS = 0
ID_NUMBER_OF_PACKAGES = 1
LITERAL_PACKET_ID = 4
version_numbers = 0


def read_input():
    hexstring = sys.stdin.readline()
    binstring = bin(int(hexstring, 16))

    # remove trailing "0b and pad with zeros"
    return (binstring[2 : len(binstring)]).zfill(len(hexstring) * 4)


def decode_length(packet):
    decoded = {}
    decoded["length_type_id"] = int(packet[6], 2)
    if decoded["length_type_id"] == ID_LENGTH_IN_BITS:
        decoded["length"] = int(packet[7 : 7 + 15], 2)
    else:
        decoded["num_packages"] = int(packet[7 : 7 + 11], 2)

    return decoded


def decode_header(packet):
    decoded = {}
    decoded["version"] = int(packet[0:3], 2)
    decoded["packet_type_id"] = int(packet[3:6], 2)
    if decoded["packet_type_id"] != LITERAL_PACKET_ID:
        decoded = decoded | decode_length(packet)
    return decoded


def num_from_literal(input):
    bitstring = ""
    for i in range(len(input) // 5):
        bitstring += input[i * 5 + 1 : i * 5 + 5]
    return int(bitstring, 2)


def decode_literal(packet):
    header = decode_header(packet)
    global version_numbers
    package_length = 6
    while packet[package_length] == "1":
        package_length += 5
    package_length += 5
    num = num_from_literal(packet[6:package_length])
    return package_length, num


def evaluate_elements(elements, id):
    if id == 4:
        return elements[0]
    elif id == 0:
        return sum(elements)
    elif id == 1:
        return math.prod(elements)
    elif id == 2:
        return min(elements)
    elif id == 3:
        return max(elements)
    elif id == 5:
        return int(elements[0] > elements[1])
    elif id == 6:
        return int(elements[0] < elements[1])
    elif id == 7:
        return int(elements[0] == elements[1])


def decode(packet):
    # print(packet)
    header = decode_header(packet)
    global version_numbers
    version_numbers += header["version"]
    package_length = 0
    elements = []
    if header["packet_type_id"] == LITERAL_PACKET_ID:
        package_length, element = decode_literal(packet)
        elements.append(element)
    elif header["length_type_id"] == ID_LENGTH_IN_BITS:
        package_length = 22 + header["length"]
        sub_packet = packet[22 : 22 + header["length"] + 1]
        position = 0
        while position + 1 < header["length"]:
            packet_position, element = decode(sub_packet[position:])
            position += packet_position
            elements.append(element)
    elif header["length_type_id"] == ID_NUMBER_OF_PACKAGES:
        sub_packet = packet[18:]
        # print("packet:\n", packet, "\nID_NUMBER_OF_PACKAGES", "sub_packet:\n", sub_packet)
        position = 0
        for i in range(0, header["num_packages"]):
            packet_position, element = decode(sub_packet[position:])
            position += packet_position
            elements.append(element)
        package_length = 18 + position
    element = evaluate_elements(elements, header["packet_type_id"])
    return package_length, element


def main():
    start_time = time.time()
    input = read_input()
    print("value of expression:", decode(input)[1])
    print("sum of version numbers:", version_numbers)
    print("--- %s seconds ---" % (time.time() - start_time))


main()


def test_decode_literal():
    print("should be length 24, num 2021", decode_literal("110100101111111000101000"))
    print("should be 11:", decode_literal("10110000011"))
    print("should be 16:", decode_literal("1011001001100000"))
    print("should be 21:", decode_literal("101100100111010001011"))
    print("should be 25:", decode_literal("10110010011101001101100000"))


def test_eval_elements():
    print("should be 2", evaluate_elements([1, 2], 6) * 1)


# test_decode_literal()
