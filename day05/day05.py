def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        vents = []
        while line:
            start, end = line.rstrip().split(" -> ")
            x1, y1 = start.split(",")
            x2, y2 = end.split(",")
            vent = ((int(x1), int(y1)), (int(x2), int(y2)))
            vents.append(vent)
            line = fp.readline()
        return vents


def print_diagram(diagram: list):
    for line in diagram:
        print(line)
    print()


def extend_diagram(size_x: int, size_y: int, diagram: list) -> list:
    if size_x >= len(diagram):
        # extend diagram (x)
        for _ in range(len(diagram), size_x + 1):
            diagram.append([0 for _ in range(len(diagram[0]))])
    if size_y >= len(diagram[0]):
        # extend diagram (y)
        for x in range(len(diagram)):
            for _ in range(len(diagram[x]), size_y + 1):
                diagram[x].append(0)
    return diagram


def process_vent(vent: tuple, diagram: list) -> list:
    start, end = vent
    x1, y1 = start
    x2, y2 = end
    is_horizontal = x1 == x2
    is_vertical = y1 == y2

    if is_horizontal:
        start_y = min(y1, y2)
        end_y = max(y1, y2)
        diagram = extend_diagram(x1, end_y, diagram)
        for y in range(start_y, end_y + 1):
            diagram[x1][y] += 1
    elif is_vertical:
        diagram = extend_diagram(max(x1, x2), y1, diagram)
        start_x = min(x1, x2)
        end_x = max(x1, x2)
        for x in range(start_x, end_x + 1):
            diagram[x][y1] += 1
    return diagram


def process_vent2(vent: tuple, diagram: list) -> list:
    start, end = vent
    x1, y1 = start
    x2, y2 = end
    is_horizontal = x1 == x2
    is_vertical = y1 == y2
    is_diagonal = abs(x1 - x2) == abs(y1 - y2)

    if is_horizontal:
        start_y = min(y1, y2)
        end_y = max(y1, y2)
        diagram = extend_diagram(x1, end_y, diagram)
        for y in range(start_y, end_y + 1):
            diagram[x1][y] += 1
    elif is_vertical:
        diagram = extend_diagram(max(x1, x2), y1, diagram)
        start_x = min(x1, x2)
        end_x = max(x1, x2)
        for x in range(start_x, end_x + 1):
            diagram[x][y1] += 1
    elif is_diagonal:
        diagram = extend_diagram(max(x1, x2), max(y1, y2), diagram)
        l = abs(x1 - x2)
        for i in range(l + 1):
            x = x1 + i if x2 - x1 > 0 else x1 - i
            y = y1 + i if y2 - y1 > 0 else y1 - i
            diagram[x][y] += 1
    return diagram


def evaluate(diagram: list) -> int:
    count = 0
    for i in range(len(diagram)):
        for j in range(len(diagram[i])):
            if diagram[i][j] > 1:
                count += 1
    return count


def part1(vents: list) -> int:
    diagram = [[0]]
    for vent in vents:
        diagram = process_vent(vent, diagram)
    return evaluate(diagram)


def part2(vents: list) -> int:
    diagram = [[0]]
    for vent in vents:
        diagram = process_vent2(vent, diagram)
    return evaluate(diagram)


if __name__ == "__main__":
    vents = read_file()
    print(f"Part 1: {part1(vents)}")
    print(f"Part 2: {part2(vents)}")
