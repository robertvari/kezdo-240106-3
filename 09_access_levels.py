import time, random

class Dice:
    def __init__(self, sides, color):
        # public attributes
        self.sides = sides
        self.color = color

        # protected attributes
        self._sides = sides
        self._color = color

        # private attributes
        self.__sides = sides
        self.__color = color
    
    def __str__(self) -> str:
        return f"Sides: {self.__sides} Color: {self.__color}"
    
    def roll(self):
        print(f"D{self.__sides} is rolling...")
        time.sleep(2)
        print(f"D{self.__sides} result: {random.randint(1, self.__sides)}")

d6 = Dice(6, "white")
d20 = Dice(20, "blue")

d6.roll()