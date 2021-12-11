import copy


def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        while line:
            line = line.rstrip()
            line = list(line)
            entries.append([int(e) for e in line])
            line = fp.readline()
        return entries


def print_map(map: list):
    for line in map:
        print(line)
    print()


def increase(map: list) -> list:
    size_x = len(map[0])
    size_y = len(map)
    for y in range(size_y):
        for x in range(size_x):
            map[y][x] += 1
    return map


def flash(map: list) -> (int, list):
    flash_count = 0
    flashed = True
    while flashed:
        flashed = False
        size_x = len(map[0])
        size_y = len(map)
        for y in range(size_y):
            for x in range(size_x):
                if map[y][x] > 9:
                    flashed = True
                    flash_count += 1
                    map[y][x] = -1  # mark as flashed
                    neighbours = get_neighbours(x, y, map)
                    for n in neighbours:
                        nx, ny = n
                        if map[ny][nx] != -1:
                            map[ny][nx] += 1
    return flash_count, map


def reset(map: list) -> list:
    size_x = len(map[0])
    size_y = len(map)
    for y in range(size_y):
        for x in range(size_x):
            if map[y][x] == -1:
                map[y][x] = 0
    return map


def get_neighbours(x: int, y: int, map: list) -> list:
    max_x = len(map[0]) - 1
    max_y = len(map) - 1
    neighbours = []

    # NW
    if y != max_y and x != 0:
        neighbours.append((x - 1, y + 1))

    # N
    if y != max_y:
        neighbours.append((x, y + 1))

    # NE
    if y != max_y and x != max_x:
        neighbours.append((x + 1, y + 1))

    # W
    if x != 0:
        neighbours.append((x - 1, y))

    # E
    if x != max_x:
        neighbours.append((x + 1, y))

    # SW
    if y != 0 and x != 0:
        neighbours.append((x - 1, y - 1))

    # S
    if y != 0:
        neighbours.append((x, y - 1))

    # SE
    if y != 0 and x != max_x:
        neighbours.append((x + 1, y - 1))

    return neighbours


def is_synced(map: list) -> bool:
    expected_state = map[0][0]
    size_x = len(map[0])
    size_y = len(map)
    for y in range(size_y):
        for x in range(size_x):
            if map[y][x] != expected_state:
                return False
    return True


def part1(map: list) -> int:
    total_flash_count = 0
    for _ in range(100):
        map = increase(map)
        flash_count, map = flash(map)
        total_flash_count += flash_count
        map = reset(map)
    return total_flash_count


def part2(map: list) -> int:
    step_count = 0
    while not is_synced(map):
        step_count += 1
        map = increase(map)
        _, map = flash(map)
        map = reset(map)
    return step_count


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(copy.deepcopy(entries))}")
    print(f"Part 2: {part2(copy.deepcopy(entries))}")
