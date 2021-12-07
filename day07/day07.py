import sys


def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline().rstrip()
        crabs = line.split(",")
        crabs = [int(crab) for crab in crabs]
        return crabs


def part1(crabs: list) -> int:
    cheapest = sys.maxsize
    for position in range(min(crabs), max(crabs)):
        fuel_usage = 0
        for crab in crabs:
            distance = abs(position - crab)
            fuel_usage += distance
        if fuel_usage < cheapest:
            cheapest = fuel_usage
    return cheapest


def part2(crabs: list) -> int:
    cheapest = sys.maxsize
    for position in range(min(crabs), max(crabs)):
        fuel_usage = 0
        for crab in crabs:
            distance = abs(position - crab)
            fuel_usage += int(distance * (1 + distance) / 2)  # sum of arithmetic sequence
        if fuel_usage < cheapest:
            cheapest = fuel_usage
    return cheapest


if __name__ == "__main__":
    crabs = read_file()
    print(f"Part 1: {part1(crabs)}")
    print(f"Part 2: {part2(crabs)}")
