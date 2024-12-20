from config import WORDS
from src.interfaces import IPlayer
from src.players import *
from src.services import start_game


def main():
    user_name = input(f"Input your name: ")
    p1 = HumanPlayer(user_name)
    p2 = PrimitiveAI()
    move_order = input(f"Who moves first?\n(0) {p1.name} (1) {p2.name}: ")
    if move_order == "1":
        players: tuple[IPlayer, IPlayer] = (p2, p1)
    else:
        players: tuple[IPlayer, IPlayer] = (p1, p2)
    start_game(WORDS, players)


if __name__ == "__main__":
    main()