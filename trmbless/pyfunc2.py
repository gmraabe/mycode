#!/usr/bin/env python3
# pyfunc.py
# Micah Raabe

import os
import sys
from blessings import Terminal
t = Terminal()
print(t.clear())

def yellow_np():
   print(t.bold_black_on_yellow('Print yellow text'))

def yellow_wp(p):
    print(t.bold_black_on_yellow(p))

def trx(p):
    x = t.width - len(p)
    return int(x)

def prompt_location():
    return t.location(0,t.height-2)

def response_location(p):
    return t.location(len(p) + 1,t.height-2)

def top_right(p):
    with t.location(trx(p), 0):
        yellow_wp(p)

def prompt(p):
    with prompt_location():
       p = p + " (q + Enter to quit):"
       print(t.reverse(p),t.clear_eol)
    with response_location(p):
       orders = input()
    return orders

def close(event):
    master.withdraw()
    sys.exit()

yellow_np()

yellow_wp("I want this to print in YELLOW")

top_right("I want this in the top right!")

orders = prompt("Press enter to continue")
input() # Wait until user presses enter before continuing

print(t.clear())

orders = ""
while orders != 'q':
    orders = prompt("Your orders")
    orders
    top_right(orders)
    if orders[:3]=='mtr':
      with t.location(0,3):
         os.system(orders)

yellow_wp("Thanks for all the fish")
