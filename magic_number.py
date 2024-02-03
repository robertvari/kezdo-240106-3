import os, random

class Game:
    def __init__(self):
        self.clear_screen()

        self.computer = Computer()
        self.player = Player()

    def start(self):
        self.intro()

    def intro(self):
        print("*"*50, "MAGIC NUMBER GAME", "*"*50)

    def clear_screen(self):
        os.system("cls")

class Computer:
    def __init__(self):
        self.max_number = 10
        self.magic_number = 0

class Player:
    def __init__(self):
        self.name = "Robert"
        self.credits = 100


game = Game()
game.start()