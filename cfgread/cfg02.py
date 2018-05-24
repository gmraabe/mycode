#/usr/bin/env python3
# cfg02.py
# Micah Raabe

## create file object in "r"ead mode
configfile = open('vlanconfig.cfg', 'r')

## display file to the screen - .read()
print(configfile.read())
configblog = configfile.read()

## break configblog across line boundaries (strips out \n)
configlist = configblog.splitlines()

## display list with no '\n'
print(configlist)

## Always close your file
configfile.close()
