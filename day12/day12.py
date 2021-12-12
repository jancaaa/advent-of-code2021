def read_file(file_name: str = "input.txt") -> list:
    with open(file_name) as fp:
        line = fp.readline()
        connections = []
        while line:
            line = line.rstrip()
            start, end = line.split("-")
            if not (end == "start" or start == "end"):
                connections.append((start, end))
            if not (end == "end" or start == "start"):
                connections.append((end, start))
            line = fp.readline()
        return connections


def get_neighbours(connections: list) -> dict:
    neighbours = dict()
    caves = set([start for start, _ in connections])
    for c in caves:
        neighbours[c] = _get_neighbours(c, connections)
    return neighbours


def _get_neighbours(current: str, connections: list) -> list:
    next = []
    for e in connections:
        start, end = e
        if start == current:
            next.append(end)
    return next


def tests_part1(small: list, medium: list, large: list):
    assert part1(small) == 10
    assert part1(medium) == 19
    assert part1(large) == 226


def tests_part2(small: list, medium: list, large: list):
    assert part2(small) == 36
    assert part2(medium) == 103
    assert part2(large) == 3509


def part1(entries: list) -> int:
    path_count = 0
    neighbours = get_neighbours(entries)
    paths = [["start"]]
    while paths:
        new_paths = []
        for p in paths:
            if p[-1] == "end":
                path_count += 1  # completed path
            else:
                for n in neighbours[p[-1]]:
                    if n.islower() and n in p:
                        continue  # already visited
                    else:
                        updated_path = p.copy()
                        updated_path.append(n)
                        new_paths.append(updated_path)
        paths = new_paths
    return path_count


def part2(entries: list) -> int:
    path_count = 0
    neighbours = get_neighbours(entries)
    paths = [["start"]]
    while paths:
        new_paths = []
        for p in paths:
            if p[-1] == "end":
                path_count += 1  # completed path
            else:
                for n in neighbours[p[-1]]:
                    if n.islower():
                        visited_small_caves = [e for e in p if e.islower()]
                    if n.islower() and n in p and len(set(visited_small_caves)) < len(visited_small_caves):
                        continue  # already visited one small cave twice on this path
                    else:
                        updated_path = p.copy()
                        updated_path.append(n)
                        new_paths.append(updated_path)
        paths = new_paths
    return path_count


if __name__ == "__main__":
    # tests
    small = read_file("small_example.txt")
    medium = read_file("medium_example.txt")
    large = read_file("large_example.txt")
    tests_part2(small, medium, large)
    tests_part2(small, medium, large)

    connections = read_file()
    print(f"Part 1: {part1(connections)}")
    print(f"Part 2: {part2(connections)}")
