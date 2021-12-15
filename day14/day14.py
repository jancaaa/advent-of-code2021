def read_file() -> (str, dict):
    with open("input.txt") as fp:
        line = fp.readline()
        template = line.rstrip()
        fp.readline()  # empty line
        line = fp.readline()
        rules = dict()
        while line:
            line = line.rstrip()
            start, end = line.split(" -> ")
            rules[start] = end
            line = fp.readline()
        return template, rules


def get_pairs(template: str) -> list:
    pairs = []

    for i in range(len(template) - 1):
        pairs.append(template[i:i + 2])
    return pairs


def count_elements(template: str, characters: set):
    counts = dict()
    for c in characters:
        counts[c] = template.count(c)
    return counts


def part1(template: str, rules: dict) -> int:
    for _ in range(10):
        pairs = get_pairs(template)
        template = template[0]
        for p in pairs:
            template += rules[p] + p[1]
    counts = count_elements(template, set(rules.values()))
    return max(counts.values()) - min(counts.values())


def part2(template: str, rules: dict) -> int:
    return


if __name__ == "__main__":
    template, rules = read_file()
    print(f"Part 1: {part1(template, rules)}")
    print(f"Part 2: {part2(template, rules)}")
