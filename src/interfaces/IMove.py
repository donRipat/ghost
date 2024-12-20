from abc import ABC, abstractmethod


class IMove(ABC):
    def __init__(self, game_round):
        self.game_round = game_round

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def cancel(self):
        pass
