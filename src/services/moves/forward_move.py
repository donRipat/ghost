from src.interfaces.IMove import IMove


class ForwardMove(IMove):
    def execute(self):
        self.game_round.current_string += self.game_round.inp[1]

    def cancel(self):
        pass
