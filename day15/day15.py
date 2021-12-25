import copy

from dijkstra import Graph


def read_file(name: str = "input.txt") -> list:
    with open(name) as fp:
        line = fp.readline()
        map = []
        while line:
            line = line.rstrip()
            line = list(line)
            map.append([int(e) for e in line])
            line = fp.readline()
    return map


def map_to_list(map: list) -> list:
    size_x = len(map[0])
    size_y = len(map)
    v_count = size_x * size_y
    graph = [dict() for _ in range(v_count)]
    for y in range(size_y):
        for x in range(size_x):
            v = y * size_y + x

            # left
            if v % size_x != 0:
                graph[v - 1][v] = map[y][x]

            # right
            if v % size_x != size_x - 1:
                graph[v + 1][v] = map[y][x]

            # top
            if v - size_x >= 0:
                graph[v - size_x][v] = map[y][x]

            # down
            if v + size_x < v_count:
                graph[v + size_x][v] = map[y][x]
    return graph


def extend_map(map: list) -> list:
    extended_map = copy.deepcopy(map)

    size = len(map)
    for i in range(4):
        for line in range(size):
            updated_line = []
            for ch in map[line]:
                updated_line.append((ch + 1 + i) % 9 if (ch + 1 + i) % 9 != 0 else 9)
            extended_map[line].extend(updated_line)

    first_row = copy.deepcopy(extended_map)

    for i in range(4):
        for line in first_row:
            updated_line = []
            for ch in line:
                updated_line.append((ch + 1 + i) % 9 if (ch + 1 + i) % 9 != 0 else 9)
            extended_map.append(updated_line)

    return extended_map


def tests():
    print("Running tests...")
    map = read_file("example.txt")
    assert part1(map) == 40
    assert part2(map) == 315
    print("Tests passed")


def part1(map: list) -> int:
    size_x = len(map[0])
    size_y = len(map)
    v_count = size_x * size_y
    graph_adj_list = map_to_list(map)
    g = Graph(v_count, graph_adj_list)
    print("Part 1: Search started... (takes a bit more time)")
    return g.dijkstra(0)


def part2(map: list) -> int:
    extended_map = extend_map(map)
    size_x = len(extended_map[0])
    size_y = len(extended_map)
    v_count = size_x * size_y
    graph_adj_list = map_to_list(extended_map)
    g = Graph(v_count, graph_adj_list)
    print("Part 2: Search started... (takes sooooo much time)")
    return g.dijkstra(0)


if __name__ == "__main__":
    tests()
    map = read_file()
    print(f"Part 1: {part1(map)}")
    print(f"Part 2: {part2(map)}")
