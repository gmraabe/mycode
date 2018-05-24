#!/usr/bin/env python3
# cfg01.py
# Micah Raabe

## create file object in "r"ead mode
configfile = open('vlanconfig.cfg', 'r')

## display file to the screen - .read()
print(configfile.read())
configfile.close()

## make a list of file lines - .readlines()
configfile = open('vlanconfig.cfg', 'r')
print(configfile.readlines())
configfile.close()

print()
configfile = open('vlanconfig.cfg', 'r')
configlist = configfile.readlines()
for x in configlist:
    print(x.strip())

## Always close your file
configfile.close()
