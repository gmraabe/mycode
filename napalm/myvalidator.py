#!/usr/bin/env python3
# myvalidator.py
# Micah Raabe

# Lab - NAPALM Changes, Validation, and Rollback

import os.path
import sys
from napalm import get_network_driver # import code from NAPALM
if len(sys.argv) != 3:
   print("You supplied ", len(sys.argv)-1, " arguments but 2 are needed")
   print("myvalidator.py requires: IP ADDRESS and VALIDATION FILENAME")
   print("example: python3 validate.py  a.b.c.d  filename")
   sys.exit()
ip = sys.argv[1]
path_quest = sys.argv[2]
driver = get_network_driver('eos')
device = driver(ip, 'admin', 'alta3')
device.open()
while not os.path.isfile(path_quest):
   print("SORRY ",path_quest," is not a file ")
   path_quest = input("What is the path to the compliance file you want to use? ")
truthyz = device.compliance_report(path_quest)
print("We determined that the target device...")
if truthyz['complies']:
  print("COMPLIES YAY-YAY-YAY-YAY!")
else:
  print("Does NOT comply with the target validation file")
device.close()
