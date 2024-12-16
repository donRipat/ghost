class Player:
    def __init__(self):
        ...

    def play(self):
        ...


class HumanPlayer(Player):
    def __init__(self, name):
        self.name = name
        ...

    def play(self, ss, words):
        return input(f"{self.name}'s move: ")


class PrimitiveAI(Player):
    def __init__(self):
        self.name = "Dummy"

    def play(self, ss, words):
        chosen_word = ""
        for word in words:
            if ss in word and len(word) > len(chosen_word):
                words_substrings = [word[i:j] for i in range(len(word))
                                    for j in range(i + 1, len(word) + 1)]
                if any([ss in words and ss != word for ss in words_substrings]):
                    continue
                chosen_word = word
        index = chosen_word.find(ss)
        move = ""
        try:
            if index > 0:
                move = f"<{chosen_word[index-1]}"
            elif index != -1:
                move = f">{chosen_word[index+len(ss)]}"
            else:
                move = "!"
                print(f"chosen_word={chosen_word},\nindex={index},\nss={ss}")
        except:
            print(f"chosen_word={chosen_word},\nindex={index},\nss={ss}")
            raise Exception("ligma")
        print(f"{self.name}'s move: {move}")
        return move
