#!/usr/bin/env python3
# cheatdice_simulation.py
# Micah Raabe

# Lab 35 - Using Classes

from cheatdice import *                   # import every class from cheatdice.py
swapper = Cheat_Swapper()                 # create player1 that cheats by swapping a dice
loaded_dice = Cheat_Loaded_Dice()         # create player2 that cheats by loading the dice
swapper_score = 0                         # initialize starting value for player1(swapper)
loaded_dice_score = 0                     # initialize starting value for player2(loaded_dice)
number_of_games = 100000                  # number of games (loops) 
game_number = 0
print("Simulation running")
print("==================")
while game_number < number_of_games:                # loop until number of games variable is reached
    swapper.roll()                                  # player1 rolls dice
    loaded_dice.roll()                              # player2 rolls dice

    swapper.cheat()                                 # player1 cheats
    loaded_dice.cheat()                             # player2 cheats

   ## Remove # before print statements to see simulation running
   ## Simulation takes approximately one hour to run with print
   ## statements or ten seconds with print statements
   ## commented out

    #print("Cheater 1 rolled" + str(swapper.get_dice()))
    #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
    if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()):
        #print("Draw!")
        pass                                         # if this round is a draw, then no one scores
    elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()):
        #print("Dice swapper wins!")
        swapper_score+= 1                            # player1 wins and gains a point
    else:
        #print("Loaded dice wins!")
        loaded_dice_score += 1                       # player2 wins and gains a point
    game_number += 1                                 # increment game number

print("Simulation complete")
print("-------------------")
print("Final scores")
print("------------")
print("Swapper won: " + str(swapper_score))          # print final scores
print("Loaded dice won: " + str(loaded_dice_score))

if swapper_score == loaded_dice_score:               # determine who won the tournament
  print("Game was drawn")
elif swapper_score > loaded_dice_score:
  print("Swapper won most games")
else:
  print("Loaded dice won most games")
