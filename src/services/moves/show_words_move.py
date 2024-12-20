from src.interfaces.IMove import IMove


class ShowWordsMove(IMove):
    def execute(self):
        print(f'The word "{self.game_round.inp[1:]}" '
              f'{"exists" if self.game_round.inp[1:] in self.game_round.words else "doesn\'t exist"}')

    def cancel(self):
        pass
