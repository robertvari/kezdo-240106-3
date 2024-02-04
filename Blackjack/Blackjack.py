import os
from game_assets.cards import Deck


class Blackjack:
    def __init__(self):
        self.__reward = 0
        self.__min_bet = 10
        self.__player_list = []

        # todo create a deck of cards
        self.__deck = None

        # todo create an AI Player
        self.__ai_player = None

        # todo create a Player
        self.__player = None

        # self.__clear_screen()
        self.__intro()

        # todo start first turn
        self.__game_loop()

    def __game_loop(self):
        pass

    # private method
    def __intro(self):
        print("="*50, "BLACKJACK", "="*50)

    def __clear_screen(self):
        os.system("cls")


Blackjack()