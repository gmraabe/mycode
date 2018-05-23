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
print(switch.get('lynx'))

print( "Second test - .get()" )
print(switch.get('lynx', "THE KEY IS IN ANOTHER CASTLE!"))

print( "Third test - .get()" )
print(switch.get('version'))

print( "Forth test - .keys()" )
print(switch.keys())

print( "Fifth test - .values()" )
print(switch.values())

print( "Sixth test - .pop()" )
print(switch.pop('version'))
print(switch.keys())
print(switch.values())

print( "Seventh test - ADD a new value" )
switch['adminlogin'] = 'kar1089'
print(switch.keys())
print(switch.values())

print( "Eighth test - ADD a new value" )
switch['password'] = 'qwerty'
print(switch.keys())
print(switch.values())
