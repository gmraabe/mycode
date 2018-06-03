#!/usr/bin/env python3
# timelen.py
# Micah Raabe

# Lab 46 - Import datetime

from datetime import datetime # required to use datetime
# Note that datetime is an object, not a simple string.

## Code to calculate a factorial
x = int(input("Enter a number: "))   # get user input
startTime = datetime.now()    # returns the time of right now from the datetime object (starts the timer)
f = 1
print("Calculating the factorial for " + str(x))  # display starting message
for i in range(1, x+1):  # loop the required number of times to calculate the factorial
    f = f * i
print("Complete")    # display complete message
print(str(x) + '! = ' + str(f))  # print the calculated factorial

## Explore the statrTime object
print('The startTime hour is: ' + str(startTime.hour))
print('The startTime minute is: ' + str(startTime.minute))
print('The startTime day is: ' + str(startTime.day))
print('The startTime month is: ' + str(startTime.month))
print('The startTime year is: ' + str(startTime.year))

## Figure out how long it took to calculate the factorial
print('The code took: ' + str(datetime.now() - startTime) + ' to run.')
