import random as rd
from config import Top_First_Letters, Top_Last_Letters

from src.interfaces import IPlayer


class PrimitiveAI(IPlayer):
    def __init__(self, name: str | None = None):
        super().__init__(name or "Dummy")

    def play(self, ss, words):
        candidates = [word for word in words if ss in word]
        if len(candidates) <= 0:
            return "!"

        for word in candidates:
            index = word.find(ss)
            if len(word) > index+len(ss) and ss + word[index+len(ss)] not in words:
                return f">{word[index+len(ss)]}"
            elif index != 0 and word[index-1] + ss not in words:
                return f"<{word[index-1]}"
        return self.__bluff(ss)

    @staticmethod
    def __bluff(ss):
        if rd.choice([True, False]):
            neighbor_letter = ss[-1]
            move = ">"
            letter_weight = {k: v for k, v in Top_Last_Letters.items() if k != neighbor_letter}
        else:
            neighbor_letter = ss[0]
            move = "<"
            letter_weight = {k: v for k, v in Top_First_Letters.items() if k != neighbor_letter}

        population = list(letter_weight.keys())
        move += rd.choices(
            population=population,
            weights=list(letter_weight.values()),
            k=1
        )[0]
        return move
