from enum import Enum

game = open("game.txt", "r").read()


class Play(Enum):
    ROCK = ("A", "X"), 1, "B"
    PAPER = ("B", "Y"), 2, "C"
    SCISSORS = ("C", "Z"), 3, "A"

    @property
    def letters(self):
        return self.value[0]

    @property
    def score(self):
        return self.value[1]

    @property
    def loses_to(self):
        return self.value[2]

    def make_play(self, play: Enum):
        if self.loses_to in play.letters:
            return self.score
        elif play == self:
            return self.score + 3
        return self.score + 6

    def get_play_by_strategy(self, strategy: str):
        if strategy == "Y":
            return self
        if strategy == "X":
            return self.wins_against()
        return self.by_letter(self.loses_to)

    def wins_against(self) -> Enum:
        for play in Play:
            if play.loses_to in self.letters:
                return play

    @staticmethod
    def by_letter(letter: str) -> Enum:
        for play in Play:
            if letter in play.letters:
                return play


def main():
    plays = game.split("\n")

    score = 0
    for play in plays:
        (opponent, you) = play.split(" ")
        score += Play.by_letter(you).make_play(Play.by_letter(opponent))

    print(f"Total score according to strategy guide: {score}")

    score = 0
    for play in plays:
        (opponent, strategy) = play.split(" ")
        opponent_play = Play.by_letter(opponent)
        score += opponent_play.get_play_by_strategy(strategy).make_play(opponent_play)

    print(f"Total score according to updated strategy guide: {score}")


if __name__ == "__main__":
    main()
