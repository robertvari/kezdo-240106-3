import os
from game_assets.cards import Deck
from game_assets.players import AIPlayer, Player

class Blackjack:
    def __init__(self):
        self.__reward = 0
        self.__min_bet = 10

        # create a deck of cards
        self.__deck = Deck()

        # create an AI Player
        self.__ai_player = AIPlayer()

        # create a Player
        self.__player = Player()

        # collect players
        self.__player_list = [self.__ai_player, self.__player]

        # self.__clear_screen()
        self.__intro()

        # todo start first round
        self.__round()

    def __round(self):
        for player in self.__player_list:
            player.init_hand(self.__deck)

        for player in self.__player_list:
            player.draw(self.__deck)

    # private method
    def __intro(self):
        print("="*50, "BLACKJACK", "="*50)

    def __clear_screen(self):
        os.system("cls")


Blackjack()