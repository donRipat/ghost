from src.interfaces.IMove import IMove


class BluffMove(IMove):
    def execute(self):
        print(f"{self.game_round.current_player.name} called a bluff")
        if any([self.game_round.current_string in word for word in self.game_round.words]):
            print(f"bluff call was INCORRECT\nPossible words are "
                  f"{[word for word in self.game_round.words if self.game_round.current_string in word][:20]}")
            self.game_round.winner = self.game_round.past_player
        else:
            print(f"bluff call was correct")
            self.game_round.winner = self.game_round.current_player

    def cancel(self):
        pass
