#!/usr/bin/env python3
# dict01.py
# Micah Raabe

## create a dictionary
switch = {'hostname': 'sw1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}

## display parts of the dictionary
print( switch['hostname'] )
print( switch['ip'] )

## request a 'fake' key
# print( switch['lynx'] )

## request a 'fake' key with .get() method
print( "First test - .get()" )
switch.get('lynx')

print( "Second test - .get()" )
switch.get('lynx', "THE KEY IS IN ANOTHER CASTLE!")

print( "Third test - .get()" )
switch.get('version')

