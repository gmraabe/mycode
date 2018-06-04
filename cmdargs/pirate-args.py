#!/usr/bin/env python3
# pirate-args.py
# Micah Raabe

# Lab 63 - Argument Parsing
# example use: python3 pirate-args.py blackbeard dabl00nz 10.2.3.55 10.2.3.1

import sys

args = sys.argv
print("This file: " + args[0])
print("Username: " + args[1])
print("Password: " + args[2])
print("IP Address: " + args[3])
print("Gateway: " + args[4])
