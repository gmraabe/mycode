#!/usr/bin/env python3
# first-oop.py
# Micah Raabe

# Lab 33 - Objects ... Scratch

from random import randint

class Player:
  def __init__(self):
    self.dice = []

  def roll(self):
    self.dice = [] # clears current dice
    for i in range(3):
      self.dice.append(randint(1,6))

  def get_dice(self):
    return self.dice

player1 = Player()
player2 = Player()

player1.roll()
player2.roll()

print("Player 1 rolled" + str(player1.get_dice()))
print("Player 2 rolled" + str(player2.get_dice()))

if sum(player1.get_dice()) == sum(player2.get_dice()):
  print("Draw!")
elif sum(player1.get_dice()) > sum(player2.get_dice()):
  print("Player 1 wins!")
else:
  print("Player 2 wins!")
