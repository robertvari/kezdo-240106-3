import os, random

class Game:
    def __init__(self):
        self.clear_screen()

        self.computer = Computer()
        self.player = Player()

    def start(self):
        self.intro()
        self.game_loop()

    def intro(self):
        print("*"*50, "MAGIC NUMBER GAME", "*"*50)

        print(f"Hello {self.player}! You have {self.player.credits} credits to play.")
        print("If you can guess my number you win 10 credits, otherwise you loose 10 credits")
        print("I you have no more credits the game is over.")
        print(f"I have number between 1 and {self.computer.max_number}. Can you guess it?")
        print("-"*50)

    def clear_screen(self):
        os.system("cls")

    def game_loop(self):
        self.computer.think_a_number()
        self.player.think_a_number()

class Computer:
    def __init__(self):
        self.max_number = 10
        self.my_number = "0"
        self.max_tries = 3
    
    def think_a_number(self):
        self.my_number = str(random.randint(1, self.max_number))

class Player:
    def __init__(self):
        self.name = "Robert"
        self.credits = 100
        self.my_number = "0"
    
    def think_a_number(self):
        self.my_number = input("What is your guess?")

    def __str__(self) -> str:
        return self.name


game = Game()
game.start()