#!/usr/bin/env python3
# getrun.py
# Micah Raabe

# Lab - NAPALM Changes, Validation, and Rollback

import os.path
import sys
from napalm import get_network_driver # import code from NAPALM
if len(sys.argv) != 2:
   print("You supplied ", len(sys.argv)-1, " arguments but 1 is needed")
   print("getrun.py requires: IP")
   print("example: python3 getrun.py  a.b.c.d")
   sys.exit()
ip = sys.argv[1]
driver = get_network_driver('eos') # get hte driver for Arista devices
device = driver(ip, 'admin', 'alta3') # apply the switch credentials
device.open() # start the connection
config = device.get_config()
# This next line EXTRACTS the running config from the glob
running_config = config['running']
print(running_config)
