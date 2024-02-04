import random

class Card:
    def __init__(self, name: str, value: int):
        self.__name = name
        self.__value = value

    @property
    def value(self):
        return self.__value

    def change_value(self):
        """
        According to Blackjack roles we can count Ace's value as 1
        """
        if self.__value == 11:
            self.__value = 1

    def __str__(self) -> str:
        return f"Name: {self.__name} Value: {self.__value}"

    def __repr__(self) -> str:
        return self.__name

class Deck:
    def __init__(self):
        self.__cards = []
        self.__create()

    def __create(self):
        self.__cards.clear()

        cards = [
            ["2", 2],
            ["3", 3],
            ["4", 4],
            ["5", 5],
            ["6", 6],
            ["7", 7],
            ["8", 8],
            ["9", 9],
            ["10", 10],
            ["King", 10],
            ["Queen", 10],
            ["Jack", 10],
            ["Ace", 11]
        ]

        suits = ["Heart", "Club", "Diamond", "Spade"]

        for suit in suits:
            for card in cards:
                card_name = f"{suit} {card[0]}"
                card_value = card[1]
                new_card = Card(card_name, card_value)
                self.__cards.append(new_card)
        
        # shuffle cards
        random.shuffle(self.__cards)
    
    def reset(self):
        """
        Create a new deck of cards for a new round
        """
        self.__create()

    def show(self):
        """
        Display the list of cards in the terminal
        """
        print(self.__cards)

if __name__ == "__main__":
    deck = Deck()