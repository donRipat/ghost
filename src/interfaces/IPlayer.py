from abc import ABC, abstractmethod


class IPlayer(ABC):
    @abstractmethod
    def play(self, ss: str, words: frozenset[str]):
        pass