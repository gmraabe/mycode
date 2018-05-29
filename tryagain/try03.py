#!/usr/bin/env python3
# try03.py
# Micah Raabe

# Lab 39 - Try and Except 01

try:
    print('Type the name of the configuration file to load.')
    configfile = input('Filename: ')
    configfileobj = open(configfile, 'r')
    switchconfig = configfileobj.read()
    x = 'Switch config file found.'
except:
    x = 'General error with obtaining configuration file!'
else:
    configfileobj.close()
finally:
    print('\n\nWriting results of routine to log file')
    ## Code to write value of x to log file
    print(x)
