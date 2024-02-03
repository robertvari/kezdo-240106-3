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

        print(f"Hello {self.player}! You have {self.player.credits} credits to play.")
        print("If you can guess my number you win 10 credits, otherwise you loose 10 credits")
        print("I you have no more credits the game is over.")
        print(f"I have number between 1 and {self.computer.max_number}. Can you guess it?")
        print("-"*50)

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