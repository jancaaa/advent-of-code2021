def read_file(name: str) -> list:
    with open(name) as fp:
        line = fp.readline()
        situation = []
        while line:
            line = line.rstrip("\n")
            situation.append(line)
            line = fp.readline()
        return situation


def get_energy_consumed(moves: dict) -> int:
    energy_consumption = dict({"A": 1, "B": 10, "C": 100, "D": 1000})
    energy = 0
    for a in moves.keys():
        energy += moves[a] * energy_consumption[a]
    return energy


def part1(situation: list) -> int:
    print("Part1 solved by hand")
    moves_counts = dict({"A": 21, "B": 13, "C": 9, "D": 17})
    print("moves counts:", moves_counts)

    return get_energy_consumed(moves_counts)


def part2(situation: list) -> int:
    return


if __name__ == "__main__":
    situation = read_file("input_part1.txt")
    print(f"Part 1: {part1(situation)}")
    situation = read_file("input_part2.txt")
    print(f"Part 2: {part2(situation)}")
