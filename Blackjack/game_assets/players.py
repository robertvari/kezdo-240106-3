import random

# Base class of a Player
class PlayerBASE:
    def __init__(self):
        self._name = None
        self._credits = 0
        self.__hand = []
        self.__playing = True

        self._create()

    def _create(self):
        self._credits = random.randint(10, 100)
        self._name = self.__get_random_name()

    def __get_random_name(self) -> str:
        first_names = ["Marnie", "Johnathan", "Mahnoor", "Hassan", "Alissa", "Millie", "Qasim", "Damon", "Shreya", "Carly"]
        last_names =  ["Roy", "Aguirre", "Sandoval", "Rogers", "Cole", "Matthams", "Allen", "Stokes", "Deleon", "Hampton"]
        return f"{random.choice(first_names)} {random.choice(last_names)}"

    def __str__(self) -> str:
        return str(self._name)


class AIPlayer(PlayerBASE):
    pass

class Player(PlayerBASE):
    # we override PlayerBASE._create
    def _create(self):
        super()._create()
        self._name = input("What is your name?")


if __name__ == "__main__":
    ai_player = AIPlayer()
    player = Player()

    print(ai_player)
    print(player)