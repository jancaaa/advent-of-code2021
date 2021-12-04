def read_file() -> (list, list):
    with open("input.txt") as fp:
        drawn_numbers = fp.readline().rstrip().split(",")
        drawn_numbers = [int(i) for i in drawn_numbers]

        fp.readline()  # empty line
        line = fp.readline()  # boards
        boards = []
        board = []
        while line:
            line = line.strip()
            if line == "":
                boards.append(board)
                board = []
            else:
                line = line.replace("  ", " ").split(" ")
                line = [int(i) for i in line]
                board.append(line)

            line = fp.readline()
        boards.append(board)
        return drawn_numbers, boards


def print_boards(boards: list):
    for board in boards:
        for line in board:
            print(line)
        print()


def mark_drawn_number(boards: list, number: int) -> list:
    for board in boards:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == number:
                    board[i][j] = "X"
    return boards


def check_boards(boards: list) -> (bool, list):
    win = False
    winning_boards = []
    for b in range(len(boards)):
        board = boards[b]
        winning_column = [True for _ in range(len(board))]
        for i in range(len(board)):
            winning_line = True
            for j in range(len(board[0])):
                if board[i][j] != "X":
                    winning_column[j] = False
                    winning_line = False
            if winning_line:
                win = True
                winning_boards.append(b)
                break  # the current board already fulfilled condition to win
        for c in winning_column:
            if c:
                win = True
                winning_boards.append(b)
                break  # the current board already fulfilled condition to win
    return win, winning_boards


def score_board(board: list) -> int:
    score = 0
    for line in board:
        for item in line:
            if item != "X":
                score += item
    return score


def part1(drawn_numbers: list, boards: list) -> int:
    win = False
    drawn_number = None
    while not win:
        drawn_number = drawn_numbers.pop(0)
        boards = mark_drawn_number(boards, drawn_number)
        win, winning_boards = check_boards(boards)
    winning_board = boards[winning_boards[0]]
    return drawn_number * score_board(winning_board)


def part2(drawn_numbers: list, boards: list) -> int:
    drawn_number = None
    while len(boards) > 1:
        drawn_number = drawn_numbers.pop(0)
        boards = mark_drawn_number(boards, drawn_number)
        win, winning_boards = check_boards(boards)
        if win:
            for board in reversed(winning_boards):
                boards.pop(board)

    win, _ = check_boards(boards)
    while not win:
        drawn_number = drawn_numbers.pop(0)
        boards = mark_drawn_number(boards, drawn_number)
        win, _ = check_boards(boards)
    return drawn_number * score_board(boards[0])


if __name__ == "__main__":
    drawn_numbers, boards = read_file()
    print(f"Part 1: {part1(drawn_numbers, boards)}")
    print(f"Part 2: {part2(drawn_numbers, boards)}")
