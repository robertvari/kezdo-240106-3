import random, time

# Base class of a Player
class PlayerBASE:
    def __init__(self):
        self._name = None
        self._credits = 0
        self.__hand = []
        self.__playing = True

        self._create()

    # poblic methods
    def init_hand(self, deck):
        self.__hand.clear()
        self.__playing = True

        self.__hand.append(deck.draw())
        
        new_card = deck.draw()
        if self.hand_value > 10 and new_card.value == 11:
            new_card.change_value()

        self.__hand.append(new_card)

    def draw(self, deck):
        while self.__playing:
            if self.hand_value < 19:
                print(f"{self._name} draws a card...")
                time.sleep(2)
                self.__hand.append(deck.draw())
            else:
                print(f"{self._name} finishes")
                time.sleep(1)
                self.__playing = False
            

    # protecteds
    def _create(self):
        self._credits = random.randint(10, 100)
        self._name = self.__get_random_name()

    def _add_card_to_hand(self, new_card):
        self.__hand.append(new_card)

    # privates
    def __get_random_name(self) -> str:
        first_names = ["Marnie", "Johnathan", "Mahnoor", "Hassan", "Alissa", "Millie", "Qasim", "Damon", "Shreya", "Carly"]
        last_names =  ["Roy", "Aguirre", "Sandoval", "Rogers", "Cole", "Matthams", "Allen", "Stokes", "Deleon", "Hampton"]
        return f"{random.choice(first_names)} {random.choice(last_names)}"

    # specials (dunder methods)
    def __str__(self) -> str:
        return str(self._name)

    @property
    def hand_value(self):
        return sum([i.value for i in self.__hand])

    @property
    def hand(self):
        return tuple(self.__hand)
    
    @property
    def playing(self):
        return self.__playing
    
    @playing.setter
    def playing(self, new_playing):
        # todo validate new_playing
        self.__playing = new_playing


class AIPlayer(PlayerBASE):
    pass

class Player(PlayerBASE):
    # we override PlayerBASE._create
    def _create(self):
        super()._create()  # calls parent's _create() method
        # self._name = input("What is your name?")
        self._name = "Robert Vari"

    def draw(self, deck):
        print(f"This is your turn {self._name}")

        while self.playing:
            print(f"Your hand: {self.hand}")
            print(f"Hand value: {self.hand_value}")

            response = input("Do you want to draw a card? (y/n)")

            if response == "y":
                new_card = deck.draw()
                print(f"Your new card: {new_card}")
                self._add_card_to_hand(new_card)
                time.sleep(3)
            else:
                self.playing = False


if __name__ == "__main__":
    import cards

    ai_player1 = AIPlayer()
    ai_player2 = AIPlayer()
    ai_player3 = AIPlayer()
    player = Player()
    deck = cards.Deck()
    player_list = [ai_player1, ai_player2, ai_player3, player]

    for player in player_list:
        player.init_hand(deck)

    for player in player_list:
        player.draw(deck)

    pass