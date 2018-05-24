#!/usr/bin/env python3
# cfg02.py
# Micah Raabe

filename = input('Enter the name of the config file: ')

## create file object in "r"ead mode
configfile = open(filename, 'r')

## display file to the screen - .read()
configblog = configfile.read()
print(configblog)

## break configblog across line boundaries (strips out \n)
configlist = configblog.splitlines()

## display list with no '\n'
print(configlist)

## Customization request 03
print('There are ' + str(configlist.__len__()) + ' lines in the file ' + str(filename))

## Always close your file
configfile.close()
