#!/usr/bin/env python3
# my2to3.py
# Micah Raabe

# Lab 20 - Migrating 2.x to 3.x py
round = 0           # integer round initiated to 0
while(True):        # sets up an infinite loop condition
    print('What is the IPv4 address used to broadcast on a local network? ')
    answer = input()    # string answer collected from user
    round = round + 1     # increase the round counter
    if (answer == '255.255.255.255'): # logic to check if user gave correct answer
        print('Correct!')
        break             # break statement escapes the while loop
    elif (round == 3):    # logic to ensure round has not yet reached 3
        print('Sorry, the answer was 255.255.255.255')
        break             # break statement escapes the while loop
    else:                 # if answer was wrong, and round is not yet equal to 3
        print('Sorry. Try again!')
