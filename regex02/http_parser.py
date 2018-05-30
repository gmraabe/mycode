#!/usr/bin/env python3
# https_parser.py
# Micah Raabe

# Lab 49 - Use RegEx to Search Text

import urllib.request
import re

while True:
    print('Where should we search? (Enter quit to exit)')
    url = input()
    if url == 'quit': break  # exit the look if user enters 'quit'
    print('Great! So we\'ll try to open this url ' + str(url) + 'to search for the phrase:')
    searchFor = input()
    searchMe = urllib.request.urlopen(url).read().decode('utf-8')

    if re.search(searchFor, searchMe):
        print('Found a match :)')
        print(re.search(searchFor, searchMe).group())
    else:
        print('No match :(')
