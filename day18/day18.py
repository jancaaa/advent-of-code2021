import math
import re
from typing import Optional


def read_file(name="input.txt") -> list:
    with open(name) as fp:
        return [line.rstrip() for line in fp]


def addition(a: str, b: str) -> str:
    return f"[{a},{b}]"


def reduce(input: str) -> str:
    action_taken = True
    while action_taken:
        action_taken = False
        output = explode(input)
        if output != input:
            action_taken = True
            input = output
        else:
            output = split(input)
            if output != input:
                action_taken = True
                input = output
    return input


def explode(input: str) -> str:
    depth = 0
    start = None
    end = None
    for i, c in enumerate(input):
        if c == "[":
            depth += 1
            if depth == 5:
                start = i
        elif c == "]":
            if depth == 5:
                end = i
                break
            depth -= 1
    if end is None:
        # nothing to explode
        return input

    output = ""
    exploding_pair = input[start:end + 1]
    el, er = exploding_pair[1:-1].split(",")
    left_part = input[:start]
    right_part = input[end + 1:]

    # get nearest left regular number
    left = get_left_number(left_part)
    if left:
        output += str(str(int(left) + int(el))).join(left_part.rsplit(left, 1))
    else:
        output += left_part

    # get nearest right regular number
    right = get_right_number(right_part)
    if right:
        if not right_part[0].isdigit():
            output += "0"
        output += right_part.replace(str(right), str(str(int(right) + int(er))), 1)
    else:
        output += "0"
        output += right_part
    return output


def split(input: str) -> str:
    numbers = [i for i in get_numbers(input) if int(i) > 9]  # get regular numbers higher than 9
    if numbers:
        to_replace = numbers[0]
        replace_by = f"[{int(to_replace) // 2},{math.ceil(int(to_replace) / 2)}]"
        output = input.replace(to_replace, replace_by, 1)
        return output
    else:
        # nothing to split
        return input


def get_left_number(input: str) -> Optional[str]:
    left_numbers = get_numbers(input)
    return left_numbers[-1] if left_numbers else None


def get_right_number(input: str) -> Optional[str]:
    right_numbers = get_numbers(input)
    return right_numbers[0] if right_numbers else None


def get_numbers(input: str) -> list:
    return re.findall(r'\d+', input)


def sum(entries: list) -> str:
    output = entries[0]
    for e in entries[1:]:
        output = addition(output, e)
        output = reduce(output)
    return output


def get_magnitude(input: str) -> int:
    while input.find("[") != -1:
        for i, c in enumerate(input):
            if c == "[":
                start = i
            elif c == "]":
                end = i
                break
        to_replace = input[start:end + 1]
        l, r = to_replace[1:-1].split(",")
        m = int(l) * 3 + int(r) * 2
        input = input.replace(to_replace, str(m))
    return int(input)


def test_add():
    assert addition("[[[[4,3],4],4],[7,[[8,4],9]]]", "[1,1]") == "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"


def test_explode():
    assert explode("[[[[[9,8],1],2],3],4]") == "[[[[0,9],2],3],4]"
    assert explode("[7,[6,[5,[4,[3,2]]]]]") == "[7,[6,[5,[7,0]]]]"
    assert explode("[[6,[5,[4,[3,2]]]],1]") == "[[6,[5,[7,0]]],3]"
    assert explode("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]") == "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
    assert explode("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]") == "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"

    assert explode("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]") == "[[[[0,7],4],[7,[[8,4],9]]],[1,1]]"
    assert explode("[[[[0,7],4],[7,[[8,4],9]]],[1,1]]") == "[[[[0,7],4],[15,[0,13]]],[1,1]]"
    assert explode("[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]") == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"


def test_split():
    assert split("[[[[0,7],4],[15,[0,13]]],[1,1]]") == "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]"
    assert split("[[[[0,7],4],[[7,8],[0,13]]],[1,1]]") == "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]"


def test_reduce():
    assert reduce("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]") == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"


def test_sum():
    example1 = read_file("example1.txt")
    assert sum(example1) == "[[[[1,1],[2,2]],[3,3]],[4,4]]"
    example2 = read_file("example2.txt")
    assert sum(example2) == "[[[[3,0],[5,3]],[4,4]],[5,5]]"
    example3 = read_file("example3.txt")
    assert sum(example3) == "[[[[5,0],[7,4]],[5,5]],[6,6]]"
    example4 = read_file("example4.txt")
    assert sum(example4) == "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"
    example5 = read_file("example5.txt")
    assert sum(example5) == "[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]"


def test_magnitude():
    assert get_magnitude("[9,1]") == 29
    assert get_magnitude("[1,9]") == 21
    assert get_magnitude("[[9,1],[1,9]]") == 129
    assert get_magnitude("[[1,2],[[3,4],5]]") == 143
    assert get_magnitude("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]") == 1384
    assert get_magnitude("[[[[1,1],[2,2]],[3,3]],[4,4]]") == 445
    assert get_magnitude("[[[[3,0],[5,3]],[4,4]],[5,5]]") == 791
    assert get_magnitude("[[[[5,0],[7,4]],[5,5]],[6,6]]") == 1137
    assert get_magnitude("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]") == 3488
    assert get_magnitude("[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]") == 4140


def part1(entries: list) -> int:
    return get_magnitude(sum(entries))


def part2(entries: list) -> int:
    largest_magnitude = 0
    for e1 in entries:
        for e2 in entries:
            if e1 != e2:
                final = sum([e1, e2])
                magnitude = get_magnitude(final)
                if magnitude > largest_magnitude:
                    largest_magnitude = magnitude
    return largest_magnitude


if __name__ == "__main__":
    test_add()
    test_explode()
    test_split()
    test_reduce()
    test_sum()
    test_magnitude()
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
