from src.interfaces.IMove import IMove


class HintMove(IMove):
    def execute(self):
        res = [
            word for word in self.game_round.words
            if self.game_round.current_string in word
        ]
        print(f"Here's your hint, dweeb: {res[:10]}")

    def cancel(self):
        pass
