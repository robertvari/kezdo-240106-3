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
        self.__deck.reset()

        for player in self.__player_list:
            player.init_hand(self.__deck)

        for player in self.__player_list:
            player.draw(self.__deck)

        self.__finish_round()

    def __finish_round(self):
        winner_list = [i for i in self.__player_list if i.hand_value <= 21]

        if not winner_list:
            print("House wins")
        else:
            sorted_winner_list = sorted(winner_list, key=lambda player: player.hand_value)
            winner = sorted_winner_list[-1]

            print(f"The winner is: {winner}")

        response = input("Do you want another round? (y/n)")
        if response == "y":
            self.__round()
        
        print("Have a nice day!")

    # private method
    def __intro(self):
        print("="*50, "BLACKJACK", "="*50)

    def __clear_screen(self):
        os.system("cls")


Blackjack()