import os
from game_assets.cards import Deck
from game_assets.players import AIPlayer, Player

class Blackjack:
    def __init__(self):
        self.__reward = 0
        self.__min_bet = 10
        self.__player_list = []

        # create a deck of cards
        self.__deck = Deck()

        # create an AI Player
        self.__ai_player = AIPlayer()

        # create a Player
        self.__player = Player()

        # collect players
        self.__player_list.append(self.__ai_player)
        self.__player_list.append(self.__player)

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