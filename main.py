from config import WORDS
from src.interfaces import IPlayer
from src.services.players import *
from src.services import GameRound


def main():
    user_name = input(f"Input your name: ")
    p1, p2 = HumanPlayer(user_name), PrimitiveAI()
    move_order = input(f"Who moves first?\n(0) {p1.name} (1) {p2.name}: ")
    if move_order == "1":
        players: list[IPlayer] = [p2, p1]
    else:
        players: list[IPlayer] = [p1, p2]

    game = GameRound(WORDS, players)
    game.start_game()


if __name__ == "__main__":
    main()