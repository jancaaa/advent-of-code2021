def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        while line:
            entries.append(line.rstrip())
            line = fp.readline()
        return entries


def count_values_on_position(entries: list, position: int) -> (int, int):
    counts = [0, 0]
    for e in entries:
        value = e[position]
        counts[int(value)] += 1
    return counts[0], counts[1]


def remove_values(entries: list, position: int, value_on_position: str) -> list:
    remaining_entries = []
    for e in entries:
        if e[position] != value_on_position:
            remaining_entries.append(e)
    return remaining_entries


def part1(entries: list) -> int:
    counts = []
    for i in range(len(entries[0])):
        counts.append([0, 0])
    gamma = ''
    epsilon = ''
    for e in entries:
        for i in range(len(e)):
            counts[i][int(e[i])] += 1
    for c0, c1 in counts:
        gamma += '0' if c0 > c1 else '1'
        epsilon += '0' if c0 < c1 else '1'
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma * epsilon


def part2(entries: list) -> int:
    position = 0
    oxygen_generator_rating = entries.copy()
    while len(oxygen_generator_rating) > 1:
        c0, c1 = count_values_on_position(oxygen_generator_rating, position)
        value_to_be_removed = '1' if c0 > c1 else '0'
        oxygen_generator_rating = remove_values(oxygen_generator_rating, position, value_to_be_removed)
        position += 1

    co2_scrubber_rating = entries.copy()
    position = 0
    while len(co2_scrubber_rating) > 1:
        c0, c1 = count_values_on_position(co2_scrubber_rating, position)
        value_to_be_removed = '0' if c0 > c1 else '1'
        co2_scrubber_rating = remove_values(co2_scrubber_rating, position, value_to_be_removed)
        position += 1

    oxygen_generator_rating = int(oxygen_generator_rating[0], 2)
    co2_scrubber_rating = int(co2_scrubber_rating[0], 2)
    return oxygen_generator_rating * co2_scrubber_rating


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
