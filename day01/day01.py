def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        while line:
            entries.append(int(line.rstrip()))
            line = fp.readline()
        return entries


def part1(entries: list) -> int:
    count = 0
    for i in range(1, len(entries)):
        if entries[i - 1] < entries[i]:
            count = count + 1
    return count


def part2(entries: list) -> int:
    count = 0
    for i in range(3, len(entries)):
        if entries[i - 3] < entries[i]:
            count = count + 1
    return count


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
