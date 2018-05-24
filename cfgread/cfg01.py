#/usr/bin/env python3
# cfg01.py
# Micah Raabe

## create file object in "r"ead mode
configfile = open('vlanconfig.cfg', 'r')

## display file to the screen - .read()
print(configfile.read())

## make a list of file lines - .readlines()
print(config.readlines())
configlist = config.readlines()

for x in configlist:
    print(x)

## Always close your file
configfile.close()
