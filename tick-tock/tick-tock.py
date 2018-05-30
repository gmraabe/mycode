#!/usr/bin/env python3
# tick-tock.py
# Micah Raabe

# Lab 45 - Import Time

import time # This is required to include time module

## Count the number of ticks from the epoch
ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970: " + str(ticks))

## Show how we can convert ticks into a useful time tuple
myTime = time.localtime(ticks) # pass ticks to localtime
print("The local time touple is: " + str(myTime))
print("The local time touple year is: " + str(myTime[0]))
print("The local time touple month is: " + str(myTime[1]))
print("The local time touple day is: " + str(myTime[2]))
print("The local time touple hour is: " + str(myTime[3]))
print("The local time touple minute is: " + str(myTime[4]))
print("The local time touple second is: " + str(myTime[5]))
print("The local time touple week is: " + str(myTime[6]))
print("The local time touple year is: " + str(myTime[7]))
print("The local time touple daylight savings is: " + str(myTime[8]))    
print("\nThe local time in human readable format is: " + time.ctime(ticks))
print("The local time in 500 seconds is: " + time.ctime(ticks + 500))
print("The local time in 500 days is: " + time.ctime(ticks + (500*24*60*60)))

# time.struct_time(tm_year=2018, tm_mon=5, tm_mday=30, tm_hour=14, tm_min=10, tm_sec=13, tm_wday=2, tm_yday=150, tm_isdst=1)

usryear = int(input("Enter a four digit year: "))
usrmonth = int(input("Enter the number of the month: "))
usrday = int(input("Enter the number of the day: "))
usrtime = usryear, usrmonth, usrday, myTime[3], myTime[4], myTime[5], myTime[6], myTime[7], myTime[8] 
usrticks = time.mktime(usrtime)
usrage = ticks - usrticks
print("There have been " + str(usrage) + " seconds since the date entered.")
print("There have been " + str(((usrage / 60) / 60) / 24) + " days since the date entered.")
print("There have been " + str((((usrage / 60) / 60) / 24) / 365) + " years since the date entered.")

