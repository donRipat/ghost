import random as rd

from config import WORDS
from src.interfaces import IPlayer
from src.services.players import *
from src.services import GameRound


def main():
    user_name = input(f"Input your name: ")
    players = [HumanPlayer(user_name), PrimitiveAI()]

    move_order = input(f"Who moves first?\n(0) {players[0].name} (1) {players[1].name} (2) random: ")
    players = move_order_select(move_order, players)

    game = GameRound(WORDS, players)
    game.start_game()

def move_order_select(move_order: str, players: list[IPlayer]):
    if move_order == '0':
        return players
    elif move_order == '1':
        return players[::-1]
    else:
        rd.shuffle(players)
        return players


if __name__ == "__main__":
    main()