#!/usr/bin/env python3
# iftest2.py
# Micah Raabe

# Lab 12 - IPv4 Testing with if

ipchk = input('Apply an IP address: ') # this line now prompts the user for input

if ipchk == '192.168.70.1': # if a match on '192.168.70.1'
    print('Looks like the IP address of the Gateway was set: ' + ipchk + ' This is not recommended.') # indented under if
elif ipchk: # if any data is provided, this will test true
    print('Looks like the IP address was set: ' + ipchk)  # indented under elif
else:   # if data is NOT provided
    print('You did not provide input.') # indented under else
