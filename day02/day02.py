def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        instructions = []
        while line:
            command, value = line.rstrip().split(" ")
            instructions.append((command, value))
            line = fp.readline()
        return instructions


def part1(instructions: list) -> int:
    position = 0
    depth = 0
    for command, value in instructions:
        if command == "forward":
            position += int(value)
        elif command == "down":
            depth += int(value)
        elif command == "up":
            depth -= int(value)
    return position * depth


def part2(instructions: list) -> int:
    position = 0
    depth = 0
    aim = 0
    for command, value in instructions:
        if command == "forward":
            position += int(value)
            depth += aim * int(value)
        elif command == "down":
            aim += int(value)
        elif command == "up":
            aim -= int(value)
    return position * depth


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
