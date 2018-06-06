#!/usr/bin/env python3
# sorted03.py
# Micah Raabe

# Lab 71 - Custom sorted ... myFunct

simpsons = [ ('Lisa', 8), ('Bart', 10), ('Maggie', 2), ('Homer', 36), ('Marge', 34) ]
def byAge(x):
    return x[1]
def secondLetter(x):
    return x[0][1]
simpsonsAge = sorted(simpsons, key=byAge)
secondsimpsons = sorted(simpsons, key=secondLetter)
print('Result of sorted(simpsons, key=byAge): ', simpsonsAge)
print('Result of sorted(simpsons, key=secondLetter): ', secondsimpsons)
