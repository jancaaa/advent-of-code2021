def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        map = []
        while line:
            line = line.rstrip()
            map.append(list(line))
            line = fp.readline()
        return map


def print_map(map: list):
    for line in map:
        print(line)


def get_neighbours(x: int, y: int, map: list) -> dict:
    size_x = len(map[0])
    size_y = len(map)
    neighbours = dict()
    # top
    if y != 0:
        neighbours["top"] = map[y - 1][x]
    # down
    if y != size_y - 1:
        neighbours["down"] = map[y + 1][x]
    # left
    if x != 0:
        neighbours["left"] = map[y][x - 1]
    # right
    if x != size_x - 1:
        neighbours["right"] = map[y][x + 1]
    return neighbours


def get_lowest_points(map: list) -> list:
    lowest_points = []
    size_x = len(map[0])
    size_y = len(map)
    for y in range(size_y):
        for x in range(size_x):
            neighbours = get_neighbours(x, y, map).values()
            if map[y][x] < min(neighbours):
                lowest_points.append((x, y))
    return lowest_points


def part1(map: list) -> int:
    sum = 0
    lowest_points = get_lowest_points(map)
    for point in lowest_points:
        x, y = point
        sum += int(map[y][x]) + 1
    return sum


def explore(x: int, y: int, map: list) -> set:
    basin = {(x, y)}
    current = map[y][x]
    neighbours = get_neighbours(x, y, map)
    for direction, value in neighbours.items():
        if value != '9' and value > current:
            if direction == "top":
                basin.update(explore(x, y - 1, map))
            elif direction == "down":
                basin.update(explore(x, y + 1, map))
            elif direction == "left":
                basin.update(explore(x - 1, y, map))
            elif direction == "right":
                basin.update(explore(x + 1, y, map))
    return basin


def part2(map: list) -> int:
    basin_sizes = []
    lowest_points = get_lowest_points(map)

    for point in lowest_points:
        x, y = point
        basin = explore(x, y, map)
        basin_sizes.append(len(basin))

    basin_sizes = sorted(basin_sizes, reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
