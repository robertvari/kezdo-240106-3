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
        pass
    
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
    deck.show()

    # play a round of Blackjack...
    deck.reset()
