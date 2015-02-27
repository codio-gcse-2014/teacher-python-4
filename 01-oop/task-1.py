# Task 1
# Press the 'Run File' menu button to execute
# 
import random
class Dice:
    value=0
    def __init__(self):
        self._value=0

    def roll(self)->int:
        self.value=random.randint(1,6)
my_dice=Dice()
my_dice.roll() #object methods are called with a dot notation: #object_name.object_method()
print(my_dice.value)