from abc import ABC, abstractmethod


class IPlayer(ABC):
    def __init__(self, name: str | None = None):
        self.name = "DefaultName" if name is None else name

    @abstractmethod
    def play(self, ss: str, words: frozenset[str]):
        pass