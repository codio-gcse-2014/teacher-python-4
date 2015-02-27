# Task 3
# Press the 'Run File' menu button to execute

import random
class Dice:
    value=0
    def __init__(self):
        self._value=0

    def roll(self)->int:
        self.value=random.randint(1,6)


my_dice=Dice() #instantiate the first object from a Dice class
his_dice=Dice()#instantiate the second object from a Dice class
my_dice.roll()
his_dice.roll()
break_down=str(my_dice.value)+" vs "+str(his_dice.value)
if my_dice.value==his_dice.value:
    print("A tie,",break_down)
elif my_dice.value>his_dice.value:
    print("I win,",break_down)    
else:
    print("I lose,",break_down)