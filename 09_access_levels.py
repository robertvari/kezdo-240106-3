import time, random

class Dice:
    def __init__(self, sides, color):
        # public attributes
        self.sides = sides
        self.color = color
    
    def __str__(self) -> str:
        return f"Sides: {self.sides} Color: {self.color}"
    
    def roll(self):
        print(f"D{self.sides} is rolling...")
        time.sleep(2)
        print(f"D{self.sides} result: {random.randint(1, self.sides)}")

d6 = Dice(6, "white")
d20 = Dice(20, "blue")

d6.sides = 10

d6.roll()