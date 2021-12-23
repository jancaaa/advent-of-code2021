def read_file() -> (int, int):
    with open("input.txt") as fp:
        line1 = fp.readline()
        line2 = fp.readline()

        _, pos1 = line1.rstrip().split(": ")
        _, pos2 = line2.rstrip().split(": ")
        return int(pos1), int(pos2)


class Player:
    def __init__(self, start_position):
        self.score = 0
        self.pawn_position = start_position

    def move(self, value: int):
        new_pos = self.pawn_position + value
        new_pos = 10 if new_pos % 10 == 0 else new_pos % 10

        self.pawn_position = new_pos
        self.score += self.pawn_position


class Dice:
    def __init__(self):
        self.current_value = 0

    def roll(self):
        if self.current_value == 100:
            self.current_value = 0

        self.current_value += 1
        return self.current_value


class DiracDice:
    def __init__(self, pos1, pos2):
        self.dice = Dice()
        self.player1 = Player(pos1)
        self.player2 = Player(pos2)
        self.rolls_count = 0

    def play(self, winning_score: int = 1000):
        player_turn = 1
        while self.player1.score < winning_score and self.player2.score < winning_score:
            value = self.roll_dice()
            if player_turn == 1:
                self.player1.move(value)
                player_turn = 2
            else:
                self.player2.move(value)
                player_turn = 1

    def roll_dice(self, count: int = 3) -> int:
        sum = 0
        for _ in range(count):
            value = self.dice.roll()
            self.rolls_count += 1
            sum += value
        return sum

    def get_loser_score(self):
        return min(self.player1.score, self.player2.score)


def part1(starting_positions: (int, int)) -> int:
    pos1, pos2 = starting_positions
    dirac_dice = DiracDice(pos1, pos2)
    dirac_dice.play()
    return dirac_dice.get_loser_score() * dirac_dice.rolls_count


def part2(starting_positions: (int, int)) -> int:
    return


if __name__ == "__main__":
    starting_positions = read_file()
    print(f"Part 1: {part1(starting_positions)}")
    print(f"Part 2: {part2(starting_positions)}")
