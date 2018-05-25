#!/usr/bin/env python3
# dice_test.py
# Micah Raabe

# Lab 34 - Class Inheritance

###  Import the classes from cheatdice.py  ###
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice

cheater1 = Cheat_Swapper()       # cheater1 will cheat by swapping dice
cheater2 = Cheat_Loaded_Dice()   # cheater2 will cheat by loading the dice

###  Roll Dice  ###
cheater1.roll()
cheater2.roll()

###  Apply Cheat for each player  ###
cheater1.cheat()
cheater2.cheat()

###  Print the dice values  ###
print("Cheater 1 rolled" + str(cheater1.get_dice()))
print("Cheater 2 rolled" + str(cheater2.get_dice()))

###  Determine who wins this round  ###
if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
  print("Draw!")
elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
  print("Cheater 1 wins!")
else:
  print("Cheater 2 wins!")
