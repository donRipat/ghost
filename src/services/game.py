from src.interfaces import IPlayer
from src.services.moves import *


class GameRound:
    def __init__(self, words: frozenset[str], players: list[IPlayer]):
        self.words = words
        self.players = players
        self.current_player = None
        self.past_player = None
        self.current_string = ''
        self.inp = None
        self.winner = None

        self.commands = {
            '>': ForwardMove(self),
            '<': BackwardMove(self),
            '?': ShowWordsMove(self),
            '!': BluffMove(self),
            ':': HintMove(self)
        }

    def start_game(self):
        while True:
            self.current_player, self.past_player = self.players[0], self.players[1]

            print(f"Current string: _{self.current_string}_")
            print(f"{self.current_player.name}'s move: ")
            self.inp = self.current_player.play(self.current_string, self.words)
            if self.current_player.__class__.__name__ != "HumanPlayer":
                print(self.inp)
            if self.inp == "":
                print(f"Make your move, {self.current_player.name}:")
                continue
            if self.inp[0] not in self.commands.keys():
                print(f"Command {self.inp[0]} does not exist")
                continue
            if self.inp[0] == ">":
                self.commands[self.inp[0]].execute()
            elif self.inp[0] == "<":
                self.commands[self.inp[0]].execute()
            elif self.inp[0] == "?":
                self.commands[self.inp[0]].execute()
                continue
            elif self.inp[0] == "!":
                self.commands[self.inp[0]].execute()
                break
            elif self.inp == ":":
                self.commands[self.inp[0]].execute()
                continue

            if self.current_string in self.words and len(self.current_string) > 3:
                print(f"{self.current_player.name} spelled the word: {self.current_string}")
                self.winner = self.past_player
                break

            self.players[0], self.players[1] = self.players[1], self.players[0]

        if self.winner is not None:
            print(f"{self.winner.name} WON!")
