#!/usr/bin/env python3
# monty_python2.py
# Micah Raabe

# Lab 16 - Using while, if, elif, else

round = 0          # round integer initiated to 0
while('true'):         # infinite loop
    round = round + 1       # increase round counter
    print('Finish the movie title, "Monty Python\'s The Life of _____"')
    answer = input()         # string answer collected from user
    if (answer.lower() == 'brian'):     # check for right answer
        print('Correct!')
        break          # break escapes loop
    elif (answer.lower() == 'shrubbery'):     # check for secret answer
        print('You gave the super secret answer!')
        break          # break escapes loop
    elif(round==3):            # check to see if round 3 has been reached
        print('Sorry, the answer was Brian.')
        break          # break escapes loop
    else:                  # if answer is wrong and round is not yet equal to 3
        print('Sorry! Try again!')
