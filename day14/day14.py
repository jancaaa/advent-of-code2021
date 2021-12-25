from collections import defaultdict


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
    pairs_counts = defaultdict(int)
    for p in get_pairs(template):
        pairs_counts[p] += 1

    for _ in range(40):
        new_pairs_count = defaultdict(int)
        for pair, count in pairs_counts.items():
            new_char = rules[pair]
            new_pairs_count[pair[0] + new_char] += count
            new_pairs_count[new_char + pair[1]] += count
        pairs_counts = new_pairs_count

    characters_count = defaultdict(int)
    for pair, char in pairs_counts.items():
        for ch in pair:
            characters_count[ch] += char

    for char, count in characters_count.items():
        characters_count[char] = (count + 1) // 2

    return max(characters_count.values()) - min(characters_count.values())


if __name__ == "__main__":
    template, rules = read_file()
    print(f"Part 1: {part1(template, rules)}")
    print(f"Part 2: {part2(template, rules)}")
