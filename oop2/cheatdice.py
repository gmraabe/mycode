#!/usr/bin/env python3
# cheatdice.py
# Micah Raabe

# Lab 34 - Class Inheritance

from random import randint

class Player:
  def __init__(self):
    self.dice = []

  def roll(self):                     # rolls 3 dice that value between 1 and 6
    self.dice = []                    
    for i in range(3):               
      self.dice.append(randint(1,6))  

  def get_dice(self):                 # return the dice values
    return self.dice

class Cheat_Swapper(Player):          
  def cheat(self):                    # change last dice to a '6'
    self.dice[-1] = 6

class Cheat_Loaded_Dice(Player):
  def cheat(self):                    # this function adds '1' to any dice that is less than a '6'
    i = 0
    while i < len(self.dice):
      if self.dice[i] < 6:
        self.dice[i] += 1
      i += 1
