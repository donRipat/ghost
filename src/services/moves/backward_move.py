from src.interfaces.IMove import IMove


class BackwardMove(IMove):
    def execute(self):
        self.game_round.current_string = self.game_round.inp[1] + self.game_round.current_string

    def cancel(self):
        pass
