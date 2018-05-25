#!/usr/bin/env python3
# pyfunc.py
# Micah Raabe

from blessings import Terminal
t = Terminal()
print(t.clear())

print(t.bold('Hi there!'))

print(t.move_down)
print(t.bold_red_on_bright_green('It hurts my eyes!'))

print(t.move_down+t.bold_underline_black_on_yellow('Look! A 1997 web page! No, the font would have to be blinking'))

print(t.move_down)
print(" Terminal width: ", t.width)
print(" Terminal height: ", t.height)

print(t.move_down+"A one-liner way to show terminal width and height",t.reverse,t.width,"by",t.height," ")

with t.location(20, t.height - 1):
   print(t.reverse + t.blink('This is at the bottom and printed in REVERSE.'))
   
