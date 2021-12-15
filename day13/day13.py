import copy


def read_file() -> (list, list):
    with open("input.txt") as fp:
        # paper
        line = fp.readline().strip()
        paper = []
        while line:
            x, y = line.split(",")
            paper.append((int(x), int(y)))
            line = fp.readline().strip()

        # fold instructions
        fold_instructions = []
        line = fp.readline()
        while line:
            line = line.strip()
            instr, value = line.split("=")
            instr = instr[-1]
            fold_instructions.append((instr, int(value)))
            line = fp.readline()
        return paper, fold_instructions


def print_paper(paper: list):
    for line in paper:
        line = "".join(line)
        line = line.replace(".", " ")
        print(line)
    print()


def create_paper(entries: list) -> list:
    paper = []
    size_x = max([x for x, _ in entries]) + 1
    size_y = max([y for _, y in entries]) + 1
    line = ["." for _ in range(size_x)]
    for y in range(size_y):
        paper.append(line.copy())

    for e in entries:
        x, y = e
        paper[y][x] = "#"

    return paper


def fold_y(y: int, paper: list) -> list:
    size_y = len(paper)
    size_x = len(paper[0])
    folded_paper = []
    # copy first half
    for i in range(y):
        folded_paper.append(paper[i].copy())

    # fold second half
    for i in range(y + 1, size_y):
        for x in range(size_x):
            if paper[i][x] == "#":
                folded_paper[y - i][x] = "#"
    return folded_paper


def fold_x(x: int, paper: list) -> list:
    size_y = len(paper)
    size_x = len(paper[0])
    folded_paper = []
    # copy first half
    for y in range(size_y):
        line = paper[y][:x]
        folded_paper.append(line)
    # fold second half
    for y in range(size_y):
        for i in range(x, size_x):
            if paper[y][i] == "#":
                folded_paper[y][x - i] = "#"
    return folded_paper


def count_dots(paper: list) -> int:
    count = 0
    size_y = len(paper)
    size_x = len(paper[0])
    for y in range(size_y):
        for x in range(size_x):
            if paper[y][x] == "#":
                count += 1
    return count


def part1(paper: list, instruction: tuple) -> int:
    direction, value = instruction
    if direction == "x":
        paper = fold_x(value, paper)
    elif direction == "y":
        paper = fold_y(value, paper)
    return count_dots(paper)


def part2(paper: list, instructions: list):
    for i in instructions:
        direction, value = i
        if direction == "x":
            paper = fold_x(value, paper)
        elif direction == "y":
            paper = fold_y(value, paper)
    print_paper(paper)


if __name__ == "__main__":
    entries, instructions = read_file()
    paper = create_paper(entries)
    print(f"Part 1: {part1(copy.deepcopy(paper), instructions[0])}")
    print("Part 2:")
    part2(copy.deepcopy(paper), instructions)
