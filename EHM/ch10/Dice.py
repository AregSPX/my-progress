from random import randint

class Die:
    def __init__(self, sides = 10):
        """defines"""
        self.sides = sides
    def roll_dice(self):
        """the interesting part"""
        print(randint(1, self.sides))

die = Die()
die.roll_dice()