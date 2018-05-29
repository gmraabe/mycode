#!/usr/bin/env python3
# myteach01.py
# Micah Raabe

# Lab 37 - Class Team Teach

## "re will cause you great joy, and it also will cause you great pain. Use it wisely."

# a, X, 9, < - ordinary characters just match themselves exactly.
# . (a period) - matches any single character except newline '\n'
# \w - matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_].
# \W - matches any non-word character.
# \b - boundary between word and non-word
# \s - matches a single whitespace character -- space, newline, return, tab	
# \S - matches any non-whitespace character.
# \t, \n, \r - tab, newline, return
# \d - decimal digit [0-9]
# ^ - matches start of the string	
# $ - match the end of the string	
# \ - inhibit the "specialness" of a character.

# re.I - Performs case-insensitive matching.
# re.M - Makes $ match the end of a line (not just the end of the string) and makes ^ match the start of any line (not just the start of the string).
# re.S - Makes a period (dot) match any character, including a newline.

import re

#---------------------------------------------------#

# Match
# re.match(pattern, string, flags = 0)

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print ("\nmatchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")

### Sample output ###

# matchObj.group() :  Cats are smarter than dogs
# matchObj.group(1) :  Cats
# matchObj.group(2) :  smarter

#---------------------------------------------------#

## Search
# re.search(pattern, string, flags = 0)
line = "Cats are dumber than dogs";

searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
   print ("\nsearchObj.group() : ", searchObj.group())
   print ("searchObj.group(1) : ", searchObj.group(1))
   print ("searchObj.group(2) : ", searchObj.group(2))
else:
   print ("Nothing found!!")

### Sample output ###

# searchObj.group() :  Cats are dumber than dogs
# searchObj.group(1) :  Cats
# searchObj.group(2) :  dumber

#---------------------------------------------------#

# another example of search

pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print('\nFound "{}" in "{}" from {} to {} ("{}")'.format(match.re.pattern, match.string, s, e, text[s:e]))

### Sample output ###

# Found "this" in "Does this text match the pattern?" from 5 to 9 ("this")

#---------------------------------------------------#

# Match vs Search
# match checks for a match only at the beginning of the string, while search checks for a match anywhere in the string 

line = "2017-07-30 17:20:29.089 3278 WARNING keystone.common.wsgi [req-98982a97-90ca-411f-843d-c4dd5186fe5a - - - - -] Authorization failed. The request you have made requires authentication. from 172.16.1.5";

matchObj = re.match( r'- - - - -] Auth', line, re.M|re.I)
if matchObj:
   print ("\nmatch --> matchObj.group() : ", matchObj.group())
else:
   print ("\nNo match!!")

searchObj = re.search( r'- - - - -] Auth', line, re.M|re.I)
if searchObj:
   print ("search --> searchObj.group() : ", searchObj.group())
else:
   print ("Nothing found!!")

### Sample output ###

#---------------------------------------------------#

# Search and Replace
# re.sub(pattern, repl, string, max=0)
phone = "123-456-7890 # This is Phone Number"          # sets string and prints original string
print('\n' + phone)

num = re.sub(r'#.*$', "", phone)                       # Delete Python-style comments
print ("Without comments:\n  Phone Num : ", num)

num = re.sub(r'\D', "", phone)                         # Remove anything other than digits
print ("Digits only:\n  Phone Num : ", num)

### Sample output ###

# No match!!
# search --> searchObj.group() :  - - - - -] Auth
#
# 123-456-7890 # This is Phone Number
# Without comments:
#   Phone Num :  123-456-7890 
# Digits only:
#   Phone Num :  1234567890

#---------------------------------------------------#

# Multiple matches in a string
print()
text = 'abbaaabbbbaaaaab'    # contains only 3 'ab'         
pattern = 'ab'
for match in re.findall(pattern, text):
    print('Found {!r}'.format(match))

### Sample output ###

# Found 'ab'
# Found 'ab'
# Found 'ab'

