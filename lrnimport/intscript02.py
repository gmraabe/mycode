#!/usr/bin/env python3
# intscript.py
# Micah Raabe

import subprocess
# from subprocess import call
subprocess.call(["ip", "link", "show", "up"])

print("This program will check your interfaces.")
interface = input("Enter an interface, like, ens3: ")
subprocess.call(["ip", "addr", "show", "dev", interface])
subprocess.call(["ip", "route", "show", "dev", interface])

