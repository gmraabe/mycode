#!/usr/bin/env python3
# myre03.py
# Micah Raabe

# Lab 75 - re.findall(re.IGNORECASE)

import re
wood = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'
search1 = re.findall(r'wo\w+', wood)        # r'...' for raw string the \w search for a 'word'
print("Results of re.findall(r'wo\w+', wood):", search1)
search2 = re.findall(r'o+', wood)
print("Results of re.findall(r'o+', wood):", search2)
search3 = re.findall(r'carrots', wood)
print("Results of re.findall(r'carrots', wood):", search3)
hobbit = "In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort. It had a perfectly round door like a porthole, painted green, with a shiny yellow brass knob in the exact middle. The door opened on to a tube-shaped hall like a tunnel: a very comfortable tunnel without smoke, with panelled walls, and floors tiled and carpeted, provided with polished chairs, and lots and lots of pegs for hats and coats—the hobbit was fond of visitors. The tunnel wound on and on, going fairly but not quite straight into the side of the hill —The Hill, as all the people for many miles round called it—and many little round doors opened out of it, first on one side and then on another. No going upstairs for the hobbit: bedrooms, bathrooms, cellars, pantries (lots of these), wardrobes (he had whole rooms devoted to clothes), kitchens, dining-rooms, all were on the same floor, and indeed on the same passage. The best rooms were all on the left-hand side (going in), for these were the only ones to have windows, deep-set round windows looking over his garden, and meadows beyond, sloping down to the river."
search4 = re.findall(r'th\w+', hobbit)
print("Results of re.findall(r'th\w+', hobbit):", search4)
igCAPSsearch5 = re.findall(r'th\w+', hobbit, re.IGNORECASE)
print("Results of re.findall(r'th\w+', hobbit, re.IGNORECASE):", igCAPSsearch5)
