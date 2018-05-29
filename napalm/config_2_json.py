#!/usr/bin/env python3
# config_2_json.py
# Micah Raabe

# Lab - NAPALM Changes, Validation, and Rollback

from napalm import get_network_driver
import json
driver = get_network_driver('eos')
device = driver('172.16.2.10', 'admin', 'alta3')
device.open() # start the connection
config = device.get_config()
print("UGLY JASON-LIKE BLOB:\r" )
print(device.get_config())
print("REAL JASON:\r" )
print(json.dumps( config ,indent=4, separators=(',', ': ')))
