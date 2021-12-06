def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline().rstrip()
        fish_ages = line.split(",")
        fish_ages = [int(e) for e in fish_ages]
        return fish_ages


def part1(fish_ages: list) -> int:
    for x in range(80):
        for i in range(len(fish_ages)):
            if fish_ages[i] != 0:
                fish_ages[i] -= 1
            else:
                fish_ages.append(8)
                fish_ages[i] = 6
    return len(fish_ages)


def part2(fish_ages: list) -> int:
    counts = []  # counts of fish with given internal state
    for i in range(9):
        counts.append(0)

    for age in fish_ages:
        counts[age] += 1

    for _ in range(256):
        in_reproducing_state = counts[0]
        for i in range(8):
            counts[i] = counts[i + 1]
        counts[8] = in_reproducing_state  # reproduce
        counts[6] += in_reproducing_state  # internal reset timer
    return sum(counts)


if __name__ == "__main__":
    fish_ages = read_file()
    print(f"Part 1: {part1(fish_ages.copy())}")
    print(f"Part 2: {part2(fish_ages)}")
