#!/usr/bin/env python3
# getjson.py
# Micah Raabe

# Lab - NAPALM Changes, Validation, and Rollback

import os.path
import sys
from napalm import get_network_driver # import code from NAPALM
if len(sys.argv) != 2:
   print("You supplied ", len(sys.argv)-1, " arguments but 1 is needed")
   print("getjson.py requires: IP")
   print("example: python3 getjson.py  a.b.c.d")
   sys.exit()
ip = sys.argv[1]
from napalm import get_network_driver
driver = get_network_driver('eos')
device = driver(ip, 'admin', 'alta3')
device.open() # start the connection
print(device.get_config()) 
