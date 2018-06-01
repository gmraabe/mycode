#!/usr/bin/env python3
# change_config.py
# Micah Raabe

# Lab 62 - Napalm Challenge

from __future__ import print_function

import napalm
import sys
import os

if len(sys.argv) != 3:
    print("You supplied ", len(sys.argv)-1, " arguments but 2 are needed")
    print("change_config.py requires: IP and MERGE_FILE")
    print("example: python3 change_config.py  A.B.C.D  MERGE_FILE")
    sys.exit()
ip = sys.argv[1]
mergefile = sys.argv[2]

while not os.path.isfile(mergefile):
    print("SORRY ", mergefile, " is not a file ")
    mergefile = input("What is the path to the compliance file you want to use? ")

driver = napalm.get_network_driver('eos')
device = driver(hostname=ip, username='admin', password='alta3')
print('Opening to ', ip)
device.open()
print('Loading replacement candidate ', mergefile)

# Prepare to diff by loading candidate
device.load_replace_candidate(filename=mergefile)

# the configuration you can check the changes:
print('\nDiff: ')
print(device.compare_config())

# You can commit or discard the candidate changes.
choice = input("\nWould you like to commit these changes? [yN]: ")
if choice == 'y':
    print('Committing ...')
    device.commit_config()
else:
    print('Discarding ...')
    device.discard_config()

# close the session with the device.
print('Bye, see you later')
device.close()
print('Done.')
