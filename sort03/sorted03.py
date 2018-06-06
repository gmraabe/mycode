#!/usr/bin/env python3
# sorted03.py
# Micah Raabe

# Lab 71 - Custom sorted ... myFunct

firewallports = [ 5060, 5061, 80, 443, 22, 25565 ]
def modTen(x):
    return x%10
print('Currently firewallports looks like this: ' + str(firewallports))
print('\nThe results of sorted(firewallports, key=modTen) function:', sorted(firewallports, key=modTen))
print('\nBut firewallports has not actually changed:', firewallports)
