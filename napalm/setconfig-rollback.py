#!/usr/bin/env python3
# setconfig.py
# Micah Raabe

# Napalm Lab - Basic Python Script

import sys
import napalm

if len(sys.argv) != 5: # NEED ONE LESS ARGUMENT
   print("You supplied ", len(sys.argv)-1, " arguments but 5 are needed")
   print("getrun.py requires: OS, IP, USER, PW, restore_file_name of device")
   print("example: python3  getrun.py  eos  a.b.c.d  username  password new_config.txt")
   sys.exit()
os = sys.argv[1]
ip = sys.argv[2]
user = sys.argv[3]
passwd = sys.argv[4]
## filename = sys.argv[5] ## THIS LINE IS NO LONGER NEEDED. WE DONT NEED TO BRING A FILENAME
from napalm import get_network_driver
import pprint as pp
driver = get_network_driver(os)
device = driver(ip,user,passwd)
device.open()
device.rollback() # THIS LINE IS NEW! THIS WILL INSTRUCT NAPALM TO APPLY THE ROLLBACK CONFIG SAVED IN THE ARISTA SWITCH
device.close()
exit()
