#!/usr/bin/env python3
# hitormiss.py
# Micah Raabe

# Lab 78 - Testing if a Match Exists

import re

#!/usr/bin/env python3
mytxt = open('grimm.txt') # open file ojbect

allLines = mytxt.readlines() # read out of buffer into list

mytxt.close() # close file

lookingfor = re.compile(r'wol[vf][es]?\w+') # compile a search expression

for oneline in allLines:   # search through the lines
    mymatchobj = lookingfor.search(oneline) # call search() and pass oneline
    if mymatchobj: # if mymatchobj has a value (if a match, then...)
        print(mymatchobj.group(), '***', oneline, end='') # Print what was matched on, ***, then the string matched.
        
