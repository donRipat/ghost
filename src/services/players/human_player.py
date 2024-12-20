from src.interfaces import IPlayer


class HumanPlayer(IPlayer):
    def __init__(self, name: str | None = None):
        super().__init__("User" if name is None else name)

    def play(self, ss, words):
        return input()