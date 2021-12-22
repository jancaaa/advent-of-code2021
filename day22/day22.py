def read_file(name: str = "input.txt") -> list:
    with open(name) as fp:
        line = fp.readline()
        instructions = []
        while line:
            line = line.rstrip()
            state, line = line.split(" ")
            x, y, z = line.split(",")
            x = _parse_range(x)
            y = _parse_range(y)
            z = _parse_range(z)
            instructions.append((state, x, y, z))
            line = fp.readline()
        return instructions


def _parse_range(coords: str) -> range:
    _, coords = coords.split("=")
    start, end = coords.split("..")
    return range(int(start), int(end) + 1)


def reboot(reactor: dict, instruction: str, is_initialization_procedure: bool = False) -> dict:
    state, _, _, _ = instruction
    cuboid = get_cuboid(instruction, is_initialization_procedure)
    for cube in cuboid:
        x, y, z = cube
        if state == "on":
            # add to reactor representation
            if x not in reactor.keys():
                reactor[x] = dict()
            if y not in reactor[x].keys():
                reactor[x][y] = dict()
            reactor[x][y][z] = True
        else:
            # off - remove from reactor representation
            if x in reactor.keys():
                if y in reactor[x].keys():
                    if z in reactor[x][y].keys():
                        del reactor[x][y][z]
                        if len(reactor[x][y].keys()) == 0:
                            del reactor[x][y]
                            if len(reactor[x].keys()) == 0:
                                del reactor[x]
    return reactor


def get_cuboid(instruction: (str, range, range, range), is_initialization_procedure: bool) -> list:
    _, x, y, z = instruction
    cubes = []
    if is_initialization_procedure:
        x = _restrict_to_initialization_area(x)
        y = _restrict_to_initialization_area(y)
        z = _restrict_to_initialization_area(z)
    for xx in x:
        for yy in y:
            for zz in z:
                cubes.append((xx, yy, zz))
    return cubes


def _restrict_to_initialization_area(original_range: range) -> range:
    start = original_range.start if original_range.start > -50 else -50
    end = original_range.stop if original_range.stop < 51 else 51
    return range(start, end)


def count_cubes_on(reactor):
    count = 0
    for x in reactor.keys():
        for y in reactor[x].keys():
            for z in reactor[x][y].keys():
                if reactor[x][y][z]:
                    count += 1
    return count


def tests():
    example = read_file("example.txt")
    assert part1(example) == 39
    larger_example = read_file("larger_example.txt")
    assert part1(larger_example) == 590784


def part1(instructions: list) -> int:
    reactor = dict()
    for i in instructions:
        reactor = reboot(reactor, i, True)
    return count_cubes_on(reactor)


def part2(instructions: list) -> int:
    return


if __name__ == "__main__":
    tests()
    instructions = read_file()
    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")
