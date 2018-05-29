#!/usr/bin/env python3
# try01.py
# Micah Raabe

# Lab 39 - Try and Except 01

try:
    print('Enter a file name: ')
    name = input()
    file = open(name, 'w')
except:
    print('Error with that file name!')
    print('Enter a file name: ')
    name = input()
    file = open(name, 'w')
finally:
    print('This code will always execute')
