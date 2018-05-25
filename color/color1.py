#!/usr/bin/env python3
# color1.py
# Micah Raabe

## Installs the crayons package.
## python3 -m pip install crayons
import crayons

# print 'red string' in red
print(crayons.red('red string'))

# Red White and Blue text
print('{} {} {}'.format(crayons.red('red'), crayons.white('white'), crayons.blue('blue')))

crayons.disable() # disables the crayons package
print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

crayons.DISABLE_COLOR = False # enable the crayons package

# This line will print in color because color is enabled
print('{} {} {}'.format(crayons.red('red'), crayons.white('white'), crayons.blue('blue')))

# print 'red string' in red
print(crayons.red('red string', bold=True))

# print 'yellow string' in yellow
print(crayons.yellow('yellow string', bold=True))

# print 'magenta string' in magenta
print(crayons.magenta('magenta string', bold=True))

# print 'white string' in white
print(crayons.white('white string', bold=True))

print()
# Print my name in at least two colors
print('{}{}{}{}{}'.format(crayons.red('M'), crayons.white('I'), crayons.blue('C'), crayons.white('A'), crayons.red('H')))

