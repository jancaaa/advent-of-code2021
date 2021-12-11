def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        while line:
            entries.append(line.rstrip())
            line = fp.readline()
        return entries


def remove_valid(line: str) -> str:
    removed = True
    while removed:
        new_line = line.replace("()", "")
        new_line = new_line.replace("[]", "")
        new_line = new_line.replace("{}", "")
        new_line = new_line.replace("<>", "")
        if line == new_line:
            removed = False
        else:
            line = new_line
    return line


def part1(entries: list) -> int:
    sum = 0
    for e in entries:
        e = remove_valid(e)
        for i in e:
            if i == ")":
                sum += 3
                break
            elif i == "]":
                sum += 57
                break
            elif i == "}":
                sum += 1197
                break
            elif i == ">":
                sum += 25137
                break
    return sum


def part2(entries: list) -> int:
    scores = []

    for e in entries:
        sum = 0
        e = remove_valid(e)
        if ")" in e or "]" in e or "}" in e or ">" in e:
            continue  # corrupted line
        else:
            for i in reversed(e):
                sum *= 5
                if i == "(":
                    sum += 1
                elif i == "[":
                    sum += 2
                elif i == "{":
                    sum += 3
                elif i == "<":
                    sum += 4
        scores.append(sum)
        middle = int(len(scores) / 2)
    return sorted(scores)[middle]


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
