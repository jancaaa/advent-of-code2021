import sys


def read_file() -> str:
    with open("input.txt") as fp:
        line = fp.readline().rstrip()
        return line


def decode(input: str) -> str:
    output = ""
    for i in input:
        if i == "0":
            output += "0000"
        elif i == "1":
            output += "0001"
        elif i == "2":
            output += "0010"
        elif i == "3":
            output += "0011"
        elif i == "4":
            output += "0100"
        elif i == "5":
            output += "0101"
        elif i == "6":
            output += "0110"
        elif i == "7":
            output += "0111"
        elif i == "8":
            output += "1000"
        elif i == "9":
            output += "1001"
        elif i == "A":
            output += "1010"
        elif i == "B":
            output += "1011"
        elif i == "C":
            output += "1100"
        elif i == "D":
            output += "1101"
        elif i == "E":
            output += "1110"
        elif i == "F":
            output += "1111"

    return output


def divide(input: str) -> (str, str, str):
    v = input[0:3]
    t = input[3:6]
    rest = input[6:]
    return v, t, rest


def parse_literal_packet(input: str) -> (int, str):
    output = ""
    while input[0] == "1":
        output += input[1:5]
        input = input[5:]

    # process last group
    output += input[1:5]
    rest = input[5:]
    return int(output, 2), rest


def parse_packet(input: str) -> (dict, str):
    v, t, content = divide(input)
    packet = dict()
    packet["v"] = int(v, 2)
    packet["t"] = int(t, 2)
    packet["subpackets"] = list()

    if packet["t"] == 4:
        # literal
        output, rest = parse_literal_packet(content)
        packet["value"] = output
        return packet, rest
    else:
        # operator
        packet["i"] = content[0]
        if packet["i"] == "0":
            length = int(content[1:16], 2)
            rest = content[16 + length:]
            content = content[16:16 + length]
            while content:
                sub, content = parse_packet(content)
                packet["subpackets"].append(sub)
        else:
            count = int(content[1:12], 2)
            content = content[12:]
            for i in range(count):
                sub, content = parse_packet(content)
                packet["subpackets"].append(sub)
            rest = content
        return packet, rest


def get_version_sum(packet: dict) -> int:
    sum = 0
    sum += packet["v"]
    for p in packet["subpackets"]:
        sum += get_version_sum(p)
    return sum


def process_packet(packet: dict) -> int:
    if packet["t"] == 0:
        value = 0
        for p in packet["subpackets"]:
            value = value + p["value"] if p["t"] == 4 else value + process_packet(p)
        return value
    elif packet["t"] == 1:
        value = 1
        for p in packet["subpackets"]:
            value = value * p["value"] if p["t"] == 4 else value * process_packet(p)
        return value
    elif packet["t"] == 2:
        value = sys.maxsize
        for p in packet["subpackets"]:
            value = min(value, p["value"]) if p["t"] == 4 else min(value, process_packet(p))
        return value
    elif packet["t"] == 3:
        value = -sys.maxsize
        for p in packet["subpackets"]:
            value = max(value, p["value"]) if p["t"] == 4 else max(value, process_packet(p))
        return value
    elif packet["t"] == 4:
        return packet["value"]
    elif packet["t"] == 5:
        return 1 if process_packet(packet["subpackets"][0]) > process_packet(packet["subpackets"][1]) else 0
    elif packet["t"] == 6:
        return 1 if process_packet(packet["subpackets"][0]) < process_packet(packet["subpackets"][1]) else 0
    elif packet["t"] == 7:
        return 1 if process_packet(packet["subpackets"][0]) == process_packet(packet["subpackets"][1]) else 0


def part2_tests():
    assert part2(decode("C200B40A82")) == 3
    assert part2(decode("04005AC33890")) == 54
    assert part2(decode("880086C3E88112")) == 7
    assert part2(decode("CE00C43D881120")) == 9
    assert part2(decode("D8005AC2A8F0")) == 1
    assert part2(decode("F600BC2D8F")) == 0
    assert part2(decode("9C005AC2F8F0")) == 0
    assert part2(decode("9C0141080250320F1802104A08")) == 1


def part1(input: str) -> int:
    packet, rest = parse_packet(input)
    return get_version_sum(packet)


def part2(input: str) -> int:
    packet, rest = parse_packet(input)
    return process_packet(packet)


if __name__ == "__main__":
    input = read_file()
    input = decode(input)
    print(f"Part 1: {part1(input)}")
    part2_tests()
    print(f"Part 2: {part2(input)}")
