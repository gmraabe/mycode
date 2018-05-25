#!/usr/bin/env python3
# intscript.py
# Micah Raabe

from subprocess import call
call(["ip", "link", "show", "up"])

print("This program will check your interfaces.")
interface = input("Enter an interface, like, ens3: ")
call(["ip", "addr", "show", "dev", interface])
call(["ip", "route", "show", "dev", interface])

