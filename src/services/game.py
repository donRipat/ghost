from src.interfaces import IPlayer
from src.services.moves import *
from src.services.moves.pass_move import PassMove


class GameRound:
    def __init__(self, words: frozenset[str], players: list[IPlayer]):
        self.words = words
        self.current_player = players[0]
        self.past_player = players[1]
        self.current_string = ''
        self.inp = None
        self.winner = None

        self.commands = {
            '>': (ForwardMove(self), "execute"),
            '<': (BackwardMove(self), "execute"),
            '?': (ShowWordsMove(self), "continue"),
            '!': (BluffMove(self), "break"),
            ':': (HintMove(self), "continue"),
            '~': (PassMove(self), "execute"),
        }

    def start_game(self):
        while True:
            self.state_move_output()
            self.inp = self.current_player.play(self.current_string, self.words)
            if self.current_player.__class__.__name__ != "HumanPlayer":
                print(self.inp)
            if self.inp == "":
                print(f"Make your move, {self.current_player.name}:")
                continue
            if self.inp[0] not in self.commands.keys():
                print(f"Command {self.inp[0]} does not exist")
                continue

            command = self.commands[self.inp[0]]
            command[0].execute()
            if command[1] == "continue":
                continue
            elif command[1] == "break":
                break

            if self.current_string in self.words and len(self.current_string) > 3:
                print(f"{self.current_player.name} spelled the word: {self.current_string}")
                self.winner = self.past_player
                break

            self.current_player, self.past_player = self.past_player, self.current_player

        if self.winner is not None:
            print(f"{self.winner.name} WON!")

    def state_move_output(self):
        print(f"Current string: _{self.current_string}_")
        print(f"{self.current_player.name}'s move: ")