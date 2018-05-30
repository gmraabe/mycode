#!/usr/bin/env python3
# merge.py
# Micah Raabe

# Lab - NAPALM Changes, Validation, and Rollback

from napalm import get_network_driver # import code from NAPALM
driver = get_network_driver('eos') # get hte driver for Arista devices
device = driver('172.16.2.20', 'admin', 'alta3') # apply the switch credentials
device.open() # start the connection
#The next two lines of code are new
device.load_merge_candidate("merge.me")
device.commit_config()
