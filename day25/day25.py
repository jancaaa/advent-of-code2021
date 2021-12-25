def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        situation = []
        while line:
            situation.append(list(line.rstrip()))
            line = fp.readline()
        return situation


def move_east(situation: list) -> (bool, list):
    return _move(situation, ">")


def move_south(situation: list) -> (bool, list):
    tsituation = [list(i) for i in zip(*situation)]  # transpose
    changed, tsituation = _move(tsituation, "v")
    situation = [list(i) for i in zip(*tsituation)]
    return changed, situation


def _move(situation: list, symbol: str) -> (bool, list):
    changed = False
    size_x = len(situation[0])
    size_y = len(situation)
    for y in range(size_y):
        new_line = situation[y].copy()
        for x in range(size_x):
            if situation[y][x] == symbol:

                # get new position
                x_new = 0 if x == size_x - 1 else x + 1

                # check if can move
                if situation[y][x_new] == ".":
                    # move
                    new_line[x_new] = symbol
                    new_line[x] = "."
        if new_line != situation[y]:
            changed = True
            situation[y] = new_line
    return changed, situation


def part1(situation: list) -> int:
    count = 0
    while True:
        count += 1
        changed_e, situation = move_east(situation)
        changed_s, situation = move_south(situation)
        if not changed_e and not changed_s:
            return count


def part2(situation: list) -> int:
    return


if __name__ == "__main__":
    situation = read_file()
    print(f"Part 1: {part1(situation)}")
    print(f"Part 2: {part2(situation)}")
