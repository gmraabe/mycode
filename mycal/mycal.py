#!/usr/bin/python
# mycal.py
# Micah Raabe

# Lab 47 - Import cal

import calendar

usryear = int(input('Enter a four digit year: '))
usrmonth = int(input('Enter a month number: '))

lilcal = calendar.month(usryear, usrmonth)
print("\nHere is a tiny calendar:\n")
print(lilcal)

#print(calendar.prcal(usryear))

print('Here is the calendar for the entire year of:\n')
print(calendar.calendar(usryear))
