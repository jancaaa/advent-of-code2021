def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        while line:
            signals, output = line.rstrip().split(" | ")
            signals = signals.split(" ")
            output = output.split(" ")
            sorted_signals = [process_signal(s) for s in signals]
            sorted_output = [process_signal(s) for s in output]
            entries.append((sorted_signals, sorted_output))
            line = fp.readline()
        return entries


def process_signal(signal: str) -> str:
    signal = sorted(signal)
    signal = ''.join(signal)
    return signal


def part1(entries: list) -> int:
    count = 0
    for e in entries:
        _, output = e
        for signal in output:
            if len(signal) in [2, 3, 4, 7]:
                count += 1
    return count


def identify(entry: tuple) -> dict:
    signals, output = entry
    signals = set(signals + output)

    len2 = set([s for s in signals if len(s) == 2])  # 1
    len3 = set([s for s in signals if len(s) == 3])  # 7
    len4 = set([s for s in signals if len(s) == 4])  # 4
    len5 = set([s for s in signals if len(s) == 5])  # 2, 3, 5
    len6 = set([s for s in signals if len(s) == 6])  # 0, 6, 9
    len7 = set([s for s in signals if len(s) == 7])  # 8

    digits = dict()

    # easy digits (1, 4, 7, 8)
    digits[1] = len2.pop()
    digits[4] = len4.pop()
    digits[7] = len3.pop()
    digits[8] = len7.pop()

    # 3
    for x in len5:
        if all(elem in x for elem in digits[1]):
            digits[3] = x
            len5.remove(x)
            break

    # 9
    for x in len6:
        if all(elem in x for elem in digits[3]):
            digits[9] = x
            len6.remove(x)
            break

    # 0
    for x in len6:
        if all(elem in x for elem in digits[1]):
            digits[0] = x
            len6.remove(x)
            break

    # 6
    digits[6] = len6.pop()

    # 5
    for x in len5:
        if all(elem in digits[6] for elem in x):
            digits[5] = x
            len5.remove(x)
            break
    # 2
    digits[2] = len5.pop()

    return dict((signal, digit) for digit, signal in digits.items())


def part2(entries: list) -> int:
    sum = 0
    for e in entries:
        digits = identify(e)
        _, output = e
        decoded = []
        for s in output:
            decoded.append(digits[s])
        decoded = int(''.join(map(str, decoded)))
        sum += decoded
    return sum


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
