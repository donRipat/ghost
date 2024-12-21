from src.interfaces import IPlayer


class HumanPlayer(IPlayer):
    def __init__(self, name: str | None = None):
        super().__init__(name or 'User')

    def play(self, ss, words):
        return input().lower()