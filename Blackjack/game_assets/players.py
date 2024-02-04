import random

# Base class of a Player
class PlayerBASE:
    def __init__(self):
        self.__name = None
        self.__credits = 0
        self.__hand = []
        self.__playing = True

        self.__create()

    def __create(self):
        self.__credits = random.randint(10, 100)
        self.__name = self.__get_random_name()

    def __get_random_name(self) -> str:
        first_names = ["Marnie", "Johnathan", "Mahnoor", "Hassan", "Alissa", "Millie", "Qasim", "Damon", "Shreya", "Carly"]
        last_names =  ["Roy", "Aguirre", "Sandoval", "Rogers", "Cole", "Matthams", "Allen", "Stokes", "Deleon", "Hampton"]
        return "Random Name"

    def __str__(self) -> str:
        return str(self.__name)


class AIPlayer(PlayerBASE):
    pass

class Player(PlayerBASE):
    pass



if __name__ == "__main__":
    ai_player = AIPlayer()
    player = Player()

    print(ai_player)
    print(player)