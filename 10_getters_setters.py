import time, random

class Dice:
    def __init__(self, sides, color):
        # private attributes
        self.__sides = sides
        self.__color = color
    
    def __str__(self) -> str:
        return f"Sides: {self.__sides} Color: {self.__color}"
    
    def roll(self):
        print(f"D{self.__sides} is rolling...")
        time.sleep(2)
        print(f"D{self.__sides} result: {random.randint(1, self.__sides)}")

    def get_sides(self):
        return self.__sides
    
    def get_color(self):
        return self.__color
    
    def set_color(self, new_color):
        valid_colors = ["white", "red", "blue"]
        assert new_color in valid_colors, f"{new_color} is not valid. Valid colors {valid_colors}"

        self.__color = new_color

d6 = Dice(6, "white")
d6.set_color("red")
print(d6)