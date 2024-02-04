import os

class Blackjack:
    def __init__(self):
        self.__reward = 0
        self.__min_bet = 10
        self.__player_list = []

        self.__clear_screen()
        self.__intro()

        # todo create a deck of cards
        # todo create an AI Player
        # todo create a Player
        # todo start first turn

    # private method
    def __intro(self):
        print("="*50, "BLACKJACK", "="*50)

    def __clear_screen(self):
        os.system("cls")

Blackjack()