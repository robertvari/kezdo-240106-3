import time, random

class Dice:
    def __init__(self, sides, color):
        # private attributes
        self.__max_number = sides
        self.__color = color
    
    def __str__(self) -> str:
        return f"Sides: {self.__max_number} Color: {self.__color}"
    
    def roll(self):
        print(f"D{self.__max_number} is rolling...")
        time.sleep(2)
        print(f"D{self.__max_number} result: {random.randint(1, self.__max_number)}")

    @property
    def sides(self):
        return self.__max_number
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, new_color):
        # todo validate new_color

        self.__color = new_color

d6 = Dice(6, "white")
print(d6)
d6.color = "Red"
print(d6)