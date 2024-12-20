from src.interfaces import IPlayer


class PrimitiveAI(IPlayer):
    def __init__(self, name: str | None = None):
        super().__init__("Dummy" if name is None else name)

    def play(self, ss, words):
        candidates = [word for word in words if ss in word]
        if len(candidates) <= 0:
            return "!"
        chosen_word = ""
        # print(f"candidates={candidates[:50]}")
        for word in candidates:
            index = word.find(ss)
            if len(word) > index+len(ss):
                if ss + word[index+len(ss)] not in words:
                    # print(f"word={word}")
                    return f">{word[index+len(ss)]}"
            elif word[index-1] + ss not in words:
                # print(f"word={word}")
                return f"<{word[index-1]}"
        return self.__bluff(ss)

    def __bluff(self, ss):
        import random as rd
        if rd.choice([True, False]):
            neighbor_letter = ss[:-1]
            move = ">"
        else:
            neighbor_letter = ss[0]
            move = "<"
        if move == ">":
            file = "../../resources/top_last_letters"
        else:
            file = "../../resources/top_first_letters"
        with open(file, "r") as fr:
            lines = fr.read().split()
        letter_weight = {}
        for line in lines:
            letter, weight = line.split(":")
            if letter != neighbor_letter:
                letter_weight[letter] = weight
        # print(letter_weight)
        population=list(letter_weight.keys())
        weights=[float(x) for x in letter_weight.values()]
        # print(population)
        # print(weights)
        move += rd.choices(
            population=population,
            weights=weights,
            k=1
        )[0]
        return move
